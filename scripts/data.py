"""Public downloads, local data contracts, and auditable provenance."""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import pandas as pd

ROOT = Path(__file__).resolve().parent


class NeedsData(Exception):
    pass


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
    os.replace(tmp, path)


class Context:
    def __init__(self, fetch=False, inputs=None, cache=None, output=None):
        self.fetch = fetch
        self.inputs = Path(inputs or ROOT / "inputs")
        self.cache = Path(cache or ROOT / "data")
        self.output = Path(output or ROOT / "results")
        self.provenance = []

    def public(self, name, url, kind):
        path = self.cache / name
        meta_path = self.cache / (name + ".json")
        if path.exists():
            if not meta_path.exists():
                raise ValueError(f"Cached {name} has no download metadata; remove it and fetch again")
            meta = json.loads(meta_path.read_text())
            if meta["sha256"] != sha256(path) or meta["source_url"] != url:
                raise ValueError(f"Cached {name} checksum/source mismatch; no silent replacement")
        else:
            if not self.fetch:
                raise NeedsData(f"Missing public cache {name}; run with --fetch (network required)")
            self.cache.mkdir(parents=True, exist_ok=True)
            request = Request(url, headers={"User-Agent": "TheoryOfEverything-research/1.0"})
            try:
                with urlopen(request, timeout=45) as response:
                    blob = response.read(30_000_001)
                    resolved = response.url
                    content_type = response.headers.get("Content-Type", "")
            except Exception as error:
                raise NeedsData(f"Public download failed for {url}: {error}") from error
            if not blob or len(blob) > 30_000_000:
                raise ValueError("Empty download or 30 MB per-file limit exceeded")
            if b"<html" in blob[:500].lower() or b"<!doctype html" in blob[:500].lower():
                raise ValueError("Server returned HTML rather than the requested data")
            if kind == "zip" and not blob.startswith(b"PK"):
                raise ValueError("Expected a ZIP archive")
            if kind == "json":
                json.loads(blob)
            tmp = path.with_suffix(path.suffix + ".tmp")
            tmp.write_bytes(blob)
            os.replace(tmp, path)
            meta = {"source_url": url, "resolved_url": resolved,
                    "retrieved_utc": datetime.now(timezone.utc).isoformat(),
                    "bytes": len(blob), "content_type": content_type, "sha256": sha256(path)}
            write_json(meta_path, meta)
        self.provenance.append({"file": name, **meta})
        return path

    def local(self, case):
        path = self.inputs / case["input"]
        if not path.exists():
            raise NeedsData(f"Provide {case['input']} and its .metadata.json sidecar; see templates and README")
        sidecar = path.with_suffix(".metadata.json")
        if not sidecar.exists():
            raise NeedsData(f"Missing provenance {sidecar.name}")
        meta = json.loads(sidecar.read_text())
        required_meta = ("sources", "construction", "coverage", "assignment")
        if any(not meta.get(key) for key in required_meta):
            raise ValueError(f"Metadata must document {required_meta}")
        f = pd.read_csv(path)
        missing = set(case["columns"]) - set(f.columns)
        if missing or f.empty:
            raise ValueError(f"Empty dataset or missing required columns: {sorted(missing)}")
        if f[case["columns"]].isna().any().any():
            raise ValueError("Missing required values; document exclusions before supplying an analysis extract")
        self.provenance.append({"file": path.name, "sha256": sha256(path),
                                "metadata_sha256": sha256(sidecar), "metadata": meta})
        return f

    def csv(self, name, frame):
        self.output.mkdir(parents=True, exist_ok=True)
        frame.to_csv(self.output / name, index=True)
        return name

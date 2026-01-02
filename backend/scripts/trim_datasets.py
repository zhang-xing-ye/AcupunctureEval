import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TRIM_COUNT = 2
MAPPINGS = [
    (
        REPO_ROOT / "backup" / "backend" / "datasets" / "qa",
        Path(__file__).parent.parent / "datasets" / "qa",
    ),
    (
        REPO_ROOT / "backup" / "backend" / "datasets" / "vqa",
        Path(__file__).parent.parent / "datasets" / "vqa",
    ),
    (
        REPO_ROOT / "backup" / "datasets" / "qa",
        REPO_ROOT / "datasets" / "qa",
    ),
    (
        REPO_ROOT / "backup" / "datasets" / "vqa",
        REPO_ROOT / "datasets" / "vqa",
    ),
]


def trim_from_full(full_root: Path, sample_root: Path) -> None:
    if not full_root.exists():
        return

    for full_path in sorted(full_root.rglob("*_full.json")):
        data = json.loads(full_path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            continue

        trimmed = data[:TRIM_COUNT]
        rel = full_path.relative_to(full_root)
        sample_name = rel.name.replace("_full", "", 1)
        target_dir = sample_root / rel.parent
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / sample_name

        target_path.write_text(
            json.dumps(trimmed, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Trimmed sample written: {target_path}")



def main() -> None:
    print("Starting dataset trimming (keep first", TRIM_COUNT, "items)")
    for full_root, sample_root in MAPPINGS:
        trim_from_full(full_root, sample_root)
    print("Dataset trimming completed.")


if __name__ == "__main__":
    main()

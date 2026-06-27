import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a model-cache placeholder for RunPod volume/S3 labs.")
    parser.add_argument("--cache-dir", default="/runpod-volume/models/demo-model")
    parser.add_argument("--model-name", default="demo-model")
    args = parser.parse_args()

    cache_dir = Path(args.cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    manifest = cache_dir / "MANIFEST.txt"
    manifest.write_text(
        f"model_name={args.model_name}\ncache_dir={cache_dir}\nreplace_this_with_real_weights=true\n",
        encoding="utf-8",
    )
    print(f"Created cache placeholder: {manifest}")


if __name__ == "__main__":
    main()

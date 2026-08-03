import hashlib
from pathlib import Path


DATASET_DIRECTORY = Path("dataset/raw")
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def calculate_file_hash(file_path: Path) -> str:
    """Create a hash value for an image file."""

    hash_value = hashlib.md5()

    with file_path.open("rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            hash_value.update(block)

    return hash_value.hexdigest()


def find_duplicate_images(dataset_directory: Path) -> list[Path]:
    """Find duplicate images in the dataset."""

    if not dataset_directory.exists():
        print(f"Dataset directory was not found: {dataset_directory}")
        return []

    hashes = {}
    duplicates = []

    for file_path in dataset_directory.rglob("*"):
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        try:
            file_hash = calculate_file_hash(file_path)

            if file_hash in hashes:
                duplicates.append(file_path)
                print(
                    f"Duplicate found: {file_path} "
                    f"matches {hashes[file_hash]}"
                )
            else:
                hashes[file_hash] = file_path

        except OSError as error:
            print(f"Could not read {file_path}: {error}")

    print(f"Total duplicate images found: {len(duplicates)}")
    return duplicates


if __name__ == "__main__":
    find_duplicate_images(DATASET_DIRECTORY)

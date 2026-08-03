from pathlib import Path
from PIL import Image


INPUT_DIRECTORY = Path("dataset/raw")
OUTPUT_DIRECTORY = Path("dataset/processed")
IMAGE_SIZE = (224, 224)


def resize_images(input_directory: Path, output_directory: Path) -> None:
    """Resize chilli leaf images to 224 x 224 pixels."""

    if not input_directory.exists():
        print(f"Input directory was not found: {input_directory}")
        return

    output_directory.mkdir(parents=True, exist_ok=True)

    supported_extensions = {".jpg", ".jpeg", ".png"}
    processed_count = 0

    for image_path in input_directory.rglob("*"):
        if image_path.suffix.lower() not in supported_extensions:
            continue

        relative_path = image_path.relative_to(input_directory)
        output_path = output_directory / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with Image.open(image_path) as image:
                image = image.convert("RGB")
                image = image.resize(IMAGE_SIZE)
                image.save(output_path)

            processed_count += 1
            print(f"Processed: {image_path}")

        except (OSError, ValueError) as error:
            print(f"Could not process {image_path}: {error}")

    print(f"Total images processed: {processed_count}")


if __name__ == "__main__":
    resize_images(INPUT_DIRECTORY, OUTPUT_DIRECTORY)

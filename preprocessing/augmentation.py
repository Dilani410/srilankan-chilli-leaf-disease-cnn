from tensorflow.keras.preprocessing.image import ImageDataGenerator


def create_training_augmentation() -> ImageDataGenerator:
    """Create augmentation settings for training images."""

    return ImageDataGenerator(
        rescale=1.0 / 255.0,
        rotation_range=20,
        width_shift_range=0.10,
        height_shift_range=0.10,
        zoom_range=0.20,
        horizontal_flip=True,
        brightness_range=(0.8, 1.2),
        fill_mode="nearest",
    )


def create_validation_generator() -> ImageDataGenerator:
    """Create normalization settings for validation and test images."""

    return ImageDataGenerator(
        rescale=1.0 / 255.0,
    )


if __name__ == "__main__":
    training_generator = create_training_augmentation()
    validation_generator = create_validation_generator()

    print("Training augmentation configuration created.")
    print("Validation and test normalization configuration created.")

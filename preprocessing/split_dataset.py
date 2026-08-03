from pathlib import Path
from sklearn.model_selection import train_test_split

DATASET_DIRECTORY = Path("dataset/processed")
RANDOM_STATE = 42


def create_dataset_split(image_paths, labels):
    """Split the dataset into training, validation and testing sets."""

    train_paths, temp_paths, train_labels, temp_labels = train_test_split(
        image_paths,
        labels,
        test_size=0.30,
        random_state=RANDOM_STATE,
        stratify=labels,
    )

    validation_paths, test_paths, validation_labels, test_labels = train_test_split(
        temp_paths,
        temp_labels,
        test_size=0.50,
        random_state=RANDOM_STATE,
        stratify=temp_labels,
    )

    return (
        train_paths,
        validation_paths,
        test_paths,
        train_labels,
        validation_labels,
        test_labels,
    )


if __name__ == "__main__":
    print("Dataset splitting script created successfully.")

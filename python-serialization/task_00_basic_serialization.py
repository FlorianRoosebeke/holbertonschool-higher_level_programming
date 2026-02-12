#!/usr/bin/python3
import json
import pickle


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to a file using pickle.

    Args:
        data: The data to serialize.
        filename: The filename to save to.
    """
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a pickle file.

    Args:
        filename: The filename to load from.

    Returns:
        The deserialized data.
    """
    with open(filename, "rb") as f:
        return pickle.load(f)

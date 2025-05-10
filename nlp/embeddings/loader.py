import numpy as np
import json
import os


def load_embeddings(npz_path):
    """Load requests and embeddings from a .npz file."""
    data = np.load(npz_path, allow_pickle=True)
    requests = data["requests"]
    embeddings = data["embeddings"]
    return requests, embeddings


def load_metadata(npz_path):
    """Load metadata from matching .json file, if it exists."""
    json_path = os.path.splitext(npz_path)[0] + ".json"
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            return json.load(f)
    else:
        return None

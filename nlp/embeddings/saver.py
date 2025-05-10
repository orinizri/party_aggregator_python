import numpy as np
import json
from datetime import datetime


def save_embeddings(texts, embeddings, output_base):
    np.savez_compressed(f"{output_base}.npz", requests=texts, embeddings=embeddings)
    metadata = {
        "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "created": datetime.utcnow().isoformat(),
        "count": len(texts),
    }
    with open(f"{output_base}.json", "w") as f:
        json.dump(metadata, f, indent=2)

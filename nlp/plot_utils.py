import numpy as np
import pandas as pd
import umap.umap_ as umap
import matplotlib.pyplot as plt
import seaborn as sns
from nlp.embeddings.loader import load_embeddings

def create_umap(npz_file, csv_file, n_neighbors=15, min_dist=0.1, n_components=2):
    """Apply UMAP to embeddings and join with cluster CSV."""
    requests, embeddings = load_embeddings(npz_file)
    df = pd.read_csv(csv_file)

    assert len(requests) == len(df), "Mismatch in request count"
    df["request"] = requests

    reducer = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, n_components=n_components)
    umap_coords = reducer.fit_transform(embeddings)

    df["x"] = umap_coords[:, 0]
    df["y"] = umap_coords[:, 1]

    return df

def plot_embedding_map(df, title="Embedding Cluster Map", hue_col="cluster", figsize=(12, 8)):
    """Reusable UMAP plot function."""
    plt.figure(figsize=figsize)
    sns.scatterplot(data=df, x="x", y="y", hue=hue_col, palette="tab10", s=60, alpha=0.9)
    plt.title(title)
    plt.xlabel("UMAP 1")
    plt.ylabel("UMAP 2")
    plt.legend(title=hue_col, bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()
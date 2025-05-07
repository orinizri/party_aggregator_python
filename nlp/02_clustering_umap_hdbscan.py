# Dimensionality reduction + clustering
import numpy as np
import pandas as pd
import hdbscan

def load_embeddings(npz_path):
    data = np.load(npz_path, allow_pickle=True)
    return data["requests"], data["embeddings"]

def run_hdbscan(embeddings, min_cluster_size=5):
    clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, prediction_data=True)
    labels = clusterer.fit_predict(embeddings)
    return labels, clusterer

def save_cluster_output(requests, labels, output_csv):
    df = pd.DataFrame({
        "request": requests,
        "cluster": labels
    })
    df.to_csv(output_csv, index=False)
    print(f"✅ Saved clustered requests to: {output_csv}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Cluster request embeddings using HDBSCAN")
    parser.add_argument("--input_npz", type=str, required=True, help="Path to .npz file with requests + embeddings")
    parser.add_argument("--min_cluster_size", type=int, default=5, help="Min cluster size for HDBSCAN")
    parser.add_argument("--output_csv", type=str, default="outputs/clustered_requests.csv", help="Output CSV path")

    args = parser.parse_args()

    requests, embeddings = load_embeddings(args.input_npz)
    labels, model = run_hdbscan(embeddings, min_cluster_size=args.min_cluster_size)
    save_cluster_output(requests, labels, args.output_csv)
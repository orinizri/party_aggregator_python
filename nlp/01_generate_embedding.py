# Embed special/song requests
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

def load_and_clean_requests(df, column):
    clean_series = (
        df[column]
        .dropna()
        .astype(str)
        .str.strip()
    )
    return clean_series[clean_series != ""]  # filter blanks

def embed_requests(requests, model_name=MODEL_NAME):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(requests.tolist(), show_progress_bar=True)
    return embeddings

def save_embeddings(requests, embeddings, output_path):
    df = pd.DataFrame({
        "request": requests,
    })
    np.savez_compressed(output_path, requests=df["request"].values, embeddings=embeddings)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate request embeddings")
    parser.add_argument("--input_csv", type=str, required=True, help="Path to cleaned CSV with requests")
    parser.add_argument("--column", type=str, default="special_requests", help="Column to embed")
    parser.add_argument("--output", type=str, default="data/embeddings/special_requests.npz", help="Output .npz path")
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    if args.column == "combined":
        specials = load_and_clean_requests(df, "special_requests")
        songs = load_and_clean_requests(df, "song_requests")
        requests = pd.concat([specials, songs]).drop_duplicates().reset_index(drop=True)
    else:
        requests = load_and_clean_requests(df, args.column)
    embeddings = embed_requests(requests)
    save_embeddings(requests, embeddings, args.output)

    print(f"✅ Saved {len(requests)} embeddings to {args.output}")
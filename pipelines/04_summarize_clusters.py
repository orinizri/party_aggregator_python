import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
import json

from nlp.cluster_summarization.summarize_clusters import summarize_clusters
from nlp.cluster_summarization.openai_client import OpenAIClient

# Load API Key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment variables or .env file")

# Load clustered data
df = pd.read_csv("outputs/song_requests_clustered.csv")

# Initialize GPT Client with Retry Logic
client = OpenAIClient(api_key=api_key, model="gpt-3.5-turbo")

# Generate timestamped output filename
timestamp = datetime.now().strftime("%Y%m%d")
output_path = f"outputs/song_request_cluster_insights_{timestamp}.json"

# Run structured summarization on valid clusters only
results = summarize_clusters(df[df["cluster"] != -1], client, output_path=output_path)

# Optional: also save as CSV flat summary for quick review
flat_output_path = f"outputs/song_request_cluster_summaries_{timestamp}.csv"
pd.DataFrame([
    {"cluster_id": r["cluster_id"], "summary": r["operational_enhancement"]}
    for r in results
]).to_csv(flat_output_path, index=False)

print(f"✅ Structured insights saved to {output_path}")
print(f"✅ Flat summaries saved to {flat_output_path}")
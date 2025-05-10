import pandas as pd
from nlp import OpenAIClient, summarize_clusters
from dotenv import load_dotenv
import os

# Load API Key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key is loaded
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment variables or .env file")

# Load clustered data
df = pd.read_csv("outputs/song_requests_clustered.csv")

# Initialize GPT Client with Retry Logic
client = OpenAIClient(api_key=api_key, model="gpt-3.5-turbo")

# Run summarization
summaries = summarize_clusters(df[df["cluster"] != -1], client)

# Save summaries to CSV
output_path = "outputs/song_request_cluster_summaries.csv"
pd.DataFrame.from_dict(summaries, orient="index", columns=["summary"]).to_csv(output_path)

print(f"✅ Summaries saved to {output_path}")
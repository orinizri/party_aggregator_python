import os
import sys
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from .openai_client import OpenAIClient
from .summarize_clusters import summarize_clusters

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ Error: Missing OPENAI_API_KEY in environment variables or .env file")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: python -m nlp.cluster_summarization <input_csv_path>")
    sys.exit(1)

input_csv_path = sys.argv[1]

if not os.path.exists(input_csv_path):
    print(f"❌ Error: File not found - {input_csv_path}")
    sys.exit(1)

df = pd.read_csv(input_csv_path)
client = OpenAIClient(api_key=api_key)

timestamp = datetime.now().strftime("%Y%m%d")
output_path = f"outputs/cluster_insights_{timestamp}.json"

summarize_clusters(df[df["cluster"] != -1], client, output_path=output_path)

print(f"✅ Structured insights saved to {output_path}")
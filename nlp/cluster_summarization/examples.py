import pandas as pd
from .openai_client import OpenAIClient
from .summarize_clusters import summarize_clusters

# Load data (example CSV with 'cluster' and 'request' columns)
df = pd.read_csv("outputs/example_clustered_data.csv")

# Initialize Client
client = OpenAIClient(api_key="your-api-key")

# Run and Save
summarize_clusters(df, client, output_path="outputs/cluster_insights_example.json")
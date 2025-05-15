import os
import json
from .prompt_templates import build_advanced_prompt
from .response_parser import parse_response


def append_to_json_file(filepath, item):
    # If file exists, load and append
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(item)

    # Write back to file
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def summarize_clusters(
    df, client, max_samples=3, output_path="outputs/cluster_insights.json"
):
    clusters = sorted(df["cluster"].unique())

    for cluster_id in clusters:
        cluster_df = df[df["cluster"] == cluster_id]
        if cluster_df.empty:
            continue

        examples = (
            cluster_df["request"]
            .sample(min(len(cluster_df), max_samples), random_state=42)
            .tolist()
        )
        prompt = build_advanced_prompt(cluster_id, examples)
        print(f"Processing Cluster {cluster_id}...")

        raw_response = client.chat(prompt)
        structured_response = parse_response(raw_response)

        result = {
            "cluster_id": int(cluster_id),  # Ensure serializable
            "examples": examples,
            **structured_response,
        }

        append_to_json_file(output_path, result)
        print(f"✅ Saved cluster {cluster_id} to {output_path}")

    print(f"✅ All clusters processed and saved to {output_path}")

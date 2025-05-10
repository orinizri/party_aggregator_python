def build_prompt(cluster_id, examples):
    example_text = "\n".join(f"- {r}" for r in examples)
    return (
        f"Analyze these requests from cluster {cluster_id}:\n\n"
        f"{example_text}\n\n"
        "Summarize this cluster in 3-5 words."
    )

def summarize_clusters(df, client, max_samples=3):
    summaries = {}
    clusters = sorted(df["cluster"].unique())

    for cluster_id in clusters:
        cluster_df = df[df["cluster"] == cluster_id]
        if cluster_df.empty:
            continue
        examples = cluster_df["request"].sample(min(len(cluster_df), max_samples), random_state=42).tolist()
        prompt = build_prompt(cluster_id, examples)
        summary = client.chat(prompt)
        summaries[cluster_id] = summary
        print(f"Cluster {cluster_id}: {summary}")

    return summaries
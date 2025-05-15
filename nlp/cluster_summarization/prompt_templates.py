def build_advanced_prompt(cluster_id, examples):
    example_text = "\n".join(f"- {r}" for r in examples)
    return f"""
You are a senior event strategist.

Analyze these real participant requests from cluster {cluster_id}:

{example_text}

Provide insights in the following structure:

1. Operational Enhancement:
2. Retention & Loyalty Strategy:
3. Audience Segment Description:
4. Referral Leverage Idea:
5. Confidence Rating (1-100):

If no clear theme, write: "No clear theme identified."
"""

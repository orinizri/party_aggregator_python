import re


def parse_response(response_text):
    def extract(label):
        pattern = rf"{label}:(.*?)(?=\n[1-5]\.|\Z)"
        match = re.search(pattern, response_text, re.DOTALL)
        return match.group(1).strip() if match else None

    return {
        "operational_enhancement": extract("1\\. Operational Enhancement"),
        "retention_strategy": extract("2\\. Retention & Loyalty Strategy"),
        "audience_segment": extract("3\\. Audience Segment Description"),
        "referral_leverage": extract("4\\. Referral Leverage Idea"),
        "confidence_rating": extract("5\\. Confidence Rating \\(1-100\\)"),
    }

import json

def parse_response(response: str) -> str:
    response = response.lower()
    if "support" in response:
        return "Support"
    elif "refute" in response:
        return "Refute"
    elif "nei" in response or "not enough information" in response:
        return "NEI"
    else:
        return "Unknown"


def save_predictions(predictions: list, filepath: str):
    with open(filepath, "w") as f:
        json.dump(predictions, f, indent=2)
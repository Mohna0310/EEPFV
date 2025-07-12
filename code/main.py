import pandas as pd
from tqdm import tqdm
import argparse
from api import query_openai
from prompts import generate_prompt
from eval import compute_label_accuracy
from utils import parse_response, save_predictions


def load_fever_dataset(path: str) -> pd.DataFrame:
    return pd.read_json(path, lines=True)


def run(dataset_path: str, prompt_type: str, output_path: str, setting: str):
    df = load_fever_dataset(dataset_path)
    predictions = []

    for _, row in tqdm(df.iterrows(), total=len(df)):
        claim = row['claim']
        ground_truth = row['label']
        prompt = generate_prompt(prompt_type, claim)
        response = query_openai(prompt)
        predicted_label = parse_response(response)
        predictions.append({'claim': claim, 'gt': ground_truth, 'pred': predicted_label})

    acc = compute_label_accuracy(predictions, setting=setting)
    print(f"Label Accuracy ({setting}): {acc:.2f}%")

    save_predictions(predictions, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--prompt", type=str, choices=["p1", "p2", "p3"], required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--setting", type=str, choices=["2-way", "3-way"], default="3-way")
    args = parser.parse_args()

    run(args.dataset, args.prompt, args.output, args.setting)
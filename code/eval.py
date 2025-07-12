def compute_label_accuracy(predictions: list, setting: str = "3-way") -> float:
    correct = 0
    total = 0
    for pred in predictions:
        gt = pred['gt']
        pr = pred['pred']
        if setting == "2-way" and gt == "NEI":
            continue
        if pr == gt:
            correct += 1
        total += 1
    return (correct / total * 100) if total > 0 else 0
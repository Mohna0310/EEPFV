def generate_prompt(prompt_type: str, claim: str) -> str:
    if prompt_type == "p1":
        return f'The claim is "{claim}". Select whether the claim is (a.) Support, (b.) Refute, (c.) NEI?'
    elif prompt_type == "p2":
        return f'The claim is "{claim}". Provide evidence for the claim, and based on the evidence, select whether the claim is (a.) Support, (b.) Refute, (c.) NEI?'
    elif prompt_type == "p3":
        return f'The claim is "{claim}". Can you generate 5 prompts for this claim and the answers for each of the prompts? For each of the answers, select whether that prompt is (a.) Support, (b.) Refute, (c.) NEI? Based on the prompts and the answers provided, select finally whether the claim is (a.) Support, (b.) Refute, (c.) NEI?'
    else:
        raise ValueError(f"Unknown prompt type: {prompt_type}")
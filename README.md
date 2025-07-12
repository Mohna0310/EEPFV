## Setup

```bash
pip install -r requirements.txt
```

Export your OpenAI API key:

```bash
export OPENAI_API_KEY="your-key-here"
```

## Run

```bash
python main.py --dataset data/shared_task_dev.jsonl --prompt p3 --output results.json --setting 3-way

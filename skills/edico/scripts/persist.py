import os
import json
import argparse
from datetime import datetime

def persist_data(topic, summary, sources, tags):
    # Determine the home directory dynamically
    home_dir = os.path.expanduser("~")
    webdata_dir = os.path.join(home_dir, ".webdata")
    log_file = os.path.join(webdata_dir, "research_log.jsonl")

    # Ensure the directory exists
    if not os.path.exists(webdata_dir):
        os.makedirs(webdata_dir, exist_ok=True)
        print(f"Created directory: {webdata_dir}")

    # Prepare the data object
    data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "topic": topic,
        "summary": summary,
        "sources": [s.strip() for s in sources.split(",")] if sources else [],
        "tags": [t.strip() for t in tags.split(",")] if tags else []
    }

    # Append to JSONL file
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
        print(f"Successfully persisted data to {log_file}")
    except Exception as e:
        print(f"Error persisting data: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Persist synthesized research data.")
    parser.add_argument("--topic", required=True, help="Topic of the research")
    parser.add_argument("--summary", required=True, help="Synthesized summary")
    parser.add_argument("--sources", help="Comma-separated URLs")
    parser.add_argument("--tags", help="Comma-separated tags")

    args = parser.parse_args()
    persist_data(args.topic, args.summary, args.sources, args.tags)

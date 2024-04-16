"""Replace the website placeholders with website domains from env_config
Generate the test data"""
import json
import os

from browser_env.env_config import *


def main() -> None:
    inp_paths = ["visualweb/test_shopping.raw.json"]

    for inp_path in inp_paths:
        output_dir = inp_path.replace('.raw.json', '')
        os.makedirs(output_dir, exist_ok=True)
        with open(inp_path, "r") as f:
            raw = f.read()
        raw = raw.replace("__REDDIT__", REDDIT)
        raw = raw.replace("__SHOPPING__", SHOPPING)
        raw = raw.replace("__WIKIPEDIA__", WIKIPEDIA)
        # raw = raw.replace("__CLASSIFIEDS__", CLASSIFIEDS)
        with open(inp_path.replace(".raw", ""), "w") as f:
            f.write(raw)
        data = json.loads(raw)
        for idx, item in enumerate(data):
            with open(os.path.join(output_dir, f"{idx}.json"), "w") as f:
                json.dump(item, f, indent=2)


if __name__ == "__main__":
    main()
"""Training entry point."""
import argparse
import yaml

from src.model import ConvNeXtLiteBlock


def build_model(cfg):
    blocks = [ConvNeXtLiteBlock(cfg["width"]) for _ in range(cfg["depth"])]
    return blocks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/base.yaml")
    args = parser.parse_args()
    with open(args.config, encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle)
    build_model(cfg)


if __name__ == "__main__":
    main()

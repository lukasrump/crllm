import argparse
import logging
import os
from crllm.app import app
from crllm.config.config_service import config_service


def cli():
    log_level = os.environ.get("LOGLEVEL", "INFO").upper()
    logging.basicConfig(level=log_level, format="%(asctime)s %(message)s")

    parser = argparse.ArgumentParser(
        description="Get Code Reviews from large language models."
    )

    parser.add_argument("input", help="Path to the sources")
    parser.add_argument(
        "-c", "--config", help="Path to the config file", default="crllm_config.toml"
    )
    parser.add_argument(
        "-l",
        "--loader",
        help="Loader to use",
        required=False,
        choices=["file", "git", "git_compare"],
    )

    args = parser.parse_args()

    config = {"crllm": {}}

    if args.loader:
        config["crllm"]["loader"] = args.loader

    config_service.set_config_path(args.config)
    config_service.override_config(config)

    app(args.input)


if __name__ == "__main__":
    cli()

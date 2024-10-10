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

    parser.add_argument("input_file", help="Path to the source code file")
    parser.add_argument(
        "-c", help="Path to the config file", default="crllm_config.toml"
    )

    args = parser.parse_args()
    config_service.get_config(args.c)

    app(args.input_file)


if __name__ == "__main__":
    cli()

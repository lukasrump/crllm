import argparse
import logging
import os
from crllm.init_project import init_project
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

    parser.add_argument(
        "-i", "--init", help="Initialize the config file", action="store_true"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output file for the generated code review",
        required=False,
        default="",
    )

    args = parser.parse_args()

    config = {"crllm": {"output": args.output}}

    if args.loader:
        config["crllm"]["loader"] = args.loader

    config_service.set_config_path(args.config)
    config_service.override_config(config)

    if args.init:
        init_project(args.input)
        return

    app(args.input)


if __name__ == "__main__":
    cli()

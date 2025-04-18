import os
import argparse
from dotenv import load_dotenv
from settings import Settings
from yaml import safe_load


def export_envs(environment: str = "dev") -> None:
    load_dotenv(f".env.{environment}")

    with open("secrets.yaml", "r") as f:
        secrets = safe_load(f)

    for key, value in secrets["keys"][0].items():
        os.environ[key] = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)

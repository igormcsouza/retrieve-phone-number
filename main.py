import argparse

from retrieve_phone_numbers import RetrievePhoneNumbers


parser = argparse.ArgumentParser(description="Retrieve phone numbers from files")
parser.add_argument(
    "--base-path",
    "-b",
    dest="base_path",
    type=str,
    default="data",
    help="Base Path where to look for phone numbers",
)


def main():
    args = parser.parse_args()

    executor = RetrievePhoneNumbers(base_path=args.base_path)
    executor()


if __name__ == "__main__":
    SystemExit(main())

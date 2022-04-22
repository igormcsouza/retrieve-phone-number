from retrieve_phone_numbers import RetrievePhoneNumbers


def main():
    executor = RetrievePhoneNumbers(base_path="data")
    executor()


if __name__ == "__main__":
    SystemExit(main())

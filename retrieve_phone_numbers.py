import re
from pathlib import Path
from typing import Optional, Sequence


def correct_numbers(
    country_code: Optional[str], area_code: Optional[str], number: str
) -> str:
    if country_code:
        country_code = country_code.replace(" ", "")
        country_code = country_code.replace("-", "")

        if not country_code.startswith("+"):
            country_code = f"+{country_code}"
    else:
        country_code = "+7"

    if area_code:
        area_code = area_code.replace(" ", "")
        area_code = area_code.replace("-", "")

        if not area_code.endswith(")"):
            area_code = f"({area_code})"
    else:
        area_code = "(812)"

    number = number.replace("-", "")
    number = f"{number[:3]}-{number[3:]}"

    return " ".join([country_code, area_code, number])


class RetrievePhoneNumbers:

    file_ext = ".txt"
    validation_pattern = r"(?P<country_code>\+?\d(-?|\s?))?(?P<area_code>(\(\d{3}\)|\d{3})(-?|\s?))?(?P<number>\d{7}|\d{3}\-\d{2}\-\d{2}|\d{3}\-\d{4})"

    def __init__(self, base_path: str):
        self.base_path = base_path

    def read_numbers_from_file(self) -> None:
        # This list is meant to be immutable after populated (mypy warns changes here.)
        self.raw_phone_numbers: Sequence[str] = list()

        for path in Path(self.base_path).rglob(f"*{self.file_ext}"):
            with open(path, "r") as f:
                self.raw_phone_numbers.extend(f.readlines())

    def fix_phone_numbers(self) -> None:
        self.corrected_phone_numbers: Sequence[str] = list()

        def valid_func(phone_number: str) -> Optional[str]:
            return re.match(self.validation_pattern, phone_number)

        for phone_number in self.raw_phone_numbers:
            result = valid_func(phone_number)
            if not result:
                continue

            corrected = correct_numbers(
                result.group("country_code"),
                result.group("area_code"),
                result.group("number"),
            )

            self.corrected_phone_numbers.append(corrected)

    def remove_duplicates(self) -> None:
        self.phone_numbers: Sequence[str] = list(set(self.corrected_phone_numbers))

    def __call__(self):
        self.read_numbers_from_file()
        self.fix_phone_numbers()
        self.remove_duplicates()

        print(self.phone_numbers)

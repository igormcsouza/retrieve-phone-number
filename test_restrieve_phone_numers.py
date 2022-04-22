from unittest import TestCase

from retrieve_phone_numbers import RetrievePhoneNumbers


class TestRetrievePhoneNumbers(TestCase):
    def test_expected_result(self):
        expected = [
            "+5 (123) 873-0393",
            "+7 (272) 728-2729",
            "+7 (122) 918-1928",
            "+1 (814) 172-2928",
            "+7 (815) 123-8272",
            "+4 (633) 198-9277",
            "+4 (627) 198-2221",
            "+6 (231) 192-1902",
            "+4 (980) 772-1902",
            "+9 (562) 818-2929",
            "+4 (124) 921-1102",
            "+7 (812) 920-1234",
        ]
        exec = RetrievePhoneNumbers("data")
        exec()
        result = exec.phone_numbers or None

        self.assertCountEqual(result, expected)

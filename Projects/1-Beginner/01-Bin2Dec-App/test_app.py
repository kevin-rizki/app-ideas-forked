import unittest
from app import bin2dec

class TestBin2Dec(unittest.TestCase):

		def test_bin2dec_valid_input(self):
				# Test valid binary inputs and expected decimal outputs
				test_cases = [
            ("0", 0),
            ("1", 1),
            ("10", 2),
            ("11", 3),
            ("1010", 10),
            ("1111", 15),
            ("10000000", 128)
				]

				for binary_input, expected_output in test_cases:
						with self.subTest(binary_input=binary_input):
								self.assertEqual(bin2dec(binary_input), expected_output)
				
		def test_bin2dec_invalid_input(self):
				# Test invalid binary inputs
				invalid_inputs = [
            "",  # Empty input
            "a",  # Non-binary character
            "12345",  # Binary input longer than 8 digits
            "101010101",  # Binary input longer than 8 digits
						"101A01"
				]

				for invalid_input in invalid_inputs:
						with self.subTest(invalid_input=invalid_input):
								with self.assertRaises(ValueError):
										bin2dec(invalid_input)

if __name__ == '__main__':
		unittest.main()
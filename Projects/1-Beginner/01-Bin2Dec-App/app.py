def bin2dec(binary_str):
		"""
		Conver a binary string to its equivalent decimal value.

		Args:
				binary_str (str): A valid binary string of up to 8 digits.

		Returns:
				int: The equivalent decimal value.
		"""
		if not binary_str:
				raise ValueError("Input cannot be empty")

		if len(binary_str) > 8:
				raise ValueError("Input exceeds maximum length of 8 digits")
		
		# Convert binary string to decimal
		decimal_value = 0
		for i, digit in enumerate(reversed(binary_str)):
				if digit not in ('0', '1'):
						raise ValueError("Input is not a valid binary string")
				decimal_value += int(digit) * (2 ** i)
			
		return decimal_value


if __name__ == "__main__":
		binary_input = input()

		decimal_output = bin2dec(binary_input)

		print("Binary:", binary_input)
		print("Decimal: ", decimal_output)
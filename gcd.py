def n_base_to_decimal(n, number):
    """Convert a number from n-base to decimal"""
    s = str(number)
    decimal = 0
    for i in range(len(s)):
        decimal += int(s[i]) * n ** (len(s) - i - 1)
    return decimal

def decimal_to_n_base(n, decimal):
	"""Convert a number from decimal to n-base"""
	s = ""
	while decimal > 0:
		s += str(decimal % n)
		decimal = decimal // n
	return s[::-1]

def n_base_to_m_base(n, m, number):
	"""Convert a number from n-base to m-base"""
	return decimal_to_n_base(m, n_base_to_decimal(n, number))

print(n_base_to_m_base(2, 10, 1101))
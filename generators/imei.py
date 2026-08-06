import random

class IMEIGenerator:
    @staticmethod
    def _calculate_luhn_check_digit(base_digits):
        total = 0
        for i, digit in enumerate(reversed(base_digits)):
            n = int(digit)
            if i % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return str((10 - (total % 10)) % 10)

    @staticmethod
    def generate():
        # Generate 14 random digits (TAC + Serial)
        base = ''.join([str(random.randint(0, 9)) for _ in range(14)])
        check_digit = IMEIGenerator._calculate_luhn_check_digit(base)
        return base + check_digit

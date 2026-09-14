class utils:
    def reversed(self, number):
        sign = -1 if number < 0 else 1
        return sign * int(str(abs(number))[::-1])

    def formatter(self, number):
        return bin(number), oct(number)

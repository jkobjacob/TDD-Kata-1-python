from functools import reduce

class StringCalculator():
    def __init__(self):
        self.delimiter = ","

    def add(self,ip_str):
        if ip_str == "":
            return 0

        else:
            return reduce(lambda acc, num: acc + int(num),
                        ip_str.split(self.delimiter),
                        0)
from functools import reduce
import re

class StringCalculator():
    def __init__(self):
        self.delimiter = ",|\\n"

    def add(self,ip_str):
        if ip_str == "":
            return 0

        else:
            return self.sums(self.split_str(ip_str,self.delimiter))
    
    @staticmethod
    def split_str(string,delimiter):
        return re.split(delimiter,string)

    @staticmethod
    def sums(lst):
        return reduce(lambda total, num: total + int(num),
                lst,
                0)
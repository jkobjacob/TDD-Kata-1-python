from functools import reduce
import re

class StringCalculator():
    def __init__(self):
        self.delimiter = ",|\\n"

    def add(self,ip_str):
        if ip_str == "":
            return 0

        else:
            [self.delimiter,ip_str] = self.process_ip_for_delimiter(ip_str)
            return self.sums(self.split_str(ip_str,self.delimiter))
    
    def process_ip_for_delimiter(self,ip_str):
        re_obj = re.search("//(.*)\\n",ip_str)

        if re_obj != None:
            return [self.delimiter + "|" + re_obj.groups()[0], ip_str.split("\n")[1]]
        
        return [self.delimiter,ip_str]

    @staticmethod
    def split_str(string,delimiter):
        return re.split(delimiter,string)

    @staticmethod
    def sums(lst):
        return reduce(lambda total, num: total + int(num),
                lst,
                0)
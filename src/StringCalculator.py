from functools import reduce
import re

class StringCalculator():

    def __init__(self):
        self.delimiter = ",|\\n"
        self.add_called_count = 0

    
    def add(self,ip_str):
        self.delimiter = ",|\\n"
        self.add_called_count = self.inc(self.add_called_count)

        if ip_str == "":
            return 0

        else:
            [self.delimiter,ip_str] = self.process_ip_for_delimiter(ip_str)
            
            return self.sums(self.split_str(ip_str,self.delimiter))
    
    #regex matching to capture delimiters in various scenarios and get the input string via a new line split
    def process_ip_for_delimiter(self,ip_str):
        re_obj = re.search("\\[(.*)\\]\\[(.*)\\]",ip_str) or re.search("\\[(.*)\\]",ip_str) or re.search("//(.*)\\n",ip_str)

        if re_obj != None:
            return [self.delimiter + "|" + self.escape(re_obj.groups()), ip_str.split("\n")[1]]
        
        return [self.delimiter,ip_str]

    
    def get_called_count(self):
        return self.add_called_count

    
    #helper to escape the delimiters due to its ambiguity in regex too. Ex: '*' denotes one or many
    @staticmethod
    def escape(i_str):
        tmp = list(map(lambda z: "".join(list(map(lambda y: "\\" + y,z))),i_str))
        return "|".join(tmp)

    
    @staticmethod
    def inc(x):
        return x + 1

    
    #split the input string using regex with the available delimiters as option.
    @staticmethod
    def split_str(string,delimiter):
        return re.split(delimiter,string)

    
    #computes the total, ignores nums > 1000, raises exception if non positive integers are found.
    @staticmethod
    def sums(lst):
        [sum_total, neg_string] = reduce(lambda acc, num: (lambda total, neg_str, n: [total + n, neg_str] if (n > 0) and (n < 1001)
                                                    else [total, num] if (neg_str == "") and (n < 0)
                                                        else [total, neg_str + " " + num] if (n < 0)
                                                            else [total, neg_str])(acc[0],acc[1],int(num)),
                                    lst,
                                    [0,""])
        
        if neg_string != "":
            raise ValueError("negatives not allowed " + neg_string)

        else:
            return sum_total
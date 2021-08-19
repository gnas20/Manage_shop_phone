import re


class MyFeatures(object):
    
    @staticmethod
    def is_valid_name(name):
        return re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)
    
    @staticmethod
    def is_valid_phone_number(phone_number):
        return phone_number.isdigit()
    
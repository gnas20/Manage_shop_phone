from MyFeatures import *
import numbers
from datetime import date, datetime
class Post:
    def __init__(self, id, name_customer, address, phone_number, name_product, amount, price, stt='ORDERED', date=None):
        self._id = id
        self._name_customer = name_customer
        self._address = address
        self._phone_number = phone_number
        self._name_product = name_product
        self._amount = amount
        self._price = price
        self._status = stt
        
        if date == None:
            self._date = datetime.today()
        else:
            self._date = date
    
    @property
    def total_money(self):
        return self._amount * self._price
    
    # id
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
            return True
        return False
    
    # name_customer
    @property
    def name_customer(self):
        return self._name_customer
    
    @name_customer.setter
    def name_customer(self, name_customer):
        # Check valid name
        if MyFeatures.is_valid_name(name_customer):
            self._name_customer = name_customer
            return True
        
        return False
    
    # address
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        if isinstance(address, str):
            self._address = address
            return True
        return False
    
    # phone_number
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if MyFeatures.is_valid_phone_number(phone_number):
            self._phone_number = phone_number
            return True
        return False
    
    # name_product
    @property
    def name_product(self):
        return self._name_product
    
    @name_product.setter
    def name_product(self, name_product):
        if isinstance(name_product, str):
            self._name_product = name_product
            return True
        return False    
    
    # amount
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int):
            self._amount = amount
            return True
        return False
    
    # price
    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, price):
        if isinstance(price, numbers.Number):
            self._price = price
            return True
        return False
    
    # status
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        if status in ["ORDERED", "DELIVERING", "PAID"]:
            self._status = status
            return True
        return False
    
    # date
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, str_date=None):
        if str_date == None:
            self._date = date.today()
            return True
        else:
            try:
                self._date = datetime.strptime(str_date, "%d/%m/%Y")
                return True
            except:
                return False
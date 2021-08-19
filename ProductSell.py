from MobilePhone import *


class ProductSell(MobilePhone):
    def __init__(self, id='', name='', company_name='', price='', amount=''):
        super().__init__(id, name, company_name, price)
        self._amount = amount
        
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int) and amount >= 0:
            self._amount = amount
            return True
        return False



class MobilePhone:
    def __init__(self, id='', name='', company_name='', price=''):
        self._id           = id
        self._name         = name
        self._company_name = company_name
        self._price        = price

    
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
    
    # name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
            return True
        return False
    
    # company_name
    @property
    def company_name(self):
        return self._company_name
    
    @company_name.setter
    def company_name(self, company_name):
        if isinstance(company_name, str):
            self._company_name = company_name
            return True
        return False
    
    # price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int) or isinstance(price, float):
            self._price = price
            return True
        return False

    def is_valid_info(self):
        if self._id == '' or self._name == '' or self._price == '' or self.company_name == '':
            return False
        return True
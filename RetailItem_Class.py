class RetailItem:
    def __init__(self, desc, inv, price):
        self.__desc = desc
        self.__inv = inv
        self.__price = price

    def set_desc(self, desc):
        self.__desc = desc

    def set_inv(self, inv):
        self.__inv = inv

    def set_price(self, price):
        self.__price = price

    def get_desc(self):
        return self.__desc

    def get_inv(self):
        return self.__inv

    def get_price(self):
        return self.__price
    
itemOne = RetailItem('Jacket', 12, 59.95)
itemTwo = RetailItem('Designer Jeans', 40, 34.95)
itemThree = RetailItem('Shirt', 20, 24.95)

print('Item #1:', itemOne.get_desc(), '-', 'Unit inventory:', itemOne.get_inv(), '-', 'Unit price:', itemOne.get_price())
print('Item #2:', itemTwo.get_desc(), '-', 'Unit inventory:', itemTwo.get_inv(), '-', 'Unit price:', itemTwo.get_price())
print('Item #3:', itemThree.get_desc(), '-', 'Unit inventory:', itemThree.get_inv(), '-', 'Unit price:', itemThree.get_price())

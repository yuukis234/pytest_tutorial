# ******************** #
class VendingMachine:
    def __init__(self, payment, product):
        self.payment = payment
        self.product = product

    def payments(self):
        return self.payment

    def product_sum (self):
        price_list = map(lambda x: x[1], self.product)
        return sum(price_list)
    
    def change(self):
        return self.payment - self.product_sum()

# ******************** #
COUNT = 220
PRODUCT = [["オレンジジュース", 110], ["烏龍茶", 100]]

# ******************** #


# ******************** #
def test_sum():
    vending_machine = VendingMachine(COUNT, PRODUCT)
    assert vending_machine.product_sum() == 210

def test_sum_max():
    MAX_PRODUCT = [["オレンジジュース", 110], ["烏龍茶", 100], ["オレンジジュース", 110], ["烏龍茶", 100], ["オレンジジュース", 110], ["烏龍茶", 100], ["オレンジジュース", 110], ["烏龍茶", 100], ["オレンジジュース", 110], ["烏龍茶", 100],]
    vending_machine = VendingMachine(COUNT, MAX_PRODUCT)
    assert vending_machine.product_sum() == 1050

def test_change():
    vending_machine = VendingMachine(COUNT, PRODUCT)
    assert vending_machine.change() == 10

def test_changen_max():
    MAX_COUNT = 10000
    vending_machine = VendingMachine(MAX_COUNT, PRODUCT)
    assert vending_machine.change() == 9790

# ******************** #
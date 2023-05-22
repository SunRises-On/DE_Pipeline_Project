from decimal import Decimal

class Receipt:
    # items = list of item objects
    # tax = tax
    def __init__(self, items = [], tax = 0):
        self.items = items
        self.tax = tax
        self.subtotal = 0
        self.total = 0
        

    def calc_subtotal(self):
        #Turn into Decimal type object
        self.subtotal = Decimal(0)

        for item in self.items:
            price = Decimal(item.price)
            self.subtotal += price
        #round to 2 decimal places
        self.subtotal = round(self.subtotal, 2)

    def calc_total(self):

        self.tax = Decimal(self.tax)
        item_tax = self.tax * self.subtotal

        #round 2 decimal places
        item_tax = round(item_tax, 2)

        self.total = item_tax + self.subtotal

    def __str__(self):
        return f"""
        tax = {self.tax} \n 
        items = {self.items}\n
        subtotal = {self.subtotal}\n
        total = {self.total} \n
    """
    
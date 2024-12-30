#24
class Shop:
    def __init__(self, base, dis_p, tax_p):
        self.base = base
        self.dis_p = dis_p
        self.tax_p = tax_p

    def cal_price(self):
        if self.base < 0 or self.dis_p < 0 or self.tax_p < 0:
            raise ValueError("Base price, discount percentage, and tax percentage cannot be negative.")
        dis = self.dis_p / 100
        tax = self.tax_p / 100
        price = (self.base - dis) + tax
        return price

    def show(self):
        try:
            price = self.cal_price()
            print(f"The final price is: {price:.2f}")
        except ValueError as ve:
            print(ve)


try:
    base = float(input("Enter Base price: "))
    dis_p = float(input("Enter Discount percentage: "))
    tax_p = float(input("Enter Tax percentage: "))
    if base < 0 or dis_p < 0 or tax_p < 0:
        raise ValueError("Base price, discount percentage, and tax percentage cannot be negative.")
    
    s = Shop(base, dis_p, tax_p)
    s.show()

except ValueError as ve:
    print(f"Error: {ve}")

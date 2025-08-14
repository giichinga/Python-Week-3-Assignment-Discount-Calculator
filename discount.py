print("What is the price of the product?")
price = float(input())
print("What is the discount percentage?")
discountPercent = float(input())

def calculateDiscount(price, discountPercent):
    discountAmount = price * (discountPercent / 100)
    return discountAmount

discountAmount = calculateDiscount(price, discountPercent)
print(f"Discount Amount: Ksh.{discountAmount:.2f}")
print(f"Final Price after Discount: Ksh.{price - discountAmount:.2f}")
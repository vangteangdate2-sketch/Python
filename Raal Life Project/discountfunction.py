# Build a Apply Discount Function

def apply_discount(price,discount):
    if not isinstance(price,(int, float)):
        return('The price should be a number')
    if not isinstance(discount,(int, float)):
        return('The discount should be a number')
    if price <= 0:
        return('The price should be greater than 0')
    if discount < 0 or discount > 100:
        return('The discount should be between 0 and 100')
    if discount == 100:
        return(0)

    return price - (price * discount / 100)

total = apply_discount(100,20)
print(total)

total1 = apply_discount(200,50)
print(total1)

total2 = apply_discount(50,0)
print(total2)

total4 = apply_discount(10,100)
print(total4)

total3 = apply_discount(74.5,20.0)
print(total3)




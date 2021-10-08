price =100000
has_good_credit = False
if has_good_credit:
    price-=price*10/100
else:
    price-=price*20/100
print(f"Down payment : {price}")
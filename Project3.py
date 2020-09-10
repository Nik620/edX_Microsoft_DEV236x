# [ ] create, call and test 
# then PASTE THIS CODE into edX

order_amount = float(input("Enter cheese order weight (numeric value in kg): "))
unit_price = 5.03 #$5/kilogram
min_order = 1.5
max_order = 100.0

if order_amount >= max_order:
    print(order_amount,"is more than currently available stock.")
elif order_amount < min_order:
    print(order_amount,"is below minimum order amount.")
else:
    print(order_amount,"kg costs","$" + str(order_amount * unit_price))

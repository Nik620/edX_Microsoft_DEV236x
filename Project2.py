# [ ] create, call and test fishstore() function 
# then PASTE THIS CODE into edX
def fishstore(fish, price):
    output = "Fish Type: " + fish + " costs $" + price
    return output

fish_entry = input("enter fish name: ")
price_entry = input("enter fish price (no symbols): ")
print(fishstore(fish_entry, price_entry))

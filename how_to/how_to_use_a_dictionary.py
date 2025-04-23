# create a dictionary
# dictionary_name = { key : value }
shopping = {
    "eggs" : 1.30,
    "bread" : 1.20,
    "milk" : 1.45,
    "chocolate" : 2.50,
}

# loop through a dictionary
for item in shopping:
    price = shopping.get(item)
    print(f"item {item} at £{price}")

# Loop through a dictionary another way
for item, price in shopping.items():
    print(f"item {item} £{price}")

# get the value of an item
item_price = shopping.get("chocolate")
print(f"item price {item_price}")

# get the value of an item another way
item_price = shopping["chocolate"]
print(f"item price {item_price}")
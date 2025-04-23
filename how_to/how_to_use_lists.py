# create a list
shopping_list = ['eggs','milk','bread','chocolate']

# loop through a list
for item in shopping_list:
    # print to terminal, f strings allow you to pass variables
    print(f"item {item}")

# count number of items
number_of_items = len(shopping_list)
print(f"the number of shopping items: {number_of_items}")

# calculate the available indexs for the shopping list
indexes = list(range(0, len(shopping_list)))
print(f"the available indexes: {indexes}")

# select the first item
first_item = shopping_list[0]
print(f"the first item: {first_item}")

# select the last item
last_item = shopping_list[3]
print(f"the last item: {last_item}")

# select the last item another way
last_item_again = shopping_list[-1]
print(f"the last item again: {last_item_again}")
# Reflection 1:
# The most surprising thing to me is that one list can be changed directly with
# methods like append, remove, and sort. I expected that I would need to create
# a new list each time, but Python can update the original list in place.
#
# Reflection 2:
# In a finance class, a Python list could save time when working with a group of
# daily sales, prices, or expenses. Instead of calculating totals, averages, and
# highest values separately in Excel, Python could complete all of them at once.


# Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print("Exercise 1")
print(inventory)
print(len(inventory))


# Exercise 2: Index practice
middle_index = len(inventory) // 2
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
print(inventory[middle_index])


# Exercise 3: Slicing
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4: Modify
print("\nExercise 4")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5: Tuple comparison
print("\nExercise 5")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: tuples cannot be changed after they are created.")
    print("Tuples are useful for coordinates because the values stay fixed.")

print(coords)


# Exercise 6: Average of a list of sales
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]
sales_total = sum(sales)
sales_count = len(sales)
sales_average = sales_total / sales_count

print(f"Total: {sales_total}")
print(f"Count: {sales_count}")
print(f"Average: {sales_average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")


# Exercise 7: Accumulator pattern
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(f"Original: {prices}")
print(f"Discounted: {discounted}")


# Exercise 8: Filter above threshold
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

high_sales_average = sum(high_sales) / len(high_sales)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {high_sales_average:.2f}")

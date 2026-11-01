# Lab 7 Self-Assessment
#
# 1. The first bug I spotted in Exercise 5 was the missing colon after the for
#    loop. I found it by reading the traceback from the bottom. This tells me
#    that I am starting to use Python's error messages to locate syntax errors,
#    but I still need print statements and line-by-line tracing for logic errors.
#
# 2. apply_discount(price, tier) takes an original price and a customer tier.
#    It checks whether the tier is gold, silver, bronze, or something else and
#    returns the price after the correct discount. A colleague could call it
#    using a price and tier without needing to read the function body.
#
# 3. AI disclosure: I used ChatGPT/Codex as a debugger and explainer while
#    completing this lab. It helped me understand the errors, organize the six
#    exercises in one file, and check my finished script. I reviewed the code
#    and comments so that I understand what each function and fix does.


# --- Exercise 1 ---
def calculate_tax(price, rate):
    """Return the tax amount for a price and tax rate."""
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    """Return the price after applying a customer-tier discount."""
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


for customer_tier in ["gold", "silver", "bronze", "none"]:
    discounted_price = apply_discount(200, customer_tier)
    print(f"{customer_tier}: ${discounted_price:.2f}")


# --- Exercise 3 ---
discounted_price = apply_discount(200, "gold")
tax_amount = calculate_tax(discounted_price, 0.07)
price_after_tax = discounted_price + tax_amount

print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${price_after_tax:.2f}")


def final_price(price, tier, tax_rate):
    """Apply a tier discount, add tax, and return the final price."""
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

# Bug 1: total = sale replaced the total on every loop. It must add each sale.
sales_total = 0
for sale in sales:
    sales_total += sale
print(f"Total: ${sales_total}")

# Bug 2: The original for statement was missing the required colon.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3: <= reached len(sales), which is outside the list. Use < instead.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
x = 100  # This variable is global.


def double_it():
    # This x is local, so it only exists inside this function.
    x = 999
    return x * 2


# The local x does not replace the global x, so these print 100, 1998, 100.
print(x)
print(double_it())
print(x)

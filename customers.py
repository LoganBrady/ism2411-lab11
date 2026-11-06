# customers.py 
# Author: [Logan Brady]
# Module 11 lab : customer dictionary & look up

# Reflection 1:
# I would use .get() when I am not sure if a key exists because it prevents
# the program from crashing. I would use bracket notation when I know the key
# should exist and want to retrieve its value directly.

# Reflection 2:
# This pattern reminds me of using SUMIF in Excel because it adds values
# based on categories. Python can be more useful for large datasets because
# it can automatically process many records using loops.

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "Alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2 ---")
customer["phone"] = '555-5555' #Adding a new key-value pair to the dictionary
print(customer)
customer["tier"] = "platinum" #Updating the value of an existing key in the dictionary
print(customer)
del customer["email"] #Removing a key-value pair from the dictionary
print(customer)

print(customer.get("ytd_spend", 0 )) #Using the get() method to retrieve a value from the dictionary, with a default value if the key is not found

print ("--- Exercise 3 ---")
print(customer.get("email", "no email on file")) #Using the get() method to retrieve a value from the dictionary, with a default value if the key is not found

try: 
     print(customer["email"]) #Using the square bracket notation to retrieve a value from the dictionary, which will raise a KeyError if the key is not found
except KeyError as error:
    print("keyerror caught:", error) #Catching the KeyError and printing an error message

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("--- Exercise 5 ---")
tier_discounts = { 
    "bronze": 0.0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
purchase = 200 
discount_rate = tier_discounts.get(customer["tier"], 0.0) #Using the get() method to retrieve a value from the dictionary, with a default value if the key is not found
final_price = purchase * (1 - discount_rate) #Calculating the final price after applying the discount
print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate * 100}%")
print(f"Final price: ${final_price:.2f}")


print("--- Exercise 6 ---")

customers = [{"name": "Bob", "tier": "silver", "ytd_spend": 3200},
             {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
             {"name": "David", "tier": "bronze", "ytd_spend": 450}]

purchase = 300

for record in customers:
    rate = tier_discounts.get(record["tier"], 0.0)
    discount = purchase * rate

    print(
        f"Name: {record['name']} | "
        f"Tier: {record['tier']} | "
        f"Discount: ${discount:.2f}"
    )

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}
for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - Only {details['stock']} left")

print("--- Exercise 8 ---")
transactions = [{"region": "South", "amount": 300},
                {"region": "North", "amount": 150},
                {"region": "South", "amount": 200},]

sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")
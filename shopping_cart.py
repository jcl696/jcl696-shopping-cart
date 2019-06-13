

# Basic Requirements 

#TODO
#The date and time of the beginning of the checkout process, formatted in a human-friendly way(e.g. 2019-06-06 11: 31 AM)

import datetime


products = [
    {"id": 1, "name": "Chocolate Sandwich Cookies",
        "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id": 2, "name": "All-Seasons Salt", "department": "pantry",
        "aisle": "spices seasonings", "price": 4.99},
    {"id": 3, "name": "Robust Golden Unsweetened Oolong Tea",
        "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id": 4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce",
        "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id": 5, "name": "Green Chile Anytime Sauce", "department": "pantry",
        "aisle": "marinades meat preparation", "price": 7.99},
    {"id": 6, "name": "Dry Nose Oil", "department": "personal care",
        "aisle": "cold flu allergy", "price": 21.99},
    {"id": 7, "name": "Pure Coconut Water With Orange",
        "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id": 8, "name": "Cut Russet Potatoes Steam N' Mash",
        "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id": 9, "name": "Light Strawberry Blueberry Yogurt",
        "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id": 10, "name": "Sparkling Orange Juice & Prickly Pear Beverage",
        "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id": 11, "name": "Peach Mango Juice", "department": "beverages",
        "aisle": "refrigerated", "price": 1.99},
    {"id": 12, "name": "Chocolate Fudge Layer Cake",
        "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id": 13, "name": "Saline Nasal Mist", "department": "personal care",
        "aisle": "cold flu allergy", "price": 16.00},
    {"id": 14, "name": "Fresh Scent Dishwasher Cleaner",
        "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id": 15, "name": "Overnight Diapers Size 6",
        "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id": 16, "name": "Mint Chocolate Flavored Syrup",
        "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id": 17, "name": "Rendered Duck Fat", "department": "meat seafood",
        "aisle": "poultry counter", "price": 9.99},
    {"id": 18, "name": "Pizza for One Suprema Frozen Pizza",
        "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id": 19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend",
        "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id": 20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink",
        "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]   


# Info Display / Inputs 


subtotal_price = 0
nyc_sales_tax = 0
selected_ids = []

while True:
     selected_id=input("Please input a product identifier: ")  # (string)

     if selected_id == "DONE":
         break
     else:
         selected_ids.append(selected_id)

## Info Display /  Outputs


print("-------------")
print("JOE'S GROCERY EMPORIUM")
print("-------------")

print("WEB: www.joesgroceryemporium.com")
print("PHONE: 888-555-1212")
print("ADDRESS: 14 West Walnut Avenue, New York, NY 10011")

# The date and time of the beginning of the checkout process, formatted in a human-friendly way(e.g. 2019-06-06 11: 31 AM)

now = datetime.datetime.now()

short_now = now.strftime("%Y-%m-%d " + "%I:" + "%M:" + "%S")

if short_now > str(11):
    print("CHECKOUT TIME: " + short_now + " PM") # placeholder until finding a better way 
else:
    print("CHECKOUT TIME: " + short_now + " AM") #placeholder until finding a better way

  
#print("CHECKOUT TIME: " + str(short_now)) # may still use this


print("-------------")

print("Shopping cart items:")



for selected_id in selected_ids:
     matching_products=[p for p in products if str(p["id"]) == str(selected_id)]  # matching_products = list
     matching_product = matching_products[0]
     subtotal_price = subtotal_price + matching_product["price"]
     nyc_sales_tax = nyc_sales_tax + (.08875 * matching_product["price"])

     print("+ " + matching_product["name"] + " " + "(${0:.2f})".format(matching_product["price"]))




print("-------------")


total_price = (subtotal_price + nyc_sales_tax)


print("Subtotal:" + " " + "${0:.2f}".format(subtotal_price))


print("Plus NYC Sales Tax (8.875%):" + " " + "${0:.2f}".format(nyc_sales_tax))


print("Total: " + "${0:.2f}".format(total_price)) # string formatting turns float --> str


print("-------------")


print("Thank you for your business, please come again!")



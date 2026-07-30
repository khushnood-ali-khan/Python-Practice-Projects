#               Shopping Cart ⭐⭐⭐
# Ask the user how many products they want.

#    For each product:
#    Product name
#    Price
#    Quantity

# Store data using dictionaries inside a list.

#    Finally display:
#    Item
#    Price
#    Qty
#    Subtotal

#    Also print:
#    Total Bill
#    Most Expensive Item
#    Cheapest Item

productsDetails = {
    "product_name" : [],
    "Price" : [],
    "Quantity" : [],
    "Subtotal" : []
}

expensive_item = 0

num_products = int(input("No of Products you Want: "))

#   Take info of the product and store them in the list
for i in range(num_products):
    prod_name = input(f"\nEnter {i+1} Product Name: ")
    prod_price = float(input("Price: "))
    no_qty = int(input("Quantity: "))

    productsDetails["product_name"].append(prod_name)
    productsDetails["Price"].append(prod_price)
    productsDetails["Quantity"].append(no_qty)

#   List down each item, quantity and there sum
for k in range(len(productsDetails["product_name"])):
    
    names = productsDetails['product_name'][k]
    prices = productsDetails['Price'][k]
    Qty = productsDetails['Quantity'][k]
    productsDetails["Subtotal"].append(prices * Qty)

    print("\n----------EACH ITEM LIST--------\n")
    print(f"Item: {names}")
    print(f"Price: {prices}")
    print(f"Qty: {Qty}")
    print(f"Subtotal: {productsDetails["Subtotal"][k]}")

cheap_item = productsDetails["Price"][0]
total = 0

# Calculate total bill and find the cheapest and expensive
for j in range(len(productsDetails["product_name"])):
    total += productsDetails["Subtotal"][j]
    if productsDetails:
        if productsDetails["Price"][j] > expensive_item:
            expensive_item = productsDetails["Price"][j]
        if productsDetails["Price"][j]< cheap_item:
            cheap_item = productsDetails["Price"][j]

# Print the final bill
print("\n----------BILL------------\n")
print(f"Total Bill: {total}")
print(f"Expensive Item: {expensive_item}")
print(f"Cheapest Item: {cheap_item}")
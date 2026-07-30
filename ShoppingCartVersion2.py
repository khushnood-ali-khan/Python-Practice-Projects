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

productList = []
subtotal = []

def product_fuc():
    # the loop will take input until the value a right type
    while True:
        no_of_product = input("Number of different products: ")
        if no_of_product.isdigit():         # isdigit() function checks if the value is a digits type
            no_of_product = int(no_of_product)
            return no_of_product
        else:
            print("Enter a Valid Number.")

def each_product(product_value):

    for i in range(product_value):      #the loop will run to the number of product

        while True:             # while loop will run until the type of the entry is right
            name = input(f"\n{i+1} Product Name: ")
            price = input("Price: ")
            quantity = input("Quantity: ")

            # this will check if the price and quantity are the right type (digit type, not negative or zero)
            if price.isdigit() and quantity.isdigit():
                price = float(price)
                quantity = int(quantity)
                product = {             # assigning the values too dictionary
                    "name" : name,
                    "price": price,
                    "quantity" : quantity
                }
                productList.append(product)     # each product will have it's own dictionary inside list
                break
            else:
                print("Invalid entry.")
            

def bill_fuc(product_list):
    print("\n-----------ITEM LIST------------")
    
    for i in product_list:
        subtotal.append(i['price']*i['quantity'])
        print(f"Name: {i['name']} Price: {i['price']} Quantity: {i['quantity']} Subtotal: {subtotal}")

    total = 0
    cheap = 0
    expensive = 0
    print("\n---------FINAL BILL---------")
    for k in product_list:
        total += subtotal[k]
        if cheap > k['price']:
            cheap += k['price']
            cheap_item += k['name']
        if expensive < k['price']:
            expensive += k['price']
            exp_item += k['name']

    print(f"Total Bill: {total}")
    print(f"Most Expensive Item: {exp_item} Price: {expensive}")
    print(f"Cheapest Item: {cheap_item} Price: {cheap}")


def main():
    product = product_fuc()
    list_of_product = each_product(product)
    bill = bill_fuc(productList)


main()
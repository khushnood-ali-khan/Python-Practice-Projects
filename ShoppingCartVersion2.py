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
    # printing the item list and indivisual bill of each item
    print("\n-----------------------ITEM LIST-----------------------")
    for i in range(len(product_list)):
        current_dic = product_list[i]
        subtotal.append(current_dic['price']*current_dic['quantity'])
        print(f"Name: {current_dic['name']}\t|Price: {current_dic['price']}   |Quantity: {current_dic['quantity']}  |Subtotal: {subtotal[i]}  |")

    total = 0
    cheap = product_list[0]['price']        #consider the 1st element is a cheapest product 
    expensive = 0
    exp_item = product_list[0]['name']      
    cheap_item = product_list[0]['name']

    #calculating the final bill and finding the cheapest and most expensive item
    for k in range(len(product_list)):
        total += subtotal[k]
        current_dic = product_list[k]

        if cheap > current_dic['price']:        # if the condition is true the cheapest item price and name will be updated 
            cheap = current_dic['price']
            cheap_item = current_dic['name']

        if expensive < current_dic['price']:
            expensive = current_dic['price']
            exp_item = current_dic['name']

    print("\n---------FINAL BILL---------")
    print(f"Total Bill: {total}")
    print(f"Expensive One: {exp_item}  Price: {expensive}")
    print(f"Cheapest One: {cheap_item}  Price: {cheap}")


def main():
    product = product_fuc()
    list_of_product = each_product(product)
    bill = bill_fuc(productList)


main()
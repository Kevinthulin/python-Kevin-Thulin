def main():

    
    while True:
        print_menu()
        
        choice = input("\n Enter a number between (1-10): ")

        if choice == "1":
            name = input("enter the name of the product: ").capitalize()
            while True:
                pid_input = input("enter the Id of the product: ")
                if pid_input.isdigit():
                    pid = int(pid_input)
                    break
                else:
                    print("enter a number to store its ID, letters are not accepted")
            products = add_product(products, name, pid)
            print(f"you have added {name} to the inventory")

        elif choice == "2":
            pid = int(input("enter the product ID: "))
            quant = int(input("Enter the quantity of the product: "))
            products = stock_product(products, pid, quant)
            print(f"You have added {quant} to the inventory with the {pid} ID")

        elif choice == "3":
            pid = int(input("What is the ID of the product: "))
            sold = int(input("The mount sold of the product: "))
            products = sell_product(products, pid, sold)
            print(f"You sold {sold} of the item with ID {pid}")

        elif choice == "4":
            pid = int(input("Enter the ID of the item: "))
            get_product_quantity(products, pid)
            print(f"you have {get_product_quantity} left")

        elif choice == "5":
            thresh = int(input("Enter a number to see if you have low stock on something: "))
            low_stock = list_low_stock(products, thresh)
            print(f"you have low stock:")
            for product in low_stock:
                print(f"ID {product['product_id']}, Name: {product['product_name']}, Quantity: {product['quantity']}")
            

        elif choice == "6":
            no_stock_products = out_of_stock(products)
            print(f"You have no more stock of:")
            for product in no_stock_products:
                print(f"Name: {product['product_name']}, ID: {product['product_id']}")

        elif choice == "7":
            for product in products:
                print(f"Name: {product['product_name']}, ID: {product['product_id']}")

        elif choice == "8":
            total_stock = total_quantity(products)
            print(f"you have total stock of: ")
            for product in products:
                print(f"{total_stock} in your inventory")

        elif choice == "9":
            sorted_list = sort_items(products)
            print("here comes the sorted list: ")
            for product in sorted_list:
                print(f"ID {product['product_id']}, Name: {product['product_name']}, Quantity: {product['quantity']}")

        elif choice == "10":
            print("you have exited the program")
            break


                     
def add_product(products, product_name, product_id):
    new_products = {
        "product_name": product_name,
        "product_id": product_id,
        "quantity": 0
    }

    products.append(new_products)
    return products

def stock_product(products, product_id, amount):
    for product in products:
        if product["product_id"] == product_id:
            product["quantity"] += amount
            break

    return products


def sell_product(products, product_id, amount):
    for product in products:
        if product["product_id"] == product_id:
            product["quantity"] -= amount
            break
    return products

def get_product_quantity(products, product_id):
    for product in products:
        if product["product_id"] == product_id:
            return product["quantity"]
    return "Product not found"

def list_low_stock(products, threshold):
    low_on_products = [product for product in products if product['quantity'] < threshold]
    return low_on_products


def out_of_stock(products):
    no_stock_left = [product for product in products if product['quantity'] == 0]
    return no_stock_left

def total_quantity(products):
    total_quant = sum(product['quantity'] for product in products)
    return total_quant

def sort_items(products):
    print("1. sort by name")
    print("2. sort by id")
    print("3. sort by quantity")
    
    choice = input("\nchose a number between (1-3)")
    
    if choice == "1":
        sort_key = sorted(products, key=lambda x: x['product_name'])

    elif choice == "2":
        sort_key = sorted(products, key=lambda x: x['product_id'])

    elif choice == "3":
        sort_key = sorted(products, key=lambda x: x['quantity'])
    else:
        print("not a valid number")
        return products
    
    return sort_key

def update_product_informataion():
    ...

    
def print_menu():

    print("\nProduct in inventory")
    print("1. Add a product to the inventory")
    print("2. Stock a product")
    print("3. Sell a Product")
    print("4. Quantity of a product")
    print("5. Any products low in stock")
    print("6. Is any product out of stock")
    print("7. Print out all the items from the inventory")
    print("8. Print out the total stock of items")
    print("9. Print inventory in order")
    print("10 To exit the program")

if __name__ == "__main__":
    main()
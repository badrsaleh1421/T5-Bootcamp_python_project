import pyfiglet  
def welcome(user):
       

       result = pyfiglet.figlet_format(f'hello {user}', font="weird")
       print(result)
       print(f"\nHello! {user}.\n")
       
def admin():
    global products
    result = pyfiglet.figlet_format('WELLCOME ADMIN ', font="weird")
    print(result)
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Logged in as " + username)
    
    while True:
        print()
        print('your access from 7 -> 10 and 0 for exit ')
        print("Categories: \n 1. Footwear \n 2. Clothing \n 3. Headwear \n 4. Show cart \n 5. To complete your payment \n 6. Edit your cart  \n 7. Modify product information \n 8. Modify product category \n 9. Add a new product \n 10. Delete a product \n 0. Quit")
        # print('1: Modify product information')
        # print('2: Modify product category')
        # print('3: Add a new product')
        # print('4: Delete a product')
        # print('0: Quit')
        option = input('Please choose an option: ')
        
        if option == '7':
            for key, product in products.items():
                print(f'{key}: {product["name"]} - Category: {product["category"]} - Price: Rs.{product["price"]}')
            try:
                choice = int(input('Select a product to modify (0 to exit): '))
                if choice == 0:
                    break
                if choice in products:
                    new_name = input('Enter new product name: ')
                    new_price = int(input('Enter new price: '))
                    products[choice]['name'] = new_name
                    products[choice]['price'] = new_price
                else:
                    print('Invalid choice.')
            except ValueError:
                print('Invalid input. Please enter a number.')
        
        elif option == '8':
            for key, product in products.items():
                print(f'{key}: {product["name"]} - Category: {product["category"]} - Price: Rs.{product["price"]}')
            try:
                choice = int(input('Select a product to modify the category (0 to exit): '))
                if choice == 0:
                    break
                if choice in products:
                    new_category = input('Enter new category: ')
                    products[choice]['category'] = new_category
                else:
                    print('Invalid choice.')
            except ValueError:
                print('Invalid input. Please enter a number.')
        
        elif option == '9':
            print('''Pls Chose one of these catagories
                                1:Footwear 
                                2:Clothing 
                                3:Headwear              ''')
            new_product_name = input('Enter the name of the new product: ')
            new_product_category = input('Enter the category of the new product: ')
            new_product_price = int(input('Enter the price of the new product: '))
            new_product_id = max(products.keys()) + 1
            products[new_product_id] = {'name': new_product_name, 'category': new_product_category, 'price': new_product_price}
            print(f'Added new product with ID {new_product_id}.')
        
        elif option == '10':
            for key, product in products.items():
                print(f'{key}: {product["name"]}')
            try:
                product_to_delete = int(input('Select a product to delete (0 to exit): '))
                if product_to_delete == 0:
                    break
                if product_to_delete in products:
                    del products[product_to_delete]
                    print(f'Deleted product with ID {product_to_delete}.')
                else:
                    print('Invalid choice.')
            except ValueError:
                print('Invalid input. Please enter a number.')
        
        elif option == '0':
            break
        elif option in ('1', '2', '3', '4', '5', '6'):
         print('invalid adminaccess')

        else:
            print('Please choose a valid option.')

def user():
    global cart, total_price
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    welcome(username)
    print("Products: \n")
    for key, product in products.items():
            print(f'{key}: {product["name"]} - Price: Rs.{product["price"]}')
    while True:

        print()
        print("Categories: \n 1. Footwear \n 2. Clothing \n 3. Headwear \n 4. Show cart \n 5. To complete your payment \n 6. Clear your cart  \n 0. Quit")
        
        choice = input("Please choose a category: ")
        
        if choice == '1':
            display_products_by_category(f'''{(products[1]['category'])}''')
        elif choice == '2':
            display_products_by_category(f'''{(products[2]['category'])}''')
        elif choice == '3':
            display_products_by_category(f'''{(products[4]['category'])}''')
        elif choice == '0':  
            break
        elif choice =='4':
            print_cart()
        elif  choice =='5':
            payment()
            break
        elif  choice =='6':
        
            clear_cart()
            
        else:
            print('Please choose a valid category.')
def clear_cart():
    global total_price
    total_price = 0
    cart.clear()
    print('your cart is clean now')     

def display_products_by_category(category):
    global cart, total_price
    print(f'Products in Category: {category}')
    
    
    while True:
        try:
            choice = int(input(f'Select a product (0 to exit): '))
            if choice == 0:
                break
            if choice in products and products[choice]['category'] == category:
                if choice not in cart:
                    cart[choice] = 0
                cart[choice] += 1
                total_price += products[choice]['price']
                print(f'Added {products[choice]["name"]} to your cart.')
            else:
                print('Invalid choice.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def print_cart():
    global cart, total_price
    print("Your Cart:")
    for product_id, quantity in cart.items():
        product = products[product_id]
        print(f'{product["name"]} - Quantity: {quantity} - Total Price: Rs.{quantity * product["price"]}')
    print(f'Total Price: Rs.{total_price}')
def payment():
    print()
    print()


    
    print('1: paypal \n 2: mada \n 3:Visa \n')
    print()
    ent = input('please enter your choice: ')
    while True:
        if ent  == '1':

            print_cart()
            print('thank you for visit us')
            break
        elif ent  == '2':

            print_cart()
            print('thank you for visit us')
            break
        elif ent  == '3':

            print_cart()
            print('thank you for visit us')
            break
        else :
            break   


products = {
    1: {'name': 'Boots', 'category': 'Footwear', 'price': 50}, 
    2: {'name': 'Coats', 'category': 'Clothing', 'price': 100},
    3: {'name': 'Jacket', 'category': 'Clothing', 'price': 20},
    4: {'name': 'Caps', 'category': 'Headwear', 'price': 20}
}

# Initialize user variables
cart = {}
total_price = 0
while True:
    
    print()
    print('1: Admin')
    print('2: User')
    print('0: Quit')
    choice = input('Please choose an option: ')
    
    if choice == '1':
        admin()
    elif choice == '2':
        user()
    elif choice == '0':
        break
    else:
        print('Please choose a valid option.')
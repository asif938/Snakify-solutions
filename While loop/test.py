def add_book(inventory, title, author, price, quantity):
    inventory.append({'title': title, 'author': author, 'price': price, 'quantity': quantity})

def update_book(inventory, title, quantity):
    for book in inventory:
        if book['title'] == title:
            book['quantity'] += quantity
            break
    else:
        print("Book not found in inventory.")

def search_book(inventory, title):
    for book in inventory:
        if book['title'] == title:
            print("Book found in inventory:")
            print(book)
            break
    else:
        print("Book not found in inventory.")

def display_inventory(inventory):
    print("Current Inventory:")
    for book in inventory:
        print(book)

# Example usage:
inventory = [
    {'title': 'Python Programming', 'author': 'John Smith', 'price': 25.99, 'quantity': 10},
    {'title': 'Data Science Handbook', 'author': 'Emily Johnson', 'price': 29.99, 'quantity': 5}
]

add_book(inventory, 'Web Development Basics', 'Michael Brown', 19.99, 8)
update_book(inventory, 'Python Programming', 3)
search_book(inventory, 'Data Science Handbook')
display_inventory(inventory)

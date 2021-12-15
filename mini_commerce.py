# mini ecommerce store for turing-dev community
'''
This is very basic in the sense that:
    - displays inventory onLoad
    - receives input as an integer 
    - stores your cart temporarily 
    - and checks you at on request 
'''

print("Welcome to the Web Store")

#inventory = print("Here is what we have in stock")
inventory = {"1. Cup Cake": 500, "2. Coke": 200, "3. Bread": 300, "4. Milk": 250, "5. Chocolate": 150}
print("Here is what we have in stock")
for index, item in inventory.items():
    print(index, item)

buy_another = 1
total_cost, total = 0, 0
  
while buy_another != 0:
    order = int(input("Type the number corresponding to what you want to buy (e.g. 4 for milk): "))
    
    if order == 1:
        qty = int(input("How many Cup Cakes would you like?: "))
        total = qty * 500
        print(qty, f"Cup Cakes would cost you {total} naira")
    
    elif order == 2:
        qty = int(input("How many bottles of Coke would you like?: "))
        total = qty * 200
        print(qty, f"bottles of Coke would cost you {total} naira")
    
    elif order == 3:
        qty = int(input("How many loaves of bread would you like?: "))
        total = qty * 300
        print(qty, f"loaves of bread would cost you {total} naira")
    
    elif order == 4:
        qty = int(input("How many tins of milk would you like?: "))
        total = qty * 250
        print(qty, f"tins of milk would cost you {total} naira")
    
    elif order == 5:
        qty = int(input("How many packs of chocolate would you like?: "))
        total = qty * 150
        print(qty, f"packs of chocolate would cost you {total} naira")        
    
    total_cost += total
    
    buy_another = int(input("Would you like to shop for anything else?\nEnter 1 to continue or 0 to checkout: "))

print(f"Your shopping cart costs {total_cost} naira\nThank you for shopping with us")    

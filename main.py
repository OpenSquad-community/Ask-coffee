# Main program file 
'''
cafe
$view menu  --> checked
menu
        1.
        2.
orderList
$order --> checked



callCustomer
$call
$payment
    web -invoie email API
    payment API

rating -- email
'''
def greeting():
    print("\nHello! Welcome to Ask coffee!")
    print("Please make yourself comfortable!")

def order():
    return int(input())
    
def menu():
    print("\nWhat kind of coffee do you want to order?\n")
    
    D = {1:"Latte",2:"Capuccino", 3:"Iced coffee"}
    for i in D:
        print(f"{i}.{D[i]}")
    print()
    print(f"User Input :-",end="")
    menuOrder = order()   
     
    print("\nWhich coffee do you want to order?\n")
    
    D1 = {"Latte":{1:"Vanilla Latte", 2:"Caramel Latte", 3:"Cinnamon Latte", 4:"Hazlenut Latte", 5:"Mocha Latte"},"Capuccino":{1:"Americano", 2:"Macchiato", 3:"Freddo Capuccino"}, "Iced coffee":{1:"Iced Caramel Macchiato", 2:"Cold-Brewed Coffee", 3:"Vietnamese Iced Coffee",4:"Caramel Coconut Iced Coffee"}}
    # D2 = {"Capuccino":{1:""}}
    X = D[menuOrder]
    for i in D1[X]:
        print(f"{i}:{D1[X][i]}")
    print()
    
    print("What type of",X,"do you want to order?\n")
    print(f"User Input :-",end="")
    orderedItem = int(input())
    # if menuOrder == 1:
    #     return D1[]
    # elif menuOrder == 2:

    # elif menuOrder==3:        
    return D1[X][orderedItem]

#def orderStorage(placeOrder):
    #return None

def main():
    greeting()
    placeOrder = menu()
    #orderStorage(placeOrder)
    
if __name__ =="__main__":
    main()    

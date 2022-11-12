import time as t

def greeting():
    print("\nHello! Welcome to Ask coffee!")
    print("Please make yourself comfortable!")

def order_func():
    return int(input())
    
def menu():
    print("\nWhat kind of coffee do you want to order?\n")
    
    D = {1:"Latte",2:"Capuccino", 3:"Iced coffee"}
    for i in D:
        print(f"{i}.{D[i]}")
    print()
    print(f"User Input :-",end="")
    menuOrder = order_func()   
     
    print("\nWhich coffee do you want to order?\n")
    
    menuData = {"Latte":{1:"Vanilla Latte", 2:"Caramel Latte", 3:"Cinnamon Latte", 4:"Hazlenut Latte", 5:"Mocha Latte"},"Capuccino":{1:"Americano", 2:"Macchiato", 3:"Freddo Capuccino"}, "Iced coffee":{1:"Iced Caramel Macchiato", 2:"Cold-Brewed Coffee", 3:"Vietnamese Iced Coffee",4:"Caramel Coconut Iced Coffee"}}
    # D2 = {"Capuccino":{1:""}}
    categoryMenu = D[menuOrder]
    
    for i in menuData[categoryMenu]:
        print(f"{i}:{menuData[categoryMenu][i]}")
    print()
    
    print("What type of",categoryMenu,"do you want to order?\n")
    print(f"User Input :-",end="")
    orderedItem = int(input())
    order = menuData[categoryMenu][orderedItem]
    priceMenu = {
        "Latte":{
            1:{"Vanilla Latte":120}, 
            2:{"Caramel Latte":140}, 
            3:{"Cinnamon Latte":150}, 
            4:{"Hazlenut Latte":200}, 
            5:"Mocha Latte"},
        "Capuccino":{
            1:"Americano",
            2:"Macchiato",
            3:"Freddo Capuccino"}, 
        "Iced coffee":{
            1:"Iced Caramel Macchiato",
            2:"Cold-Brewed Coffee",
            3:"Vietnamese Iced Coffee",
            4:"Caramel Coconut Iced Coffee"}
    }
    subMenuPrice = {}
    test = []
    for j in priceMenu:
        test.append(priceMenu[j])

    for j in test:
        subMenuPrice[order] = j[orderedItem][order] 
    return (subMenuPrice,order)

def orderStorage(placeOrder):
    # chief 
    t.sleep(5)
    return call_customer(True)

def call_customer(orderStatus):   
    if orderStatus:
        print("Your order is prepared, please collect it.")
    t.sleep(5)
    return collected_Status()


def collected_Status():
    orderCollected = input(f"\nDid you collect your order: yes/no:-")
    if orderCollected =='yes':
        return None
    elif orderCollected=='no':
        t.sleep(2)
        collected_Status()
    else:
        print("\nPlease enter valid input.")
        collected_Status()

         

def payment(placeOrderDic, placeOrder):

    print(f"----------------INVOICE---------------")
    billAmount = 0
    for i in placeOrder:
        print(f"order placed:-{i} Price:{placeOrderDic[placeOrder]}")
        billAmount += placeOrderDic[placeOrder]
    print(f"Bill amount :{billAmount}")

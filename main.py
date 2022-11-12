import time as t
import user_function
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

def main():
    user_function.greeting()
    placeOrderDic, placeOrder= user_function.menu()
    for i in placeOrder:
        print(f"\nThanks for ordering {i} priced at {placeOrderDic[placeOrder]}.")
        print(f"Your order will be here soon.\n")
    user_function.orderStorage(placeOrder) 
    user_function.payment(placeOrderDic,placeOrder)

    
if __name__ =="__main__":
    main()    
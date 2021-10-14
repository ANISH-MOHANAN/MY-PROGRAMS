#design two functions to find discount
def student_discount(price):
    return price-(price*10/100)
def regular_customer_discount(new_price):
    return new_price-(new_price*5/100)
price=int(input("enter the price of product: "))
total_amount=regular_customer_discount(student_discount(price))
print(total_amount)
customer = {"name": "godiya", "order_amount": 25000, "loyalty_card": True, "is_student": False}
print(customer["loyalty_card"])
print(customer["is_student"])
print(customer["order_amount"])
discount = 0

if customer ["loyalty_card"]:
    discount += 10
if customer["order_amount"] > 20000:
    if customer ["loyalty_card"]:
        discount += 5
    else:
        print("free drink")
if customer ["is_student"]:
    discount += 5
#print(discount_p)
discount_amount = (discount / 100) * customer["order_amount"] 
customer.update({
    "discount": discount,
    "discount": discount,
    "amount_to_pay": customer["order_amount"] - discount
})
print(customer)
order_summary = {"customer1": customer}














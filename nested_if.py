is_registered = True
age = 19
if is_registered:
    if age >= 18:
        print("you can vote")
    else:
        print("you are registered but too young to vote")
else:
    print("you are not registered")

username = "christy"
password = "1234"
if username == "christy":
    if password == "1234":
        print("login successful")
    else:
        print("incorrect password")
else:
   print("username not found")
age = 16
weekday = True
if age < 18:
    if weekday:
        print("discount applied") 
    else:
        print("normal price")
else:
    print("adult price")
loyalty_card = True
total = 25000
if loyalty_card:
    if total > 20000:
        print("15% discunt")
    else:
        print("10% dicount")
else:
    if total > 20000:
        print("free soft drrink")
    else:
        print("no discount")























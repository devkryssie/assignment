menu = '''
|-----------------------------------|-
|         welcome                   |
|     login to login                |
|      register to register         |
|     enter 3 to exit               |
-----------------------------------  
'''
print(menu)
verification_fee = 1500
db = {
      "ekuke":{
         "username": "ekuke",
          "password": "admin123",
           "balance": 3000,
             "is_verified": True
    }
}
your_choice = input("select command: ").lower().strip()
if your_choice not in ["login", "register", "exit"]:
    print("invalid command")
elif your_choice == "register":
    print("fill in the form below to register your account")
    username = input("create username: ").lower().strip()
    if username in db:
        print(f"\nusername {usrname} already taken")
    else:
        password = input("\ncreate password")
        initial_amount = float(input("initial amount"))
        db[username] = {
            "username": username,
            "password": password,
            "initial_amount": initial_amount,
            "is_verified": False
       }
    print("account created successfully")
    print(f"welcome {username} ")
    print(" ")
    print(db)
    verification = input("do you want to verify your account?:").lower().strip()
    if verification == "yes" or "y":
        if initial_amount > verification_fee:
            initial_amount -= verification_fee
            db.update({"is_verified": True})
            db.update({"initial_amount": initial_amount})
            print("\n account veriification successfully")
        else:
            print("insufficient balance")
    elif veriification == "no" or "n":
        print("you can choose to verify your acount later")
    print(db)
logins = input("enter ur username: ")
if logins in db:
    password = input("enter password:")
    if password == db[username]:
        print(f"welcome back {username} login successful")
    else:
        print("incorrect password try again")
else:
    print("username not found please register first")














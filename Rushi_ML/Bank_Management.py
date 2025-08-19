import json 
import random
import string 
from pathlib import Path 

class Bank:
    database = 'data.json'
    data =[]

    try:
        if Path(database).exists():
            with open(database, 'r') as file:
                data = json.load(file)
        else:
            print("No such file exists")
    except Exception as e:
        print(f"An error occurred: {e}")

    @classmethod
    def __update_data(cls):
        with open(cls.database,'w') as file:
            file.write(json.dumps(cls.data))

    @classmethod
    def __generate_account_number(cls):
        cap_alpha = random.choices(string.ascii_uppercase, k=1)
        small_alpha = random.choices(string.ascii_lowercase, k=3)
        digits = random.choices(string.digits, k=3)
        sp_char = random.choices("!@#$%^&*", k=1)
        acc_no = cap_alpha + small_alpha + digits + sp_char
        random.shuffle(acc_no)
        return ''.join(acc_no)
    
    def Createaccount(self):
        info = {
            "name": input("Enter your name: "),
            "email": input("Enter your email: "),
            "age": int(input("Enter your age: ")),
            "pin": int(input("Enter 4 digit pin: ")),
            "account_number": self.__generate_account_number(),
            "balance": 0
        }
        if info['age']<18:
            print("You are not eligible to create an account")
            return
        else:
            self.data.append(info)
            self.__update_data()
            print("Account created successfully")
            for i in info:
                print(f"{i}: {info[i]}")

    def depositmoney(self):
        acc_no = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        check = False
        for i in self.data:
            if i['account_number'] == acc_no and i['pin'] == pin:
                check=True
                amount = int(input("Enter the amount to deposit: "))
                i['balance'] += amount
                self.__update_data()
                print(f"Deposited {amount}. New balance: {i['balance']}")
                break    
        if check==False:
            print("invalid account number or pin") 

    def withdrawmoney(self):
        acc_no = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        check = False
        for i in self.data:
            if i['account_number'] == acc_no and i['pin'] == pin:
                check = True
                amount = int(input("Enter the amount to withdraw: "))
                if amount > i['balance']:
                    print("Insufficient balance")
                    return
                i['balance'] -= amount
                self.__update_data()
                print(f"Deposited {amount}. New balance: {i['balance']}")
                break
        if check == False:
                print("Invalid account number or pin")
    
    def showdetails(self):
        acc_no = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        check=False
        for i in self.data:
            if i['account_number'] == acc_no and i['pin'] == pin:
                check=True
                print("Account details:")
                for j in i:
                    print(f"{j}: {i[j]}")
                break
        if check==False:
                print("Invalid account number or pin")

    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin "))

        userdata = [i for i in Bank.data if i['account_number'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found ")
        
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name or press enter : "),
                "email":input("please tell your new Email or press enter to skip :"),
                "pin": (input("enter new Pin or press enter to skip: "))
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"]=="":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['account_number'] = userdata[0]['account_number']
            newdata['balance'] = userdata[0]['balance']      

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]
            
            print("Details updated successfully")
            self.__update_data()

    def Delete(self):
        acc_no = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        check = False
        for i in self.data:
            if i['account_number'] == acc_no and i['pin'] == pin:
                check = True
                self.data.remove(i)
                self.__update_data()
                print("Account deleted successfully")
                return
        if check == False:
            print("Invalid account number or pin")

user = Bank()

print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()

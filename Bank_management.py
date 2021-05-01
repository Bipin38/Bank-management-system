import getpass
import os

class Bank:
    def __init__(self):
        self.client_details_list = []
        self.logedin = False
        self.cash = 1000
        self.transfer_cash = False 

#FUNCTION FOR ACCOUNT REGISTRATION
    def register(self, name, phone_number, password):
        cash = self.cash
        condition = True

        if len(str(phone_number))!=10:
            print("Invalid phone number. Please enter a valid phone number.!")
            condition = False

        if len((password))<5 or len(password)>18:
            print("\n!!!!!!!! ALERT !!!!!!!!!!\nThe length of the password must be greater than 5 and less than 18.")
            condition = False

        if condition == True:
            print("\n Account created succesfully \n")
            self.client_details_list = [name, phone_number, password, cash]
            with open(f"{name}.txt", 'w') as f:
                for details in self.client_details_list:
                    f.write(str(details)+ "\n")


#FUNCTION FOR LOGIN.
    def login(self, name, phone_number, password):
        self.logedin = False
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(phone_number) in self.client_details_list:
                if password in self.client_details_list:
                    self.logedin = True
                        
            if self.logedin == True:
                print(f"\nYou are logged in as {name}")
                self.cash = int(self.client_details_list[3])
                self.name = name

            else:
                print("\nWrong details!!.Enter correct details.\n")
                name = input("Enter your name: ")
                phone_number = int(input("Enter phone number: "))
                password = str(input("Enter password: "))
                Bank_object.login(name, phone_number, password)


    #FUNCTION TO ADD CASH AFTER LOGIN.
    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt", 'w') as f:
                f.write(details.replace(str(self.client_details_list[3]), str(self.cash)))

            print("Amount added succesfully.")

        else:
            print("Enter correct value of amount.")

        
    # FUNCTION TO TRANSFER CASH TO ANOTHER ACCOUNT.
    def Transfer_cash(self, amount , name ,ph):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TranferCash = True

        
        if self.TranferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details.split("\n")
            
            with open(f"{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("Amount Transfered Successfully to",name,"-",ph)
            print("Balacne left =",left_cash)  
            self.cash = left_cash 

        else:
            print("Invalid phone number.")
            


        
#FUNCTION TO EDIT DETAILS.
    def change_password(self, password):
        if len(password)<5 or len(password)>18:
            print("The length of the password must be greater than 5 and less than 18.")

        else:
            old_password = input("Enter old password.")
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            if old_password == str(self.client_details_list[2]):
                with open(f"{self.name}.txt", "w") as f:
                    f.write(details.replace(str(self.client_details_list[2]),str(password)))
                print("Password has  been changed.")

            else:
                print("Invalid old password.")

    def change_phone_number(self, phone_number):
        if len(str(phone_number))!=10:
            print("Invalid phone number. Please enter a valid phone number.!")
            
        else:
            old_phone_number = str(input("Enter old phone number."))
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            if old_phone_number == str(self.client_details_list[1]):
                with open(f"{self.name}.txt", "w") as f:
                    f.write(details.replace(str(self.client_details_list[1]),str(phone_number)))

                print("Phone number has been changed succesfully.")

            else:
                print("Invalid phone number.")

    #FUNCTION TO DELETE EXISTING ACCOUNT.
    def delete_account(self, name, phone_number, password):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")

    
        if str(phone_number) in self.client_details_list:
            if password == str(self.client_details_list[2]):
                os.remove(f"{name}.txt")
                print("\n Account deleted succesfully. \n")

            else:
                print("Invalid details.")


if __name__ == "__main__":
    Bank_object = Bank()
while True:
    print("\n**********Welcome to the bank.**********")
    print("\n1. login")
    print("2. Create an new account")
    print("3. Delete an account.")
    print("4. Exit.\n")

    user = int(input("Make decission. "))
    if user == 1:
        print("\n\nlogging in\n")
        name = input("Enter your name: ")
        phone_number = int(input("Enter phone number: "))
        password = str(input("Enter password: "))
        Bank_object.login(name, phone_number, password)
        while True:
            if Bank_object.logedin:
                print("\n1.Add amount")
                print("2.Check balance")
                print("3.Transfer amount")
                print("4.Edit profile")
                print("5.Logout\n")

                login_user = int(input())
                if login_user == 1:
                    print("Balance = ",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1.Back menu")
                    print("2.logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                    else:
                        print("Enter correct details.")
                        break

                elif login_user == 2:
                    print("Balance = ",Bank_object.cash)
                    print("\n1.Back menu")
                    print("2.logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print("Balance = ",Bank_object.cash)
                    amount = int(input("Enter the amount."))
                    if 0 < amount <= Bank_object.cash:
                        name = input("Enter the name of the person to whom you want to send: ")
                        phone_number = int(input("Enter the phone number"))
                        Bank_object.Transfer_cash(amount, name, phone_number)
                        
                        print("\n1.Back menu")
                        print("2.logout")

                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                        else:
                            print("Enter correct details.")
                            break

                    elif amount < 0:
                        print("Enter a valid amount.")

                    elif amount > Bank_object.cash:
                        print("You don't have enough amount to transfer")

                elif login_user == 5:
                    print("Are you sure you want to logout?\nIf YES press 'Y' else press 'N' for NO")
                    choice = str(input())
                    if choice == 'Y' or 'y':
                        break
                    elif choice == 'N' or 'n':
                        continue
                    else:
                        print("\nInvalid choice.\n")

                   

                elif login_user == 4:
                    print("1.Change phone number.")
                    print("2.Change password.")
                    choice = int(input())
                    if choice == 1:
                        phone_number = input("Enter new phone number.")
                        Bank_object.change_phone_number(phone_number)
                        break
                        
                    elif choice == 2:
                        password = input("Enter new password.")
                        Bank_object.change_password(password)
                        break
                       

    elif user == 2:
        print("Creating new account.")
        name = input("Enter your name: ")
        phone_number = int(input("Enter phone number: "))
        password = input("Enter password: ")

        Bank_object.register(name, phone_number, password)

    elif user == 3:
        print("You are about to delete account with given details.")
        name = input("Enter your name: ")
        phone_number = int(input("Enter phone number: "))
        password = input("Enter password: ")

        Bank_object.delete_account(name, phone_number, password)


    elif user == 4:
        break

    else:
        print("\nInvalid choice!!\nPlease choose correct option.")
        continue

        
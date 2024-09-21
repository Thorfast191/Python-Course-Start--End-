import random

#Arrays:
acc_nums = []
acc_names = []
ages = []
acc_balance = []

#Start the system
while True:
    print("Welcome to our banking management system.")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Please choose one option or you may choose option 5 to exit our system:")

    if choice == "1":
        #get account details
        acc_num = ""
        #generate account number
        for i in range(11):
            acc_num += str(random.randint(0,9))
        #Ensure account number is unique
        if acc_num  in acc_names:
            print("Account number already exists.")
        acc_name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        initial_deposit = float(input("Please deposit some money to create an account:"))

        #Append details
        acc_nums.append(acc_num)
        acc_names.append(acc_name)
        ages.append(age)
        acc_balance.append(initial_deposit)

        print("Congratulations! Your account has been created.🆗")
        print(f"Your account information,\n account number: {acc_num},\n account name: {acc_name},\n age: {ages[0]},\n account balance: {acc_balance[0]}")

    elif choice == "2":
        acc_num = input("Enter your account number: ")
        if acc_num not in acc_nums:
            print("Account not found. Please try again.")
        else:
            index = acc_nums.index(acc_num)
            deposit_ammount = float(input("Enter the amount to deposit: "))
            acc_balance[index] += deposit_ammount
            print(f"Deposit successful. Your new balance is: {acc_balance[index]}")

    elif choice == "3":
        acc_num = input("Enter your account number: ")
        if acc_num not in acc_nums:
            print("Account not found. Please try again.")
        else:
            index = acc_nums.index(acc_num)
            withdraw_ammount = float(input("Enter the amount to withdraw: "))
            if withdraw_ammount >= acc_balance[index]:
                print("Insufficient Balance Sorry 😢")
            else:
                acc_balance[index] -= withdraw_ammount
                print(f"Deposit successful. Your new balance is: {acc_balance[index]}")

    elif choice == "4":
        acc_num = input("Enter your account number: ")
        if acc_num not in acc_nums:
            print("Account not found. Please try again.")
        else:
            index = acc_nums.index(acc_num)
            print(f"Your account balance is: {acc_balance[index]}")         

    elif choice == "5":
        print("Thank you for using our banking management system. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")


        




    

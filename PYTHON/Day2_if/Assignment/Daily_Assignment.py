balance = 5000
amount = 0
Withdraw = 0

print("........ATM Menu........")

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your Balance is:", balance)

elif choice == 2:
    # Deposit
    amount = int(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print(balance)
    else:
        print("Invalid amount")

elif choice == 3:
    # Withdraw
    Withdraw = int(input("Enter Withdraw Amount: "))

    if Withdraw > 0:
        if Withdraw <= balance:
            balance = balance - Withdraw
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid withdrawal amount")

else:
    # Invalid choice
    print("Invalid choice")
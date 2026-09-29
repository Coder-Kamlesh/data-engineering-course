#123 = True
#Balance = 5000
#withdraw = 2000

#if(123 == true):
    #print("Password Correct! :")
    #if(withdraw<=5000):
    #print("Withdraw Succesfully")
    #else:
#print("Enter Correct Ammount :")
#else:
   # print("Password Incorrect")#

# Initial ATM State
card_inserted = True
correct_pin = 1234
account_balance = 5000

# User Input Simulation
entered_pin = 1234
withdrawal_amount = 2000

# Level 1: Check if the card is inserted
if card_inserted:
    print("Card detected.")
    
    # Level 2: Check if the PIN is correct (Nested inside card check)
    if entered_pin == correct_pin:
        print("PIN verified successfully.")
        
        # Level 3: Check if account has enough funds (Nested inside PIN check)
        if account_balance >= withdrawal_amount:
            account_balance -= withdrawal_amount
            print(f"Transaction successful! Please collect ${withdrawal_amount}.")
            print(f"Remaining balance: ${account_balance}")
        else:
            print("Transaction failed: Insufficient balance.") # Runs if balance is low
            
    else:
        print("Transaction failed: Incorrect PIN.") # Runs if PIN is wrong
        
else:
    print("Please insert your ATM card to begin.") # Runs if no card is found

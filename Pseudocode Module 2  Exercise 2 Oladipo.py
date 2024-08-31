start
     # Declarations
         accountBalance = 0
         overDrawnFee = 0
         overdrawnTimes = 0  # Assuming you have a variable to track the number of times the account has been overdrawn

     # Calculate overdraft fee
         if accountBalance < 0:
         overDrawnFee = (accountBalance * 0.01) - (5 * overdrawnTimes)
         else:
         overDrawnFee = 0

     # Calculate the new account balance
        newAccountBalance = accountBalance - overDrawnFee

     # Output the new account balance
        print("New Account Balance:", newAccountBalance)

stop        

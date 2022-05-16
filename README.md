## > bearrobotics_project
Implement a simple ATM controller<br>
>Insert Card => Chcek PIN number => See Balance/Deposit/Withdraw


## > Requirements

>python 3.8+

### 1. main.py

Without connect to Database, You must create User Data for test.
``` 
account_list = list()
account_list.append(UserData("1234123412341234", "1234", "123412341234", 100))
account_list.append(UserData("1000000000000000", "1234", "9999999999", 90))
```
Make Atm instance and insert card number.
```
atm = Atm(account_list)

card = input("Please Insert Card\n")
result = atm.insert_card(card)
```
After chacking card information, ATM User can choice Balance/Deposit/Withdraw
### 2. user_data.py
'user_data.py' is a class to validate user information and update balance.

### 3. controller.py
controller.py is actual functional class.

## > How to use
**python main.py**


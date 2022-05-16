from controller import Atm
from user_data import UserData


if __name__ == "__main__":
    # create test_account information
    account_list = list()
    account_list.append(UserData("1234123412341234", "1234", "123412341234", 100))
    account_list.append(UserData("1000000000000000", "1234", "9999999999", 90))

    # use atm
    atm = Atm(account_list)

    # insert card
    card = input("Please Insert Card\n")
    result = atm.insert_card(card)

    # card & pin-number is valid => select menu
    if result is not None:
        print("Please Select Action Between")
        # select_action is integer
        select_action = int(input("1. Balance, 2.Deposit, 3.Withdraw\n"))
        print("------------------------------")
        action_result = atm.select_account(result, select_action)

        print("Thank You For Using Our Service")



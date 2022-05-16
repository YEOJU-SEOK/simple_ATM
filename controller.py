import time

from user_data import *


class Atm:
    def __init__(self, account_list):
        self.account_list = account_list

    # insert card
    def insert_card(self, card):
        # check card number
        card_info = ''
        for account in self.account_list:
            if card == account.card:
                card_info = account

        if card_info == '':
            print("Invalid Card")
            return
        else:
            # check pin-number
            pin_num = input("Please input your PIN number\n")

            check_pin = self.check_pin_number(card_info, pin_num)
            if check_pin:
                print("Welcome")
                return card_info
            else:
                print("Invalid Pin Number, Try Again")
                return None

    # check pin number
    def check_pin_number(self, card_info, pin_num):
        if card_info.pin != pin_num:
            return False
        else:
            return True

    # Select Balance/Deposit/Withdraw
    def select_account(self, info, action):
        # 1. Balance
        if action == 1:
            print("Your Account's Balance is ", info.balance)
            return
        # 2. Deposit and 3. Withdraw
        elif action == 2 or action == 3:
            if action == 2:
                money = input("Please Insert Amount To Deposit : ")
            else:
                money = input("Please Insert Amount To Withdraw : ")

            if not money.isnumeric():
                cnt = 0
                while cnt < 3:
                    print("Invalid Amount")
                    if cnt == 2:
                        print("Exceed Insert, Try Again")
                        return
                    cnt += 1
                    money = input("Please Insert Amount : ")
                    if money.isnumeric():
                        break


            print("In Progress......")
            time.sleep(2)

            if action == 2:
                info.deposit(money)
            else:
                info.withdraw(money)

            print("Your Account's Balance Is", info.balance)
            return True


class UserData:
    def __init__(self, card: str, pin: str, account_num: str, balance: int):
        self.card = self._is_valid_card(card)
        self.pin = self._is_valid_pin(pin)
        self.account_num = self._is_valid_account_num(account_num)
        self.balance = self._is_valid_balance(balance)

    def _is_valid_card(self, card):
        if len(card) != 16:
            raise ValueError("Card must be 16 characters.")
        return card

    def _is_valid_pin(self, pin):
        if len(pin) != 4:
            raise ValueError("Pin Number must be 4 characters.")
        return pin

    def _is_valid_account_num(self, account_num):
        if len(account_num) < 10 or len(account_num) > 15:
            raise ValueError("Account Number must be 10-15 characters.")
        return account_num

    def _is_valid_balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be minus.")
        return balance

    def deposit(self, money):
        self.balance += int(money)

    def withdraw(self, money):
        self.balance -= int(money)
from abc import ABC, abstractmethod
from enum import Enum, auto


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def __str__(self):
        return f'Balance: {self.balance}'

    # These deposit and withdraw methods are good but does not persists or have undo/redo support
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance: {self.balance}')

    def withdraw(self, amount):
        if self.balance - amount > BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance: {self.balance}')
            return True
        return False


class Command(ABC):
    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, bank_account: BankAccount, action, amount):
        self.action = action
        self.amount = amount
        self.bank_account = bank_account
        self.success = None

    class Action(Enum):
        WITHDRAW = auto()
        DEPOSIT = auto()

    def invoke(self):
        if self.action == BankAccountCommand.Action.DEPOSIT:
            self.bank_account.deposit(self.amount)
            # Success should be tracked, otherwise the undo functionality would not work correctly
            self.success = True
        elif self.action == BankAccountCommand.Action.WITHDRAW:
            self.bank_account.withdraw(self.amount)
            self.success = True

    def undo(self):
        if not self.success:
            return
        if self.action == BankAccountCommand.Action.WITHDRAW:
            self.bank_account.deposit(self.amount)
        elif self.action == BankAccountCommand.Action.DEPOSIT:
            self.bank_account.withdraw(self.amount)


if __name__ == '__main__':
    ba = BankAccount()
    bac = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    bac.invoke()
    print(ba)
    bac2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
    bac3 = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 20)

    bac2.invoke()
    bac3.invoke()

    print(ba)

    bac3.undo()
    print(ba)
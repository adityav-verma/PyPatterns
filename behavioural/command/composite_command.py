from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List


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
    def __init__(self):
        self.success = None

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
        return self.success

    def undo(self):
        if not self.success:
            return
        if self.action == BankAccountCommand.Action.WITHDRAW:
            self.bank_account.deposit(self.amount)
        elif self.action == BankAccountCommand.Action.DEPOSIT:
            self.bank_account.withdraw(self.amount)
        return self.success


# This is good, but if a single command fails, this will still invoke or redo things, basically it does not
# take all the commands success/failure into consideration
class CompositeBankAccountCommand(Command, list):
    def __init__(self, items: List[BankAccountCommand] = []):
        for item in items:
            self.append(item)

    def invoke(self):
        for cmd in self:
            cmd.invoke()

    def undo(self):
        for cmd in self:
            cmd.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acc, to_acc, amount):
        super(MoneyTransferCommand, self).__init__(
            [
                BankAccountCommand(from_acc, BankAccountCommand.Action.WITHDRAW, amount),
                BankAccountCommand(to_acc, BankAccountCommand.Action.DEPOSIT, amount)
            ]
        )

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                ok = cmd.invoke()
            else:
                # handle roll back of all sub commands etc here
                cmd.success = False
                self.success = False
        self.success = ok


if __name__ == '__main__':
    ba = BankAccount(100)
    ba2 = BankAccount(0)
    print(ba)
    print(ba2)

    mtc = MoneyTransferCommand(ba, ba2, 34)
    mtc.invoke()
    print('After transfer')
    print(ba)
    print(ba2)
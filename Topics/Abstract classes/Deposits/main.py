from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        pass

    def add_interest(self):
        pass


class SavingsAccount(Account):
    min_amount = 10

    def add_money(self, amount):
        if amount < self.min_amount:
            print("Cannot add to SavingsAccount: amount too low.")
            return
        self.sum += amount


class Deposit(Account):
    min_amount = 50

    def add_money(self, amount):
        if amount < self.min_amount:
            print("Cannot add to Deposit: amount too low.")
            return
        self.sum += amount

    def add_interest(self):
        self.sum += self.interest * self.sum

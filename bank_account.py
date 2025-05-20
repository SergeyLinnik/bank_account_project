class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Приватный атрибут

    def deposit(self, amount):
        if amount <= 0:
            print("Сумма пополнения должна быть положительной.")
            return
        self.__balance += amount
        print(f"Пополнено: +{amount}. Баланс: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма для снятия должна быть положительной.")
            return
        if amount > self.__balance:
            print("Недостаточно средств.")
            return
        self.__balance -= amount
        print(f"Снято: -{amount}. Баланс: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Текущий баланс: {self.__balance}"

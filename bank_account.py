class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Приватный атрибут

    # Метод для пополнения счета
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено: +{amount}. Баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной.")

    # Метод для снятия средств
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Снято: -{amount}. Баланс: {self.__balance}")
            else:
                print("Недостаточно средств.")
        else:
            print("Сумма должна быть положительной.")

    # Геттер для получения текущего баланса
    def get_balance(self):
        return self.__balance

    # Опционально: можно добавить метод __str__ для удобного вывода
    def __str__(self):
        return f"Текущий баланс: {self.__balance}"

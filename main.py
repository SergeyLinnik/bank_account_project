from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Начальный баланс 100

    print(account)  # Вывод начального баланса

    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200)  # Попытка снять больше, чем есть

    print(f"Финальный баланс: {account.get_balance()}")

if __name__ == "__main__":
    main()

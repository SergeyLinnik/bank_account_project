from bank_account import BankAccount

def main():
    account = BankAccount(100)

    print(account)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200)  # Попытка снять больше, чем есть
    account.withdraw(-10)  # Некорректная сумма
    account.deposit(-5)    # Некорректная сумма

    print(f"Финальный баланс: {account.get_balance()}")

if __name__ == "__main__":
    main()

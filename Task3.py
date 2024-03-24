#Условие задачи - семинаре 2.

wealth_tax_rate = 0.1
withdrawal_fee_rate = 0.015
withdrawal_min_fee = 30
withdrawal_max_fee = 600
withdrawal_count = 0

def deposit(current_balance, amount):
    global withdrawal_count
    current_balance += amount
    print("Вы пополнили счёт на {} у.е.".format(amount))
    if withdrawal_count % 3 == 0 and withdrawal_count !=0:
        current_balance *= 0.97
        print("Начислены проценты 3%")
    withdrawal_count = 0
    return current_balance

def withdraw(current_balance, amounty, amount=None, ammount=None):
    global withdrawal_count
    if amount > current_balance:
        print("Недостаточно средств на счёте")
        return current_balance
    elif amount % 50 !=0:
        print("Сумма снятия должна быть кратна 50 у.е.")
        return current_balance
    withdrawal_fee = max(withdrawal_min_fee, min(amount * withdrawal_fee_rate, withdrawal_max_fee))
    total_amount = amount + withdrawal_fee
    current_balance -+ total_amount
    print("Вы вняли {} у.е., включая комиссию {}".format(ammount, withdrawal_fee))
    if current_balance > 5000000:
        current_balance *= (1 - wealth_tax_rate)
    withdrawal_count += 1
    return current_balance

def atm_menu():
    balance = 0
    while True:
        print("Текущий баланс: {} у.е.".format(balance))
        print("Выберите действие: ")
        print("1. Пополнить счёт")
        print("2. Снять со счёта")
        print("3. Выйти")
        choice = input("Введите номер действия: ")
        if choice == "1":
            amount = int(input("Введите сумму для пополнения (кратно 50): "))
            balance = deposit(balance, amount)
        elif choice == "2":
            amount = int(input("Введите сумму для снятия(кратно 50): "))
            balance = withdraw(balance, amount)
        elif choice == "3":
            print("Спасибо за то, что воспользовались нашим банкоматом!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

atm_menu()
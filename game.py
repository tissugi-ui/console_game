def read_choice(prompt,allowed):
    while True:
        choice = input(prompt).strip()
        if choice in allowed:
            return choice
        print("неккоректный ввод.попробуйте еще раз")

def show_rules():
    print("\n=== Правила игры===")
    print("у вас есть 2000 тенге")
    print("цены товаров:300,500,600,700,900 тенге")
    print("нужно купить ровно 3 товара")
    print("один и тот же товар можно покупать несколько раз")
    print("если после третьей покупки осталось от 0 до 200 тенге- победа")
    print("если денег не хватает ни на один товар - поражение")

def can_buy(balance, price):
    return price > 0 and balance >= price
def buy(balance,price):
    if can_buy(balance, price):
        return balance - price
    return balance
def is_success(balance, count):
    return count == 3 and 0 <= balance <=200

def play_game():
    balance = 2000
    count=0
    prices=[300,500,600,700,900]
    print("\n=== покупка в столовой ===")

    while count < 3:
        print("\nваш баланс: ", balance, "тенге")
        print("товары:")

        for i in range(len(prices)):
            print(i + 1, "-", prices[i], "тенге")

        choice = read_choice(
            "выберите товар (1-5): ",
            ["1", "2", "3","4","5"]
        )
        price = prices[int(choice)- 1]
        if can_buy (balance, price):
            balance = buy(balance,price)
            count += 1
            print("покупка совершена")
        else:
            print("недостаточно денег,покупка не засчитана")

            can_buy_any = False

            for item_price in prices:
                if can_buy(balance, item_price):
                    can_buy_any = True
                    break

            if not can_buy_any:
                print("Ни один товар больше не по карману.")
                print("Поражение!")
                return

        print("\nПокупок сделано:", count)
        print("Осталось:", balance, "тенге")

        if is_success(balance, count):
                print("Победа!")
        else:
                print("Поражение!")

def main():
    while True:
        print("\n=== МЕНЮ ===")
        print("1 - Начать")
        print("2 - Правила")
        print("0 - Выход")

        choice = read_choice(
            "Выберите пункт: ",
            ["0", "1", "2"]
                )

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Игра завершена.")
            break
main()

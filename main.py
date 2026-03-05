"""
Калькулятор ресторанного счёта
Версия 2.0 — для стажировки
Автор: Костерин Даниил
"""

def print_color(text, color):
    """Выводит текст цветом (для красоты)."""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
    }
    reset = "\033[0m"
    print(colors.get(color, "") + text + reset)


def get_number(prompt, value_type="float", allow_zero=False):
    """
    Запрашивает у пользователя число с проверкой.
    - prompt: текст вопроса
    - value_type: "float" или "int"
    - allow_zero: разрешать ли ноль
    """
    while True:
        try:
            if value_type == "float":
                value = float(input(prompt))
            else:
                value = int(input(prompt))

            if value < 0:
                print_color("Ошибка: число не может быть отрицательным", "yellow")
            elif value == 0 and not allow_zero:
                print_color("Ошибка: ноль не допускается", "yellow")
            else:
                return value
        except ValueError:
            print_color("Ошибка: введите число", "red")


def get_payment_method(prompt):
    """Запрашивает способ оплаты (нал / карта)."""
    while True:
        method = input(prompt).lower().strip()
        if method == "нал":
            return "нал"
        elif method == "карта":
            return "карта"
        else:
            print_color("Введите 'нал' или 'карта'", "red")


def main():
    """Основная функция программы."""
    print_color("=== Калькулятор ресторанного счёта ===", "cyan")

    # Ввод данных
    bill = get_number("Сумма счёта: ", "float", allow_zero=False)
    tip_percent = get_number("Чаевые (%): ", "float", allow_zero=True)
    people = get_number("Количество человек: ", "int", allow_zero=False)
    payment = get_payment_method("Нал или карта? ")

    tip_rate = tip_percent / 100
    total = bill

    # Сервисный сбор для больших компаний
    if people > 6:
        service_fee = bill * 0.10
        total = bill + service_fee
        print_color("Добавлен сервисный сбор 10% (большая компания)", "yellow")

    # Чаевые
    total = total * (1 + tip_rate)

    # Оценка чаевых
    if tip_rate < 0.1:
        print_color("Чаевые меньше 10% — официант расстроен", "red")
    elif tip_rate < 0.15:
        print_color("Чаевые 10–15% — нормально", "yellow")
    else:
        print_color("Чаевые больше 15% — официант счастлив!", "green")

    # Комиссия за карту
    if payment == "карта":
        total = total * 1.03
        print_color("Добавлена комиссия 3% за оплату картой", "yellow")
    else:
        print_color("Оплата наличными", "green")

    # Итог
    per_person = total / people
    print_color(f"Общий счёт: {total:.2f} руб.", "cyan")
    print_color(f"Каждый должен: {per_person:.2f} руб.", "cyan")


if __name__ == "__main__":
    main()
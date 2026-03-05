# ---- ФУНКЦИЯ ДЛЯ ЦВЕТА ----
def print_color(text, color):
    if color == "red":
        print("\033[91m" + text + "\033[0m")
    elif color == "green":
        print("\033[92m" + text + "\033[0m")
    elif color == "yellow":
        print("\033[93m" + text + "\033[0m")
    elif color == "cyan":
        print("\033[96m" + text + "\033[0m")
    else:
        print(text)


def get_number(prompt, value_type="float", allow_zero=False):
    while True:
        try:
            if value_type == "float":
                value = float(input(prompt))
            else:
                value = int(input(prompt))

            if value < 0:
                print_color("Ты ебанутый? Отрицательные числа нельзя!", "yellow")
            elif value == 0 and not allow_zero:
                print_color("Ты ебанутый? Ноль нельзя!", "yellow")
            else:
                return value
        except:
            print_color("Ты ебанутый? Цифры вводи, бля!", "red")

def get_payment_method(prompt):
    while True:
        method = input(prompt).lower().strip()
        if method == "нал":
            return "нал"
        elif method == "карта":
            return "карта"
        else:
            print_color("Только 'нал' или 'карта', брат! И без понтов.", "red")


bill = get_number("Сколько вы потратили?\n", "float", allow_zero=False)
tip_percent = get_number("Сколько процентов хотите оставить чаевых?\n", "float", allow_zero=True)
people = get_number("Сколько человек в компании?\n", "int", allow_zero=False)
payment = get_payment_method("Нал или карта?\n")

service_fee = 0
total = bill
tip_rate = tip_percent / 100


#Считаем сколько долбаёбов и накидываем сервисный если их дохуя
if people > 6:
    service_fee = bill * 0.10
    total = bill + service_fee
    print_color("Ну пиздец, вас много. +10% сверху", "yellow")
else:
    total = bill


total = total * (tip_rate + 1)


if tip_rate < 0.1:
    print_color("Ебать, я в ахуе, ебать вы нищие.", "red")
elif tip_rate < 0.15:
    print_color("Спасибо, но можно было бы и побольше.", "yellow")
else:
    print_color("Ебать братишка ты красава, сейчас оплатите и я отсосу каждому.", "green")


if payment == "карта":
    total = total * 1.03
    print_color("В следующий раз что бы ты эту себе карту в жопу засунул и пришёл с наличкой.", "yellow")
else:  # payment == "нал"
    print_color("О, в этот раз с наличкой", "green")


print_color(f"Общий счёт: {total:.2f} рублей.", "cyan")
print_color(f"Каждый должен заплатить: {total / people:.2f} рублей.", "cyan")
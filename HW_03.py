# ============================================  Задание  ====================================================
# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:
#
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# 2. Далее для каждого билета запрашивается возраст посетителя,
#    в соответствии со значением которого выбирается стоимость:
#       Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
#       От 18 до 25 лет — 990 руб.
#       От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек
#    на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
# ===========================================================================================================


# ======================================  Объявим функции  ==========================================================
# Функция ввода количества билетов
def input_quantity_tickets():
    count = 0
    while True:
        try:  # Добавляем конструкцию try-except для отлова ошибки на вводе:
            count += 1  # счетчик для разных инструкций при вводе неправильного формата количества
            if count == 1 and global_count == 0:
                quantity = int(
                    input(
                        "Здравствуйте, уважаемый клиент! Сколько билетов Вы хотите приобрести?\nПри заказе более 3х "
                        "билетов, действуют скидки: ").lstrip().lstrip("!,@,#,$,%,^,&,*,(,),"))
            else:
                quantity = int(
                    input("Введите количество билетов: ").lstrip().lstrip("!,@,#,$,%,^,&,*,(,),"))
        except ValueError:
            print("Упс, возможно вы ввели буквы, попробуйте еще раз: ")
        else:
            break
    return abs(quantity)


# Функция ввода возраста посетителя и добавление его в словарь
# возвращающая словарь - номер_посетителя: возраст с небольшими проверками ввода:
def input_age( quantity_tickets, dict_base_client ):
    count = 0  # счетчик для разных сообщений при вводе, и при вводе неправильного формата возраста
    count_repeat = len(dict_base_client.keys())  # счетчик для повторного добавления билетов
    for item in range(1, quantity_tickets + 1):
        while True:
            try:  # Добавляем конструкцию try-except для отлова ошибки на вводе:
                if count == quantity_tickets:
                    break
                count += 1
                if count == 1 and global_count == 0:
                    age = int(
                        input(
                            f"Введите возраст первого посетителя(например: 21), для лиц моложе 18 участие бесплатно: ")
                        .lstrip().lstrip("!,@,#,$,%,^,&,*,(,),"))
                elif count > 10:
                    age = int(
                        input("У вас большая компания, введите еще возраст: ").lstrip().lstrip("!,@,#,$,%,^,&,*,(,),"))
                else:
                    age = int(
                        input("Введите возраст следующего участниках: ").lstrip().lstrip(
                            "!,@,#,$,%,^,&,*,(,),"))
            except ValueError:
                print("Упс, возможно вы ввели буквы, попробуйте еще раз: ")
                count -= 1
            else:
                if age == 0:
                    print(
                        "Грудного ребенка, лучше оставить в другой комнате с няней ('Няни недорого: няни.рф'): ")
                    count -= 1
                    continue
                else:
                    if global_count > 0:  # последующие добавления билетов
                        dict_base_client[item + count_repeat] = abs(age)
                    else:
                        dict_base_client[item] = abs(age)  # первое добавления билетов
                    break
    return dict_base_client


# Функция вывода выписки о заказе билетов
def output_tickets( dict_base_client ):
    # создадим ценник билетов по возрастам (если нужно будет быстро поменять)
    price_for_17, price_for_17_25, price_from_25 = 0, 990, 1390
    total_price = 0
    print()
    print(" Выписка ".center(120, "="))
    for person, age in dict_base_client.items():
        if age < 18:
            price = price_for_17
        elif 18 <= age < 25:
            price = price_for_17_25
        else:
            price = price_from_25
        print(f"{person} посетитель, возраст: {age}, цена билета: {price}")
        total_price += price
    print("="*120)
    if len(dict_base_client.keys()) <= 3:
        print(
            f"Всего заказано билетов {len(dict_base_client.keys())}, цена без акции - 10% за акцию "
            f"'Зарегистрируй 4 и больше билетов, получи скидку': {total_price} у.е.")
    else:
        print(
            f"Всего заказано билетов {len(dict_base_client.keys())},задействована акция 'Зарегистрируй 4 и больше "
            f"билетов, получи скидку 10%' Цена: {total_price - total_price*0.1} у.е.")

    print("="*120)


# ======================================  Сама программа  ==========================================================
main = True  # зациклим программу, для того что бы у пользователя была возможность докупить билеты
dict_base_client = {}  # небольшая база: номер посетителя: возраст
global_count = 0  # глобальный счетчик, для того что бы не здороваться с пользователем каждый раз при докупке билетов
# создадим базу данных пользователя, запросим количество нужных билетов, и возраст посетителей:
while main:
    quantity_tickets = input_quantity_tickets()  # Введем количество билетов
    # Введем возраст посетителя и добавим его в словарь к номеру посетителя
    dict_base_client = input_age(quantity_tickets, dict_base_client)
    # выведем отчет о заказе билетов
    output_tickets(dict_base_client)
    while True:  # реализуем возможность докупить билеты
        continue_purchase = input("Хотите докупить билеты? (Y/N)").upper()
        if continue_purchase == "Y":
            global_count += 1
            break
        elif continue_purchase == "N":
            main = False  # остановим цикл
            print("Заказ успешно сформирован, перевожу на страницу оплаты!")
            break
        else:
            print("Введите, только Y или N")
            continue
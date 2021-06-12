from DiscountCard import DiscountCard


flag = True
try:
    person = DiscountCard()
    while flag:
        menu_option = int(input(
            '1 - Розмір знижки\n2 - Номер карти\n3 - Дата видачі карти\n4 - Купити товар\n5 - Збільшити величину знижки\n6 - Вихід'))
        if menu_option == 1:
            discount_full = person.show_discount()
            print(f'Розмір знижки : {int(discount_full*100)}%')

        elif menu_option == 2:
            person.show_number_card()

        elif menu_option == 3:
            person.show_date()
        elif menu_option == 4:
            buy = int(input('Введіть суму покупки: '))
            ask = int(input('Будете використовувати вашу карту?(1-Так/2-Ні'))
            if ask == 1:
                result = buy-((buy*person.show_discount()*100)/100)
                person.set_plus_sum(buy)
                print('До сплати:''{:.2f}'.format(result), 'UAH')
                person.get_save_sum_pay()
            elif ask == 2:
                print(f'До сплати {buy}UAH')

            else:
                print('Uncorrect option')

        elif menu_option == 5:
            result = 1000-(person.get_save_sum_pay() -
                           int(person.get_save_sum_pay()/1000)*1000)
            print(result)
        elif menu_option == 6:
            break
        else:
            print('Uncorrect option')
except ValueError:
    print('Uncorrect value!!!')

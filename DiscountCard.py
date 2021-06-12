from datetime import datetime


class DiscountCard():
    def __init__(self, discount=0.01, number_card=123456, save_sum_pay=0, current_date=datetime.now()):
        self.number_card = number_card
        self.discount = discount
        self.__save_sum_pay = save_sum_pay
        self.current_date = current_date

    def show_number_card(self):
        print(f'Номер карти : {self.number_card}')

    def show_discount(self):
        if self.__save_sum_pay >= 1000:
            self.discount = self.discount + (self.__save_sum_pay//1000)/100
            self.__save_sum_pay = 0
        return self.discount

    def get_save_sum_pay(self):
        return self.__save_sum_pay

    def set_plus_sum(self, buy):
        self.__save_sum_pay = self.__save_sum_pay+buy

    def show_date(self):
        print(f'Карту отримано ---- >{self.current_date.strftime("%x")}')

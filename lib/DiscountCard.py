"""1. Написати клас "Карточка на знижку", який містить наступну інформацію: 

Номер карточки 
Розмір знижки (знижка передбачається накопичуваною; на початковому етапі вона рівна 1%. За кожні 1000 грн. покупки, сума знижки збільшується на 1%.) 
Приховане допоміжне поле для збереження вартості накупленого товару 
Дата видачі карточки в форматі "12/02/1200") 
Забезпечити можливість: 
Купляти товар з використанням карточки на знижку; 
Виводити інформацію про поточну величину знижки; 
Виводити інформацію про те, на яку суму ще необхідно докупити товару, щоб величина знижки збільшилась."""
from random import randint
import datetime


class Discount_Card:
    def __init__(self):
        self.__card_number = randint(10000000, 99999999)
        self.__date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.__discount = 1
        self.__summ = 0

    def buy_goods(self, money: float):
        if money > 0:
            paid = money-(money*self.__discount)/100
            print(
                f'Your discount is  {money * self.__discount / 100} UAH. You need to pay {paid} UAH.')

            confirm = input("Do you want to continue?: y/n --> ")
            if confirm.lower() == 'y':
                self.__summ += paid
                if round(self.__summ//1000+1) <= 50:
                    self.__discount = round(self.__summ//1000+1)
                else:
                    self.__discount = 50
                print("Congratulations! Operation is correct.\n")
            elif confirm.lower() == 'n':
                print("Bye!\n")
            else:
                print("Error! Wrong command. Try again!\n")
        else:
            print("Uncorrect cost! Please try again.\n")

    def discount_info(self):
        # Displays discount info
        print(
            f'Card number:{self.__card_number}. Your discount is {self.__discount}%.\n')

    def discount_inc_info(self):
        """Display information on how much you still need to buy additional goods to increase the size of the discount"""
        next_lev = 1000-(self.__summ % 1000)
        if next_lev == 0:
            next_lev = 1000
        if self.__discount < 50:
            print(
                f'Card number:{self.__card_number}. For the next level you need to buy more goods for {next_lev} UAH.\n')
        else:
            print('Your discount is 50% and already max!!!')

    @property
    def card_number(self):
        return self.__card_number

    @property
    def summ(self):
        return self.__summ

    @property
    def discount(self):
        return self.__discount

    @property
    def date(self):
        return self.__date

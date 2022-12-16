import datetime
import math

rates = {'USD': 64.65, 'RUB': 1}


class Rec:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        try:
            if datetime.datetime.strptime(date, '%Y-%m-%d'):
                self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        except:
            self.date = datetime.date.today()

    def __repr__(self):
        return f"{self.amount} - {self.comment} - {self.date}"


class Calc:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stat(self):
        res = 0
        for record in self.records:
            if record.date == datetime.date.today():
                res += record.amount
        return res

    def last_sevendays_stat(self):
        sum = 0
        onlyseven = 0
        for record in self.records:
            if onlyseven < 7:
                onlyseven += 1
                sum += record.amount
            elif onlyseven >= 7:
                break
        return sum

    def curr_date_count(self):
        dates_for_sum = input('Введите даты, через пробел (2020-12-25 2022-10-10) -')
        sum = 0
        sum_dates = dates_for_sum.split(' ')

        for record in self.records:

            if str(datetime.datetime.strptime(record.date, "%Y-%m-%d")) in sum_dates:
                sum += record.amount

        return sum


class CashCL(Calc):

    def __init__(self, currency, limit):
        super().__init__(limit)
        self.currency = currency

    def get_today_cash_remained(self):
        sum_for_limit = 0
        for record in self.records:
            if datetime.date.today() == record.date:
                sum_for_limit += record.amount

        if self.limit > sum_for_limit:
            for key, value in rates.items():
                if self.currency == key:
                    print(f'На сегодня осталось {math.floor(self.limit - (sum_for_limit / value))} {key}')
        return '----------'


class CaloriesCL(Calc):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        return str(f'Ваш лимит на сегодня - {self.limit - self.get_today_stat()} ккалл.')


user = CashCL('USD', 1000)
userX = CaloriesCL(1000)
user.add_record(Rec(30, 'Покупка продуктов', '2022-12-16'))
user.add_record(Rec(200, 'Замена процессора', ''))
user.add_record(Rec(500, 'Подарок на день рождения', '2022-12-15'))
user.add_record(Rec(5, 'Транспорт', '2022-12-18'))

userX.add_record(Rec(256, 'Спортзал', ''))

print(user.get_today_stat())
print(user.last_sevendays_stat())
print(user.get_today_cash_remained())
print(userX.get_calories_remained())
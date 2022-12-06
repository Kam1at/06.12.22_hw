class Person():
    def __init__(self, fio, age, passport, weight):
        if self.verify_fio(fio):
            self.__fio = fio

        if self.verify_age(age):
            self.__age = age

        if self.verify_weight(weight):
            self.__weight = weight

        if self.verify_ps(passport):
            self.__passport = passport

    def verify_fio(self, fio):
        symbol_list = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        try:
            ll = fio.split(" ")
        except:
            raise ValueError("ФИО должно быть строкой")
        ss = "".join(ll)
        if len(ll) != 3:
            raise ValueError("Неверный формат записи ФИО")
        if len(ll[0]) <= 0 or len(ll[1]) <= 0 or len(ll[2]) <= 0:
            raise ValueError("В ФИО должен быть хотя бы один символ")
        for x in ss:
            if x not in symbol_list:
                raise ValueError("В ФИО можно использовать только буквенные символы")
        else:
            return True

    def verify_age(self, age):
        if type(age) == int and 14 <= age <= 150:
            return True
        else:
            raise ValueError('Возраст должен быть целым числом от 14 до 150')

    def verify_weight(self, weight):
        if type(weight) == float and 25.0 <= weight:
            return True
        else:
            raise ValueError('Вес должен быть вещественным числом от 25 и выше')

    def verify_ps(self, passport):
        try:
            ll = passport.split(" ")
        except:
            raise ValueError("Неверный формат паспорта")

        ss = "".join(ll)

        if type(passport) is not str:
            raise ValueError("Паспорт должен быть строкой")

        if len(ll[0]) != 4 or len(ll[1]) != 6:
            raise ValueError("Неверный формат паспорта")

        try:
            int(ss)
        except:
            raise ValueError("Серия и номер паспорта должны содержать только числа")

        else:
            return True

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport
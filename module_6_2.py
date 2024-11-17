class Vehicle:
    """ Vehicle - это любой транспорт с атрибутами собственник, модель, цвет, мощность """
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = self.check_value(owner)
        self.__model = self.check_value(model)
        self.__color = self.check_value(color)
        if isinstance(engine_power, int):
            self.__engine_power = engine_power
        else:
            raise ValueError(
                f'Значения {engine_power} должны быть целым числом')

    @staticmethod
    def check_value(x):
        """ Проверить является ли x строкой. Иначе вернуть исключение. """
        if isinstance(x, str):
            return x
        else:
            raise ValueError(f'Значение должно быть строкой')

    def get_model(self):
        """ Получить модель """
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        """ Получить мощность """
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        """ Получить цвет """
        print(f'Цвет: {self.__color}')

    def set_color(self, new_color):
        """ Меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS,
        в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>"""
        # Проверить, явлляется ли new_color строкойи привести его в нижний регистр
        color = self.check_value(new_color).lower()
        if color in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

print('__Изначальные свойства__')
vehicle1.print_info()

print('__Меняем свойства (в т.ч. вызывая методы)__')
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

print('__Проверяем что поменялось__')
vehicle1.print_info()
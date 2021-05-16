print('Задание 2.')


class Apparel:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def Coat(self):
        return self.size / 6.5 + 0.5

    @property
    def Suit(self):
        return 2 * self.height + 0.3


a = Apparel((int(input('Введите ваш размер: '))), (int(input('Введите ваш рост: '))))
print('Расход ткани на пальто', "{:.2f}".format(a.Coat))
print('Расход ткани на костюм', "{:.2f}".format(a.Suit))

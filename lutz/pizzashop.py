from employee import Servant, PizzaRobot


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, servant):
        print(f'{self.name} orders from {servant}')

    def pay(self, servant):
        print(f'{self.name} pay for the item to {servant}')


class Oven:
    def bake(self):
        print('Oven  bakes')


class PizzaShop:
    def __init__(self):
        self.servant = Servant('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.servant)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.servant)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Jenny')

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary += self.salary * percent

    def work(self):
        print(f'{self.name} does stuff')

    def __repr__(self):
        return f'Employee: {self.name} - {self.salary}'


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 5000)

    def work(self):
        print(f'{self.name} makes food')


class Servant(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 3000)

    def work(self):
        print(f'{self.name} interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(f'{self.name} makes pizza')


if __name__ == '__main__':
    bob = PizzaRobot(name='bob')
    print(bob)
    bob.work()
    bob.give_raise(percent=0.2)

    for klass in Employee, Chef, Servant, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()

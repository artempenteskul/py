class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def get_last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent=0.1):
        self.pay *= (1 + percent)

    def __str__(self):
        return f'Person: {self.name}, salary: {self.pay}'


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def give_raise(self, percent=0.1, bonus=0.1):
        Person.give_raise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, human):
        self.members.append(human)

    def give_raises(self, percent=0.1):
        for human in self.members:
            human.give_raise(percent=percent)

    def show_all(self):
        for human in self.members:
            print(human)


bob = Person('Bob Smith', 'developer')
sue = Person('Sue Adams', job='manager', pay=500)
tom = Manager('Tom Jones', pay=750)


if __name__ == '__main__':
    print(bob.name, bob.job)
    print(sue.name, sue.job, sue.pay)
    print(sue.give_raise(percent=0.2))
    print(sue)
    print(bob.get_last_name())
    print(tom.give_raise(percent=0.23))
    print(tom)
    print(tom.job)

    print('\n--All-three--')
    for person in (bob, sue, tom):
        person.give_raise(percent=0.15)
        print(person)

    print('\nDevelopment department')
    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raises(percent=0.12)
    development.show_all()

    print(list(bob.__dict__.keys()))
    print(list(bob.__dict__.items()))

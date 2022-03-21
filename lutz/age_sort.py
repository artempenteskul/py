class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} - {self.age}'


mike = Person('Mike', 22)
alice = Person('Alice', 33)
bob = Person('Bob', 44)

people = [bob, alice, mike]

people.sort(key=lambda x: x.age)


if __name__ == '__main__':
    print(mike)
    print(alice.name)
    print(bob.age)

    for person in people:
        print(person)

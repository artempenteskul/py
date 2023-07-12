class Person:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    person1 = Person('John')
    person2 = person1

    print(person1.name)
    print(person2.name)

    person1.name = 'Tim'

    print(person1.name)
    print(person2.name)

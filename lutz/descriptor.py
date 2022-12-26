class CardHolder:
    acct_len = 8
    retire_age = 60

    def __init__(self, acct, name, age, address):
        self.acct = acct
        self.name = name
        self.age = age
        self.address = address

    class Name:
        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value

    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if 0 <= value >= 150:
                raise ValueError('Invalid age.')
            else:
                self.age = value

    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace(' ', '_')
            if len(value) != instance.acct_len:
                raise TypeError('Invalid acct number.')
            else:
                self.acct = value

    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage

        def __set__(self, instance, value):
            raise TypeError('Cannot set remain')

    remain = Remain()

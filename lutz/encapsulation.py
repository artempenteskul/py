class MyClass:
    def __init__(self):
        self.public_var = 'Public property.'
        self._protected_var = 'Protected property.'
        self.__private_var = 'Private property.'

    def public_method(self):
        print('Public method.')

    def _protected_method(self):
        print('Protected method.')

    def __private_method(self):
        print('Private method.')


if __name__ == '__main__':
    obj = MyClass()

    # accessing public properties
    print(obj.public_var)
    obj.public_method()

    # accessing protected properties
    print(obj._protected_var)
    obj._protected_method()

    # accessing private properties
    print(obj._MyClass__private_var)
    obj._MyClass__private_method()

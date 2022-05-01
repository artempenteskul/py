class Tree:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def info(self):
        return f'{self.name}, {self.age}, {self.height}'

    def grow(self):
        self.age += 1
        self.height += 2


class FruitTree(Tree):
    def __init__(self, name, age, height):
        self.amount = height * 4
        super(FruitTree, self).__init__(name=name, age=age, height=height)


if __name__ == '__main__':
    fruit_tree = FruitTree('apple', 12, 24)
    print(fruit_tree.amount)
    print(fruit_tree.name)
    print(fruit_tree.age)

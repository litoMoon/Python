import pytest


class Fruit:
    def __init__(self, name,color):
        self.name = name
        self.color=color

    def __eq__(self, other):
        return self.color == other.color

@pytest.fixture
def fruit1():
    return Fruit("apple","red")

@pytest.fixture
def fruit2(fruit1):
    # fruit1.color="yellow"
    curFruit=Fruit(fruit1.name,"yellow")
    # curFruit.color="yellow"
    return [curFruit,Fruit("orange","yellow")]

def est_fruit(fruit1,fruit2):
    assert fruit1 in fruit2
# Polymorphism is the act of having multiple forms in a way of behaving
# differently depending on what conditions u were called in

# To make it more real and understandable, it's like having one thing
# that you can use for different tasks and in every kind of tasks it
# behaves differently and delivers different service

# To translate this into a pythonic way, to achieve polymorphism in python
# We have four ways :
# 1 _ Duck Typing
# 2 _ Method Overloading
# 3 _ Operator Overloading
# 4 _ Mehod Overriding

# Let's see each one in a detailed way:

# DUCK TYPING :

# duck typing is the act of judging something based on its behavior like
# the old saying: if it walks like a duck, quacks like a duck, swims like
# a duck, then it's probably a duck.
# So based on the behavior we judged that the creature is a duck
# Let's translate it into a pythonic way:

# First let's know the diff btwn Static and dynamic typing:
# Dynamic typing is a feature of not having to specify the data type
# of variables during compile time, python distinguishes the data types
# itself in run time But static typing means that we have to specify
# the data types of variables in compile time, like in C and Java

class Duck:
    def swim(self):
        print('I swim like a duck')

    def quack(swim):
        print('I quack like a duck')


class Chicken:
    def swim(self):
        print('I cant swim')

    def quack(self):
        print('I cant quack')


class Human:
    def swim(self):
        print('I can swim')


def display(animal):
    animal.swim()
    animal.quack()
    print('\nSo is it or is it not a duck ?\n')


first = Duck()
display(first)
second = Chicken()
display(second)
third = Human()
# display(third)

# So in duck typing we only care if the objects have these methods we need
# But we don't care what class they are thanks to dynamic typing


# OPERATOR OVERLOADING:
print(1 + 2)  # print(int.__add__(1, 2))
print('1' + '2')  # print(str.__add__('1', '2'))

# METHOD OVERLOADING:
# Python does not support method overloading by default, but there
# are some ways how we can achieve this

# Method overloading is the act of defining multiple methods
# with the same name but with different parameters in the same class
# Since python doesn't support polymorphism by default then if we just
# define multiple methods with the same name in the same class
# It's gonna take the last definition by default


class Trial:
    def addition(self, *args):
        total = 0
        for i in args:
            total += i
        return total


n = Trial()
print(n.addition(1, 2, 4, 5, 6, 7, 7))

print('\n')
# METHOD OVERRIDING:
# method overriding is when we have a method in a base class the we
# modify  on its implemetation or add to it in child classes
# And the method must keep the same name and parameters


class Base:
    def thanks(self):
        print('thank you from base class')


class Child1(Base):
    def thanks(self):
        super().thanks()
        print('And from Child1')


class Child2(Base):
    def thanks(self):
        print('Leave the child2 alone!')


l = [Base(), Child1(), Child2()]
for m in l:
    m.thanks()
    print('     ==     ==     ')

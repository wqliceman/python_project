class TheThing(object):
    def __init__(self):
        self.number = 0

    def some_function(self):
        print "I got called"

    def add_me_up(self, other):
        self.number += other
        return self.number



def test():
    a = TheThing()
    b = TheThing()

    a.some_function()
    b.some_function()

    print a.add_me_up(20)
    print b.add_me_up(40)

    print a.number
    print b.number

if __name__ == "__main__":
    test()

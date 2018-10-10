from byotest import assert_equal



def add(x, y):
    return x + y


assert_equal(add(5, 3), 9)

assert_equal(add(5, 3), 8)
assert_equal(add(2, 2), 4)
assert_equal(add(-1, -5), -6)
assert_equal(add(-7, 2), -5)
assert_equal(add(0, 0), 0)
assert_equal(add(65535, 1), 65536)


print("All tests pass")

'''
Write a function called get_change, which accepts one argument amount (an integer). The function should return the coins needed to dispense that amount.
The coin denominations are Euro
(1, 2, 5, 10, 20, 50, 100, 200)
The function should return the fewest coins possible to make the amount.
E.g. 76c = 50, 20, 5, 1
     44c = 20, 20, 2, 2
'''

def get_change
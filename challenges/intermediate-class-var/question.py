"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""


class Foo:
    """Hint: No need to write __init__"""


## End of your code ##
Foo.bar = 1
Foo.bar = "1"  # expect-type-error

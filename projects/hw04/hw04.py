def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    seq = 0
    this_fib = 0
    next_fib = 1
    def print_fib():
        nonlocal this_fib
        nonlocal next_fib
        nonlocal seq
        if seq == 0:
            seq += 1
            return this_fib
        elif seq == 1:
            seq += 1
            return next_fib
        else:
            this_fib, next_fib = next_fib, this_fib + next_fib
            return next_fib
    return print_fib


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    wrong_lst = []
    def withdraw(amount, passin):
        nonlocal wrong_lst
        nonlocal balance
        if len(wrong_lst) == 3:
            return 'Your account is locked. Attempts: ' + str(wrong_lst)
        else:
            if passin != password:
                wrong_lst.append(passin)
                return 'Incorrect password'
            else:
                if amount > balance:
                    return 'Insufficient funds'
                else:
                    balance  = balance - amount
                    return balance
    return withdraw



class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2019
    >>> dime = mint.create(Dime)
    >>> dime.year
    2019
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2019
    >>> nickel.worth()  # 5 cents + (81 - 50 years)
    36
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (156 - 50 years)
    116
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (156 - 50 years)
    126

    """
    current_year = 2019

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        return kind(self.year)


    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.current_year


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        if Mint.current_year - self.year >= 50:
            return self.cents + (Mint.current_year - self.year - 50)
        else:
            return self.cents

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    balance = 0
    stock = 0

    def __init__(self, product, price):
        self.product = product
        self.price = price


    def vend(self):
        if self.stock == 0 and self.balance == 0:
            return 'Machine is out of stock.'
        elif self.stock == 0 and not balance == 0:
            return 'Machine is out of stock. Here is your $' + '{}'.format(self.balance)
        elif not self.stock == 0 and self.balance < self.price:
            return 'You must deposit $' + str(self.price - self.balance) + ' more.'
            #f'You must deposit ${self.price - self.balance} more.'
        elif not self.stock == 0 and self.balance == self.price:
            self.stock -= 1
            self.balance -= self.price
            return 'Here is your ' + str(self.product) + '.'
        else:
            self.stock -= 1
            change = self.balance - self.price
            self.balance = 0
            return 'Here is your ' + str(self.product) + ' and $' + str(change) + ' change.'
            # return f'Here is your {self.product} and ${change} change.'


    def restock(self, num):
        self.stock += num
        return 'Current ' + str(self.product) + ' stock: ' + str(self.stock)

    def deposit(self, money):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(money) + '.'
        else:
            self.balance += money
            return 'Current balance: $' + str(self.balance)



def remove_all(link , value):
    """Remove all the nodes containing value in link. Assume that the
    first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    while link.rest is not Link.empty:
        if link.rest.first == value:
            link.rest = link.rest.rest
        else:
            link = link.rest



def generate_paths(t, x):
    """Yields all possible paths from the root of t to a node with the label x
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    """

    def path(t):
        path_lst = []
        if t.is_leaf():
            path_lst.append([t.label])
            return path_lst
        else:
            for b in t.branches:
                for i in path(b):
                    path_lst = path(b).insert(0, t.label)
            return path_lst
    yield from [elem for elem in path_lst if x in elem]

    """

    """

    def path(t, path_lst):
        if t.is_leaf():
            path_lst.append([t.label])
        else:
            sub_paths = []
            for b in t.branches:
                sub_paths = path(b, [])
                for sub_path in sub_paths:
                    path_lst.append([t.label] + sub_path)
            return path_lst

    yield from [elem for elem in path(t, []) if x in elem]

    """


    if t.label == x:
        yield [x]
    for b in t.branches:
        for path in generate_paths(b,x):
            "*** YOUR CODE HERE ***"
            yield [t.label] + path




## Link Class ##

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

## Tree Class ##

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

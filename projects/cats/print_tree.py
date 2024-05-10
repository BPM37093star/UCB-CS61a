def  print_tree(t, indent = 0):
    if is_leaf(t):
        print(label(t))
    for b in branches(t):
        indent += 1
        print(/t * indent, label(b))


def fib_tree(n):
    if n == 0:
        return tree(0)
    elif n == 1:
        return tree(1)
    else:
        return tree(n, [fib(n - 2), fib_tree(n - 1)]

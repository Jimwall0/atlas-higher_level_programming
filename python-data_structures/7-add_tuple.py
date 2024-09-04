#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = (0, 0)
    for n in range(2):
        if not tuple_a[n] and not tuple_b[n]: new[n] = 0
        elif not tuple_a[n]: new[n] = 0 + tuple_b[n]
        elif not tuple_b[n]: new[n] = 0 + tuple_a[n]
        else: new[n] = tuple_a[n] + tuple_b[n]
    return new


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

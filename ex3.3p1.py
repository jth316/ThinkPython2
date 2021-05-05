def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_row():
    print('- - - -', end=' ')
    print('+', end=' ')

def print_column():
    print('|        ', end=' ')

def print_rows():
    print('+', end=' ')
    do_twice(print_row)
    print()

def print_columns():
    do_twice(print_column)
    print('|')

def print_across():
    print_rows()
    do_four(print_columns)

def print_grid():
    do_twice(print_across)
    print_rows()

print_grid()
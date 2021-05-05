def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_across():
    print('+', '- - - -', end=' ')
   

def print_row():
    do_four(print_across)
    print('+')

def print_down():
    print('|', '       ', end=' ')

def print_column():
    do_four(print_down)
    print('|')

def print_section():
    print_row()
    do_four(print_column)

def print_grid():
    do_four(print_section)
    print_row()

print_grid()
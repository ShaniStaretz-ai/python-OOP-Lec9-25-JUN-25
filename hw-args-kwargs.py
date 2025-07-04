def sum_numbers(*args):
    return sum(args)

def print_user_info(**kwargs):
    out=''
    last_key=next(reversed(kwargs))
    for key,value in kwargs.items():
        out+=key+': '+str(value)
        if key!=last_key:
            out+=', '
    print(out)

def combine_values(*args, **kwargs):
    print(f"sum:{sum_numbers(*args)}")
    print_user_info(**kwargs)

def greet_user(**kwargs):
    name=kwargs.get('name', 'Guest')
    print(f"Hello {name}")

if __name__ == '__main__':
    print(sum_numbers(1, 2, 3, 4))
    print_user_info(name="Dana", age=30, city="Tel Aviv")
    combine_values(2, 4, 6, name="Tom", job="Dev")
    greet_user(name="Lior")
    greet_user()
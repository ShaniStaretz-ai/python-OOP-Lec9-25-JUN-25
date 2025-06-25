def sum_args(x, y, *args):
    return x + y + sum(args)


def print_info(fname, lname, address, *args, **kwargs):
    if 'hide' in kwargs.keys() and kwargs['hide']:
        print(f'first name is{fname}')
    else:
        print(f'first name is {fname} last name is {lname} address is {address}')
    if 'upper' in kwargs.keys() and kwargs['upper']:
        print(f'first name is {fname.upper()} last name is {lname.upper()} address is {address.upper()}')


def safe_run(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'error occurred: {e}')

    return wrapper


@safe_run
def do_div(a, b):
    return a / b


if __name__ == '__main__':
    print(sum_args(1, 2, 3))
    result = do_div(3, 0)
    if result: #if an error happened, will return None, else will print the result
        print(result)

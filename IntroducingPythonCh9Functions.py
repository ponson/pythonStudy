
def document_it(func):
    def new_function1(*args, **kwargs):
        print("Running functions: ", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        print("locals: ", locals())
        return result

    print("locals: ", locals())
    return new_function1


def square_it(func):
    def new_function2(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function2


@document_it
@square_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

print("globals:", globals())
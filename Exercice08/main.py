

def log_decorator(func):
    def wrapper():
        print("Message avant exécution")
        func()
        print("Message après exécution")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()

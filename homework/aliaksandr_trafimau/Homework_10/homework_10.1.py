def finish_me(func):
    def wrapper():
        func()
        print('Finished')
    return wrapper


@finish_me
def say_hello():
    print("Hello")
say_hello()

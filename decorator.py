# NOTE Decorator không có tham số
def decorator_example(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@decorator_example
def say_hello():
    print("hello")


say_hello()


# Decorator có tham số
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result

    return wrapper


@decorator_with_args
def add(a, b):
    return a + b


result = add(3, 4)
print(result)  # Output: 7


def require_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("user") != "admin":
            raise PermissionError("You must be an admin to call this function.")
        func(*args, **kwargs)

    return wrapper


@require_admin
def update_settings(*args, **kwargs):
    print("Settings updated.")


update_settings(user="guest")  # This will work

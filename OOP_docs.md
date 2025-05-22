# OOP

## Class

Class (lớp) là khuôn mẫu (template) để tạo ra các Object (đối tượng).
Nó mô tả các thuộc tính (attributes) và hành vi (methods) chung của một nhóm đối tượng.

```python
class Person:
    def __init__(self, name, age):
        self.name = name        # Thuộc tính
        self.age = age

    def say_hello(self):        # Phương thức (method)
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
```

## Object

Object (đối tượng) là một thể hiện (instance) cụ thể của một class
Nó có dữ liệu riêng và có thể gọi các phương thức định nghĩa trong class.

```python
person1 = Person("Nguyên", 25)   # Object
person1.say_hello()              # Gọi method
```

| Modifier  | Cách viết | Ý nghĩa trong Python                              |
| --------- | --------- | ------------------------------------------------- |
| Public    | `name`    | Truy cập công khai                                |
| Protected | `_name`   | Truy cập nội bộ, không nên dùng bên ngoài         |
| Private   | `__name`  | Ẩn tên bằng "name mangling", tránh truy cập ngoài |

# Abstraction

Trừu tượng là ẩn đi chi tiết phức tạp, chỉ cung cấp giao diện cần thiết để sử dụng.

Trong Python, trừu tượng thường được thực hiện qua lớp trừu tượng (abstract class) và phương thức trừu tượng (abstract method).

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
```

# Polymorphism

Đa hình là khả năng sử dụng chung một interface nhưng hành vi khác nhau tuỳ theo đối tượng.
Trong Python, bạn không cần khai báo kiểu rõ ràng – miễn là object có phương thức tương ứng.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_sound(animal):
    print(animal.speak())

make_sound(Dog())  # Woof!
make_sound(Cat())  # Meow!
```

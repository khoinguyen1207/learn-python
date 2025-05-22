int_num = 5
# print(int_num)
# print(type(int_num))


int_float = 5.2
# print(int_float)
# print(type(int_float))


my_str = "Hello, World!"
my_str_2 = "Toi la 'Python' ne!"
my_str_4 = """
Toi la 'Python' ne!
Toi la "Python" ne!
"""
# print(my_str)
# print(my_str_2)
# print(my_str_4)


# List
my_list = [-1, 12, 8, "Hello", True]
my_list_2 = []
my_list.append(10)
my_list.extend([11, 12, 13])
my_list.insert(0, 0)
# my_list_sorted = sorted(my_list)
reverse_list = my_list[::-1]  # hoặc my_list.reverse() start:end:step
# print(my_list.index(-1))


# => List có thể thay đổi, có trùng lặp, có thứ tự


# Tuple
my_tuple = (1, 2, 3, 4, 5)
init_tuple = ()
one_item_tuple = (1,)  # Phải có dấu phẩy

tuple_to_list = list(my_tuple)  # Chuyển tuple thành list
tuple_to_list.append(6)  # Thay đổi list
list_to_tuple = tuple(tuple_to_list)  # Chuyển list thành tuple

count_tuple = my_tuple.count(
    1
)  # Đếm số lần xuất hiện của 1 trong tuple, nếu không có thì trả về 0
index_item = my_tuple.index(1)  # Tìm vị trí của 1 trong tuple, nếu không có thì báo lỗi

typle_1 = ("a", 2, 3.5, "b")
typle_2 = ("a", 2, 3.5, "b")
# print(f"Id tuple_1: {id(typle_1)}")
# print(f"Id tuple_2: {id(typle_2)}")
# => Id tuple_1: 140706195584064 và Id tuple_2: 140706195584064 vì tuple_1 và tuple_2 đều trỏ đến cùng một vùng nhớ
# => Tuple không thể thay đổi, có trùng lặp, có thứ tự


# Set
my_set = {1, 2, 3, 4, 5}
my_set_2 = set()  # Tạo set rỗng
my_set.add(9)
my_set.remove(2)  # => Xóa phần tử trong set với giá trị 1
my_set.discard(
    2
)  # => Xóa phần tử trong set với giá trị 1, nếu không có thì không báo lỗi


set_1 = {1, 2, 3}
set_2 = {5, 2, 4}

set_3 = set_1.union(set_2)  # Lấy tất cả các phần tử trong hai set
set_4 = set_1.intersection(set_2)  # Lấy các phần tử chung trong hai set
set_5 = set_1.symmetric_difference(set_2)  # Lấy các phần tử khác nhau trong hai set
set_6 = set_1.difference(set_2)  # Lấy các phần tử trong set_1 mà không có trong set_2
set_7 = set_2.difference(set_1)  # Lấy các phần tử trong set_2 mà không có trong set_1

# => Set không có thứ tự, không có trùng lặp, có thể thay đổi


# Dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict_2 = dict()
my_dict_3 = {}
my_dict["sex"] = "Male"

# for key, v in my_dict.items():
#     print(f"{key}: {v}")

# => Dict Có thể thay đổi, không có thứ tự, có trùng lập value, không có trùng lặp key


# For loop
my_list = [1, 2, 3, 4, 5]
# for i in range(len(my_list)):
#     print(f"Index: {i}, Value: {my_list[i]}")  # In ra index và value của list


# Copy file
import datetime
import json
import shutil
import os


def copy_file(src, dst):
    shutil.copy(os.path.join(src, "c.txt"), os.path.join(dst, "c.txt"))


source_dir = "source_dir"
des_dir = "des_dir"
copy_file(source_dir, des_dir)


# File handling
with open("my_file.txt", "a") as f:
    f.write("\nTao la 'Python' ne!")

with open("my_file.txt", "r") as f:
    content = f.read()
    # print(content)

# with là context manager, nó sẽ tự động quản lý tài nguyên


# OOP
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age


my_stu = Student("John", 20)
# my_stu.greet()
# print(my_stu.age)

# ============================================
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


#  Dump and Load JSON
from datetime import date, datetime
import json

initial_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling"],
    "dob": datetime.now(),
}

# with open("data.json", "w") as f:
#     json.dump(
#         initial_dict,
#         fp=f,
#         indent=4,
#         default=lambda x: x.isoformat() if isinstance(x, datetime) else str(x),
#     )


with open("data.json") as f:
    my_content = json.load(f)

print(my_content)
my_content["dob"] = datetime.fromisoformat(my_content["dob"])
print(my_content)

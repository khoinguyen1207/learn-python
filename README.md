# Data Type and Variables

- int
- float
- complex => ex: z = 2 + 3j
- string
- boolean: True / False
- None

# Arithmetic operators

- Addition +
- Subtraction -
- Multiplication `*`
- Division /
- Modulus %
- Exponentiation `**` (Lũy thừa)
- Floor division //

  - Ex: 10 // 3 => 3 Nhận được số nguyên lớn nhất nhỏ hơn hoặc bằng kết quả
  - 20 // 3 = 6 => floor division
  - 20 % 3 = 2 => modulus

# String type

my_str = "hello"

- len(my_str) -> 5
- my_str[0] => h
- my_str[1] => e
- my_str[4] => 0
- my_str[-1] => o
- my_str[-2] => l

# Slicing for string

my_str = "hello"

- my_str[1:4] => `ell` indices: 1, 2, 3
- my_str[1:] => `ello` indices: 1, 2, 3, 4
- my_str[:-1] => `hell` không bao gồm index -1

# Nối chuỗi

str_1 = "hel"
str_2 = "lo"
=> str_1 + str_2 = "hello

```python
if "lo" in str_1_2:
    return True
else:
    return False
```

# Method

- my_str.upper()
- my_str.lower()

**string là immutable**

# Python Collection Types

| Kiểu dữ liệu | Mô tả                        | Có thể thay đổi? | Cho phép trùng lặp?  | Có thứ tự? |
| ------------ | ---------------------------- | ---------------- | -------------------- | ---------- |
| `list`       | Danh sách các phần tử        | ✅ Có            | ✅ Có                | ✅ Có      |
| `tuple`      | Danh sách cố định            | ❌ Không         | ✅ Có                | ✅ Có      |
| `set`        | Tập hợp các phần tử duy nhất | ✅ Có            | ❌ Không             | ❌ Không   |
| `dict`       | Cặp key-value (từ điển)      | ✅ Có            | ✅ (value), ❌ (key) | ✅ Có      |

## 🔹 List

Danh sách có thể thay đổi, chứa các phần tử theo thứ tự.

```python
my_list = [3, 1, 2]

my_list.append(4)         # [3, 1, 2, 4]
my_list.extend([5, 6])    # [3, 1, 2, 4, 5, 6]
my_list.insert(0, 0)      # [0, 3, 1, 2, 4, 5, 6]
my_list.remove(3)         # [0, 1, 2, 4, 5, 6]
val = my_list.pop()       # Xóa và trả về 6
idx = my_list.index(4)    # Trả về 3
count_1 = my_list.count(1)# Trả về 1
my_list.sort()            # [0, 1, 2, 4, 5]
my_list.reverse()         # [5, 4, 2, 1, 0]
copy_list = my_list.copy()
my_list.clear()           # []
```

## 🔹 Tuple

Danh sách **không thay đổi**, dùng cho dữ liệu cố định.

**Cú pháp:**

```python
my_tuple = (1, 2, 3)
empty_tuple = ()
one_item_tuple = (5,)  # Dấu phẩy quan trọng!
```

## 🔹 Set

Tập hợp **không có phần tử trùng**, không đảm bảo thứ tự.

**Cú pháp:**

```python
empty_set = set()  # Không dùng {} vì {} là dict rỗng!
set_1 = {1, 2, 3}
set_2 = {5, 2, 4}

set_3 = set_1.union(set_2) # Lấy tất cả các phần tử trong hai set
set_4 = set_1.intersection(set_2) # Lấy các phần tử chung trong hai set
set_5 = set_1.symmetric_difference(set_2) # Lấy các phần tử khác nhau trong hai set
set_6 = set_1.difference(set_2) # Lấy các phần tử trong set_1 mà không có trong set_2
set_7 = set_2.difference(set_1) # Lấy các phần tử trong set_2 mà không có trong set_1
```

> ⚠️ `{}` sẽ tạo dict, không phải set!

## 🔹 Dictionary (dict)

Lưu trữ dữ liệu dưới dạng `key: value`.

**Cú pháp:**

```python
my_dict = {
  "name": "Nguyên",
  "age": 25
}
# Thêm hoặc cập nhật
my_dict["age"] = 26
# Truy xuất
print(my_dict["name"])
```

## 📌 Ghi chú:

- `list`, `tuple`: giữ nguyên thứ tự chèn phần tử.
- `set`: tự loại bỏ trùng lặp, không có thứ tự.
- `dict`: key là duy nhất, value có thể trùng.

> 💡 **Mẹo học nhanh:**
>
> - Dùng `list` khi cần thêm/xoá/sắp xếp.
> - Dùng `tuple` khi dữ liệu không cần thay đổi.
> - Dùng `set` để lọc phần tử trùng lặp.
> - Dùng `dict` để tra cứu theo khóa (key).

# File handling

```python
file = open("filename.txt", "mode")
```

- Example:

```python
with open("my_file.txt", "a") as f:
    f.write("\nTao la 'Python' ne!")

with open("my_file.txt", "r") as f:
    content = f.read()
    print(content)
```

| Chế độ (`mode`) | Ý nghĩa                                | Ghi chú                                      |
| --------------- | -------------------------------------- | -------------------------------------------- |
| `'r'`           | **Read** – mở file chỉ để đọc          | Mặc định. Báo lỗi nếu file không tồn tại.    |
| `'w'`           | **Write** – mở file để ghi             | Tạo mới hoặc _ghi đè_ nếu file đã tồn tại.   |
| `'a'`           | **Append** – ghi thêm vào cuối file    | Không xóa nội dung cũ. Tạo file nếu chưa có. |
| `'x'`           | **Create** – tạo file mới              | Báo lỗi nếu file đã tồn tại.                 |
| `'b'`           | **Binary** – mở file ở chế độ nhị phân | Dùng kết hợp: `'rb'`, `'wb'`, `'ab'`...      |
| `'t'`           | **Text** – mở file ở chế độ văn bản    | Mặc định. Dùng kết hợp: `'rt'`, `'wt'`...    |
| `'+'`           | **Read & Write** – cho phép đọc và ghi | Dùng kết hợp: `'r+'`, `'w+'`, `'a+'`...      |

# Generator expression

Cú pháp cơ bản

```python
(expression for item in iterable if condition)

Ex:
gen = (x**2 for x in range(5))
print(gen)           # <generator object ...>
print(next(gen))     # 0
print(next(gen))     # 1

```

Rất giống list comprehension, chỉ khác là:

- List comprehension dùng []

- Generator expression dùng () (không phải tuple)

# Exception handling

```python
try:
    # Code có thể gây ra lỗi
except ExceptionType:
    # Code xử lý lỗi
else:
    # Chạy nếu không có lỗi xảy ra trong try
finally:
    # Luôn chạy, dù có lỗi hay không



# Ex:
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0.")
    else:
        print("Kết quả:", result)
    finally:
        print("Kết thúc hàm divide.")

# Gọi hàm
divide(10, 2)
divide(5, 0)
```

# Regular Expression trong Python

| Hàm                                | Mô tả                                  |
| ---------------------------------- | -------------------------------------- |
| `re.match(pattern, string)`        | Kiểm tra chuỗi khớp với pattern từ đầu |
| `re.search(pattern, string)`       | Tìm phần khớp đầu tiên trong chuỗi     |
| `re.findall(pattern, string)`      | Trả về tất cả phần khớp dưới dạng list |
| `re.sub(pattern, replace, string)` | Thay thế phần khớp bằng chuỗi khác     |
| `re.split(pattern, string)`        | Tách chuỗi theo pattern                |

| Pattern  | Ý nghĩa                            |              |
| -------- | ---------------------------------- | ------------ |
| `.`      | Bất kỳ ký tự nào                   |              |
| `\d`     | Chữ số (0–9)                       |              |
| `\D`     | Không phải chữ số                  |              |
| `\w`     | Ký tự chữ + số + `_`               |              |
| `\W`     | Không phải ký tự `\w`              |              |
| `\s`     | Khoảng trắng (space, tab, newline) |              |
| `\S`     | Không phải khoảng trắng            |              |
| `^`      | Bắt đầu chuỗi                      |              |
| `$`      | Kết thúc chuỗi                     |              |
| \`a      | b\`                                | `a` hoặc `b` |
| `*`      | 0 hoặc nhiều lần                   |              |
| `+`      | 1 hoặc nhiều lần                   |              |
| `?`      | 0 hoặc 1 lần                       |              |
| `{n}`    | Lặp đúng `n` lần                   |              |
| `[abc]`  | Một trong các ký tự a, b hoặc c    |              |
| `[^abc]` | Không phải a, b hoặc c             |              |
| `(abc)`  | Nhóm ký tự                         |              |

- Example:

```python
text = "Liên hệ: contact@gmail.com hoặc admin@abc.edu"
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
print(emails)
# ['contact@gmail.com', 'admin@abc.edu']
```

```python
sdt = "0988123456"
if re.match(r"^0\d{9}$", sdt):
    print("Số điện thoại hợp lệ")
else:
    print("Không hợp lệ")
```

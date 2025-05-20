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

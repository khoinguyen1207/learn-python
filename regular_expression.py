import re

my_str = "Hello, World! World! Hello, World!"
match_data = re.match("Hello", my_str)  # Tìm kiếm chuỗi "Hello" trong my_str
# Output: <re.Match object; span=(0, 5), match='Hello'>

print(match_data)  # Nếu không tìm thấy thì trả về None
print(match_data.span())  # In ra vị trí bắt đầu và kết thúc của chuỗi tìm thấy
print(match_data.group())  # In ra chuỗi tìm thấy


search_data = re.search("W", my_str)  # Tìm kiếm chuỗi "World" trong my_str

# Output: <re.Match object; span=(7, 8), match='W'>
print(search_data)  # Nếu không tìm thấy thì trả về None
print(search_data.span())  # In ra vị trí bắt đầu và kết thúc của chuỗi tìm thấy
print(search_data.group())  # In ra chuỗi tìm thấy


findall_data = re.findall(
    "World", my_str
)  # Tìm kiếm tất cả các chuỗi "World" trong my_str
# Output: ['World', 'World', 'World']
print(findall_data)  # Nếu không tìm thấy thì trả về []


test_str = "Xin chao cac ban, toi la 'Python' ne!"
split_data = re.split(",", test_str)
# Output: ['Xin chao ', ' ban, toi la \'Python\' ne!']
print(split_data)  # Nếu không tìm thấy thì trả về []
print(" -".join(split_data))  # In ra chuỗi đã tách


# Tìm kiếm và thay thế chuỗi
test_str_2 = "I love Python, Python is my favorite language!"
replace_data = re.sub("Python", "Java", test_str_2)
# Output: 'I love Java, Java is my favorite language!'
print(replace_data)  # Nếu không tìm

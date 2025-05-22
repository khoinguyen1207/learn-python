# Decorator

Decorator là một mẫu thiết kế trong lập trình, cho phép bạn thêm chức năng mới vào một đối tượng mà không làm thay đổi cấu trúc của nó. Decorator thường được sử dụng để mở rộng chức năng của các lớp mà không cần phải tạo ra các lớp con mới.

```python
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
update_settings(user="admin")  # This will raise PermissionError
```

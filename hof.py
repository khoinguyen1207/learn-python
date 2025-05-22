def calculate_sum(list):
    return sum(list)


def higher_order_function(func, my_list):
    return func(my_list)


result = higher_order_function(calculate_sum, [3, 4, 5])
print(result)


# NOTE return function as it result
def place_order_binance(order_id):
    print(f"Placing order on binance: {order_id}")


def place_order_okx(order_id, size):
    print(f"Placing order on okx: {order_id} and size: {size}")


def place_order_bybit(order_id):
    print(f"Placing order on bybit: {order_id}")


place_order_func = {
    "binance": place_order_binance,
    "okx": place_order_okx,
    "bybit": place_order_bybit,
}


def get_place_order_func(exchange):
    return place_order_func[exchange]


my_func = get_place_order_func("binance")
my_func("1234567890")

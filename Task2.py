# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def hashable(key):
    pass


def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hashable(key):
            result[key] = value
        else:
            result[str(key)] = value
    return result
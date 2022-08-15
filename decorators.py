from datetime import datetime
from typing import Callable


def decoration_logger(function: Callable):
    def multi_time(*args, **kwargs):
        with open('log/info_functions_log.txt', 'a', encoding='utf-8') as f:
            f.write(f'Дата и время: {str(datetime.now())}\nИмя функции: {str(function.__name__)}\n'
                    f'Аргументы до вызова: {(args, kwargs)}\n')
            result = function(*args, **kwargs)
            f.write(f'Возвращаемое значение: {str(result)}\n\n')
        return result

    return multi_time


def decoration_log_dir(path: str):
    def decoration_log(function: Callable):
        def multi_time(*args, **kwargs):
            with open(f'{path}', 'a', encoding='utf-8') as f:
                f.write(f'Дата и время: {str(datetime.now())}\nИмя функции: {str(function.__name__)}\n'
                        f'Аргументы до вызова: {(args, kwargs)}\n')
                result = function(*args, **kwargs)
                f.write(f'Возвращаемое значение: {str(result)}\n\n')
            return result

        return multi_time

    return decoration_log
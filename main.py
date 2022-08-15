from decorators import decoration_log_dir, decoration_logger


@decoration_log_dir('log/multiplication_log.txt')
def multiplication(a: int, b: int):
    return a * b


@decoration_logger
def test(b: str):
    return b


if __name__ == '__main__':
    multiplication(3, 14)
    test('Hello word')
    pass
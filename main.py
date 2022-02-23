import typing


def print_hello() -> None:
    """
    Print 'Hello' on the terminal.
    :return: None.
    """
    msg: str = "Hello"
    print(msg)
    return None


if __name__ == "__main__":
    print_hello()

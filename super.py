# Simple Python script demonstrating a few common concepts

def greet(name: str) -> str:
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    print(greet("World"))
    print("Is 10 even?", is_even(10))
    print("Is 11 even?", is_even(11))

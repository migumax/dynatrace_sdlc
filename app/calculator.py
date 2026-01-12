def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b must not be 0")
    return a / b
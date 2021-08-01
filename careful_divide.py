def careful_divide(a: float, b: float) -> float:
    """Divide a by b
    
    Raises:
        ValueError: when inputs cannot be divided
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError(f'invalid input {a} and {b}')

careful_divide(21.1, 0.0)
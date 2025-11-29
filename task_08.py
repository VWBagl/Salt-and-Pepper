def multiply_numbers(inputs=None):
    numbers = [int(i) for i in str(inputs) if i in '0123456789']
    
    if not numbers:
        return None
    
    result = 1
    for num in numbers:
        result *= num

    return result



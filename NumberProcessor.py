class NumberProcessor:
    def __init__(self) -> None:
        pass

    def decimal_to_binary_array(self, number):
        binary_array = []
        
        while number != 0:
            binary_array.insert(0, number % 2 == 1)
            number //= 2
        
        return binary_array

    
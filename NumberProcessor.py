import HexNumber
class NumberProcessor:
    def __init__(self):
        self.hex_map = HexNumber.HexNumber([False,False,False,False]).hex_map
        self.normalize_binary_array = True

    def set_normalize_binary_array(self, state):
        self.normalize_binary_array = state

    def decimal_to_binary_array(self, number):
        binary_array = []
        
        while number != 0:
            binary_array.insert(0, number % 2 == 1)
            number //= 2
        
        if self.normalize_binary_array == True:
            while len(binary_array) < 4:
                binary_array.insert(0, False)

        return binary_array

    def find_hex_map_index(self, char):
        index = None
        for idx, value in self.hex_map.items():
            if value == char:
                return idx
        
        return None
                

    def hexa_to_decimal(self, number):
        return self.find_hex_map_index(number)

    def hexa_to_binary_array(self, number):
        decimal =  self.hexa_to_decimal(number)
        return self.decimal_to_binary_array(decimal)
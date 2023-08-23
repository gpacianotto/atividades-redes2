class HexNumber:
    def __init__(self, bool_array):
        if len(bool_array) != 4:
            raise ValueError("The boolean array must have a length of 4")
        
        self.bool_array = bool_array
        self.genDecimalValue()
        self.genHexaChar()

    def genDecimalValue(self):
        value = 0
        index = 0
        
        while index < len(self.bool_array):
            if(self.bool_array[index] == True):
                value = value + (2 ** (len(self.bool_array) - (index + 1)))
            index += 1
        self.decimalValue = value

    def genHexaChar(self): 
        hex_map = {
            0: '0', 1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'A', 11: 'B',
            12: 'C', 13: 'D', 14: 'E', 15: 'F'
        }
        if self.decimalValue in hex_map:
            self.hexaChar = hex_map[self.decimalValue]
        else:
            self.hexaChar = "X"

    
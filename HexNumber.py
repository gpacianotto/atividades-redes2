class HexNumber:
    def __init__(self, bool_array):
        self.hex_map = {
            0: '0', 1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'A', 11: 'B',
            12: 'C', 13: 'D', 14: 'E', 15: 'F'
        }
        if len(bool_array) != 4:
            raise ValueError("The boolean array must have a length of 4")
        
        self.bool_array = bool_array
        self.genDecimalValue()
        self.genHexaChar()
        self.gen_binary_array()
        self.gen_binary_string()
    
    def __str__(self):
        return self.bool_array
    
    def __repr__(self) -> str:
        return str(self.bool_array)

    def gen_binary_array(self) :
        result = []
        for state in self.bool_array:
            if state == True:
                result.append(1)
            elif state == False:
                result.append(0)
            else: result.append(-1)
        
        self.binary_array = result
    
    def gen_binary_string(self):
        binary_array = self.binary_array
        result = ""
        for binary in binary_array:
            if(binary == 1):
                result+="1"
            elif(binary == 0):
                result+="0"
        
        self.binary_string = result


    def genDecimalValue(self):
        value = 0
        index = 0
        
        while index < len(self.bool_array):
            if(self.bool_array[index] == True):
                value = value + (2 ** (len(self.bool_array) - (index + 1)))
            index += 1
        self.decimalValue = value

    def genHexaChar(self): 
        hex_map = self.hex_map
        if self.decimalValue in hex_map:
            self.hexaChar = hex_map[self.decimalValue]
        else:
            self.hexaChar = "X"

    
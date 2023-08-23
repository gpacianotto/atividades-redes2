import HexNumber

hexmap = ['0', '1', '2', '3', '4', '5','6','7','8','9','A','B','C','D','E','F']

class IPv6Interpreter:
    def __init__(self, prefix):
        self.hex_map = HexNumber.HexNumber([False,False,False,False]).hex_map
        self.prefix = prefix

    def process_address(self):
        raw = self.prefix

        for char in raw:
            if(self.hex_map.__contains__(char)):
                print(char)
            else:
                print("X")
import HexNumber
import NumberProcessor

class IPv6Interpreter:
    def __init__(self, prefix):
        self.hex_map = HexNumber.HexNumber([False,False,False,False]).hex_map
        self.prefix = prefix
        print("prefix " + prefix)

    def process_address(self):
        raw = self.prefix
        result = {
            "hexa_values": []
        }
        for char in raw:
            char_upper = char.upper()
            if char_upper in self.hex_map.values():
                binary_array = NumberProcessor.NumberProcessor().hexa_to_binary_array(char_upper)
                hexa_number = HexNumber.HexNumber(binary_array)
                result["hexa_values"].append(hexa_number)
            # elif char_upper == ":":

            else:
                print("X")
        print(result)
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
        zero = [
            HexNumber.HexNumber([False, False, False, False]),
            HexNumber.HexNumber([False, False, False, False]),
            HexNumber.HexNumber([False, False, False, False]),
            HexNumber.HexNumber([False, False, False, False])
        ]
        buffer = []
        ipv6 = []
        for char in raw:
            char_upper = char.upper()
            
            if char_upper in self.hex_map.values():
                print("char lido: " + char_upper)
                binary_array = NumberProcessor.NumberProcessor().hexa_to_binary_array(char_upper)
                
                hexa_number = HexNumber.HexNumber(binary_array)
                # result["hexa_values"].append(hexa_number)
                buffer.append(hexa_number)
                print("hexa_number:  " + str(hexa_number))
            elif char_upper == ":":
                while len(buffer) < 4:
                    buffer.insert(0, HexNumber.HexNumber([False, False, False, False]))
                ipv6.append(buffer)
                buffer = []
            elif char_upper == "/":
                print("PEGOU A BARRA")
                while len(buffer) < 4:
                    buffer.insert(0, HexNumber.HexNumber([False, False, False, False]))
                ipv6.append(buffer)
                buffer = []
            else:
                print("DEU ALGUM ERRO CABULOSO")
        while len(ipv6) < 8:
            ipv6.append(zero)
        print(ipv6)
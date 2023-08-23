import HexNumber
import NumberProcessor
import IPv6Interpreter

# array = NumberProcessor.NumberProcessor().decimal_to_binary_array(11)

# print(array)

# number = HexNumber.HexNumber(array)

# print(number.decimalValue)
# print(number.hexaChar)

# print(NumberProcessor.NumberProcessor().decimal_to_binary_array(25))

print(IPv6Interpreter.IPv6Interpreter("2001:db8::/32").process_address())
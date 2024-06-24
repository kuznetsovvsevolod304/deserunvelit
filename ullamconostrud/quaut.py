def fletcher_checksum(data):
    sum1 = 0
    sum2 = 0
    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255
    checksum = (sum2 << 8) | sum1
    return checksum

# Example usage
data = b'Hello, world!'
checksum = fletcher_checksum(data)
print("Fletcher checksum:", checksum)

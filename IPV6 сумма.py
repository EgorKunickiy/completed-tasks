def process_the_string(ipv6_str):

    separator = ipv6_str[4]
    number_blocks_16 = ipv6_str.split(separator)
    number_blocks_10 = []

    for block in number_blocks_16:
        result = 0
        for number in block:
            result += int(number, 16)
        result = str(result)
        number_blocks_10.append(result)

    return ''.join(number_blocks_10)

if __name__ == "__main__":

    print(process_the_string('1B1D:AF01:3847:F8C4:20E9:0111:DFEA:AAAA'))
    print(process_the_string('1111:1111:1111:1111:1111:1111:1111:1111'))
    print(process_the_string('1111-1111-1111-1111-1111-1111-1111-1111'))
    print(process_the_string('ABCD_1111_ABCD_1111_ABCD_1111_ABCD_1111'))
def from_16_to_10(str):
    separator = str[4]
    number_blocks_16 = str.split(separator)
    number_blocks_10 = []
    for block in number_blocks_16:
        sss = 0
        for iter in block:
            sss += int(iter, 16)
        sss = sss.__str__()
        number_blocks_10.append(sss)
    return ''.join(number_blocks_10)
if __name__ == "__main__":
    print(from_16_to_10('1B1D:AF01:3847:F8C4:20E9:0111:DFEA:AAAA'))
    print(from_16_to_10('1111:1111:1111:1111:1111:1111:1111:1111'))
    print(from_16_to_10('1111-1111-1111-1111-1111-1111-1111-1111'))
    print(from_16_to_10('ABCD_1111_ABCD_1111_ABCD_1111_ABCD_1111'))

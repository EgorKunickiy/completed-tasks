def substract_of_years(str1, str2):
    year1 = int(str1[:4])
    year2 = int(str2[:4])

    return abs(year1 - year2)

if __name__ == '__main__':
    print(substract_of_years('1997/10/10', '2015/10/10'))
    print(substract_of_years('2015/10/10', '1997/10/10'))
def Recalculation_of_years (humanYears):
    catYears = 15
    dogYears = 15
    if humanYears == 1:
        return [humanYears, catYears, dogYears]
    elif humanYears == 2:
        catYears += 9
        dogYears += 9
        return [humanYears, catYears, dogYears]
    else:
        catYears += 9 + (humanYears-2)*4
        dogYears += 9 + (humanYears-2)*5
        return [humanYears, catYears, dogYears]

if __name__ == '__main__':

    print(Recalculation_of_years(1))
    print(Recalculation_of_years(2))
    print(Recalculation_of_years(3))
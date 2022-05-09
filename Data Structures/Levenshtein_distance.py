def levenstein(first_word: str, final_word: str, action: bool):

    matr = [[i+j if i * j == 0 else 0 for j in range(len(final_word) + 1)]
            for i in range(len(first_word) + 1)]
    for i in range(1, len(first_word) + 1):
        for j in range(1, len(final_word) + 1):
            if first_word[i - 1] == final_word[j - 1]:
                matr[i][j] = matr[i-1][j-1]
            else:
                matr[i][j] = 1+min(matr[i-1][j], matr[i][j-1], matr[i-1][j-1])

    if action:
        list_actions = []
        i = len(first_word)
        j = len(final_word)
        for counter in range(max(i, j)):
            if matr[i][j] == matr[i-1][j]+1:
                list_actions.append('удаление')
                i -= 1
            elif matr[i][j] == matr[i][j-1]+1:
                list_actions.append('вставка')
                j -= 1
            elif matr[i][j] == matr[i-1][j-1]:
                list_actions.append('соответствие')
                i -= 1
                j -= 1
            elif matr[i][j] == matr[i-1][j-1]+1:
                list_actions.append('замена')
                i -= 1
                j -= 1
        return list(reversed(list_actions))
    else:
        return matr[len(first_word) - 1][len(final_word) - 1]


if __name__ == "__main__":
    print(levenstein('asdf', 'sdj', True))

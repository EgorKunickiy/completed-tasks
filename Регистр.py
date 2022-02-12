def register(str):
    block_words = str.lower().split()
    block_words[0] = block_words[0].capitalize()
    block_words[-1] = block_words[-1].capitalize()
    return ' '.join(block_words)

if __name__ == '__main__':
    print(register('lorEm iPsUm dolOr Sit amet'))
tokens_to_split = ('*', '/', '^', '+', '-', '(', ')', '=')


def splitting_string_into_tokens(s: str):
    s = s.replace(' ', '')
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in tokens_to_split:
            tokens.append(s[i])
            i += 1
        elif '0' <= s[i] <= '9':
            num = ''
            while i < len(s) and '0' <= s[i] <= '9':
                num += s[i]
                i += 1
            tokens.append(num)
        else:
            return []

    return tokens


if __name__ == '__main__':
    expression = input('Enter math expression you want to split into tokens: ')
    print(f'List of tokens: {splitting_string_into_tokens(s=expression)}')

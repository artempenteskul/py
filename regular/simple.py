import re

text_to_search = 'adn abc aAkk ABC def 0 32 113'

pattern = re.compile(r'\d\d')

matches = pattern.finditer(text_to_search)
test_matches = pattern.findall(text_to_search)

for match in matches:
    print(match)

print(test_matches)


sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'^Start')

res = pattern.findall(sentence)
print(res)

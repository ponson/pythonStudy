
class UppercaseException(Exception):
    pass

words = ['alex`', 'obies', 'CAT']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
import re


# @params("input,expected", [
#     ("hello", ['hello']),
#     ("hello world", ['hello', 'world']),
#     ("raggggg hammer dog", ['raggggg', 'hammer', 'dog']),
#     ("18-wheeler tarbox", ['18-wheeler', 'tarbox']),
#     ("12", None),
# ])
def words(text):
    return re.findall(r'', text)

    assert s.words(input) == expected

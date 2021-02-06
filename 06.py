def get_odd_and_even( word ):
    index = 0
    even_indexed = ""
    odd_indexed = ""
    for char in word:
        if( index % 2  == 0):
            even_indexed += char
        else:
            odd_indexed += char
        index += 1
    print( even_indexed + " " + odd_indexed )

test_cases = int(input())
words = list()
for i in range(0, test_cases):
    line = input()
    words.append( line )
for word in words:
    get_odd_and_even( word )
'''
Design an encode function that takes a list of strings and joins them into
one single string, and a matching decode function that takes that single
string and recovers the exact original list, in order. The strings can
contain any characters at all, including digits, the # character, or
sequences that look like your own encoding format, so a naive
join-with-a-delimiter scheme is not safe. For this exercise, the list is
given to you as a single input string strs, with elements separated by
"|".

Encode the resulting list with your own scheme, then immediately decode what you just encoded, and return the recovered list re-joined the same way, with `"|"` between elements.

An empty strs means an empty list, and two adjacent "|" characters mean an empty-string element sits between them.

Input: strs = "cat|dog"
Output: "cat|dog"
encoding "cat" and "dog" with a length-prefix scheme like "3#cat3#dog" and decoding it back recovers ["cat", "dog"] exactly
Input: strs = "4#dog|cat"
Output: "4#dog|cat"
the element "4#dog" looks like it could confuse a naive decoder, but a length-prefix scheme reads exactly 5 characters for it regardless of what they are, recovering it intact
Input: strs = "|a|"
Output: "|a|"
the list ["", "a", ""] round-trips correctly, including the empty-string elements
Constraints
0 <= number of strings in the list <= 200
0 <= length of each string <= 200
strings may contain any characters, including digits and '#', except the '|' used by this exercise's input/output transport format
'''
def encode(str):
    encodedStr=''
    strArr=str.split("|")
    for i in range(len(strArr)):
        lenght=f"{len(strArr[i])}"
        encodedStr+=(lenght+'#'+strArr[i])
    return encodedStr

def decode(str):
    decodedStr=[]
    i=0
    while i <len(str):
        j=i
        while j<len(str) and str[j]!='#':
            j+=1

        length=int(str[i:j])
        i=j+1
        decodedStr.append(str[i:i+length])
        i+=length

    return '|'.join(decodedStr)
def EncodeDecodeString(strs):
    encoded= encode(strs)
    decoded= decode(encoded)
    return decoded

print(EncodeDecodeString("cat|dog|mouse"))
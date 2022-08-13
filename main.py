# String Tokenizer

string = "1+2*(3-4)"


def stringTokenizer(string):
    result = []
    accu = ""

    for char in string:
        if char in "+-*/(){}[]^":
            if accu != "":
                result.append(char)
                accu = ""
            result.append(char)
        else:
            accu = accu + char
    return result


result = stringTokenizer(string)
print(result)

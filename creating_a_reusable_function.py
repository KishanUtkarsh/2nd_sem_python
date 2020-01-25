def emogi_converter(massage):
    words=massage.split()
    emogi={
        ":)":"F",
        ":(":"U"
    }
    output=''
    for word in words:
        output+=emogi.get(word,word)+' '

    return output


massage=input(">")
print(emogi_converter(massage))
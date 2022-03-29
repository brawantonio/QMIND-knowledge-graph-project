import json

def processText(text):
    
    words = text.split()

    col = {}
    for word in words:
        ascii_sum = 0
        for c in word:
            ascii_sum = ascii_sum + ord(c)
            col[word] = {
                "x" : ord(c),
                "y" : ascii_sum
            }
       

    return json.dumps(col)

    
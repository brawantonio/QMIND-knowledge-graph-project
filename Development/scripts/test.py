import json

def processText(text):
    
    words = text.split()

    col = []
    for word in words:
        ascii_sum = 0
        for c in word:
            ascii_sum = ascii_sum + ord(c)
            obj =  {
                "url": "https://www.cityofkingston.ca/documents/10180/7273601/" + word + "/2b7ea9d3-245f-40b8-9be2-2139632fe1e8",
                "Pcx" : ord(c),
                "Pcy" : ascii_sum,
                "Cos" : ascii_sum / ord(c)
             }
        col.append(obj)
       

    return json.dumps(col)

    
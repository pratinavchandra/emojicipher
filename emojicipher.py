def encode(message):
    to_encode = message
    encoded =""
    for letter in to_encode:
        val = ord(letter)-97
        if len(str(val)) < 2:
            emoji="\\"+"U0001f60"+str(val)
        elif val < 0:
            emoji="\\"+"U0001f6"+str(val+97)   
        else:    
            emoji="\\"+"U0001f6"+str(val)
        encoded=encoded+emoji
    print(encoded.encode().decode('unicode_escape'))
def decode(message):
    to_decode = message
    to_decode = to_decode.lower()
    decoded = ""
    for letter in to_decode:
        val=int('{:X}'.format(ord(letter)).replace("1F",""))-600
        if val < 25:
            val = val+97    
        decoded=decoded+chr(val)
    print(decoded)         
option=input("Enter \n 1. To Encode \n 2. To Decode\n: ")
message=input("Enter message: ")
if option == "1":
    encode(message)
if option == "2":
    decode(message)        
global code
#global loc
code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
def base64_encrypt(text):
    con = ''
    for i in text :
        asc = ord(i)                        # Ascii Conversion
        binary = bin(asc)                   # Binary Conversions
        binary = binary[2:]                 # removing '0b'
        con =  con + '0' + binary                  #Concatining all
    n = 6
    chunks = [con[i:i+n] for i in range(0, len(con), n)]
    for i in chunks:
        if len(i) != 6:
            pz = 6 - len(i) 
            loc = chunks.index(i) 
            zero=''
            for n in range(0,pz):
                zero += '0' 
            z = zero + i   
            chunks.insert(loc,z)     
        else:
            pass
    encypt = ''
    for i in chunks:
        i = '00' + i
        i = int(i,2)
        i = code[i]
        encypt += str(i)
    #encypt += '=='
    print(encypt)
   
if __name__ == '__main__':
    text = input("Enter the string to encrypt:\t")
    base64_encrypt(text)
  
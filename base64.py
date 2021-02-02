global code
code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

                                # Encryption Function
def base64_encrypt(text):
    con = ''
    for i in text :
        asc = ord(i)                                            # ASCII COnversion
        binary = bin(asc)                                       # Binary Conversion
        binary = binary[2:]                 
        con =  con + '0' + binary                               # Concatenate all
    n = 6
    chunks = [con[i:i+n] for i in range(0, len(con), n)]        # Grourping into 6 Char
    for i in chunks:                                            # If any grp has less thn 6 char add additional required 00
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
        i = '00' + i                                            # Convert six-bit bytes into eight-bit bytes, by prepend the prefix “00”
        i = int(i,2)                                            # Decimal COnversion
        i = code[i]                                             # Base64 Chart Char COnversion
        encypt += str(i)
    #encypt += '=='
    print(encypt)
    
    
                                    # Decryption Function
def base64_decrypt(text1):
    con = ''
    #text1 = text1[:-2]
    dbinary = []
    for i in text1:
        index = code.index(i)
        binary = bin(index)
        binary = binary[2:]
        dbinary.append(binary)
    for i in dbinary:
        if len(i) != 6:
            pz = 6 - len(i)
            loc = dbinary.index(i)
            zero=''
            for n in range(0,pz):
                zero += '0'    
                z = zero + i   
            dbinary.insert(loc,z)
            dbinary.pop(loc+1)
    for i in dbinary:      
        con = con + i  
    n = 8
    chunks = [con[i:i+n] for i in range(0, len(con), n)]  
    decrypt = '' 
    for i in chunks:
        if len(i) != 8:
            loc = chunks.index(i)
            chunks.pop(loc)    
        else:
            i = int(i,2)
            i = chr(i)
            decrypt += str(i)
    print(decrypt)
    
                                     # Main
if __name__ == '__main__':
    text = input("Enter the string to encrypt:\t")
    base64_encrypt(text)
    text1 = input("Enter the string to decrypt:\t")
    base64_decrypt(text1)
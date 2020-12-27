import binascii

from tools.idafchev import repeating_key_xor,single_byte_xor

cipher_bytes  = binascii.unhexlify('134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9')
plaintext_seed='HTB{'
decrypt_key=[]

for i in range(len(plaintext_seed)):
    for key in range(256): # brute force
        byte_key=bytes([key])
        try:    
            text = single_byte_xor( bytes([cipher_bytes[i]]) , byte_key).decode('utf-8')
            if text == plaintext_seed[i]:
                decrypt_key.append(byte_key)
        except:
            continue

key_bytes=b''.join(decrypt_key)
bytes_out = repeating_key_xor(cipher_bytes,key_bytes)
text=bytes_out.decode('utf-8')
print(text)
import rsa

first_key = rsa.importKey(open('./challenge/key1.pem', "rb").read())
first_message = open('./challenge/message1').read()

second_key = rsa.importKey(open('./challenge/key1.pem', "rb").read())
second_message = open('./challenge/message2').read()


first_message_decrypted = rsa.decrypt(first_message, first_key)
print(first_message_decrypted)
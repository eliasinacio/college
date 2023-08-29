import rsa 

publicKey, privateKey = rsa.newkeys(512)

m = input('Digite a mensagem: ')

mc = rsa.encrypt(m.encode(), publicKey)

print('Mensagem original: ', m)
print('Mensagem criptografada: ', mc)

md = rsa.decrypt(mc, privateKey).decode()

print('Mensagem descriptografada: ', md)
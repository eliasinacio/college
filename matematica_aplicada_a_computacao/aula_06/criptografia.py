# cifra de cesar

from string import ascii_uppercase

a = list(ascii_uppercase)
m = input('Digite a mensagem: ')

m = m.upper()
mc = ""

for i in m:
    l = ord(i) - 65
    
    if i in a:
        mc += a[(l+3)%26]       # codifica
        # mc += a[(l-3)%26]     # decodifica
    else:
        i

print(f'Mensagem criptografada: {mc}')
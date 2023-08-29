# cifra de cesar
# a == e

from string import ascii_uppercase

a = list(ascii_uppercase)
m = "IRXIRHMQIRXS"

m = m.upper()
mc = ""

for i in m:
    l = ord(i) - 65
    
    if i in a:
        mc += a[(l-4)%26]
    else:
        i

print(f'Mensagem criptografada: {mc}')
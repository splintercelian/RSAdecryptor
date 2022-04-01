from sys import argv

help_message = """

RSAdecryptor is a tool to decrypt a message encrypted using RSA protocol
In order to successfully decrypt the cipher c you need to have p, q and e
*** Note that p and q can be obtained sometimes if n is small and you have it ***

usage : python3 rsadecryptor.py <p> <q> <e> <c>

"""

def decrypt(p,q,e,c):
    n = p*q
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    m = pow(c,d,n)
    return(bytearray.fromhex(hex(m)[2:]).decode('ascii'))

def main():

    if len(argv) < 5 or not argv[1] or not argv[2] or not argv[3] or not argv[4]:
        print(help_message)
    else:
        p = int(argv[1])
        q = int(argv[2])
        e = int(argv[3])
        c = int(argv[4])
        print(decrypt(p,q,e,c))

if __name__ == '__main__':
    main()

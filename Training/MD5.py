import hashlib
def MD5(sana):
    return hashlib.md5(sana.encode("utf-8")).hexdigest()
x = input("Anna")
print (MD5(x))

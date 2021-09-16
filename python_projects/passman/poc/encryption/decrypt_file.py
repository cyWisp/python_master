import os, random, struct, hashlib
from Crypto.Cipher import AES
from sys import argv

def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = f"{in_filename.replace('.enc', '')}"

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0: break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

def get_key(password):
    return hashlib.sha256(password.encode("utf-8")).digest()

if __name__ == '__main__':
    file, pw = argv[1], argv[2]
    key = get_key(pw)

    decrypt_file(key, file)
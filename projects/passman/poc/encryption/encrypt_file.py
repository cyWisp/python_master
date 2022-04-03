import os, random, struct, hashlib
from Crypto.Cipher import AES
from sys import argv

    #     Encrypts a file using AES (CBC mode) with the
    #     given key.

    #     key:
    #         The encryption key - a string that must be
    #         either 16, 24 or 32 bytes long. Longer keys
    #         are more secure.

    #     in_filename:
    #         Name of the input file

    #     out_filename:
    #         If None, '<in_filename>.enc' will be used.

    #     chunksize:
    #         Sets the size of the chunk which the function
    #         uses to read and encrypt the file. Larger chunk
    #         sizes can be faster for some files and machines.
    #         chunksize must be divisible by 16.

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):    
    # file name if not given
    if not out_filename: out_filename = in_filename + '.enc'

    # create initialization vector
    iv = ''.join(chr(random.randint(33, 0x7E)) for i in range(16)).encode()
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    print(f"file size: {filesize}")

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0: break
                elif len(chunk) % 16 != 0: chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

def create_key(password):
    return hashlib.sha256(password.encode("utf-8")).digest()

if __name__ == '__main__':
    target, password = argv[1], argv[2]
    key = create_key(password)
    encrypt_file(key, target)
    




    



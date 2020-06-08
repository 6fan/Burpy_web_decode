# coding:utf-8
import re
import base64
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex, hexlify
from Crypto.Util.Padding import pad


# decode str
g_iv = b'abcdefgabcdefg'
g_key = '12345678123456781234567812345678'.encode('utf-8')


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def encrypt(text):
    key = g_key
    mode = AES.MODE_CBC
    iv = g_iv
    cryptos = AES.new(key, mode, iv)
    b64_text = base64.b64encode(text)
    print b64_text
    pad_pkcs7 = pad(b64_text.encode('utf-8'), AES.block_size, style='pkcs7')
    cipher_text = cryptos.encrypt(pad_pkcs7)
    return hexlify(cipher_text)


def decrypt(text):
    key = g_key
    iv = g_iv
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    pad_pkcs7 = pad(text, AES.block_size, style='pkcs7')
    plain_text = cryptos.decrypt(a2b_hex(text))
    result = base64.b64decode(plain_text)
    return result.decode('utf-8')


class Burpy:

    '''
    header is list, append as your need
    body is string, modify as your need
    '''

    def __init__(self):
        self.key = ""
        self.iv = ""
        self.apicode = ""
        self.head = ""

    def main(self, header,     body):
        header.append("Main: AAA")
        print "head:", header
        print "body:", body
        return header, body

    def encrypt(self, header,     body):
        _new_body = encrypt(body)
        return header, _new_body

    def decrypt(self, header,     body):
         _new_body = decrypt(body)

        return header, _new_body

    def sign(self, header,     body):
        header.append("Sign: AAA")
        return header, body

    def processor(self, payload):
        return payload + "burpyed"

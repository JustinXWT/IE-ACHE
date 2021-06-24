import time
import hashlib
import random
import logging
import socket
import re, uuid
import base64
import os, random, struct
import subprocess
from collections import namedtuple
from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Hash import SHA256
from optparse import *
from _thread import *
import asn1tools
import threading
import cProfile, pstats, io
from random import randint
import json
from json import JSONEncoder
pr = cProfile.Profile()
pr.enable()

encrypt_start = time.perf_counter()
print("Printing secret key...\n")
secret_key = "secret.key"

print("Printing nbit key...\n")
nbit_key = "nbit.key"

output_secret_key = encrypting(SK, secret_key)
print("This file", output_secret_key, "is encrypted secret key\n")

output_nbit_key = encrypting(SK, nbit_key)
print("This file", output_nbit_key, "is encrypted nbit key\n")

s = open(output_secret_key, "rb")
keycontent = s.read(8192)

t = open(output_nbit_key, "rb")
nbitcontent = t.read(8192)

#Encode key in BER format
priv_key_BER = asn1_file.encode('DataKey', {'key': keycontent, 'nbit': nbitcontent})

# Send the BER encoded file to the peer
while (keycontent and nbitcontent):
    self.connection.sendall(priv_key_BER)
    keycontent = s.read(8192)
    nbitcontent = t.read(8192)
    priv_key_BER = asn1_file.encode('DataKey', {'key': keycontent, 'nbit': nbitcontent})
s.close()
t.close()

encrypt_stop = time.perf_counter()
#writing time taken to generate shared key between keygen and client
KeyExchangeTiming = open('time.txt', 'a')
encrypt_time_total = round((encrypt_stop - encrypt_start), 3)
KeyExchangeTiming.write('\nTotal Time Taken to Encryption/Decryption of keys for' + str(self.connection) + ': ')
KeyExchangeTiming.write(str(encrypt_time_total))
KeyExchangeTiming.write(str('\n============================='))
KeyExchangeTiming.close()

print('Original secret key file size: ', os.path.getsize(secret_key))
print ('Encrypted secret key file size: ', os.path.getsize(output_secret_key))
os.system("md5sum secret.key")

print('Original nbit key file size: ', os.path.getsize(nbit_key))
print ('Encrypted nbit key file size: ', os.path.getsize(output_nbit_key))
os.system("md5sum nbit.key")

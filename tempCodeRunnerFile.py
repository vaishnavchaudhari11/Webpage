L4 = L3
R4 = R3

f3 = L4^K2
L5 = R4^f3
R5 = L4

f4 = L5^K1
L6 = R5^f4
R6 = L5
PT1 = L6+R6


PT1 = int(PT1, 2)
RPT = binascii.unhexlify( '%x'% PT1)
print("Retrieved Plain Text is: ", RPT)
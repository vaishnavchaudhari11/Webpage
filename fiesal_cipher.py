from pydoc import plain

a=(input("Enter the plain text:: "))
print(a)



l1=a[0:(len(a)//2)]
r1=a[len(a)//2:]
l1=int(l1)
r1=int(r1)
print(l1)
print(r1)
# a=int(a)
print("Enter the key of length",int((len(a))/2))
k=int(input())
print("\n")
print("the key you have entered is",k)

def encryption(l1,r1,k):
    l2=r1
    r2=l1^r1^k
    cipher=str(l2)+str(r2)
    return l2,r2,cipher

L2,R2,Cipher=encryption(l1,r1,k)
print("For encrption part 1 of cipher text is:-",L2)
print("For encrption part 2 of cipher text is:-",R2)
print("The entire cipher text is:- ",Cipher)
print("\n")


def decryption(L2,R2,k):
    r1=L2
    l1=R2^r1^k
    plain=str(l1)+str(r1)
    return plain
plain_text=decryption(L2,R2,k)
print("After the decrption plain text is",plain_text)
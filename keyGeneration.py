from helper import *

parityBitDropTable=[57, 49, 41, 33, 25, 17, 9, 1,
58, 50, 42, 34, 26, 18, 10, 2,
59, 51, 43, 35, 27, 19, 11, 3,
60, 52, 44, 36, 63, 55, 47, 39,
31, 23, 15, 7, 62, 54, 46, 38,
30, 22, 14, 6, 61, 53, 45, 37,
29, 21, 13, 5, 28, 20, 12, 4]

shiftInEachRound=[ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

dCompressionTable=[14, 17, 11, 24, 1, 5, 3, 28,
15, 6, 21, 10, 23, 19, 12, 4,
26, 8, 16, 7, 27, 20, 13, 2,
41, 52, 31, 37, 47, 55, 30, 40,
51, 45, 33, 48, 44, 49, 39, 56,
34, 53, 46, 42, 50, 36, 29, 32]

def parityBitPermutation(bitArray):
    tempbitArray=[]
    for i in parityBitDropTable:
        tempbitArray.append(bitArray[i-1])
    return tempbitArray

def compressionDBox(left,right):
    key=list(left)
    key.extend(right)
    tempKey=[]
    for i in dCompressionTable:
        tempKey.append(key[i-1])
    return tempKey

def generateKey(key):
    KeybitArray=stringTo64BitArray(key)
    KeybitArray=parityBitPermutation(KeybitArray[0])

    left=KeybitArray[0:28]
    right=KeybitArray[28:]
    RoundKeys=[]
    for i in shiftInEachRound:
        left=left[i:]+left[0:i]
        right=right[i:]+right[0:i]
        RoundKeys.append(compressionDBox(left,right))

    return RoundKeys

def generateReverseKey(key):
    return generateKey(key).reverse()

if __name__=="__main__":
    print(generateKey("abcdefgh"))
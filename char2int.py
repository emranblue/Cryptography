def char2int(char):
    trans_number=[]
    for c in char.lower():
        trans_number.append(ord(c)-96)
    return trans_number

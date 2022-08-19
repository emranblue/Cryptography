def int2char(arr):
    result=""
    for i in arr:
        result+=chr(i+96)
    return result.upper()

def intero(s):
    roman_to_int = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    i = 0
    result = 0
    while i < len(s):
        #sotrazione:
        if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            result = result + roman_to_int[s[i+1]] - roman_to_int[s[i]]
            i += 2
        else:            
            result += roman_to_int[s[i]]
            i += 1

    return result 

if __name__== "__main__":
    if intero ("MCMXCIV") == 1994:
        print("ok")
    else:
        print("error")


# alternative:
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                number-=roman[s[i]]
            else:
                number+=roman[s[i]]
        return number+roman[s[-1]]








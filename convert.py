def convertToTupleNum:
    a="+9.99847600,+9.910000E+37,+9.910000E+37,+3.598180E+03,+1.946000E+04"
    a = a+ ','
    num ,power  = "",""
    active = 0
    integers = []
    for char in a:
        if char is ',':
            num=num.strip()
            power=power.strip()
            if len( power ) is 0:
                power=0
            integers.append( float(num)*(10**float(power)) )
            num = ""
            power = ""
            active = 0
        elif char is 'E':
            active = 1
        else :
            if active == 0:
                num = num + char
            else:
                power = power + char

if __name__ == "__main__": test()
    for i in integers:
        print(i)

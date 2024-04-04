
def timeConversion(s):
    # Write your code here
    meridian = s[-2:]
    if( meridian == "PM") and s[:2]!= '12':
        s= str( 12 + int(s[:2])) + s[2:]
    if (meridian == "AM") and s[:2] == '12':
        s = "00" + s[2:]
    return s[:-2]
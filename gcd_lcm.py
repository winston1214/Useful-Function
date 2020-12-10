# @Author YoungMinKim

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b= b,a%b
    return a
def lcm(a,b):
    return a*b // gcd(a,b)
if __name__ == "__main__":
    print(gcd(8,12))
    print(lcm(8,12))
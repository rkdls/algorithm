'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import math

def fifth_power(a):
    a = int(a)
    return int(math.pow(a,5))

if __name__ == '__main__':


    answer = 0
    count=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        for f in range(0,10):
                            result = fifth_power(a)+fifth_power(b)+fifth_power(c)+fifth_power(d)+fifth_power(e)+fifth_power(f)
                            count+=1
                            if int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)) == result:
                                # print(str(a)+str(b)+str(c)+str(d)+str(e))
                                print(result, a, b, c, d, e)
                                # print(result, fifth_power(a), fifth_power(b), fifth_power(c), fifth_power(d), fifth_power(e))
                                answer+=result

    print('정답',answer)
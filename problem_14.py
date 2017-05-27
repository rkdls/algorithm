'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def collatzProblem(i):
    count = 0
    while i != 1:
        data = i
        if data % 2 ==0 :
            data = data/2
        else:
            data = 3*data + 1
        i = data
        count +=1
    return count, i

if __name__ == "__main__":

    numb = 1000000
    max = 0
    val = 0
    for i in range(2,numb+1):
        # print('처음 i값', i)

        count, val_2 = collatzProblem(i)
        if max < count :
            max = count
            val = i
    print(max,val)
        # print('계산끝')
        #524 837799

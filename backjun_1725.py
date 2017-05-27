import time
# s = '''16 2 1 4 5 1 3 3 4 4 4 4 40 400 500 1000 2000'''
# s = '''7 2 1 4 5 1 3 3'''
# s = s.split(' ')
s=''
for i in range(0,8000):
    if i==0:
        s += '8000'+ ' '
        continue
    s += str(i)+' '
s = s[:-1].split(' ')
print(s)
if __name__ == '__main__':
    st = time.time()
    h = []
    n, j, m_n, maxdata, w = 0, 0, 0, 0, 0
    for i, val in enumerate(s):
        if i == 0:
            # 가로
            w = int(val)
            continue
        # 높이
        h.append(int(val))
    m = list(set(h))
    result = [0]
    if n+1 == w:
        result.append(h[n]*(1))
        exit()
    print('h :', h)
    print('m :', m)
    hLeng = len(h)
    mLeng = len(m)
    while True:
        if m[m_n] <= h[n]:
            n += 1
            j += 1
            if n+1 <= hLeng:
                continue
        if n+1 < w:
            # tempData = m[m_n] * i
            # if maxdata <= tempData:
            #     maxdata = tempData
            if j != 0:
                # result.append(m[m_n] * j)
                if maxdata <m[m_n] * j:
                    maxdata=m[m_n] * j
            n+=1
            j=0
            continue
        if j!=0:
            if maxdata <m[m_n] * j:
                maxdata =m[m_n] * j
            # result.append(m[m_n]*j)
        # if maxdata <= m[m_n]*(i):
        #     maxdata = m[m_n]*(i)
        j=0
        m_n +=1
        n =0
        if m_n == mLeng:
            break
    # print('result :', result)
    # print('max :', max(result))
    print('max ',maxdata)
    print('time :', (time.time()-st))

'''=========================================================='''
# s = '''7 2 1 4 5 1 3 3'''
# s = s.split(' ')
# if __name__ == '__main__':
#     s = int(input())
#     h = []
#     w = s
#     n, j, m_n, maxdata= 0, 0, 0, 0
#     for i in range(0,s):
#         data = input()
#         h.append(int(data))
#     m = list(set(h))
#     result = []
#     if n+1 == w:
#         result.append(h[n]*(1))
#     while True:
#         if m[m_n] <= h[n]:
#             n+=1
#             j+=1
#             if n+1 <= len(h):
#                 continue
#         if n+1 < w:
#             result.append(m[m_n] * j)
#             n+=1
#             j=0
#             continue
#         result.append(m[m_n]*j)
#         j=0
#         m_n +=1
#         n =0
#         if m_n == len(m):
#             break
#     print(max(result))
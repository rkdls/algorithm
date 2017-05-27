# def mul(a, b):
#     return int(a)*int(b)
#
# s = '''4 1 2 3 4'''
#
# s = s.split(' ')
# data = []
# count = 0
# for i, val in enumerate(s):
#     if i == 0:
#         count = val
#         continue
#     data.append(val)
# data = list(set(data))
# mul_result = []
# for j, val_i in enumerate(data):
#     for val_k in range(j+1,len(data)):
#         mul_result.append(mul(val_i,data[val_k]))
# print(sum(mul_result))

def mul(a, b):
    return int(a)*int(b)

if __name__ == '__main__':
    count = int(input())
    data = input()
    data = data.split(' ')
    mul_result = []
    for j, val_i in enumerate(data):
        for val_k in range(j+1,len(data)):
            mul_result.append(mul(val_i,data[val_k]))

    result = 0

    for a,b in enumerate(mul_result):
        result += b
    # print(sum(mul_result))
    print(result)
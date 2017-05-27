def is_pal(data, ydata):
    data=str(data).split(' ')
    a,b = data
    ydata = ydata.replace(' ','')
    i_data = str(ydata[(int(a)-1):(int(b))])
    i_data = i_data.strip()
    reversed_data = i_data[::-1]
    reversed_data = reversed_data.strip()
    if str(ydata[(int(a)-1):(int(b))]) == reversed_data:
        return 1
    return 0
if __name__ == "__main__":
    ylength = input()
    ydata = input()
    q_len = int(input())
    dd = []
    for a in range(q_len):
        a = input()
        dd.append(is_pal(a, ydata))
    for d in range(len(dd)):
        print(dd[d])
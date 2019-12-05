import sys

data = sys.stdin.read()

data = data.splitlines()

tc = int(data[0])

for i in range(0, tc):
    
    flag = i + (i+1)
    arr_size = int(data[flag])
    arr = [int(x) for x in data[flag+1].split()]
   
    res = arr_size * (arr_size+1) / 2
    s = sum(arr)

    print(int(res - s))


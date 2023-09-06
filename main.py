f1 = input()
f2 = input()
f3 = input()
f4 = input()
f = [list(map(int, f1.split(" "))),list(map(int, f2.split(" "))),list(map(int, f3.split(" "))),list(map(int, f4.split(" ")))]
print(f)
trash = 0
all = 0
def check(sq1, sq2):
    global trash
    if sq1[0] < sq2[1]:
        if sq2[3] < sq1[1]:
            trash+=abs(sq1[2] - sq2[0]) * abs(sq1[1] - sq2[3])
        else:




for obj in f:
    w = abs(obj[2] - obj[0])
    l = abs(obj[1] - obj[3])
    total = w * l
    all += total
print(all)
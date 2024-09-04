lines = {"AT":102, "AJ":377, "AB":193, "JO":106, "OE":240, "OI":254, "LB":179, "LK":216, "LN":180}
trucks = [str(a) for a in input().split()]
default = list("KNLBATJOEI")
map = []
for i in default:
    if i in trucks:
        map.append(i)
a = default.index(map[0])
b = default.index(map[-1])
line = default[a:b + 1]
if "T" not in trucks and "T" in line:
    line.remove("T")
if "K" not in trucks and "K" in line:
    line.remove("K")
if "N" not in trucks and "N" in line:
    line.remove("N")
if "I" not in trucks and "I" in line:
    line.remove("I")
if "E" not in trucks and "E" in line:
    line.remove("E")
ans = 0
for i in range(len(line) - 1):
    if line[i] + line[i + 1] in lines.keys():
        ans += lines[line[i] + line[i + 1]]
    elif line[i + 1] + line[i] in lines.keys():
        ans += lines[line[i + 1] + line[i]]
print(ans)
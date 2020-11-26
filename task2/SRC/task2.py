f = open('{}.txt'.format())
#считываем кооридинаты
line = f.readline()
center = []
radius = 0
points = []
k = ''
for i in line[line.find('center: ['):]:
    if '0' <= i <= '9' or i == '.':
        k += i
    elif i == ',':
        center.append(float(k))
        k = ''
    elif i == ']':
        center.append(float(k))
        k = ''
        break

for i in line[line.find('radius: '):]:
    if '0' <= i <= '9' or i == '.':
        k += i
    elif i == ',' or i == '}':
        radius = float(k)
        k = ''
        break

for i in line[line.find('line: '):]:
    if '0' <= i <= '9' or '.':
        k += i
    elif i == ',' or i == ']':
        points.append(float(k))
        k = ''
    elif i == '}':
        break
        
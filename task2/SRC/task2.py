import glob
#считываем кооридинаты
name = glob.glob('*.txt')
f = open(name[0], 'r')

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
    if '0' <= i <= '9' or i == '.':
        k += i
    elif k != '' and i == ',' or i == ']':
        points.append(float(k))
        k = ''
    elif i == '}':
        break

#поиск пересечений, решаем квадратное уравнениие
vector = [points[3] - points[0],
          points[4] - points[1],
          points[5] - points[2]]

b = (2 * vector[0] * (points[0] - center[0]) +
     2 * vector[1] * (points[1] - center[1]) +
     2 * vector[2] * (points[2] - center[2]))

c = ((points[0] - center[0]) ** 2 +
     (points[0] - center[0]) ** 2 +
     (points[0] - center[0]) ** 2 - radius ** 2)

a = vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2

discr = b**2 - 4 * a * c
t = 0
if discr < 0:
    print('Коллизий не найдено')
elif discr == 0:
    t = - b / 2 / a
    print(t*vector[0] + points[0],
          t*vector[1] + points[1],
          t*vector[2] + points[2])
else:
    t = (- b + discr**0.5) / 2 / a
    print(t * vector[0] + points[0],
          t * vector[1] + points[1],
          t * vector[2] + points[2])
    t = (-b + discr**0.5) / 2 / a
    print(t * vector[0] + points[0],
          t * vector[1] + points[1],
          t * vector[2] + points[2])

import re
import glob

line = map(str, input().split())
name = glob.glob('*.log')
fin = open(name[0], 'r')


vtot = int(fin[0])
vcur = int(fin[1])
vinit=0
vfinal=0
errin=0
errout=0
trytotin=0
trytotout=0
vtotin=0
vtotnotin=0
vtotout=0
vtotnotout=0
a = 0
b = 0
for i in fin:
    if i.split()[0] > line[1] and a != 1:
        vinit = vcur
        a = 1
    if i.split()[1] > line[2] and b != 1:
        vfinal = vcur
        b = 1
    if 'top up' in i:
        vtry = int[i.find('top up ')+6:i.rfind('l')]
        if vcur+vtry>vtot:
            errin += 1
            trytotin += 1
            vtotnotin += vtry
        else:
            trytotin += 1
            vcur += vtry
            vtotin += vtry
    elif 'scoop' in i:
        vtry = int[i.find('scoop ')+6:i.rfind('l')]
        if vcur-vtry<0:
            errout += 1
            trytotout += 1
            vtotnotout += vtry
        else:
            trytotout += 1
            vcur -= vtry
            vtotout += vtry
tryerrinper = errin / trytotin
tryerroutper = errout / trytotout
fout = open('.csv', 'w')
print(trytotin, tryerrinper, vtotin, vtotnotin, trytotout, tryerroutper, vtotout, vtotnotout, vinit, vfinal, file=fout)

#從翡翠歌詞下載歌詞轉乘excel對應

f = open('input.txt','r')
o = open('output.txt','w')
chinese = []
spell = []
n = 0
while True:
    line = f.readline()
    if len(line) == 0:
        break
    if n%2 == 0:
        for i in line:
            if i == ' ' or i == '\n':
                continue
            chinese.append(i)
    else:
        line = line.split()
        for i in line:
            if i == ' ' or i == '\n':
                continue
            spell.append(i)
    n = n + 1

for i in range(len(chinese)):
    text = chinese[i]+'\t'+spell[i]+'\n'
    o.write(text)
    
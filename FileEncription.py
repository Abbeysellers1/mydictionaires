import csv


codes = { 'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C':'!', 'c': '$', 'D': '^', 'd':'&', 'E': '*', 'e':'-', 'F':'|', 'f':'1', 'G': '2', 'g':'3', 'H':'4', 'h':'5', 'I':'6', 'i': '7', 'J':'8', 'j':'10', 'K':'=', 'k':'+', 'L':'-', 'l': '_', 'M':':', 'm':';', 'N': '/', 'n':',', 'O':'.', 'o':'q', 'P':'y', 'p': 't', 'Q':'[', 'q':']', 'R': 'z', 'r':'x', 'S':'c', 's':'v', 'T':'b', 't':'n', 'U':'m', 'u':'a', 'V':'s', 'v':'d', 'W':'f', 'w': 'g', 'X':'h', 'x': 'j', 'Y':'k', 'y':'l', 'Z':'p', 'z':'i'}

infofile= open('info_security.txt', 'r')
info_read=infofile.read()
infofile.close()

outfile=open('encrypted.txt','w')

for code in info_read:
    if code in codes:
        outfile.write(codes[code])
    else:
        outfile.write(code)
outfile.close()
outfile=open('info_security.txt','r')
info_read=outfile.read()
outfile.close()

codedwords=codes.items()

for code in info_read:
    if not code in codes.values() or codes=='.' or codes==',' or codes=='?' or codes=='!':
        print(code)
    else:
        for x,y in codedwords:
            if code==x and code!='.':
                print(x, end='')


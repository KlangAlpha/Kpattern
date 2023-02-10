import os,sys

filename = "zigzag_stock.py"

if len(sys.argv) > 1:
    filename = sys.argv[1]


from Klang import Kl,Klang
Klang.Klang_init()

from threading import Thread

def th_task(code):
    os.system('python3  ' + filename + " " + code + " 0 " + " " + "default" + " 100" )

def do_task(tasklist):
    for stock in tasklist:
        new_thread = Thread(target=th_task,args=(stock["code"],))
        new_thread.start()
    new_thread.join() #等待最后一个结束

count = 12 
for index in range(0,len(Kl.stocklist),count):
    do_task(Kl.stocklist[index:index+count])

# 生成结果列表
for _,_ ,filelist in os.walk('./images'):
    filelist.sort()
    f = open("./images/data.json","w+")
    f.write("data='[")
    pnglist = []
    for afile in filelist[:]:
        if ".png" in afile:
            pnglist.append(afile)
    for png in pnglist[:-1]:
        f.write('"'+png+'",')
    
    f.write('"'+pnglist[-1]+'"')
    f.write("]';")
    f.close()

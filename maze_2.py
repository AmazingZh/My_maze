import tkinter
import numpy as np
from tkinter import *
from tkinter import scrolledtext
import os

dirs=[(0,1),(1,0),(0,-1),(-1,0)] 

def drawboard(board,colors,startx=10,starty=10,cellwidth=30):
    width=2*startx+len(board[0])*cellwidth
    height=2*starty+len(board)*cellwidth
    # scr = scrolledtext.ScrolledText(root, width=width, height=height,font=("隶书",18))
    canvas.config(width=width,height=height)
    for i  in range(len(board[0])):
        for j in range(len(board)):
            index=board[j][i]
            cellx=startx+i*30
            celly=starty+j*30
            if(i==0 and j==0):
                color=colors[4]
            elif(i==m-1 and j==n-1):
                color=colors[5]
            else:
                color=colors[index]
            canvas.create_rectangle(cellx,celly,cellx+cellwidth,celly+cellwidth,
                    fill=color,outline="black")
    canvas.update()

def creatMaze(n,m):
   maze = np.random.randn(n,m)
   maze = 1/(1+np.exp(-maze))
   maze = np.add(maze,0.5)
   maze =  maze.astype(int)
   maze = maze.tolist()
   maze[0][0]=maze[n-1][m-1]=0
   return maze

def mark(maze,pos):  #给迷宫maze的位置pos标"3"表示"到过了"
	maze[pos[0]][pos[1]]=3

def passable(maze,pos): #检查迷宫是否可通行
	return maze[pos[0]][pos[1]]==0

def bfs(maze,n,m):
    global head,tail
    head=0
    tail=0
    start=(0,0,0)
    global path
    path=[]
    path.append(start)
    tail = tail+1
    while head<tail :
        pos=path[head]
        head = head + 1
        for i in range(4):
            nextp = (pos[0]+dirs[i][0],pos[1]+dirs[i][1],head-1)
            if(nextp[0]<0 or nextp[0]>=n or nextp[1]<0 or nextp[1]>=m):
                continue
            if(nextp[0]==n-1 and nextp[1]==m-1):
                path.append(nextp)
                tail=tail+1
                return True
            if(passable(maze,nextp) and maze[nextp[0]][nextp[1]]!=3):
                path.append(nextp)
                mark(maze,nextp)
                tail = tail+1
    return False

def readfile(filename): 
  with open(filename,'r') as f: 
    for line in f.readlines(): 
      linestr = line.strip() 
      print(linestr)
      linestrlist = linestr.split("\t") 
      print(linestrlist)
      linelist = map(int,linestrlist)# 方法一 
      # linelist = [int(i) for i in linestrlist] # 方法二 
      print(linelist)

if __name__ == '__main__':
    global n,mç
    while True:
        i=os.system("clear")
        print("***************************************************************************************************")
        print("\t\t\t\t\t1.Begin the Maze")
        print("\t\t\t\t\t2.quit")
        print("***************************************************************************************************")
        print("Please input your choice:")
        n=str(input())
        if(n=='1'):
            print("Please input the Rows and columns:")
            n,m = map(str,input().split())
            if(n.isdigit()==False or m.isdigit()==False or n=='0' or m=='0' or( n=='1' and m=='1')):
                print("\t\t\t\t\tInput Error!")
                tt=str(input())
            else:
                n=int(n)
                m=int(m)
                global root
                root=Tk()
                root.title("小张的迷宫")
                canvas=Canvas(root,bg="orange")
                canvas.pack()
                colors=['white','grey','blue','white','green','red','pink']

                # scrolly = Scrollbar(root)
                # scrolly.pack(side=RIGHT, fill=Y)
                # global mylb
                # mylb = Listbox(root, yscrollcommand=scrolly.set)
                # for item in range(1, 20):
                    # mylb.insert(END, item)
                # mylb.pack()
                # scrolly.config(command=mylb.yview)

                while True:
                    maze = creatMaze(n,m)
                    if(bfs(maze,n,m)): 
                        file=open('data.txt','w')
                        file.write(str(maze))
                        file.close()
                        break

                maze[n-1][m-1] = 2
                f=path[tail-1][2]
                while f:
                    maze[path[f][0]][path[f][1]] = 2
                    f=path[f][2]
                maze[path[f][0]][path[f][1]] = 2

                drawboard(maze,colors)
                root.mainloop()
        elif n=='2':
            exit(0)
        else:
            print("\t\t\t\t\tInput Error!")
            tt=str(input())
            
        
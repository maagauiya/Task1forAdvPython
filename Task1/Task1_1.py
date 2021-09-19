n=int(input())
list=[]
for i in range(n):
    list.append(input())
def func(st,end,list):
    if(st==end):
        print(list)
    for i in range(st,end):
        list[st],list[i]=list[i],list[st]
        func(st+1,end,list)
        list[st], list[i] = list[i], list[st]
func(0,len(list),list)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def setmin(smt,value):
    vertex=0
    minimum = 999
    for i in range(0,6):
	    if smt[i]==False and value[i]<minimum:
	        vertex=i
	        minimum=value[i]
	        #print("minimum:,vertex:",minimum,vertex)
    return vertex
	
def prims(graph):
    value=[999,999,999,999,999,999]
    parent=[-1]*6
    smt=[False]*6
    value[0]=0
    parent[0]=-1
    for i in range(0,6):
        u=setmin(smt,value)
        smt[u]=True
        #print("---------start-----------")
        for j in range(0,6):
            if graph[u][j]!=0 and smt[j]==False and graph[u][j]<value[j]:
                value[j]=graph[u][j]
                #print("smt:",smt)
                #print("value:",value)
                parent[j]=u
                #print("parent:",parent)
        #print("--------end------------")  
    print(parent)
graph=[[0, 4, 6, 0, 0, 0],
[4, 0, 6, 3, 4, 0],
[6, 6, 0, 1, 8, 0],
[0, 3, 1, 0, 2, 3],
[0, 4, 8, 2, 0, 7],
[0, 0, 0, 3, 7, 0]]
prims(graph)

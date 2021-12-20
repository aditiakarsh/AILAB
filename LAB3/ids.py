from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.noofvertex=vertices
        self.graph=defaultdict(list)
    def addEdge(self,start,end):
        self.graph[start].append(end)
    def search(self,src,target,maxdepth):
        if src==target:
            return True
        if maxdepth<=0:
            return False
        for i in self.graph[src]:
            if self.search(i,target,maxdepth-1):
                return True
        return False
    def iterativesearch(self,src,target,maxdepth):
        for i in range(maxdepth):
            if self.search(src,target,i):
                return True
        return False


def main():
    print("Enter the number of vertices: ",end="")
    n=int(input())
    g=Graph(n)
    print("Enter number of edges: ",end="")
    noofedges=int(input())
    print("Enter edges-")
    for i in range(noofedges):
        edge=list(map(int,input().split(",")))
        g.addEdge(edge[0],edge[1])
    while(True):
        print("Enter src vertex: ",end="")
        src=int(input())
        print("Enter target vertex: ",end="")
        target=int(input())
        print("Enter the max depth: ",end="")
        maxdepth=int(input())
        if g.iterativesearch(src,target,maxdepth):
            print("Can Reach")
        else:
            print("Can not reach")
        print("Do you want too continue y/n: ",end="")
        c=input()
        if c=='n':
            return


main()

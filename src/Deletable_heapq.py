## heapq with delete function

class deletable_heapq():
    def __init__(self,ls=None):
        self.contents=defaultdict(int)
        if ls:
            self.arr=[]
            for i in ls:
                self.arr.append(i)
                self.contents[i]+=1
            heapify(self.arr)
        else:
            self.arr=[]

    def top(self):
        while self.arr:
            _top=self.arr[0]
            if _top not in self.contents or self.contents[_top]==0:
                heappop(self.arr)
            else:
                return _top
        return None
        
    def pop(self):
        while self.arr:
            _top=self.arr[0]
            if _top not in self.contents:
                heappop(self.arr)
            else:
                rt=heappop(self.arr)
                self.contents[rt]-=1
                return rt
        return None

    def append(self,x):
        heappush(self.arr,x)
        self.contents[x]+=1
        return

    def delete(self,x):
        if self.contents[x]>0:
            self.contents[x]-=1
        return

class Custmer():
    def _init_(self,name,numer_tiket):
        self.name=name
        self.numer_tiket=numer_tiket
    def _str_(self):
        return f"Name{self.name},Tiket{self.numer_tiket}"
class Queue():
    def _init_(self):
        self.queue=[]
        self.next_numer_tiket =1  
    def enqueue(self, name):
        custmer=Custmer(name,self.next_numer_tiket)
        self.queue.append(custmer)
        self.next_numer_tiket+=1
        print(f"{name},{custmer.numer_tiket}")
    # def dqueue(self):
    #     return self.queue.pop(0)
myqueue=Queue()
myqueue.enqueue("mohamed")
myqueue.enqueue("ahamed")
print(myqueue.queue)
#print(myqueue.dqueue())

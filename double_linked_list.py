class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next
        
class DLL:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self,data):
        node = Node(None ,data, self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(None,data,None)
            return
       
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(itr, data, None)
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of range")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                if itr.next:
                    itr.prev.next = itr.next
                    itr.next.prev = itr.prev
                else:
                    itr.prev.next = None
                    if itr.prev:
                        itr.prev.prev = None
                
                break

            itr = itr.next
            count += 1



    def printdll(self):
        itr = self.head
        DLLstr = ""
        while itr:
            DLLstr += "<--"+str(itr.data)+"-->"
            itr = itr.next
        print(DLLstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count


if __name__ == "__main__":
    d1 = DLL()
    d1.insert_at_beggining(3)
    d1.insert_at_beggining(2)
    d1.insert_at_beggining(1)
    d1.insert_at_end(4)
    d1.insert_at_beggining("A")
    d1.remove_at(1)
    d1.get_length()
    d1.printdll()

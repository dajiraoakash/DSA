class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        #Removing at beggining
        if index == 0:
            self.head = self.head.next
            
        #Removing at an index
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beggining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            print("If case")
            self.head.next = Node(data_to_insert,self.head.next)
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def remove_by_value(self,data_to_remove):
        if self.head is None:
            return
        if self.head.data == data_to_remove:
            self.head.next = None
        
        itr = self.head
        while itr.next:
            if itr.next.data == data_to_remove:
                itr.next = itr.next.next
                break
            itr = itr.next

    def data_type(self, data_to_inspect):
        itr = self.head
        while itr:
            if itr.data == data_to_inspect:
                dt = type(itr.data)
                break
            itr = itr.next
        return dt

    #Inserting a list
    def insert_list(self,list_data):
        for data in list_data:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
        itr = self.head
        LLstr = ""
        while itr:
            LLstr += str(itr.data) + "-->"
            itr = itr.next
        print(LLstr)



if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_at_beggining(10)
    l1.insert_at_beggining(9)
    l1.insert_at_end(5859)
    l1.get_length()
    l1.insert_list(["A","K","A","S","H"])
    l1.remove_at(3)
    l1.insert_at(3, "A")
    l1.insert_after_value(5859,"S")
    l1.remove_by_value(5859)
    l1.printLL()


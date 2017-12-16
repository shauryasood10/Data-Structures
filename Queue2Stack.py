
# coding: utf-8

# In[6]:

class Queue2Stack(object):
    
    def __init__(self):
        
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,item):
        self.stack1.append(item)
        
        
    def dequeue(self):
        for i in range(len(self.stack1)):
            s = self.stack1.pop()
            self.stack2.append(s)
        return self.stack2.pop()    
        
        


# In[7]:

q = Queue2Stack()


# In[8]:

for i in xrange(5):
    q.enqueue(i)


# In[9]:

for i in xrange(5):
    print q.dequeue()


# In[ ]:




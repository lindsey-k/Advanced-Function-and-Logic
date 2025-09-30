#!/usr/bin/env python
# coding: utf-8

# In[5]:


def while_inner_plus(a):
    cur = a
    while any(isinstance(x, list) for x in cur):  
        for x in cur:
            if isinstance(x, list):
                cur = x               
                break
    return [n + 1 for n in cur]                

if __name__ == "__main__":
    print(while_inner_plus([1,2,3,[4,5,[8,9]]]))   


# In[ ]:





# In[ ]:





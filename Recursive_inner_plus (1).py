#!/usr/bin/env python
# coding: utf-8

# In[2]:


def recursive_inner_plus(a):
    if all(not isinstance(x, list) for x in a):    
        return [n + 1 for n in a]
    for x in a:                                    
        if isinstance(x, list):
            return recursive_inner_plus(x)

if __name__ == "__main__":
    print(recursive_inner_plus([1,2,3,[4,5,[8,9]]]))  


# In[ ]:





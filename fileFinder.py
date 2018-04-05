
# coding: utf-8

# In[5]:


from os import listdir
from os.path import isdir


# In[2]:


def getFiles(path):
    #print path
    files = []
    f = listdir(path)
    #print f
    for i in f:
        ffile = path+'/'+i
        #print i
        #print(path+'/'+i)
        if isdir(path+'/'+i):
            files += (getFiles(ffile))
            #a = getFiles(path+'/'+i)
            #for j in a:
            #    files.append(j)
        else:
            files.append(ffile)
        #print files
    return files


# In[3]:


def filterType(files, ending):
    l = len(ending)
    filtered = []
    for i in files:
        candEnding = i[-l:]
        if candEnding == ending:
            filtered.append(i)
    return filtered


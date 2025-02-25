#!/usr/bin/env python
# coding: utf-8

# In[2]:


#read keyword (by default it will read)
ipfile=open("input")
txt=ipfile.read()
print(txt)
ipfile.close()


# In[7]:


#readlines -will read the file line by line 
ipfile=open("input")
lines=ipfile.readlines()
print(lines)
ipfile.close()


# In[7]:


ipfile=open("input")
lines=ipfile.readlines()
for i in lines:
    print("The next line is:"+i)
ipfile.close()


# In[10]:


#write
opfile=open("Output.txt",'w')
msg ="This is a nice day"
opfile.write(msg)
opfile.close()


# In[4]:


#append
opfile=open("Output.txt",'a')
msg ="Tmrw is thursday"
opfile.write(msg)
msg1="day after tmrw is friday"
opfile.write(msg1)
opfile.close()


# In[9]:


#copy conents from one file(input) to another file(output)
ipfile=open("input")
#txt1=ipfile.read()
lines1=ipfile.readlines()
opfile=open("Outputfile.txt",'w')
#opfile.write(txt1)
for l in lines1:
    opfile.write(l)
ipfile.close()
opfile.close()


# In[20]:


#program to print only the odd number of lines
ipfile=open("input")
txt2=ipfile.readlines()
j=txt2[0::2]
for i in j :
    print(i)
ipfile.close()


# In[ ]:





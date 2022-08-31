#!/usr/bin/env python
# coding: utf-8

# # exercice de récursivité

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# Ex 1 : calculer la somme : 1 + 2 + 3 + ... + n ?

# In[2]:


# construire une fonction somme_1(n) exploitant une boucle for

def somme_1(n):
    r = 0
    for i in range(n+1):
        r = r + i                 #   r += i
    return r


# In[5]:


somme_1(10)


# In[6]:


# construire une fonction somme_2(n) exploitant le résultat de somme(n-1)

def somme_2(n):
    if n == 0:                      # condition d'arrêt
        return 0
    else:
        return n + somme_2(n-1)     # récurrence


# In[7]:


somme_2(10)


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# Ex 2 : calculer x**n ?

# In[22]:


# puissance_1(x, n) avec for

def puissance_1(x, n):
    r = 1
    for i in range(n):
        r = r * x                 #   r *= x
    return r


# In[23]:


puissance_1(2,5)


# In[28]:


# puissance_2(x, n) par récursivité
def puissance_2(x, n):
    if n == 0:                             # condition d'arrêt
        return 1
    else:
        return x * puissance_2(x, n-1)     # récurrence


# In[29]:


puissance_2(2,5)


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# Ex 3 : suite de fibonacci - U_0 = 1 , U_1 = 1 et U_n = U(n-1) + U_(n-2)

# In[31]:


# cas du n-ième terme de la suite de fibonacci(n) par récursivité
def fibonacci(n):
    if n == 0:                                     # conditions d'arrêts
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)     # récurrence


# In[32]:


fibonacci(0)


# In[33]:


fibonacci(1)


# In[34]:


fibonacci(10)


# In[ ]:





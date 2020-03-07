#!/usr/bin/env python
# coding: utf-8

# In[1132]:


import pandas as pd
import numpy as np
import itertools
import math
data = pd.read_csv("associationruletestdata.csv",header=None)
dataRows,dataCols=data.shape


# In[1321]:


data2=[]
for i in range(0,dataRows):
    tempSet=set()
    for j in range(0,dataCols):
        tempSet.add("G"+str(j+1)+"_"+str(data.iloc[i][j]))
    data2.append(tempSet)


# In[ ]:





# In[1322]:


def initialThresholding(dataSet,threshVal):
    temp1=dataSet[0]
    result=[]
    for i in range(0,len(dataSet)):
            temp1=temp1.union(dataSet[i]) 
            
    for ele in temp1:
        count=0
        for j in range(len(dataSet)):
            if ele in dataSet[j]:
                count+=1
            if count>=threshVal:
                temp=set([ele])
                result.append(temp)
                break
        
    return result
                
        
                
            
    


# In[1323]:


def thresholdSet(dataSet,threshVal):
    result=[]
    for i in range(len(dataSet)):
        tempSet=dataSet[i]
        count=0
        for j in range(len(data2)):
            if dataSet[i].issubset(data2[j]):
                count+=1
                
        if count>=threshVal:
            result.append(tempSet)
            
    return result


# In[1324]:


def countForRule(dataSet):
    result=[]
    count=0
    for i in range(len(data2)):
        if dataSet.issubset(data2[i]):
            count+=1
    return count


# In[1325]:


def combinationForTwo(dataSet):
    result=[]
    for i in range(len(dataSet)-1):
        for j in range(i+1,len(dataSet)):
            result.append(dataSet[i].union(dataSet[j]))

    return result


# In[1326]:


def removeDuplicate(dataSet):
    result1=[]
    result = set()
    for item in dataSet:
        if item.issubset(result) is False:
            result.union(item)
            result1.append(item)
    return result1

# In[1327]:


def combinationGeneration(dataSet,count):
    result=[]
    for i in range(len(dataSet)):
        temp=set()
        for j in range(i+1,len(dataSet)):
            if len(dataSet[i].intersection(dataSet[j]))==count-2 :
                temp=dataSet[i].union(dataSet[j])
                result.append(temp)
    return result
    


# In[1604]:


support30=[]
supp=30
res=initialThresholding(data2,supp)
support30.extend(res)
res1=combinationForTwo(res)
res2=thresholdSet(res1,supp)
support30.extend(res2)
i=3
print("numberoflength-1frequentitemsets for 30% : "+str(len(res)))
print("numberoflength-2frequentitemsets for 30% :  "+str(len(res2)))
while len(res2)!=0:
    res3=combinationGeneration(res2,i)
    res3=removeDuplicate(res3)
    res4=thresholdSet(res3,supp)
    print("numberoflength-"+str(i)+"frequentitemsets for 30% :  "+str(len(res4)))
    i+=1
    support30.extend(res4)
    res2=res4


# In[1329]:


support40=[]
supp=40
res=initialThresholding(data2,supp)
support40.extend(res)
res1=combinationForTwo(res)
res2=thresholdSet(res1,supp)
support40.extend(res2)
i=3
print("numberoflength-1frequentitemsets for 40% : "+str(len(res)))
print("numberoflength-2frequentitemsets for 40% :  "+str(len(res2)))
while len(res2)!=0:
    res3=combinationGeneration(res2,i)
    res3=removeDuplicate(res3)
    res4=thresholdSet(res3,supp)
    print("numberoflength-"+str(i)+"frequentitemsets for 40% :  "+str(len(res4)))
    i+=1
    support40.extend(res4)
    res2=res4


# In[1330]:


support50=[]
supp=50
res=initialThresholding(data2,supp)
support50.extend(res)
res1=combinationForTwo(res)
res2=thresholdSet(res1,supp)
support50.extend(res2)
i=3
print("numberoflength-1frequentitemsets for 50% : "+str(len(res)))
print("numberoflength-2frequentitemsets for 50% :  "+str(len(res2)))
while len(res2)!=0:
    res3=combinationGeneration(res2,i)
    res3=removeDuplicate(res3)
    res4=thresholdSet(res3,supp)
    print("numberoflength-"+str(i)+"frequentitemsets for 50% :  "+str(len(res4)))
    i+=1
    support50.extend(res4)
    res2=res4


# In[1331]:


support60=[]
supp=60
res=initialThresholding(data2,supp)
support60.extend(res)
res1=combinationForTwo(res)
res2=thresholdSet(res1,supp)
support60.extend(res2)
i=3
print("numberoflength-1frequentitemsets for 60% : "+str(len(res)))
print("numberoflength-2frequentitemsets for 60% :  "+str(len(res2)))
while len(res2)!=0:
    res3=combinationGeneration(res2,i)
    res3=removeDuplicate(res3)
    res4=thresholdSet(res3,supp)
    print("numberoflength-"+str(i)+"frequentitemsets for 60% :  "+str(len(res4)))
    i+=1
    support60.extend(res4)
    res2=res4


# In[1332]:


support70=[]
supp=70
res=initialThresholding(data2,supp)
support70.extend(res)
res1=combinationForTwo(res)
res2=thresholdSet(res1,supp)
support70.extend(res2)
i=3
print("numberoflength-1frequentitemsets for 70%   "+str(len(res)))
print("numberoflength-2frequentitemsets for 70%   "+str(len(res2)))
while len(res2)!=0:
    res3=combinationGeneration(res2,i)
    res3=removeDuplicate(res3)
    i+=1
    res4=thresholdSet(res3,supp)
    print("numberoflength-"+str(i)+"frequentitemsets for 70%   "+str(len(res4)))
    support70.extend(res4)
    res2=res4


# In[1333]:


for i in range(len(support50)):
    support50[i]=set(sorted(support50[i]))


# In[1345]:


support50


# In[1506]:


def generateRule(level,latticelength):
    if latticelength == 0:
        return []
    
    level2 = []
    for i in range(len(level)):
        for j in range(i+1,len(level)):
            head = set()
            body = set()
            if len(level[i][0].intersection(level[j][0]))==latticelength:
                head = level[i][0].intersection(level[j][0])
                body = level[i][1].union(level[j][1])
                level2.append([head,body])
           
    return level2


        


# In[1507]:


def helper(support):
    output = []

    for item in temp:
        if len(item)>1:
            level1 = []
            for val in item:
                head = set()
                body = set()
                body.add(val)
                head = item - set([val])
                level1.append([head,body])
                #result.append([head,body])

            current_level = level1
            level_length = len(item) - 2
            while len(current_level) > 0:
                tan=[]
                ## for each rule in current level find high confidence rule and use that to generate next level rule, Confidence
                for i in range(len(current_level)):
                    te=[]
                    lhs=current_level[i][0]
                    rhs=current_level[i][1]
                    num=countForRule(lhs.union(rhs))
                    den=countForRule(lhs)
                    confidence=num/float(den)
                    te.append(lhs)
                    te.append(rhs)
                    if confidence>0.7:
                        tan.append(te)
                        output.extend(tan)
                next_level = generateRule(tan, level_length)
                level_length -= 1
                current_level = next_level
    return output


# In[1602]:


output1=helper(support50)
output1=removeDuplicate(output1)
output=output1


# In[1603]:


len(output1)



# Template 1.1

# In[1600]:


output


# In[ ]:





# In[1537]:



def tempset1(tempSet):
    result111=[]
    for i in range(len(output1)):
        head=output1[i][0]
        body=output1[i][1]
        if tempSet in head or tempSet in body:
            result111.append([head,body])
    print(result111)
    print("-------------------------------------------------------")
    print("count of template 11 : "+str(len(result111)))

    print(len(result111))
    return result111
    


# Template 1.2

# In[1573]:


def template12(tempSet):
    result12=[]
    for i in range(len(output1)):
        head=output1[i][0]
        body=output1[i][1]
        if tempSet in head or tempSet in body:
            continue
        else:
            result12.append([head,body])
    print(result12)

    print("-------------------------------------------------------")
    print("count of template 12 : "+str(len(result12)))

    print(len(result12))
    return result12


# Template 1.3

# In[1586]:


def template13(tempSet1,tempSet2):
    result13=[]
    for i in range(len(output1)):
        head=output1[i][0]
        body=output1[i][1]
        temp=output1[i][0].union(output1[i][1])
        if tempSet1 in temp and tempSet2 not in temp:
            result13.append([head,body])
        if tempSet2 in temp and tempSet1 not in temp:
            result13.append([head,body])
    print(result13)
    print("-------------------------------------------------------")
    print("count of template 13 : "+str(len(result13)))
    print(len(result13))
    return result13


# Template 1.4

# In[1575]:


def template14(tempSet):
    result14=[]
    for i in range(len(output1)):
        head=output1[i][0]
        body=output1[i][1]
        if tempSet in head:
            result14.append([head,body])
    print(result14)

    print("-------------------------------------------------------")
    print("count of template 14 : "+str(len(result14)))

    print(len(result14))
    return result14


# Template 1.5

# In[1590]:


def template15(tempSet):
    result15=[]
    for i in range(len(output1)):
        head=output1[i][0]
        if tempSet not in head:
            result15.append([head,body])
    print(result15)

    print("-------------------------------------------------------")
    print("count of template 15 : "+str(len(result15)))
    print(len(result15))
    return result15


# Template 1.6

# In[1542]:


def template16(tempSet1,tempSet2):
    result16=[]
    for i in range(len(output)):
        head=output[i][0]
        body=output[i][1]
        if tempSet1 in head and tempSet2 not in head or tempSet2 in head and tempSet1 not in head :
            result16.append([head,body])
        else:
            continue
    print(result16)

    print("-------------------------------------------------------")
    print("count of template 16 : "+str(len(result16)))

    print(len(result16))
    return result16


# Template 1.7

# In[1543]:


def template17(tempSet):
    result17=[]
    for i in range(len(output)):
        head=output[i][0]
        body=output[i][1]
        if tempSet in body:
            result17.append([head,body])
    print(result17)

    print("-------------------------------------------------------")
    print("count of template 17 : "+str(len(result17)))
    print(len(result17))
    return result17


# Template 1.8

# In[1544]:


def template18(tempSet):
    result18=[]
    for i in range(len(output)):
        head=output[i][0]
        body=output[i][1]
        if tempSet not in body:
            result18.append([head,body])
    print(result18)

    print("-------------------------------------------------------")
    print("count of template 18 : "+str(len(result18)))
    print(len(result18))
    return result18


# Template 1.9

# In[1545]:


def template19(tempSet1,tempSet2):
    result19=[]
    for i in range(len(output)):
        head=output[i][0]
        body=output[i][1]
        if tempSet1 in body and tempSet2 not in body or tempSet2 in body and tempSet1 not in body :
            result19.append([head,body])
    print(result19)

    print("-------------------------------------------------------")
    print("count of template 19 : "+str(len(result19)))
    print(len(result19))
    return result19


# Template 2.1

# In[1613]:


def template21(size):
    result21=[]
    for i in range(len(output)):
        head=output[i][0]
        body=output[i][1]
        temp=head.union(body)
        if len(temp)>=size:
            result21.append([head,body])
    print result21
    print("----------------------------------------------------")
    print("count of template 21 : "+str(len(result21)))
    print len(result21)
    return result21


# Template 2.2

# In[1614]:


def template22(size):
    result22=[]
    for i in range(len(output)):
        head=output[i][0]
        body=output[i][1]
        if len(head)>=size:
            result22.append([head,body])
    print result22
    print("----------------------------------------------------")
    print("count of template 22 : "+str(len(result22)))
    print len(result22)
    return result22


# Template 2.3

# In[1605]:


def template23(size):
    result23=[]
    for i in range(len(output1)):
        head=output1[i][0]
        body=output1[i][1]
        if len(body)>=size:
            result23.append([head,body])
    print result23
    print("----------------------------------------------------")
    print("count of template 23 : "+str(len(result23)))
    print len(result23)
    return result23


# Template 3.1

# In[1549]:


def template31(tempSet1,tempSet2):
    result31=[]
    result1=template14(tempSet1)
    result2=template17(tempSet2)
    result1.extend(result1+result2)
    result31=removeDuplicate(result1)
    print(result31)
    print("----------------------------------------------------")
    print("count of template 31 : "+str(len(result31)))
    print len(result31)
    return result31


# Template 3.2

# In[1550]:


def template32(tempSet1,tempSet2):
    result32=[]
    result1=template14(tempSet1)
    result2=template17(tempSet2)
    for i in range(len(result1)):
        temp=result1[i][0].union(result1[i][1])
        for j in range(len(result2)):
            temp1=result2[j][0].union(result2[j][1])
            if len(temp1)==len(temp) and len(temp.intersection(temp1))==len(temp):
                temp=temp.intersection(temp1)
                result32.append([result1[i][0],result1[i][1]])
            else:
                continue
    result32=removeDuplicate(result32)    
    print(result32)
    print("----------------------------------------------------")
    print("count of template 32 : "+str(len(result32)))
    print len(result32)
    return result32


# Template 3.3

# In[1551]:


def template33(tempSet1,size):
    result31=[]
    result1=template14(tempSet1)
    result2=template23(size)
    result1.extend(result1+result2)
    result31=removeDuplicate(result1)
    print(result31)
    print("----------------------------------------------------")
    print("count of template 33 : "+str(len(result31)))
    print len(result31)
    return result31


# Template 3.4

# In[1552]:


def template34(tempSet1,size):
    result31=[]
    result1=template14(tempSet1)
    result2=template23(size)
    for i in range(len(result1)):
        temp=result1[i][0].union(result1[i][1])
        for j in range(len(result2)):
            temp1=result2[j][0].union(result2[j][1])
            if len(temp1)==len(temp) and len(temp.intersection(temp1))==len(temp):
                temp=temp.intersection(temp1)
                result31.append([result1[i][0],result1[i][1]])
            else:
                continue
    result31=removeDuplicate(result31)
    print("----------------------------------------------------")
    print("count of template 34 : "+str(len(result31)))
    print len(result31)
    return result31


# Template 3.5

# In[1619]:


def template35(size1,size2):
    result31=[]
    result1=template22(size1)
    result2=template23(size2)
    result1.extend(result1+result2)
    result31=removeDuplicate(result1)
    print(result31)
    print("----------------------------------------------------")
    print("count of template 35 : "+str(len(result31)))
    print len(result31)
    return result31


# In[1554]:


def template36(size1,size2):
    result31=[]
    result1=template22(size1)
    result2=template23(size2)
    for i in range(len(result1)):
        temp=result1[i][0].union(result1[i][1])
        for j in range(len(result2)):
            temp1=result2[j][0].union(result2[j][1])
            if len(temp1)==len(temp) and len(temp.intersection(temp1))==len(temp):
                temp=temp.intersection(temp1)
                result31.append([result1[i][0],result1[i][1]])
            else:
                continue
    result31=removeDuplicate(result31)
    print(result31)
    print("----------------------------------------------------")
    print("count of template 36 : "+str(len(result31)))
    return result31


# In[1555]:


template11('G59_Up')


# In[1556]:


template12('G59_Up')


# In[1587]:


template13("G59_Up","G10_Down")


# In[1588]:


res=template14("G59_Up")
res


# In[1591]:


template15("G59_Up")


# In[1592]:


template16("G10_Down","G59_Up")


# In[1593]:


template17("G59_Up")


# In[1594]:


template18("G59_Up")


# In[1595]:


template19("G59_Up","G10_Down")


# In[1615]:


template21(3)


# In[1616]:


template22(2)


# In[1617]:


template23(1)


# In[1567]:


template31("G10_Down","G59_Up")


# In[1568]:


template32("G10_Down","G59_Up")


# In[1569]:


template33("G10_Down",2)


# In[1570]:


template34("G10_Down",2)


# In[1620]:


template35(1,2)


# In[1572]:


template36(1,2)


# In[ ]:





# In[1612]:


output


# In[ ]:





# In[ ]:





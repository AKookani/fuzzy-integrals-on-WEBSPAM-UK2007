from itertools import combinations
import numpy as np
import pandas as pd
import random

#please import the dataset by replacing the "WEB" file address belsow
mydata = pd.read_csv("C:\\Users\\Ali\\Desktop\\WEB.txt", sep ="\t")

def sugeno(value, measure):
    c=(np.zeros(len(value))).astype(int)
    y=(np.zeros(len(value))).astype(int)
    for i in range(len(value)):
        c[i]=len(np.array(list(combinations(z[0:len(value)], i+1))))
        y[i] = min(value[len(value)-i-1],measure[np.sum(c)-1])
    return max(y)/100

def choquet(value, measure):
    c=(np.zeros(len(value))).astype(int)
    y=(np.zeros(len(value))).astype(int)
    for i in range(len(value)):
        if i==(len(value)-1):
            y[i] = (value[len(value)-i-1])*(measure[np.sum(c)-1])
        else:
            c[i]=len(np.array(list(combinations(z[0:len(value)], i+1))))
            y[i] = ((value[len(value)-i-1])-(value[len(value)-i-2]))*(measure[np.sum(c)-1])
    return (np.sum(y))/10000

mydata=pd.DataFrame.to_numpy(mydata)
y1=np.zeros(4274);
y2=np.zeros(4274);
for j in range(4274):
    k=0;
    x=np.sort(mydata[j,1:11]);
    x = x[~np.isnan(x)];
    x = (100*x).astype(int)
    z=(np.zeros((2**len(x))-1)).astype(int);
    for i in range(len(x)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(1, 99);
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 2)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 3)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 4)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 5)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 6)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 7)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 8)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 9)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 10)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
        else:
            z[k]=random.randint(max(comb[i]), 99)
            k += 1;
    comb = np.array(list(combinations(z[0:len(x)], 11)));
    for i in range(len(comb)):
        if (len(z)-k)==1:
            z[k]=100;
            y1[j]=sugeno(x, z)
            y2[j]=choquet(x, z)
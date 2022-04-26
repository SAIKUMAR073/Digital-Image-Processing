###################----------Shannon Fano Coding-----###################
import math

p = input("Enter the comma separated list of probabilities").split(",")
for i in range(0,len(p)):
    p[i] = float(p[i])
p.sort(reverse=True)
#print(p)
Code=[""]*len(p)
def next_stage(p,si=0,ei=len(p)):
    if(ei-si<=1):
        return
    elif(ei-si==2):
        Code[si]+='0'
        Code[si+1]+='1'
        return
    sum = 0
    diff = []
    for i in range(si,ei):
        sum+=p[i]
        sum2 = 0        
        for j in range(i+1,ei,1):
            sum2 = sum2 + p[j]
        sum2 = round(sum2,2)
        diff.append(round((sum - sum2),2))
    diff=[abs(x) for x in diff]
    index_2121 = diff.index(min(diff)) + si
    for i in range(si,ei):
        if(i <= index_2121):
            Code[i] += "0"
        elif(i > index_2121):
            Code[i] += "1"
    next_stage(p,si,index_2121+1)
    next_stage(p,index_2121+1,ei)

next_stage(p,0,len(p))
#print(Code)

H = 0
L = 0
for i in range(0,len(p)):
    H = H + (p[i]*math.log((1/p[i]),2))
    L = L + (p[i]*len(Code[i]))
print("probablities",end="      ")
print("Code")
for i in range(0,len(p)):
    print(p[i],end="                ")
    print(Code[i])
print("Entropy is {}".format(round(H,2)))
print("Average CodeWord Length is {}".format(round(L,2)))
print("Efficiency is {}".format(round(((H/L)*100),2)))
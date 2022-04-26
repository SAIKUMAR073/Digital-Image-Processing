###################----------Huffman Coding-----###################

import math

l = input("Enter the comma separated list of probabilities").split(",")
for i in range(0,len(l)):
    l[i] = float(l[i])

res=[""]*len(l)
probabbility_array=[]

for i in range(len(l)):
    probabbility_array.append([l[i],[i]])

probabbility_array.sort(key=lambda x:[x[0],len(l)-x[1][0]],reverse=True)

while(len(probabbility_array)>=2):
    for x in probabbility_array[-2][1]:
        res[x]+="0"

    probabbility_array[-2][0]+=probabbility_array[-1][0]
    probabbility_array[-2][0]=round(probabbility_array[-2][0],3)

    for x in probabbility_array[-1][1]:
        res[x]+="1"
        probabbility_array[-2][1].append(x)

    probabbility_array.pop()

    j=-2
    while(j>= -len(probabbility_array) and (probabbility_array[j+1][0] > probabbility_array[j][0]) ):
        probabbility_array[j] , probabbility_array[j+1] = probabbility_array[j+1] , probabbility_array[j]
        j-=1
res=[x[::-1] for x in res]

print(res)

H = 0
L = 0
for i in range(0,len(l)):
    H = H + (l[i]*math.log((1/l[i]),2))
    L = L + (l[i]*len(res[i]))
print("probablities",end="      ")
print("Code")
for i in range(0,len(l)):
    print(l[i],end="                ")
    print(res[i])
print("Entropy is {}".format(round(H,2)))
print("Average CodeWord Length is {}".format(round(L,2)))
print("Efficiency is {}".format(round(((H/L)*100),2)))
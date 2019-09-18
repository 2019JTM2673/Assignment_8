#......Problem 1............
print("Enter binary bit dat that has to be transmitted: ",end=' ')
s=input()
count=0
for i in s:        #...loop to count number of 1 in string...
    #print(i)
    if i=='1':
        count=count+1
        #..condition for even and odd parity check....
if count%2==0:
            print("This is even parity" )
            p=s[:len(s)]+'1'
            print("Parity bit data:", p)  #...for even parity....
            #print (p)
            #print (type(p))
            q= list(p)
            #print(q)
            for k in range(0, len(q)): 
                q[k] = int(q[k]) 
               
            #print (q)
        
            #for r in q:
            #   print(r, end="") 
           
             #print (type(q))
            #print("Parity bit data:", p)  #...for even parity....
            #'010' in p
            #td=[ch for ch in q]
            #td = int(td)
            #print(td) 
            for j in range(len(q)):
                if q[j]==0 and q[j+1]==1 and q[j+2]==0:
                    
                    q.insert(j+3, 0)  
                    print(q)
                    q.append(0)
            q.append(1)
            q.append(0)
            q.append(1) 
            #print (q)
            #s= " "
            #r= s.join(q)
            #print(r)
            print("Transmitted Data:")
            for l in q:
                #print("Transmitting Data:", l)
                print(l, end='')
         




else:
            print("This is Odd parity" )
            p=s[:len(s)]+'0'
            print("Parity bit data:", p)  #...for even parity....
            #print (p)
            #print (type(p))
            q= list(p)
            #print(q)
            for k in range(0, len(q)): 
                q[k] = int(q[k]) 
               
            #print (q)
        
            #for r in q:
            #   print(r, end="") 
           
             #print (type(q))
            #print("Parity bit data:", p)  #...for even parity....
            #'010' in p
            #td=[ch for ch in q]
            #td = int(td)
            #print(td) 
            for j in range(len(q)):
                if q[j]==0 and q[j+1]==1 and q[j+2]==0:
                    
                    q.insert(j+3, 0)  
                    print(q)
                    q.append(0)
            q.append(1)
            q.append(0)
            q.append(1) 
            #print (q)
            #s= " "
            #r= s.join(q)
            #print(r)
            print("Transmitted Data:")
            for l in q:
                #print("Transmitting Data:", l)
                print(l, end='')



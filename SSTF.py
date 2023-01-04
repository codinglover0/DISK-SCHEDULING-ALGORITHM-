                    #SSTF DISK SCHEDULING ALGORITHM

#request queue is the sequence of desired track numbers to read/write data.
request_queue=[98,183,37,122,14,124,65,67]
l=[]
m=[]
n=[]

#initialise seek time to zero
seek_time=0
total_head_movement=0
final_position=0

#current posititon is the track number where arm head is present initially.
current_position=53

#appending seek time in an empty list l.
while(len(request_queue)>0):
    for i in range(len(request_queue)):
        particular_seek_time=abs(current_position-request_queue[i])
        l.append(particular_seek_time)       
    min_seek_time=min(l)                      #finding minimum seek time among all seek times stored in l.
    index_min_seek_time=l.index(min_seek_time)     #finding index in l, of minimum seek time.
    m.append(request_queue[index_min_seek_time])    #determining next track position and storing it in list m.
    n.append(abs(current_position-m[0]))           #appending seek time in list n , of next track position. 
    current_position=m[0]
    request_queue.remove(m[0])    
    l=[]
    m=[]
    
#printing total no. of head movements.    
for i in range(len(n)):
    total_head_movement+=n[i]        
print('Total head movements are:',total_head_movement)
    
        
        








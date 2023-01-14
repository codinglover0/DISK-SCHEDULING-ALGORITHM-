                    #FCFS DISK SCHEDULING ALGORITHM

#request queue is the sequence of desired track numbers to reaad/write data.
request_queue=[98,183,37,122,14,124,65,67]
l=[]

#initialise seek time to zero
seek_time=0
total_head_movements=0
final_position=0

#current posititon is the track number where arm head is present initially.
current_position=53

while(len(request_queue)>0):
    seek_time=abs(current_position-request_queue[0])
    l.append(seek_time)
    current_position=request_queue[0]
    request_queue.remove(request_queue[0])
    seek_time=0

#printing total no. of head movements ( avg seek time ).        
for i in range(len(l)):        
    total_head_movements+=l[i]
print('Total head movements are:',total_head_movements)    








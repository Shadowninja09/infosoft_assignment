# INFOSOFT ASSIGNMENT FILE

Infosoft assignment problem 3 debugging

In Problem 3 calender.py these are the issues that I'm able to find-out

ERROR 1 IN Line 9 : - if node.start <= self.end:(ex-6<=4)
Solution : - if node.start >= self.end:(6>=4)
Explanation : - for booking the new event after the previous event if starting time of the new event is greater than 
                equals to the ending time of the previous event, 

ERROR 2 IN Line 14 : - elif node.end >= self.start:(ex-6>=4)
Solution : - elif node.end <= self.start:(6<=4)
Explanation : for booking the event and putting it before the previous event if starting time of the previously booked 
              event is greater than equals to the ending time of the new event

ERROR 3 MISSING ELSE STATEMENT
Solution : - else:          return False
Explanation : - For handling overlapping condition
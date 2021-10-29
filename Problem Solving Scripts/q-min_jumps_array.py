
"""
we have an array {1,4,3,7,1,2,6,7,6,10} we need to reach at the end of the array 
and we have to do this using minimum number of jumps.

So let each element in the array represent the number of steps we can move forward. 
So 1 means one step forward, 4 means 4 steps forward.
Now starting at 1 we reach 4. So that is one jump. Now we are at 4 so we will 
move 4 steps forward, as we are moving 4 steps forward we compare each element with 4. 
Since 3<4 we will ignore it. Now 7>4, so we will store it as we will use this later. 
Now from 4 we hv reached 2. So that is 2 jumps.

Now since 4 steps are over, we will use the 7 that we had stored and move 7- 3 
(the position of 7 in the array) steps. So we will reach the end of the array in 
total 3 jumps.
"""


def jumps(self):
    jumps = [0] * len(self.arr)
    jumps[0] = 1
    for i in range(1, len(self.arr)):
        for j in range(i):
            if self.arr[j] + j >= i:
                jumps[i] = max(jumps[i], jumps[j] + 1)
    return jumps[-1]

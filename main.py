
x = int(input("> "))



for side1 in range(1,x):
    
    for side2 in range(1,x):
        
        for side3 in range(1,x):
            if side1 == side2 and side2 == side3:
                continue
            
            triangle = (side1, side2, side3)
            
            t = [side1, side2, side3]
            
            largest = max(triangle)
            
            t.remove(largest)
            
            if t[0]**2 + t[1]**2 == largest**2:
                print(triangle)
            
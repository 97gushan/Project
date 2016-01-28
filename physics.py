
def gravity(v, dt):
    """ this method simulates the fall of an object with
        the acceleration of 9.82"""
        
    # a constant
    k = 0.06
    
    # calculate the new velocity
    v = v + (k + dt) * 9.82
    
    # calculate the distance traveled
    dy = (k + dt) * v
    
    # return the distance and the velocity
    return(dy, v)
    
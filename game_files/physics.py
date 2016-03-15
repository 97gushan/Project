from math import cos, sin

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
    

def throw(v, angle, dt):
    k = 0.02
    
    v_x = v*cos(angle) * (k+dt)
    v_y = v*sin(angle) * (k+dt)
    
    return [v_x, v_y]
import simplegui
wd = 600
hi = 400
br = 20
vel = [0,0]
bp = [wd/2,hi/2]

def draw(c):
    bp[0] += vel[0]
    bp[1] += vel[1]
    
    #collide and  reflect off of left hand side of canvas
    
    if bp[0] <= br:
        vel[0] = -vel[0]
        bp[0] = br        
    
    if bp[1] <= br:
        vel[1] = -vel[1]
        bp[1] = br
        
    if bp[0] >= wd-br:
        vel[0] = -vel[0]
        bp[0] = wd-br
        
    if bp[1] >= hi-br:
        vel[1] = -vel[1]
        bp[1] = hi-br
        
    c.draw_circle(bp,br,2,"Red","White")
    
def kd(key):    
    acc = 1
    if key == simplegui.KEY_MAP["left"]:     
        vel[0] -= acc
        
    if key == simplegui.KEY_MAP["right"]:        
        vel[0] += acc
        
    if key == simplegui.KEY_MAP["down"]:        
        vel[1] += acc
        
    if key == simplegui.KEY_MAP["up"]:                        
        vel[1] -= acc
    
    print bp,vel
        
frame = simplegui.create_frame("Position ball",wd,hi)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kd)

frame.start()
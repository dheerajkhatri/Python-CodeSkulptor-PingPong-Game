import simplegui
import random
time_count = 3000              #timer of update velocity of ball 
wd = 600
hi = 600 					   #height of canvas
len_mover = 120                #length of movers
br = 15                        #ball radius
mov_w = 20      #mover width 
mover_move = 35 # mover move length
max_score = 10  # max scoer of game
rand_x = 0      #random int for  ball speed
rand_y = 0      #when anyone get point 
v_inc = 0.3     #increment speed of ball with time
extra = 25      # end correction should be greater than br
csound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
csound.set_volume(0.7)

def init():
    global vel,bp,mov1_s,mov1_e,mov2_s,mov2_e,score1,score2,completed,rand_x,rand_y
    rand_x = random.choice([-2,2,-3,3])
    rand_y = random.choice([-2,2,-3,3])
    vel = [rand_x,rand_y]                    #velocity of ball
    bp = [wd/2,hi/2]               #ball position
    mov1_s = [0,hi/2-len_mover/2]  #mover 1 start point coordinates
    mov1_e = [0,hi/2+len_mover/2]
    mov2_s = [wd,hi/2-len_mover/2]
    mov2_e = [wd,hi/2+len_mover/2]  
    score1 = 0
    score2 = 0
    completed = 0

    
def collision():    
    global bp,vel,score1,score2,rand_x,rand_y   
    #handle the ball
    bp[0] += vel[0]
    bp[1] += vel[1]
    
    #collide and  reflect off of left hand side of canvas
    if bp[1] <= br and bp[0] > br/2+mov_w and bp[0] < wd-mov_w-br/2:
        vel[1] = -vel[1]
        bp[1] = br

    if bp[1] >= hi-br and bp[0] > br/2+mov_w and bp[0] < wd-mov_w-br/2:
        vel[1] = -vel[1]
        bp[1] = hi-br   
    
    if bp[0] <= br/2+mov_w:        
        #print vel
        if mov1_s[1]-extra <= bp[1] and bp[1] <= mov1_e[1]+extra:
            vel[0] = -vel[0]
            bp[0] = br/2+mov_w  
            csound.play()
        else:
            #print str(mov1_s[1]) + " " + str(bp[1]) + " " + str(mov1_e[1])           
            score2 += 1
            bp = [wd-2*br,(mov2_s[1]+mov2_e[1])/2]
            rand_x = random.randint(2,4)
            rand_y = random.randint(2,4)
            vel = [rand_x,rand_y]                 
        
    if bp[0] >= wd-mov_w-br/2:
        #print vel
        if mov2_s[1]-extra <= bp[1] and bp[1] <= mov2_e[1]+extra:
            vel[0] = -vel[0]    
            bp[0] = wd-br/2-mov_w            
            csound.play()
        else :
            #print str(mov2_s[1]) + " " + str(bp[1]) + " " + str(mov2_e[1])           
            score1 += 1
            bp = [2*br,(mov1_s[1]+mov1_e[1])/2]
            rand_x = -random.randint(2,4)
            rand_x = random.randint(2,4)            
            vel = [rand_x,rand_y]        

def is_completed():
    global vel,bp,completed
    if score1 >= max_score or score2 >= max_score :
        vel = [0,0]
        bp = [wd/2,hi/3]
        completed = 1        

            
def draw(c):           
        
    c.draw_line(mov1_s,mov1_e, mov_w, 'Green')
    c.draw_line(mov2_s,mov2_e, mov_w, 'Violet')       
    
    c.draw_text("Player 1 score",[wd/2-165,20],25,'Green')
    c.draw_text(str(score1),[wd/2-105,60],25,'Green')
    
    c.draw_text("Player 2 score",[wd/2+45,20],25,'Violet')
    c.draw_text(str(score2),[wd/2+75,60],25,'Violet')
    
    is_completed()
    if completed == 1:
        if score1 > score2:
              c.draw_text("Player 1 Won the match",[wd/2-wd/3,hi/2],45,'Green')
        elif score2 > score1:
              c.draw_text("Player 2 Won the match",[wd/2-wd/3,hi/2],45,'Violet')        
        else:
            c.draw_text("Game tied",[wd/3-wd/4,hi/2],45,'Red')  
            
    collision()            
    c.draw_circle(bp,br,2,"Red","White")   
    
    
def kd(key):
    if key == simplegui.KEY_MAP["s"]:   
        if mov1_e[1] < hi:
            mov1_s[1] += mover_move
            mov1_e[1] += mover_move
            
    if key == simplegui.KEY_MAP["w"]:   
        if mov1_s[1] > 0 :
            mov1_s[1] -= mover_move
            mov1_e[1] -= mover_move
            
    if key == simplegui.KEY_MAP["down"]:   
        if mov2_e[1] < hi:
            mov2_s[1] += mover_move
            mov2_e[1] += mover_move
        
    if key == simplegui.KEY_MAP["up"]:   
        if mov2_s[1] > 0 :
            mov2_s[1] -= mover_move
            mov2_e[1] -= mover_move

def time_handler():    
    global vel    
    if bp[0] > br/2+mov_w and bp[0] < wd-mov_w-br/2:
        if vel[0] > 0 and vel[0] < 8:
            vel[0] += v_inc
        elif vel[0] <0 and vel[0] >-8:        
            vel[0] -= v_inc
            
        if vel[1] > 0 and vel[1] < 8:
            vel[1] += v_inc
        elif vel[1] < 0 and  vel[1] > -8:            
            vel[1] -= v_inc
            
def reset_handler():            
    init()
        
frame = simplegui.create_frame("PONG",wd,hi)
init()
frame.set_draw_handler(draw)
frame.set_keydown_handler(kd)
reset_button = frame.add_button('Reset Game' , reset_handler)
stimer = simplegui.create_timer(time_count,time_handler)
frame.start()
stimer.start()
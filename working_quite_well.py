import simplegui
import random
time_count = 3000              #timer of update velocity of ball 
wd = 600
hi = 600 					   #height of canvas
score1 = 0
score2 = 0
len_mover = 120                #length of movers
br = 15                        #ball radius
vel = [5,5]                    #velocity of ball
bp = [wd/2,hi/2]               #ball position
mov1_s = [0,hi/2-len_mover/2]  #mover 1 start point coordinates
mov1_e = [0,hi/2+len_mover/2]
mov2_s = [wd,hi/2-len_mover/2]
mov2_e = [wd,hi/2+len_mover/2]        
mov_w = 20      #mover width 
mover_move = 35 # mover move length
max_score = 10  # max scoer of game
rand_x = 0      #random int for  ball speed
rand_y = 0      #when anyone get point 
v_inc = 0.3     #increment speed of ball with time
extra = 25      # end correction should be greater than br

def draw(c):
    global score1,score2,bp,vel,rand_x,rand_y   
     
    if score1 >= max_score or score2 >= max_score :
        vel = [0,0]
        bp = [wd/2,hi/3]
        stop_game(c)
        
    c.draw_line(mov1_s,mov1_e, mov_w, 'Green')
    c.draw_line(mov2_s,mov2_e, mov_w, 'Violet')       
    
    c.draw_text("Player 1 score",[wd/2-165,20],25,'Green')
    c.draw_text(str(score1),[wd/2-105,60],25,'Green')
    
    c.draw_text("Player 2 score",[wd/2+45,20],25,'Violet')
    c.draw_text(str(score2),[wd/2+75,60],25,'Violet')
    
    
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
        if mov1_s[1]-extra <= bp[1] and bp[1] <= mov1_e[1]+extra:
            vel[0] = -vel[0]
            bp[0] = br/2+mov_w                  
        else:
            print str(mov1_s[1]) + " " + str(bp[1]) + " " + str(mov1_e[1])           
            score2 += 1
            bp = [wd-2*br,(mov2_s[1]+mov2_e[1])/2]
            rand_x = random.randint(2,4)
            rand_y = random.randint(2,4)
            vel = [rand_x,rand_y]                 
        
    if bp[0] >= wd-mov_w-br/2:
        if mov2_s[1]-extra <= bp[1] and bp[1] <= mov2_e[1]+extra:
            vel[0] = -vel[0]    
            bp[0] = wd-br/2-mov_w            
        else :
            print str(mov2_s[1]) + " " + str(bp[1]) + " " + str(mov2_e[1])           
            score1 += 1
            bp = [2*br,(mov1_s[1]+mov1_e[1])/2]
            rand_x = -random.randint(2,4)
            rand_x = random.randint(2,4)            
            vel = [rand_x,rand_y]        
        
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
        
def stop_game(c):
    
    if score1 > score2:
          c.draw_text("Player 1 Won the match",[wd/2-wd/3,hi/2],45,'Green')
    elif score2 > score1:
          c.draw_text("Player 2 Won the match",[wd/2-wd/3,hi/2],45,'Violet')        
    else:
          c.draw_text("Game tied",[wd/3-wd/4,hi/2],45,'Red')  

def time_handler():    
    global vel
    if bp[0] > br/2+mov_w and bp[0] < wd-mov_w-br/2:
        if vel[0] > 0:
            vel[0] += v_inc
        else :
            vel[0] -= v_inc
        if vel[1] > 0:
            vel[1] += v_inc
        else :            
            vel[1] -= v_inc
            
frame = simplegui.create_frame("PONG",wd,hi)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kd)
stimer = simplegui.create_timer(time_count,time_handler)
frame.start()
stimer.start()
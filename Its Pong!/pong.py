import pygame
import time
import random
white = (255,255,255)
black = (0,0,0)
displaywidth = 800
displayheight = 600
ballstart = random.randint(1,2)
pygame.init()
clock = pygame.time.Clock()

# Please accept me into Troy University. :)

         # display settings
gamedisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption("It's Pong!")
         #
class images:

    def __init__(self):
        self.itslineimg = "itsline.png"
        self.theline = pygame.image.load(self.itslineimg)
        
        self.itspongimg = "its pong!!.png"
        self.itspong = pygame.image.load(self.itspongimg)
        

    def line(self):
        gamedisplay.blit(self.theline,(-5,70))



    def its_pong(self):
        gamedisplay.blit(self.itspong, (-110,-70))
        
        
class ball:
    


   
    def __init__(self):
        #images
        self.b_img = "transparentball.png"
        self.ballimg = pygame.image.load(self.b_img)
        

        #ball position
        self.x = 400
        self.y = 300
        
        #ballspeed
        self.xs = 3
        self.ys = 3

        

    def b_imgblit(self):
        
        
        
        gamedisplay.blit(self.ballimg, (self.x,self.y))
        
        
    def ballmove(self):
        self.x = self.x + self.xs
        self.y = self.y + self.ys




    def detectpaddle(self):
        #Im sure theres a better solution to detect the paddle,
        #but this is the first one i could think of.
        self.paddletop = game1paddle1.paddle1y + 58
        self.paddlebottom = game1paddle1.paddle1y - 58
        self.aipaddletop = ai_1.paddle2y + 58
        self.aipaddlebottom = ai_1.paddle2y - 58


        if ball1.y  < self.paddletop  and ball1.y > self.paddlebottom:
            if ball1.x < 32:
                self.xs = self.xs * -1

        
        if ball1.y  < self.aipaddletop and ball1.y > self.aipaddlebottom:
            if ball1.x > 695:
                self.xs = self.xs * -1

        #



    def detectborder(self):
        if self.y >= displayheight * 0.9 or self.y <= displayheight * 0.1:
            self.ys = self.ys * -1



class player:
    def __init__(self):
        # paddle position
        self.paddle1y = 100
        
        #
        #paddlespeed
        self.paddle1speed = 4.5
        #

        #images
        self.paddle1img = "paddle.png"
        #

        
        
        
    def paddle1(self):



         #paddle borders
       if self.paddle1y <= displayheight * 0.15:
           self.paddle1y = displayheight * 0.149
           
       if self.paddle1y >= displayheight * 0.80:
           self.paddle1y = displayheight * 0.799
       
       #
       

        
       #loads paddle image then displays it
       p1img = pygame.image.load(self.paddle1img)
       gamedisplay.blit(p1img, (25, self.paddle1y))
       #
       


       
       #checking pressed keys
       self.paddle1keys = pygame.key.get_pressed()
       #
       

       #moves paddle
       if self.paddle1keys[pygame.K_UP]:
           self.paddle1y = self.paddle1y + self.paddle1speed
       if self.paddle1keys[pygame.K_DOWN]:
           self.paddle1y = self.paddle1y - self.paddle1speed
           
       #


class AI():
    def __init__(self):
        self.paddle2img = "paddle.png"
        self.paddle2 = pygame.image.load(self.paddle2img)
        
        
        self.direction = 0
        
        self.paddle2y = 300

    def paddleai(self):
        #detects ball location and moves paddle to it
        if ball1.xs == 3:
            if ball1.ys == -3:
                self.direction = -2.5

            else:
                self.direction = 2.5
           
            #response
            if self.paddle2y != ball1.y:
                    self.paddle2y = self.paddle2y + self.direction
        #
        
      


    def paddle2blit(self):
        
        gamedisplay.blit(self.paddle2, (755, self.paddle2y))
                         

        
    def AIdetectborder(self):
        if self.paddle2y <= displayheight * 0.15:
           self.paddle2y = displayheight * 0.149
           
        if self.paddle2y >= displayheight * 0.80:
           self.paddle2y = displayheight * 0.799


   

            
        
def update():
    pygame.display.update()
        
        

#class instances
ball1 = ball()

image1 = images()
game1paddle1 = player()
ai_1 = AI()
#    



#game loop 
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    #imagefunctions
    image1.its_pong()
    image1.line()
    #
    
    
    #ball functions
    ball1.b_imgblit()
    ball1.ballmove()
    ball1.detectborder()
    ball1.detectpaddle()
    
   
    #player functions    
    game1paddle1.paddle1()
    
    ai_1.AIdetectborder()
    ai_1.paddleai()
    ai_1.paddle2blit()
    
    
    update()
  

    
    gamedisplay.fill(white)
  

    clock.tick(60)


pygame.quit()
quit()

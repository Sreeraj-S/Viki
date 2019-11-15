import pygame
import time
import random
pygame.init()

myfont = pygame.font.SysFont("monospace", 55)
compfont=pygame.font.SysFont("monospace", 20)
initbg0=[pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init0.png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init.0.png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init..0.png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init...0.png")]
initbg1=[pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init1.png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init.1.png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init..1.png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init...1.png")]
initbg2=[pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init1 (2).png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init.1 (2).png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init..1 (2).png"),pygame.image.load("F:\\sreeraj\\viki\\initpic\\Init...1 (2).png")]
initmahagandhi=[pygame.image.load("F:\\sreeraj\\viki\\Mahatma -Gandhi\\Mahatma-Gandhi.jpg"),pygame.image.load("F:\\sreeraj\\viki\\Mahatma -Gandhi\\Mahatma-Gandhi1.jpg")]
loadbg0=[pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load0.png"),pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load.0.png"),pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load..0.png"),pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load...0.png")]
loadbg1=[pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load1.png"),pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load.1.png"),pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load..1.png"),pygame.image.load("F:\\sreeraj\\viki\\loadpic\\load...1.png")]
initbg=[initbg0,initbg1,initbg2]
loadbg=[loadbg0,loadbg1]
loadbg=random.choice(loadbg)
initbg=random.choice(initbg)
whitebg =pygame.image.load("F:\\sreeraj\\viki\\download.jpg")
class Gui():
    def __init__(self):
        self.win = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
        pygame.display.set_caption("Viki")
        self.i=0
        self.num=1
        self.transparent = (0, 0, 0, 0)
        self.loadnum=1
        self.mahagandhinum=0
        self.mahanum=0
        self.x1=450
        self.x2=683
        self.y1=0
        self.vel = 20
        self.test=''
        self.test1=''
        self.comcommand = ''
        self.usecommand =''
    def initreset(self):
        self.num = 0
    def loadreset(self):
        self.loadnum = 0
    def mahareset(self):
        self.mahanum = 1
    def compcommand(self,command):
        
        self.comcommand = command
    def usercommand(self,command):
        self.usecommand = command
    def run(self):
        run = True
        while run:
            pygame.time.delay(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            while self.num==1:
                self.win.blit(initbg[self.i],(150,0))
                pygame.display.update()
                time.sleep(1.5)
                self.i+=1
                if self.i == 4:
                    self.i=0
            self.i = 0
            while self.loadnum==1:
                self.win.blit(loadbg[self.i],(150,0))
                pygame.display.update()
                time.sleep(1.5)
                self.i+=1
                if self.i == 4:
                    self.i=0
            self.i=0
            self.win.fill((0,0,0))
            pygame.display.update()
            while self.mahagandhinum < len(initmahagandhi):
                self.win.blit(initmahagandhi[self.mahagandhinum],(215,0))
                pygame.display.update()
                time.sleep(5)
                self.mahagandhinum+=1
                
                
            self.win.fill((0,0,0))
            pygame.display.update()

            while self.mahanum == 0:
                
                self.win.blit(pygame.image.load("F:\\sreeraj\\viki\\Mahatma -Gandhi\\Mahatma-Gandhi2.jpg"),(315,0))
                pygame.display.update()
                time.sleep(3.5)
                while self.mahanum == 0:
                    label = myfont.render("\"MISS YOU GANDHI JI\"", 1, (0,255,255))
                    self.win.blit(label, (300,675))
                    pygame.display.update()
                    time.sleep(10)
                self.win.fill((0,0,0))
                pygame.display.update()
                while True:
                    self.win.blit(pygame.image.load("F:\\sreeraj\\viki\\Capture.PNG"),(563,277))
                    pygame.display.update()
                    while True:
                        if not self.comcommand == self.test:
                            label1 = compfont.render(self.comcommand, 1, (255,255,255))
                            self.win.blit(label1, (self.x1,self.y1))
                            pygame.display.update()
                            time.sleep(1)
                            self.y1+=self.vel
                            self.test = self.comcommand
                            
                        elif not self.test1 == self.usecommand:
                            label1=compfont.render(self.usecommand, 1, (255,255,255))
                            self.win.blit(label1, (self.x2,self.y1))
                            pygame.display.update()
                            time.sleep(1)
                            self.y1+=self.vel
                            self.test1 = self.usecommand




                
        
        pygame.quit()
    
            
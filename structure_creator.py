import pygame as py

class StructureCreator:

    def __init__(self):
        self.velky_dom_img = py.transform.scale(py.image.load('images/large_house.png'), (300,300))
        self.mid_dom_img = py.transform.scale(py.image.load('images/mid_house.png'), (250,250))
        self.maly_dom_img = py.transform.scale(py.image.load('images/small_house.png'), (150,150))
        pass

    def draw(self,pozadie,building_name,b_x,b_y):
        ret = []
        #pre les
        if(building_name=="maly_dom"):
            ##strecha
            #pygame.draw.polygon(screen, color, (point-x, point-y, point-z))
            #ret.append(py.draw.polygon(pozadie.obrazovka,(240,0,0),[(b_x+75,b_y-250),(b_x-20,b_y-150),(b_x+170,b_y-150)]))
            ##telo
            

            ret.append(py.draw.rect(pozadie.obrazovka,(204,102,0),[b_x,b_y-150,150,150]))
            rect = py.Rect(b_x, b_y-150, 150, 150)
            pozadie.obrazovka.blit(self.maly_dom_img, rect)
            
            ret.append(210)
        
        if(building_name=="stredny_dom"):
            ##strecha
            #pygame.draw.polygon(screen, color, (point-x, point-y, point-z))
            #ret.append(py.draw.polygon(pozadie.obrazovka,(240,0,0),[(b_x+125,b_y-390),(b_x-40,b_y-250),(b_x+290,b_y-250)]))
            ##telo
            ret.append(py.draw.rect(pozadie.obrazovka,(255,255,255),[b_x,b_y-250,250,250]))
            rect = py.Rect(b_x, b_y-250, 250, 250)
            pozadie.obrazovka.blit(self.mid_dom_img, rect)

            ret.append(330)
        
        if(building_name=="velky_dom"):
            ##strecha
            #pygame.draw.polygon(screen, color, (point-x, point-y, point-z))
            #ret.append(py.draw.polygon(pozadie.obrazovka,(240,0,0),[(b_x+150,b_y-480),(b_x-60,b_y-300),(b_x+360,b_y-300)]))
            ##telo
            ret.append(py.draw.rect(pozadie.obrazovka,(255,255,255),[b_x,b_y-300,300,300]))
            rect = py.Rect(b_x, b_y-300, 300, 300)
            pozadie.obrazovka.blit(self.velky_dom_img, rect)
            
            ret.append(400)
        
        if(building_name=="strom"):
            pass
        if(building_name=="mravenisko"):
            pass
        if(building_name=="hovno"):
            pass

        return ret

    def was_collision(self,building_name,b_x,b_y,p_x,p_y):
        if(building_name=="maly_dom"):
            pass
        if(building_name=="stredny_dom"):
            pass
        if(building_name=="velky_dom"):
            pass
        if(building_name=="strom"):
            pass
        if(building_name=="mravenisko"):
            pass
        if(building_name=="hovno"):
            pass

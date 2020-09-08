












import pygame

def text_to_screen(screen,text,x,y,size=15,color=(255,255,255),
                   font_type='monospace'):
    try:
        text=str(text)
        font=pygame.font.Font('C:\Windows\Fonts\CURLZ___.TTF',size)
        ##font=pygame.font.Font('',size)
        text=font.render(text,True,color)
        screen.blit(text,(x,y))
        
    except Exception,e:
        print 'Font Error, saw it coming'
        raise e

    

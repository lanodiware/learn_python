from ent import *

FPS = 50


def updatescr():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


def drawstuff():
    World.SCHERMO.blit(World.image, (0, 0))
    World.SCHERMO.blit(Ground.image, (Ground.grposx, Ground.grposy))
    World.SCHERMO.blit(Button.sprite, (World.sf_lar/2-112, 50))


def draw_human(entity):
    World.SCHERMO.blit(entity.sprite, (entity.posy, entity.posx))


def gravity_pull(entity, ground):
    if entity.posx + entity.height*0.5 < ground:
        entity.velocity += entity.gravity
        entity.posx += entity.velocity
    else:
        entity.velocity = 0

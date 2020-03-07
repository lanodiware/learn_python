import events
from ent import *

person = Human(height=50, width=50, posx=100, posy=100, velocity=0)
pygame.init()


while True:
    events.updatescr()
    events.drawstuff()
    events.draw_human(person)
    events.gravity_pull(person, Ground.grposy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


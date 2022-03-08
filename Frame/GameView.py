from pygame.display import set_mode, update, set_caption
from pygame.time import Clock
from pygame import init, quit, QUIT
from pygame.event import get as events
from GameStage import GameStages

from sys import exit as end


class window:
    def __init__(self):
        init()
        Name = "Title"
        mode = (600, 400)

        self.screen = set_mode(mode)
        set_caption(Name)
 
        self.currentStage = GameStages['test'] # some stage
        self.currentStage.Enter(mode)

    def Main(self):
        clock = Clock()
        callback: str or None= None
        while True:
            for eve in events():
                if eve.type == QUIT:
                    self.currentStage.Exit()
                    quit()
                    end(0)
                else:
                    print('not quit', end="\r")
                    callback = self.currentStage.Control(eve)

                if callback:
                    self.callbackControl(callback)
                    callback = None

                self.currentStage.Update()
                self.currentStage.Rend(self.screen)
                update()
                clock.tick(10)

    def callbackControl(self, callback):
        pass

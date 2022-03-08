from Utils.Panel import TextElement, Panel
from GameStage.GameStage import GameStage
from pygame import KEYDOWN,K_RETURN

class Test(GameStage):
    def __init__(self):
        super().__init__('test')
        self.panel = None

    def Enter(self, dp_mode):
        print('stage enter')
        self.Panel = Panel(dp_mode,color=(128,128,128))
        self.text = TextElement("0", (100,200),Size=50)
        self.Panel.AddElement(self.text)

    def Exit(self):
        print('stage exit unexpectedly')

    def End(self):
        print('stage exit normally')

    def Rend(self, screen):
        self.Panel.DrawScreen(screen,(0,0))

    def Update(self):
        self.text.text = self.text.text+'1'
        self.Panel.Update()

    def Control(self, eve):
        if eve.type == KEYDOWN:
            if eve.key == K_RETURN:
                self.text.text = '0'
                print('Pressed')
        return None

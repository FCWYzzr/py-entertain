from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.sprite import Sprite, Group
from pygame.image import load
from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface
from Utils.Panel import Element


def _collide(ra, rb):
    c1 = ra.top <= rb.top <= ra.bottom
    c2 = ra.left <= rb.left <= ra.right
    return c1 and c2


def collide(a, b, doKill=False):
    ans = []
    for o in b:
        if _collide(a.rect, o.rect) or _collide(o.rect, a.rect):
            ans.append(o)
    if doKill:
        for o in ans:
            b.remove(o)
    return ans


class Button(Element):
    def __init__(self, image, pos, command=None):

        if isinstance(image, str):
            self.NonFocusImg = load(image + '_NF.png').convert()
            self.FocusImg = load(image + '_F.png').convert()
        else:
            self.NonFocusImg = Surface(image.get_size())
            self.NonFocusImg.fill((255, 255, 255))
            self.NonFocusImg.blit(image, (0, 0))
            self.FocusImg = Surface(image.get_size())
            self.FocusImg.blit(self.NonFocusImg, (0, 0))
            X, Y = self.FocusImg.get_size()
            for x in range(X):
                for y in range(Y):
                    color = self.FocusImg.get_at((x, y))
                    color = Color(255 - color.r, 255 - color.g, 255 - color.b, color.a)
                    self.FocusImg.set_at((x, y), color)
        self._ready = False
        if command is not None:
            self.command = command
        super().__init__(Surface(self.FocusImg.get_size()), pos)
        self.image.blit(self.NonFocusImg, (0, 0))

    def V_ready(self):
        self.image.set_alpha(30)

    def V_Unready(self):
        self.image.set_alpha(255)

    def ready(self):
        self._ready = True
        self.V_ready()

    def unReady(self):
        self._ready = False
        self.V_Unready()

    def isReady(self):
        return self._ready

    def Focus(self):
        self.image.blit(self.FocusImg, (0, 0))

    def UnFocus(self):
        self.image.blit(self.NonFocusImg, (0, 0))


class Buttons(Group):

    def GetClick(self, pos) -> Button:
        mouse = Sprite()
        mouse.rect = Rect(*pos, 1, 1)
        click = collide(mouse, self)
        return None if not click else click[0]

    def Buttons(self) -> list[Button]:
        return self.sprites()

    def GetReady(self) -> Button:
        ready = [btn for btn in self.Buttons() if btn.isReady()]
        return None if not ready else ready[0]


def ButtonControl(eve, buttons, Pos, PressButton):
    for btn in buttons.Buttons():
        if btn.isReady():
            btn.V_Unready()
        else:
            btn.UnFocus()

    btn = buttons.GetClick(Pos)
    btn2 = buttons.GetReady()
    if btn and btn2:
        if btn2 == btn:
            btn.V_ready()
    elif btn:
        btn.Focus()

    if eve.type == MOUSEBUTTONDOWN:
        if PressButton[0]:
            btn = buttons.GetClick(Pos)
            if btn:
                btn.ready()
    elif eve.type == MOUSEBUTTONUP:
        if not PressButton[0]:
            btn = buttons.GetClick(Pos)
            if btn and btn.isReady():
                return btn.command()
            elif buttons.GetReady():
                buttons.GetReady().unReady()
    return None



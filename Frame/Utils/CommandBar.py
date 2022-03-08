from collections import deque
from pygame import KEYDOWN, K_RETURN, K_BACKSPACE
from pygame.surface import Surface
from pygame.font import SysFont, init
from Utils.Panel import Element


def s(ss: str):
    pass


Function = type(s)


def Cmd(func: Function):
    CName = func.__name__

    def Wrapper(arg: str):
        args = arg.split()
        assert args[0] == CName
        return func(*args[1:])

    Wrapper.__name__ = CName
    return Wrapper


init()

cmdFont = SysFont('Comic Sans MS', 15, False)


class CommandBar(Element):
    def __init__(self, pos, commands: dict[str, Function]):
        self.text = deque("Enter")
        textSur = cmdFont.render(''.join(self.text), False, (0, 0, 0))
        bGround = Surface((450, textSur.get_height() + 10))
        bGround.fill((128, 128, 128))
        fGround = Surface((440, textSur.get_height()))
        fGround.fill((255, 255, 255))
        bGround.blit(fGround, (5, 5))
        self.background = bGround
        self.commands: dict[str, Function] = commands
        super().__init__(Surface(bGround.get_size()), pos)

    def update(self):
        textSur = cmdFont.render(''.join(self.text), False, (0, 0, 0))
        self.image.blit(self.background, (0, 0))
        self.image.blit(textSur, (10, 5))

    def control(self, eve):
        if eve.type == KEYDOWN:
            if eve.key == K_RETURN:
                cmd: str = ''.join(self.text)
                self.text.clear()
                for c in self.commands.keys():
                    if c == cmd[:len(c)]:
                        self.commands[c].__call___(cmd)
                        break
                else:
                    self.commands['__err__'].__call__(cmd)
            elif 'a' <= chr(eve.key) <= 'z' or eve.key == ord(' '):
                self.text.append(chr(eve.key))
            elif eve.key == K_BACKSPACE:
                if self.text:
                    self.text.pop()

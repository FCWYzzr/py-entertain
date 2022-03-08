from pygame import init, quit, QUIT
from pygame.image import load
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.sprite import Sprite, Group
from pygame.font import SysFont
from copy import deepcopy


class Element(Sprite):
    def __init__(self, image: Surface or list[Surface], pos: [int, int]):
        super().__init__()
        self.image = deepcopy(image) if isinstance(image, list) else image.copy()
        self.rect = Rect(*pos, *image.get_size())

    def Image(self):
        """
        :return: Surface
        return a image you like, recover the .image property
        """
        return self.image

    def Rect(self):
        """
        :return: Rect
        return a rect you like, recover the .rect property
        """
        return self.rect

    def condition(self, eve) -> bool:
        """
        :param eve: Event
        :return: whether this element will get eve or not
        default no condition (always true)
        """
        return True

    def control(self, eve):
        """
        :param eve:
        :return: None
        operate the game like:
            if self.Condition(eve):
                something
        you don't actually need a if-else sentence
        default do nothing
        """
        pass

    def update(self):
        """
        :return: None
        this is where the image changed, or operate something else
        """


class TextElement(Element):
    def __init__(self, default_text, pos,
                 Font: str or None = None,
                 Size: int or None = None,
                 Bold: bool or None = None,
                 Color: tuple[int, int, int] or None = None):
        Font = Font if Font else "Times New Man"
        Size = Size if Size else 15
        Bold = Bold if (Bold is None) else False
        Color = Color if Color else (0, 0, 0)

        FontStyle = SysFont(Font, Size, Bold)
        Image = FontStyle.render(default_text, False, Color)
        super().__init__(Image, pos)
        self.style = FontStyle
        self.text = default_text
        self.Color = Color

    def update(self):
        self.image = self.style.render(self.text, False, self.Color)


class Panel:
    def __init__(self, display_mode: tuple[int, int], color=(255, 255, 255)):
        self.surface = Surface(display_mode)
        self.elements: Group[Element] = Group()
        self.df_color = color

    def AddElement(self, e: Element):
        self.elements.add(e)

    def DrawElements(self):
        ele: Element
        self.surface.fill(self.df_color)
        for ele in self.elements.sprites():
            self.surface.blit(ele.Image(), ele.rect)

    def DrawScreen(self, screen, dest):
        self.DrawElements()
        screen.blit(self.surface, dest)

    def Control(self, eve):
        ele: Element
        for ele in self.elements.sprites():
            if ele.condition(eve):
                ele.control(eve)
    def Update(self):
        for ele in self.elements.sprites():
            ele.update()

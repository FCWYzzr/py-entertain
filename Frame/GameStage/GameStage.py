class GameStage:
    def __init__(self, name):
        self.Name = name

    def Enter(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: None
        the operations when getting into this Stage
        """
        pass

    def Exit(self):
        """
        :return: None
        the operations when UNEXPECTED exit occurred
        """
        pass

    def End(self):
        """
        :return: None
        the operations when NORMALLY exit current stage
        """
        pass

    def Rend(self, screen):
        """
        :param screen: Surface, usually the display surface
        :return: None
        Rend current stage on screen
        """
        pass

    def Update(self):
        """
        :return: None
        Updates on schedule
        """
        pass

    def Control(self, eve):
        """
        :param eve: event
        :return: tuple[str,any]
        Update or operations based on events,
        return a command(and params to proceed if needed)
        if need the window do something
        """
        pass

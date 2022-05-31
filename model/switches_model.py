class SwitchesValues:
    """
    This class is for modeling behavior and attributes of objects which are used in Switches page testing.
    """

    def __init__(self, tinted=None, default=None):
        """
        Method which lets the class initialize the object's attributes
        :param tinted:
        :param default:
        """
        self.tinted = tinted
        self.default = default

    def __repr__(self):
        """
         Method used to represent a class's objects as a string
         :return:
         """
        return "%s:%s" % (self.default, self.tinted)

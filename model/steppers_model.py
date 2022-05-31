class SteppersValues:
    """
    This class is for modeling behavior and attributes of objects which are used in Steppers page testing.
    """

    def __init__(self, tinted=None, default=None, custom=None):
        """
        Method which lets the class initialize the object's attributes
        :param tinted:
        :param default:
        :param custom:
        """
        self.tinted = tinted
        self.default = default
        self.custom = custom

    def __repr__(self):
        """
        Method used to represent a class's objects as a string
        :return:
        """
        return "%s:%s:%s" % (self.default, self.tinted, self.custom)

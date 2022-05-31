class SlidersValues:
    """
    This class is for modeling behavior and attributes of objects which are used in Sliders page testing.
    """

    def __init__(self, tinted=None, default=None, custom=None, images=None):
        """
        Method which lets the class initialize the object's attributes
        :param tinted:
        :param default:
        :param custom:
        """
        self.tinted = tinted
        self.default = default
        self.custom = custom
        self.images = images

    def __repr__(self):
        """
         Method used to represent a class's objects as a string
         :return:
         """
        return "%s:%s:%s:%s" % (self.default, self.tinted, self.custom, self.images)

class PickerValues:
    """
    This class is for modeling behavior and attributes of objects which are used in Picker page testing.
    """

    def __init__(self, red=None, green=None, blue=None):
        """
        Method which lets the class initialize the object's attributes
        :param tinted:
        :param default:
        :param custom:
        """
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        """
         Method used to represent a class's objects as a string
         :return:
         """
        return "%s:%s:%s" % (self.red, self.green, self.blue)

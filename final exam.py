class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tentList = []
        self.add_tent(tent_loc)
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for i in self.tentList:
            if Location.dist_from(i, new_tent_loc) < 0.5:
                return False
        self.tentList.append(new_tent_loc)
        return True
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        try:
            self.tentList.remove(tent_loc)
        except:
            raise ValueError("There is not a tent at this location")
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        printableList = []
        for i in self.tentList:
            printableList.append(Location.__str__(i))
        return sorted(printableList)
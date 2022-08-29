class Terrain(): 
    """
    Terrain is the land area and type of surface
    """
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def coords_within_boundary(self, _x_pos: int, _y_pos: int) -> bool:
        """ Test if coordinates is within the set boundary
        """
        True

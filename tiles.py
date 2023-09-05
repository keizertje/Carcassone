from dataclass import DataClass


meadow: str = "meadow"
village: str = "village"
road: str = "road"
monastery: str = "monastery"

top: str = "top"
left: str = "left"
right: str = "right"
bottom: str = "bottom"
middle: str = "middle"
top_road_left: str = "top_road_left"
top_road_right: str = "top_road_right"
left_road_left: str = "left_road_left"
left_road_right: str = "left_road_right"
right_road_left: str = "right_road_left"
right_road_right: str = "right_road_right"
bottom_road_left: str = "bottom_road_left"
bottom_road_right: str = "bottom_road_right"


class MeeplePlace: pass


class MeeplePlace(DataClass):
    place_type: str = ""
    meeple_place = True
    has_village_extra: bool = False  # only for villages
    
    def __eq__(self, other: str | MeeplePlace | None):
        """
        :param self: MeeplePlace
        :param other: str
        :return: self.place_type == other
        """
        if type(other) == str:
            return self.place_type == other
        elif type(other) == MeeplePlace:
            return self.place_type == other.place_type
        elif other is None:
            return True


class Tile(DataClass):
    letter: str

    top: MeeplePlace
    left: MeeplePlace
    right: MeeplePlace
    bottom: MeeplePlace
    middle: MeeplePlace = MeeplePlace(meeple_place=False)
    connections: dict[str, list[str]] = []
 
    def turn(self, times=1):
        for _ in range(times):
            _top = self.left
            _left = self.bottom
            _bottom = self.right
            _right = self.top

            _connections = {}
            convertings = {
                top: right,
                top_road_left: right_road_left,
                top_road_right: right_road_right,
                right: bottom,
                right_road_left: bottom_road_left,
                right_road_right: bottom_road_right,
                bottom: left,
                bottom_road_left: left_road_left,
                bottom_road_right: left_road_right,
                left: top,
                left_road_left: top_road_left,
                left_road_right: top_road_right,
                middle: middle
            }
            for key in self.connections.keys():
                _connections[convertings[key]] = [convertings[i] for i in self.connections[key]]

            self.top = _top
            self.left = _left
            self.right = _right
            self.bottom = _bottom
            self.connections = _connections

        return self

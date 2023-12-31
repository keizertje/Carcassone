from PIL.ImageTk import PhotoImage

from tiles import *
from PIL import Image, ImageTk


tile: int = 0
image: int = 1

tiles: list[Tile] = [
    Tile(letter="a",
         top=MeeplePlace(place_type=meadow),
         left=MeeplePlace(place_type=meadow),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=road),
         middle=MeeplePlace(place_type=monastery),
         connections={top: [left, right, bottom_road_left, bottom_road_right],
                      left: [top, right, bottom_road_left, bottom_road_right],
                      right: [top, left, bottom_road_left, bottom_road_right],
                      bottom: [],
                      bottom_road_left: [top, left, right],
                      bottom_road_right: [top, left, right]}),
    
    Tile(letter="b",
         top=MeeplePlace(place_type=meadow),
         left=MeeplePlace(place_type=meadow),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=meadow),
         middle=MeeplePlace(place_type=monastery),
         connections={top: [left, right, bottom],
                      left: [top, right, bottom],
                      right: [top, left, bottom],
                      bottom: [top, left, right]}),
    
    Tile(letter="c",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=village),
         connections={top: [left, right, bottom],
                      left: [top, right, bottom],
                      right: [top, left, bottom],
                      bottom: [top, left, right]}),
    
    Tile(letter="d",
         top=MeeplePlace(place_type=road),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=road),
         connections={top: [bottom],
                      top_road_left: [bottom_road_right, left],
                      top_road_right: [bottom_road_left],
                      left: [top_road_left, bottom_road_right],
                      right: [],
                      bottom: [top],
                      bottom_road_left: [top_road_right],
                      bottom_road_right: [top_road_left, left]}),
    
    Tile(letter="e",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=meadow),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [],
                      left: [right, bottom],
                      right: [left, bottom],
                      bottom: [left, right]}),
    
    Tile(letter="f",
         top=MeeplePlace(place_type=meadow),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [],
                      left: [right],
                      right: [left],
                      bottom: []}),
    
    Tile(letter="g",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=meadow),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=village),
         connections={top: [bottom],
                      left: [],
                      right: [],
                      bottom: [top]}),
    
    Tile(letter="h",
         top=MeeplePlace(place_type=meadow),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [],
                      left: [],
                      right: [],
                      bottom: []}),
    
    Tile(letter="i",
         top=MeeplePlace(place_type=meadow),
         left=MeeplePlace(place_type=meadow),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=village),
         connections={top: [left],
                      left: [top],
                      right: [],
                      bottom: []}),
    
    Tile(letter="j",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=meadow),
         right=MeeplePlace(place_type=road),
         bottom=MeeplePlace(place_type=road),
         connections={top: [],
                      left: [right_road_left, bottom_road_right],
                      right: [bottom],
                      right_road_left: [left, bottom_road_right],
                      right_road_right: [bottom_road_left],
                      bottom: [right],
                      bottom_road_left: [right_road_right],
                      bottom_road_right: [left, right_road_left]}),
    
    Tile(letter="k",
         top=MeeplePlace(place_type=road),
         left=MeeplePlace(place_type=road),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [left],
                      top_road_left: [left_road_right],
                      top_road_right: [bottom, left_road_left],
                      left: [top],
                      left_road_left: [top_road_left],
                      left_road_right: [bottom, top_road_right],
                      right: [],
                      bottom: [left_road_left, top_road_right]}),
    
    Tile(letter="l",
         top=MeeplePlace(place_type=road),
         left=MeeplePlace(place_type=road),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=road),
         connections={top: [],
                      top_road_left: [left_road_right],
                      top_road_right: [bottom_road_left],
                      left: [],
                      left_road_left: [bottom_road_right],
                      left_road_right: [top_road_left],
                      right: [],
                      bottom: [],
                      bottom_road_left: [top_road_right],
                      bottom_road_right: [left_road_left]}),
    
    Tile(letter="m",
         top=MeeplePlace(place_type=village, has_village_extra=True),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [left],
                      left: [top],
                      right: [bottom],
                      bottom: [right]}),
    
    Tile(letter="n",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [left],
                      left: [top],
                      right: [bottom],
                      bottom: [right]}),
    
    Tile(letter="o",
         top=MeeplePlace(place_type=village, has_village_extra=True),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=road),
         bottom=MeeplePlace(place_type=road),
         connections={top: [left],
                      left: [top],
                      right: [bottom],
                      right_road_left: [bottom_road_right],
                      right_road_right: [bottom_road_left],
                      bottom: [right],
                      bottom_road_left: [right_road_right],
                      bottom_road_right: [right_road_left]}),
    
    Tile(letter="p",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=road),
         bottom=MeeplePlace(place_type=road),
         connections={top: [left],
                      left: [top],
                      right: [bottom],
                      right_road_left: [bottom_road_right],
                      right_road_right: [bottom_road_left],
                      bottom: [right],
                      bottom_road_left: [right_road_right],
                      bottom_road_right: [right_road_left]}),
    
    Tile(letter="q",
         top=MeeplePlace(place_type=village, has_village_extra=True),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [left, right],
                      left: [top, right],
                      right: [top, left],
                      bottom: []}),
    
    Tile(letter="r",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=meadow),
         connections={top: [left, right],
                      left: [top, right],
                      right: [top, left],
                      bottom: []}),
    
    Tile(letter="s",
         top=MeeplePlace(place_type=village, has_village_extra=True),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=road),
         connections={top: [left, right],
                      left: [top, right],
                      right: [top, left],
                      bottom: [],
                      bottom_road_left: [],
                      bottom_road_right: []}),
    
    Tile(letter="t",
         top=MeeplePlace(place_type=village),
         left=MeeplePlace(place_type=village),
         right=MeeplePlace(place_type=village),
         bottom=MeeplePlace(place_type=road),
         connections={top: [left, right],
                      left: [top, right],
                      right: [top, left],
                      bottom: [],
                      bottom_road_left: [],
                      bottom_road_right: []}),
    
    Tile(letter="u",
         top=MeeplePlace(place_type=road),
         left=MeeplePlace(place_type=meadow),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=road),
         connections={top: [bottom],
                      top_road_left: [bottom_road_right],
                      top_road_right: [bottom_road_left],
                      left: [],
                      right: [],
                      bottom: [top],
                      bottom_road_left: [top_road_right],
                      bottom_road_right: [top_road_left]}),
    
    Tile(letter="v",
         top=MeeplePlace(place_type=meadow),
         left=MeeplePlace(place_type=road),
         right=MeeplePlace(place_type=meadow),
         bottom=MeeplePlace(place_type=road),
         connections={top: [right, left_road_right, bottom_road_left],
                      left: [bottom],
                      left_road_left: [bottom_road_right],
                      left_road_right: [top, right, bottom_road_left],
                      right: [top, left_road_right, bottom_road_left],
                      bottom: [left],
                      bottom_road_left: [top, right, left_road_right],
                      bottom_road_right: [left_road_left]}),
    
    Tile(letter="w",
         top=MeeplePlace(place_type=meadow),
         left=MeeplePlace(place_type=road),
         right=MeeplePlace(place_type=road),
         bottom=MeeplePlace(place_type=road),
         connections={top: [left_road_right, right_road_left],
                      left: [],
                      left_road_left: [bottom_road_right],
                      left_road_right: [top, right_road_left],
                      right: [],
                      right_road_left: [top, left_road_right],
                      right_road_right: [bottom_road_left],
                      bottom: [],
                      bottom_road_left: [right_road_right],
                      bottom_road_right: [left_road_left]}),
    
    Tile(letter="x",
         top=MeeplePlace(place_type=road),
         left=MeeplePlace(place_type=road),
         right=MeeplePlace(place_type=road),
         bottom=MeeplePlace(place_type=road),
         connections={top: [],
                      top_road_left: [left_road_right],
                      top_road_right: [right_road_left],
                      left: [],
                      left_road_left: [bottom_road_right],
                      left_road_right: [top_road_left],
                      right: [],
                      right_road_left: [top_road_right],
                      right_road_right: [bottom_road_left],
                      bottom: [],
                      bottom_road_left: [right_road_right],
                      bottom_road_right: [left_road_left]}),
]

numbers: list[int] = [
    2,
    4,
    1,
    3,
    5,
    2,
    1,
    3,
    2,
    3,
    3,
    3,
    2,
    3,
    2,
    3,
    1,
    3,
    2,
    1,
    8,
    9,
    4,
    1
]

stack: list[list[Tile, ImageTk.PhotoImage]] = []

for i, num in enumerate(numbers):
    for _ in range(num):
        stack.append([tiles[i], None])


def imaging(width: int, cards=None, turn=0):
    if cards is None:
        cards = range(sum(numbers))
    
    for c in cards:
        l = stack[c][tile].letter
        opened = Image.open(f"assets/{l}.png").resize((width, width)).rotate(turn)
        tkimage = ImageTk.PhotoImage(image=opened)
        stack[c][image] = tkimage

from tkinter import *
from data import *
from random import randrange


class App(Tk):
    placed_cards: dict[tuple[int, int]: int] = {}
    image_width: int = 120
    offset = image_width / 2
    camx, camy = (offset + image_width, offset + image_width)
    mousex, mousey = (0, 0)
    mouse_down = False
    
    current_tile_index: int = 1
    current_tile: Tile = stack[0][tile]
    current_tile_turns: int = 0
    
    def __init__(self):
        super().__init__()
        
        imaging(self.image_width)
        
        # creating widgets
        self.canvas = Canvas(bg="white")
        self.current_tile_canvas = Canvas(width=160, height=160, bg="white")
        self.turn_button = Button(text="turn", command=lambda: self.turn())
        
        # bindings
        self.canvas.bind("<B1-Motion>", lambda e: self.swipe_start())
        self.canvas.bind("<ButtonRelease-1>", lambda e: self.swipe_end(e))
        self.canvas.bind("<MouseWheel>", lambda e: self.scroll(e))
        
        # packing widgets
        self.canvas.pack(expand=True, fill=BOTH)
        self.current_tile_canvas.pack(side=LEFT)
        self.turn_button.pack(side=RIGHT)
        
        self.loop()
    
    def swipe_start(self):
        self.mouse_down = True
    
    def swipe_end(self, e):
        if not self.mouse_down:
            self.click(e.x, e.y)
        self.mouse_down = False
    
    def scroll(self, e):
        self.image_width += e.delta // 30
        if self.image_width > 160:
            self.image_width = 160
        elif self.image_width < 10:
            self.image_width = 10
        imaging(self.image_width)
    
    def click(self, x, y):
        zero_x1 = self.camx - (self.camx % self.image_width)
        zero_y1 = self.camy - (self.camy % self.image_width)
        mouse_x1 = x - (x % self.image_width)
        mouse_y1 = y - (y % self.image_width)
        x_tile = (mouse_x1 - zero_x1) / self.image_width
        y_tile = (zero_y1 - mouse_y1) / self.image_width
        if self.validate(self.current_tile_index, self.current_tile, x_tile, y_tile):
            self.add(self.current_tile_index, x_tile, y_tile)
            self.next_tile()
    
    def validate(self, i, t, x, y):
        conditions = []
        empties = 0
        
        try:
            top_tile = stack[self.placed_cards[(x, y + 1)]][tile]
        except KeyError:
            empties += 1
        else:
            conditions.append(t.top == top_tile.bottom)
        try:
            left_tile = stack[self.placed_cards[(x - 1, y)]][tile]
        except KeyError:
            empties += 1
        else:
            conditions.append(t.right == left_tile.left)
        try:
            right_tile = stack[self.placed_cards[(x + 1, y)]][tile]
        except KeyError:
            empties += 1
        else:
            conditions.append(t.left == right_tile.right)
        try:
            bottom_tile = stack[self.placed_cards[(x, y - 1)]][tile]
        except KeyError:
            empties += 1
        else:
            conditions.append(t.bottom == bottom_tile.top)
        
        if (x, y) not in self.placed_cards.keys() and i not in self.placed_cards.values():
            return False not in conditions and empties < 4
        else:
            return False
        
    def next_tile(self):
        for i in range(1, len(stack)):
            if self.current_tile_index + i in self.placed_cards.values():
                self.current_tile_index += i
                break
        else:
            pass
    
    def turn(self):
        self.current_tile_turns += 90
        stack[self.current_tile_index][tile].turn()
        imaging(width=self.image_width, cards=[self.current_tile_index], turn=self.current_tile_turns)
    
    def add(self, i, x, y):
        self.placed_cards[(int(x), int(y))] = i
        print(*self.placed_cards.items(), "\n", sep="\n")
    
    def draw_img(self, i, x, y):
        self.canvas.create_image(x * self.image_width + self.camx, -y * self.image_width + self.camy, image=stack[i][image])
    
    def draw_cards(self):
        self.canvas.delete("all")
        for c, i in self.placed_cards.items():
            self.draw_img(i, *c)
    
    def loop(self):
        if self.mouse_down:
            self.camx += self.winfo_pointerx() - self.mousex
            self.camy += self.winfo_pointery() - self.mousey
        
        self.draw_cards()
        
        self.current_tile = stack[self.current_tile_index][tile]
        self.current_tile_canvas.create_image(80, 80, image=stack[self.current_tile_index][image])
        
        self.mousex, self.mousey = self.winfo_pointerxy()
        self.after(10, lambda: self.loop())

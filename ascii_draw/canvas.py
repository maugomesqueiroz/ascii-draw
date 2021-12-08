import os

from .utils import Colors

class Canvas:

    def __init__(self, size:tuple):
        self.size = size
        self.frame = None


    def render_canvas(self, fill=' ', border='-'):
        # Creates the different lines and rows
        height, width = self.size
        self.frame = [ 
            [fill for _ in range(width)] for _ in range(height)
        ]

        if border:
            horizontal_border = [border for _ in range(width)]
            vertical_border_char = '|'
            self.frame[0] = horizontal_border
            self.frame[-1] = horizontal_border
            for i in range(height):
                self.frame[i][0] =  vertical_border_char
                self.frame[i][-1] = vertical_border_char 


    def render_point(self, y, x,char='X',color=None):
        char_str= f'{color}{char}{Colors.reset}' if color else char
        try:
            self.frame[y][x] = char_str
        except:
            # Out of bounds
            pass


    def update_screen(self):
        self.clear_console()
        print('') #new line
        for row in self.frame:
            for item in row:
                print(item, end='')
            print('') #new line


    @staticmethod
    def clear_console() -> None:
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)


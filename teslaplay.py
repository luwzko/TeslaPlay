from unicurses import *
import random
# teslaplay imports
from classes.settings import Settings
from classes.game import Game
from classes.misc import Misc

class TeslaPlay:
    def __init__(self):
        # curses init
        stdscr = initscr(); noecho(); start_color(); curs_set(0)
        self.y, self.x = getmaxyx(stdscr)
        # settings and games setup and misc
        self.settings = Settings("settings.yaml")
        self.games = [ Game(g[0], g[1][0], g[1][1], g[1][2]) for g in self.settings.get_games() ]
        self.miscellaneous = Misc()
        # colors
        init_color(20, 0, 600, 1000); init_pair(10, 20, COLOR_BLACK) # banner color - lightblue
        #star colors
        init_pair(1, COLOR_RED, COLOR_BLACK)
        init_pair(2, COLOR_GREEN, COLOR_BLACK)
        init_pair(3, COLOR_YELLOW, COLOR_BLACK)
        init_pair(4, COLOR_BLUE, COLOR_BLACK)
        init_pair(5, COLOR_MAGENTA, COLOR_BLACK)
        init_pair(6, COLOR_CYAN, COLOR_BLACK)
        # menu
        self.choices, self.n_choices = ["Play", "Library", "Settings", "About"], 4
        self.highlight, self.choice = 0, 1
        # setup windows in curses
        self.win_menu = newwin(self.y, self.x, 0, 0)
        self.win_banner = newwin(11, 100, 1, (self.x-98)//2)
        self.win_content = newwin(12, 100, 11, (self.x-98)//2 - 1)
        # window star
        self.win_star_l = newwin(self.y - 2, (self.x-98)//2 - 1, 1, 1)
        self.win_star_r = newwin(self.y - 2, (self.x-98)//2 - 1, 1, (self.x+98)//2)
        # list of windows
        self.windows = [self.win_menu, self.win_banner, self.win_content, self.win_star_l, self.win_star_r]
        # window xy
        self.content_y, self.content_x = getmaxyx(self.win_content)
        self.l_star_y, self.l_star_x = getmaxyx(self.win_star_l)
        self.r_star_y, self.r_star_x = getmaxyx(self.win_star_r)
        #borders
        box(self.win_menu)
        # title
        mvwaddstr(self.win_banner, 0, 0, self.miscellaneous.banner, color_pair(10))
        # keypad
        keypad(self.win_menu, True)
    
    def menu(self):
        # display stars
        _x = self.x // 2 - 1
        _y = self.y // 2
        # show selected game
        mvwaddstr(self.win_menu, _y, _x + 4, f": {self.choice}")
        # menu highlight
        for i in range(0, self.n_choices):
            
            if (self.highlight == i):
                wattron(self.win_menu, A_REVERSE)
                mvwaddstr(self.win_menu, _y, _x, self.choices[i])
                wattroff(self.win_menu, A_REVERSE)
            else:
                mvwaddstr(self.win_menu, _y, _x, self.choices[i])
            _y += 1
        # refresh all windows
        [wrefresh(scr) for scr in self.windows]

    def display_stars(self):
        for l in range(75):
            _x = random.randint(0, self.l_star_x)
            _y = random.randint(0, self.l_star_y)
            _clr = random.randint(1, 7)
            mvwaddstr(self.win_star_l, _y, _x, self.miscellaneous.star, color_pair(_clr))

        for r in range(75):
            _x = random.randint(0, self.r_star_x)
            _y = random.randint(0, self.r_star_y)
            _clr = random.randint(1, 7)
            mvwaddstr(self.win_star_r, _y, _x, self.miscellaneous.star, color_pair(_clr))

    def play(self):
        # run selected game
        self.games[self.choice - 1].run()

    def library(self):
        #title
        mvwaddstr(self.win_content, 1, self.content_x//2 - 4, "Library")
        box(self.win_content)
        #game display
        games = self.settings.get_content()
        for game, y in zip(self.games, range(3, len(self.games) + 3)):
            mvwaddstr(self.win_content, y, 2, f"{game.id}. {game.game_name} : {game.description}")

    def setts(self):
        #title
        mvwaddstr(self.win_content, 1, self.content_x//2 - 4, "Settings")
        box(self.win_content)
        #content
        for string, _y in zip(self.miscellaneous.setts_menu, range(3, len(self.miscellaneous.setts_menu) + 3)):
            mvwaddstr(self.win_content, _y, 2, string)

    def about(self):
        #title
        mvwaddstr(self.win_content, 1, self.content_x//2 - 4, "About")
        box(self.win_content)
        #content
        for string, _y in zip(self.miscellaneous.about_menu, range(3, len(self.miscellaneous.about_menu) + 3)):
            mvwaddstr(self.win_content, _y, 2, string)

    # main loop
    def main(self) -> None:
        self.display_stars()
        while True:
            self.menu()
            c = wgetch(self.win_menu)

            # handles for arrow keys
            if c == KEY_UP and self.highlight > 0:
                self.highlight -= 1 
            elif c == KEY_DOWN and self.highlight < (self.n_choices - 1):
                self.highlight += 1

            if c == KEY_LEFT and self.choice > 1:
                self.choice -= 1
            elif c == KEY_RIGHT and self.choice < len(self.games):
                self.choice += 1

            # handle for enter key
            if c == 10:
                wclear(self.win_content)
                if self.highlight == 0:
                    self.play()
                    # show play
                elif self.highlight == 1:
                    self.library()
                    # show library
                elif self.highlight == 2:
                    self.setts()
                    # show settings
                elif self.highlight == 3:
                    self.about()
                    # show about
    # destructor
    def __del__(self):
        endwin()

if __name__ == "__main__":
    # run TeslaPlay
    teslaplay = TeslaPlay()
    teslaplay.main()

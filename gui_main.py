from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from board import Board
from searches import a_star_search, greedy_search, bfs, bfs2
from functools import partial
from timeit import default_timer as timer
from threading import Thread


class TestApp(App):
    board = Board()
    a_star_id = 'A Star'
    greedy_id = 'Greedy'
    breadth_first_id = 'Breadth First'
    tile_1 = None
    tile_2 = None
    tile_3 = None
    tile_4 = None
    tile_5 = None
    tile_6 = None
    tile_7 = None
    tile_8 = None
    tile_0 = None
    generate_random_button = None
    solve_button = None
    a_star_button = None
    greedy_button = None
    breadth_first_button = None
    current_solver_id = a_star_id
    selected_color = [0, .5, 0, 1]
    unselected_color = [0, 1, 0, 1]
    seconds_between_moves = .25
    solver_thread = None
    animation_frames = []

    def select_search(self, instance):
        self.a_star_button.background_color = self.unselected_color
        self.greedy_button.background_color = self.unselected_color
        self.breadth_first_button.background_color = self.unselected_color
        if instance.text == self.a_star_id:
            self.a_star_button.background_color = self.selected_color
            self.current_solver_id = self.a_star_id
        elif instance.text == self.greedy_id:
            self.greedy_button.background_color = self.selected_color
            self.current_solver_id = self.greedy_id
        elif instance.text == self.breadth_first_id:
            self.breadth_first_button.background_color = self.selected_color
            self.current_solver_id = self.breadth_first_id

    def generate_random(self, instance):
        if self.solver_thread and self.solver_thread.is_alive():
            print("Can't. Still solving.")
            return
        while len(self.animation_frames) != 0:
            self.animation_frames.pop().cancel()
        self.animation_frames = []
        self.board.scramble()
        self.reposition_tiles(self.board.get_current_state())

    def start_solver_thread(self, instance):
        if self.solver_thread and self.solver_thread.is_alive():
            print("Can't. Still solving.")
            return
        self.solver_thread = Thread(target=self.solver)
        self.solver_thread.daemon = True
        self.solver_thread.start()

    def solver(self):
        while len(self.animation_frames) != 0:
            self.animation_frames.pop().cancel()
        self.animation_frames = []
        print("Solving with {0}".format(self.current_solver_id))
        if self.current_solver_id == self.a_star_id:
            solver = a_star_search
        elif self.current_solver_id == self.greedy_id:
            solver = greedy_search
        elif self.current_solver_id == self.breadth_first_id:
            solver = bfs2
        else:
            return
        start = timer()
        steps = solver(self.board)
        time = timer()-start
        print("Done in {0} seconds".format(time))
        print("Move count: {0}".format(len(steps)))
        self.board = steps[-1]
        if len(steps) != 0:
            steps.pop(0)
        for i in range(len(steps)):
            self.animation_frames.append(
                Clock.schedule_once(
                    partial(lambda a, b: self.reposition_tiles(a), steps[i].get_current_state()),
                    self.seconds_between_moves + i*self.seconds_between_moves))

    def reposition_tiles(self, board):
        for y in range(3):
            for x in range(3):
                self.move_tile(board[y][x], x, y)

    def move_tile(self, value, x, y):
        tile_to_move = None
        if value == 1:
            tile_to_move = self.tile_1
        elif value == 2:
            tile_to_move = self.tile_2
        elif value == 3:
            tile_to_move = self.tile_3
        elif value == 4:
            tile_to_move = self.tile_4
        elif value == 5:
            tile_to_move = self.tile_5
        elif value == 6:
            tile_to_move = self.tile_6
        elif value == 7:
            tile_to_move = self.tile_7
        elif value == 8:
            tile_to_move = self.tile_8
        elif value == 0:
            tile_to_move = self.tile_0
        tile_to_move.pos_hint = {'x': x*1/3, 'top': 1-(1/3*y)}

    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        main_layout = GridLayout(rows=2)
        board_layout = FloatLayout(size_hint=(1, .9))
        self.tile_1 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 0, 'top': 1}, text='1', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_2 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 1 / 3, 'top': 1}, text='2', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_3 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 2 / 3, 'top': 1}, text='3', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_4 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 0, 'top': 2 / 3}, text='4', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_5 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 1 / 3, 'top': 2 / 3}, text='5', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_6 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 2 / 3, 'top': 2 / 3}, text='6', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_7 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 0, 'top': 1 / 3}, text='7', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_8 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 1 / 3, 'top': 1 / 3}, text='8', background_color=[1, 0, 0, 1], font_size=24)
        self.tile_0 = Button(size_hint=(1 / 3, 1 / 3), pos_hint={'x': 2 / 3, 'top': 1 / 3}, text='', background_color=[0, 0, 0, 0], font_size=24)
        board_layout.add_widget(self.tile_1)
        board_layout.add_widget(self.tile_2)
        board_layout.add_widget(self.tile_3)
        board_layout.add_widget(self.tile_4)
        board_layout.add_widget(self.tile_5)
        board_layout.add_widget(self.tile_6)
        board_layout.add_widget(self.tile_7)
        board_layout.add_widget(self.tile_8)
        board_layout.add_widget(self.tile_0)
        controls_layout = GridLayout(cols=3, size_hint=(1, .1))
        self.generate_random_button = Button(text='Generate Random', background_color=[1, 0, 1, 1], on_press=self.generate_random)
        self.solve_button = Button(text='Solve', background_color=[1, 0, 1, 1], on_press=self.start_solver_thread)
        search_type_layout = GridLayout(rows=3)
        self.a_star_button = Button(text=self.a_star_id, background_color=self.selected_color, on_press=self.select_search)
        self.greedy_button = Button(text=self.greedy_id, background_color=self.unselected_color, on_press=self.select_search)
        self.breadth_first_button = Button(text=self.breadth_first_id, background_color=self.unselected_color, on_press=self.select_search)
        search_type_layout.add_widget(self.a_star_button)
        search_type_layout.add_widget(self.greedy_button)
        search_type_layout.add_widget(self.breadth_first_button)
        controls_layout.add_widget(self.generate_random_button)
        controls_layout.add_widget(self.solve_button)
        controls_layout.add_widget(search_type_layout)
        main_layout.add_widget(board_layout)
        main_layout.add_widget(controls_layout)
        return main_layout


if __name__ == '__main__':
    print("Starting 8 puzzle solver GUI...")
    TestApp().run()

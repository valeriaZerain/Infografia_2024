import arcade
import numpy as np
from game_object import Object3D

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Fox projection"

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.fox_vertices = [
            (0, 1, 0),
            (0.5, 0.5, 1),
            (-0.5, 0.5, 1),
            (0.5, -0.5, 1),
            (-0.5, -0.5, 1),
            (0, 0.5, 1.5),
            (0, 0.8, 1.2),
            (0.4, 0.5, 1.5),
            (-0.4, 0.5, 1.5),
            (0, -0.5, -0.5),
            (0.5, -0.8, 0),
            (-0.5, -0.8, 0)
        ]

        self.fox_edges = [
            (0, 1), (0, 2), (1, 3), (2, 4),
            (3, 4), (1, 5), (2, 5),
            (5, 6), (6, 7), (6, 8),
            (1, 7), (2, 8),
            (4, 9), (3, 9),
            (9, 10), (9, 11),
            (10, 11)
        ]

        self.fox = Object3D(
            self.fox_vertices,
            self.fox_edges,
            arcade.color.ORANGE
        )

        self.fox.translate(399, 399, 399)
        self.fox.scale(100,100,100)

    def on_mouse_motion(self, x, y, dx, dy):
        nose_pos = np.array(self.fox.vertices[3])[:2]
        target_pos = np.array([x, y])

        direction = nose_pos - target_pos
        angle = np.arctan2(direction[1], direction[0])

        self.fox = Object3D(
            self.fox_vertices,
            self.fox_edges,
            arcade.color.ORANGE
        )
        self.fox.translate(399,399, 399)
        self.fox.scale(100, 100, 100)

        self.fox.rotate(angle, "x")
        self.fox.rotate(angle, "y")
        self.fox.rotate(angle, "z")

    def on_draw(self):
        arcade.start_render()
        self.fox.draw()

if __name__ == "__main__":
    app = App()
    arcade.run()
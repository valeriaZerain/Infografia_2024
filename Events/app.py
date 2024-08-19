import random

import arcade
from game_object import Polygon2D, Tank

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Polygon2d"
SPEED = 50
ANGULAR_SPEED = 1.5

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.objects = []
        self.tank = Tank(400,400,arcade.color.ARMY_GREEN)
        self.objects.append(self.tank)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank.speed = -SPEED
        if symbol == arcade.key.RIGHT:
            self.tank.angular_speed = ANGULAR_SPEED
        if symbol == arcade.key.LEFT:
            self.tank.angular_speed = -ANGULAR_SPEED
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.tank.shoot(100)

        # if button == arcade.MOUSE_BUTTON_LEFT:
        #     self.objects.append(
        #         Polygon2D(
        #             vertices=[
        #                 (x - 50, y - 50),
        #                 (x - 50, y + 50),
        #                 (x + 50, y + 50),
        #                 (x + 50, y - 50),
        #             ],
        #             color=self.get_random_color()
        #         )
        #     )
        #     print(f"objetos: {len(self.objects)}")
    def on_update(self, delta_time: float):
        self.tank.update(delta_time)
    def on_key_release(self, symbol: int, modifiers: int):
        # if symbol == arcade.key.C:
        #     self.objects.append(
        #         Polygon2D(
        #             vertices=[
        #                 (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50),
        #                 (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50),
        #                 (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 + 50),
        #                 (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50),
        #             ],
        #             color=arcade.color.ANDROID_GREEN
        #         )
        #     )
        #     print(f"objetos: {len(self.objects)}")
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.tank.angular_speed = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.tank.speed = 0

    def on_draw(self):
        arcade.start_render()
        for obj in self.objects:
            obj.draw()

    def get_random_color(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
            )


if __name__ == "__main__":
    app = App()
    arcade.run()
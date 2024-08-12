import arcade
from circle import get_circle
from bresenham import get_line
import math

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Circulos con bresenham"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 5
        #Circulo
        self.xc = 80
        self.yc = 20
        self.r = 20
        self.circle_color = arcade.color.RED_DEVIL
        #Rectangulo
        self.xr = 80
        self.yr = 80
        self.wr = 20
        self.hr = 30
        self.rectangle_color = arcade.color.AQUAMARINE
        #Triangulo
        self.xt = 80
        self.yt = 111
        self.wt = 20
        self.ht = 15
        self.triangle_color = arcade.color.GOLD
        #Pentagono
        self. yp = 90
        self.rp = 5
        self.pentagon_color = arcade.color.RED_ORANGE

        self.speed = 25
        self.velocity = [self.speed, self.speed]

    def on_update(self, delta_time: float):
        self.xc += delta_time * self.velocity[0]
        self.yc += delta_time * self.velocity[1]

        # Logica del rebote en X
        if (self.xc + self.r > SCREEN_WIDTH // self.pixel_size
            or self.xc - self.r < 0):
            self.velocity[0] = -1 * self.velocity[0]

        # Logica del rebote en Y
        if (self.yc + self.r > SCREEN_HEIGHT // self.pixel_size
            or self.yc - self.r < 0):
            self.velocity[1] = -1 * self.velocity[1]

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_rectangle(self.xr, self.yr, self.wr, self.hr, self.rectangle_color)
        self.draw_triangle(self.xt, self.yt, self.wt, self.ht,self.triangle_color)
        self.draw_rectangle(86, 80, 8,10, arcade.color.COFFEE)
        self.draw_pentagon(60, self.yp, self.rp, self.pentagon_color)
        self.draw_pentagon(73, self.yp, self.rp, self.pentagon_color)
        self.draw_pentagon(110, self.yp, self.rp, self.pentagon_color)
        self.draw_pentagon(125, self.yp, self.rp, self.pentagon_color)
        self.draw_pentagon(90, 100, 4, arcade.color.BLUE)
        self.draw_scaled_circle(60, 90, 2, arcade.color.YELLOW)
        self.draw_scaled_circle(73, 90, 2, arcade.color.YELLOW)
        self.draw_scaled_circle(110, 90, 2, arcade.color.YELLOW)
        self.draw_scaled_circle(125, 90, 2, arcade.color.YELLOW)
        self.draw_rectangle(59, 80, 1, 5, arcade.color.GREEN)
        self.draw_rectangle(72, 80, 1, 5, arcade.color.GREEN)
        self.draw_rectangle(109, 80, 1, 5, arcade.color.GREEN)
        self.draw_rectangle(124, 80, 1, 5, arcade.color.GREEN)
    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2,
                0,
                v_l + self.pixel_size / 2,
                SCREEN_HEIGHT,
                [20, 20, 20]
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0,
                h_l + self.pixel_size / 2,
                SCREEN_WIDTH,
                h_l + self.pixel_size / 2,
                [20, 20, 20]
            )

    def draw_circle_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_circle(self, xc, yc, r, color):
        arcade.draw_circle_outline(
            xc * self.pixel_size,
            yc * self.pixel_size,
            r * self.pixel_size,
            color,
            5
        )

    def draw_rectangle(self, x, y, w, h, color):
        points1 = get_line(x,y,x+w,y)
        self.draw_line_points(points1,color)
        points2 = get_line(x,y,x,y+h)
        self.draw_line_points(points2, color)
        points3 = get_line(x, y+h, x+w, y+h)
        self.draw_line_points(points3, color)
        points4 = get_line(x+w, y, x+w, y+h)
        self.draw_line_points(points4, color)

    def draw_line_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_triangle(self, x, y, w, h,color):
        points1 = get_line(x, y, x+w ,y)
        self.draw_line_points(points1, color)
        points2 = get_line(x,y,x+(w/2),y+h)
        self.draw_line_points(points2, color)
        points3 = get_line(x+(w/2),y+h, x+w, y)
        self.draw_line_points(points3, color)

    def draw_pentagon(self, x, y, r, color):
        vertices = []
        for i in range(5):
            angle = math.radians(72 * i)
            vx = x + int(r * math.cos(angle))
            vy = y + int(r * math.sin(angle))
            vertices.append((vx, vy))

        # Dibujar las líneas entre los vértices
        for i in range(5):
            next_index = (i + 1) % 5
            points = get_line(vertices[i][0], vertices[i][1], vertices[next_index][0], vertices[next_index][1])
            self.draw_line_points(points, color)

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
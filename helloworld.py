from manim import *


class HelloWorld(Scene):
    def construct(self):
        hello = MathTex(r"\text{Hello World!}")
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        square = Square(side_length=2.0, color=BLUE, fill_color=TEAL, fill_opacity=0.5)
        welcome = MathTex(r"\text{Welcome to MAA SE 2024!}")

        self.play(Write(hello))
        self.wait(5)
        self.play(Transform(hello, circle))
        self.wait(3)
        self.play(Transform(hello, square))
        self.wait(3)
        self.play(Transform(hello, welcome))
        self.wait(5)




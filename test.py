from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class EquationAndGraphics(Scene):
    def construct(self):
        # Create the equation
        equation = MathTex("e^{i\\pi} + 1 = 0")
        equation.to_edge(LEFT)
        # Create the 3D graphics
        graphics = Sphere()
        graphics.set_fill(BLUE, opacity=0.5)
        graphics.next_to(equation, RIGHT)
        # Animate the equation and graphics simultaneously
        self.play(
            Write(equation),
            Create(graphics)
        )
        self.wait()

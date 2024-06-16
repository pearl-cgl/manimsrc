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

class Equivariance(ThreeDScene):
    def construct(self):
        resolution_fa = 8
        self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
        def param_surface(u, v):
            x = u
            y = v
            z = 0.1 * np.sin(x) * np.cos(y)
            return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5],
        )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)

        background_tangent = Surface(
            lambda u, v: axes.c2p(u, v,
                0.1 * np.cos(3) * np.cos(3) * (u - 3) - 0.1 * np.sin(3) * np.sin(3) * (v - 3) + .1),
            resolution=(resolution_fa, resolution_fa),
            v_range=[2, 4],
            u_range=[2, 4],
            fill_opacity=.5,
            fill_color=BLUE,
        )
        self.add(surface_plane, background_tangent)
        self.wait(3)

# Z := (\f \x f (\v x x v)) (\f \x f (\v x x v))
# (Lf. Lx. f (Lv. x x v)) (Lf. Lx. f (Lv. x x v)) https://lambster.dev/
# when compared to Y (the narcissistic bird as defined by Smullyan),
# the Z has one more abstraction after the first lambda f,
# effectively blocking further reduction unless additional term is applied
# which allows the Z to be used in eager evaluation languages,
# such as JavaScript, Python, etc.
# and thus it's called the "Secretly Narcissistic Bird", the bird
# that only replies itself when asked,
# well, also the "Politely Narcissistic Bird" if you will)
# TODO polyvariadic Y
class SecretlyNarcissisticBird(Scene):
    def construct(self):
        # Add title
        title = Text("Secretly Narcissistic Bird", font_size=48)
        title.to_corner(UL)
        text = Text("""\
notes for editing:

Z := (\\f \\x f (\\v x x v)) (\\f \\x f (\\v x x v))

when compared to Y (the narcissistic bird as defined by Smullyan),
the Z has one more abstraction after the first lambda f,
effectively blocking further reduction unless additional term is applied
which allows the Z to be used in eager evaluation languages,
such as JavaScript, Python, etc.
and thus it's called the "Secretly Narcissistic Bird", the bird
that only replies itself when asked,
well, also the "Politely Narcissistic Bird" if you will)\
                    """, font="Noto Sans", font_size=12)
        text.to_edge(DOWN)
        self.add(title)
        
        # TODO dalle secretly narcissistic bird, trace to vector
        bird = SVGMobject("bird.svg")
        bird.set_fill(YELLOW, opacity=0.8)
        bird.scale(1)
        bird.to_corner(DR)
        self.play(Create(bird), Write(text), run_time=3)
        self.wait()
        
        variables = VGroup(MathTex("f"), MathTex("x_1"), MathTex("x_2"), MathTex("y")).arrange_submobjects().shift(UP)

        eq1 = MathTex("(", "\\lambda {{f}}.",   "(",  "\\lambda {{x_1}}.", "((", "{{f}} {{f}})", ")(", "\\lambda {{x_2}}.", "((", "{{x_1}} {{x_1}}", ")", "{{x_2}}", "))))))",
                      "(\\lambda {{x_0}}. {{x_0}})")
        eq2 = MathTex("(", "\\lambda {{x_1}}.", "((", "\\lambda {{x_1}}.", "",   "{{x_1}}",      "(",  "\\lambda {{x_2}}.", "((", "{{x_1}} {{x_1}}", ")", "{{x_2}}", "))))")

        self.add(eq1)
        self.wait(3)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2)) # FIXME https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html
        self.wait(3)

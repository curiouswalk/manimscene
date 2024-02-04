# Cycloid
A cycloid is a mathematical curve traced by a point on the circumference of a circle as it rolls along a straight line. A curtate cycloid, also known as a contracted cycloid, is traced by a point at a radius smaller than the radius of the rolling circle. On the other hand, a prolate cycloid, also known as an extended cycloid, is traced by a point at a radius greater than the radius of the rolling circle. Cycloids have significant applications in various fields, including mathematics, physics, and engineering.

https://github.com/curiouswalk/manim/assets/157306209/a82826b4-18e0-4bc0-a450-a4ddde7190ae

>[!TIP]
> This project is done in Jupyter Notebook on Google Colab.
>
> <a href="https://colab.research.google.com/github/curiouswalk/manim/blob/main/source/cycloid/cycloid.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Scene Script

```python
from manim import *

config.disable_caching = True

class Cycloid(Scene):

    def construct(self):

        frame_width = config.frame_width

        length = frame_width * 0.8

        numline = NumberLine(
            x_range=[-TAU, TAU, PI], length=length, color="#a3aea7"
        ).to_edge(DOWN, buff=1.5)

        circle = Circle(radius=length / (TAU * 2), color="#00ffff").next_to(
            numline.get_start(), UP, buff=0.25
        )

        cc = Dot(color=circle.color).move_to(circle)

        p = Dot(radius=0.1, color=circle.color).move_to(circle)

        line = Line(cc, p, color="#a3aea7", stroke_opacity=[0.25, 1, 0.25])

        lp = VGroup(line, p)

        trail = TracedPath(
            cc.get_center, dissipating_time=0.2, stroke_color=cc.color, stroke_width=4
        )
        cix = circle.get_x()

        cr = circle.radius

        pr = ValueTracker(0.0)

        cycloids = VGroup()

        def update_function(m):

            angle = PI / 2 - (circle.get_x() - cix) / cr

            pos = (
                circle.get_center()
                + np.array([np.cos(angle), np.sin(angle), 0.0]) * pr.get_value()
            )
            m[0].put_start_and_end_on(circle.get_center(), pos)

            m[1].move_to(pos)

        def play_animation(txt, radius, color):
            text = Tex(txt).scale(1.25).to_edge(UP, buff=0.75)

            self.play(
                pr.animate.set_value(radius),
                FadeIn(text),
                p.animate.set_color(color),
                run_time=1.5,
            )

            self.wait(1)

            path = TracedPath(p.get_center, stroke_color=p.color, stroke_width=5)

            self.add(path)

            trail.set_stroke(opacity=[1, 0])

            self.play(
                circle.animate(run_time=2.5, rate_func=linear).shift(RIGHT * length)
            )

            self.wait(2)

            path.clear_updaters()

            cycloids.add(path.copy())

            trail.set_stroke(opacity=[0, 1])
            self.play(
                circle.animate(rate_func=linear, run_time=2.5).shift(LEFT * length)
            )
            self.wait(1)
            self.play(FadeOut(path), FadeOut(text), run_time=1.5)

            self.wait(0.5)

        self.wait(0.25)

        self.play(
            Create(numline, lag_ratio=0),
            Create(circle),
            FadeIn(lp, cc, scale=0),
            run_time=1.5,
        )

        self.wait(1)

        self.add(trail)
        circle.add(cc)

        lp.add_updater(update_function)

        play_animation(txt="Cycloid", radius=cr, color="#ffff00")

        play_animation(txt="Prolate Cycloid", radius=cr * 1.5, color="#ff0000")

        play_animation(txt="Curtate Cycloid", radius=cr * 0.5, color="#0000ff")

        self.wait(0.5)

        self.play(pr.animate.set_value(0.0), p.animate.set_color(circle.color))

        VGroup(trail, lp).clear_updaters()
        circle.remove(cc)

        self.wait(0.5)

        self.play(
            Uncreate(circle),
            FadeOut(cc, lp, scale=0),
            Uncreate(numline, lag_ratio=0),
            run_time=1.5,
        )

        cycloids.scale_to_fit_width(frame_width).set_stroke(opacity=[0, 1, 0]).center()

        self.wait(1)

        self.play(Create(cycloids, lag_ratio=0, rate_func=linear, run_time=2.5))

        self.wait(2)

        self.play(Uncreate(cycloids, lag_ratio=0, rate_func=linear, run_time=2.5))

        self.wait(0.25)

```

# Cycloid
A cycloid is a mathematical curve traced by a point on the circumference of a circle as it rolls along a straight line. A curtate cycloid, also known as a contracted cycloid, is traced by a point at a radius smaller than the radius of the rolling circle. On the other hand, a prolate cycloid, also known as an extended cycloid, is traced by a point at a radius greater than the radius of the rolling circle. Cycloids have significant applications in various fields, including mathematics, physics, and engineering.

https://github.com/user-attachments/assets/be572ccc-be52-4768-9944-0cb2e362dc98

>[!TIP]
> This project is done in Jupyter Notebook on Google Colab.
>
> <a href="https://colab.research.google.com/github/curiouswalk/manim/blob/main/source/cycloid/cycloid.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Scripts

## Imports

```python
from manim import *
config.disable_caching = True
config.media_embed = True
```
## Initialization
Run this to get started.
```python
frame_width = config.frame_width

length = frame_width * 0.8

num_line = NumberLine(x_range=[-TAU, TAU, PI], length=length, color="#a3aea7").to_edge(
    DOWN, buff=2
)
circle_radius = length / (TAU * 2)

circle = Circle(radius=circle_radius, color="#00FFFB").next_to(
    num_line.get_start(), UP, buff=0.25
)
dashed_circle = DashedVMobject(circle)

dot = Dot(color=circle.color).move_to(circle)

point = Dot(radius=0.1, color=circle.color).move_to(circle)

line = Line(dot, point, color="#a3aea7", stroke_opacity=[0.25, 1, 0.25])

update_mob = VGroup(dashed_circle, line, point)

trail = TracedPath(
    dot.get_center, dissipating_time=0.15, stroke_color=dot.color, stroke_width=4
)
dot_x = dot.get_x()

radius = ValueTracker(0.0)

def updater_function(mob):

    angle = PI / 2 - (dot.get_x() - dot_x) / circle_radius

    pos = dot.get_center() + (
        np.cos(angle) * radius.get_value(),
        np.sin(angle) * radius.get_value(),
        0.0,
    )
    mob[0].move_to(dot.get_center())

    mob[1].become(
        Line(dot.get_center(), pos, color="#a3aea7", stroke_opacity=[0.25, 1, 0.25])
    )
    mob[2].move_to(pos)


mobjects = VGroup(update_mob, num_line, trail, dot)

def anim_point_radius(self, r, color=circle.color, anim=None, rt=1.5):
    update_mob.add_updater(updater_function)
    anim_list = [
        radius.animate.set_value(r * circle_radius),
        point.animate.set_color(color),
    ]
    if anim:
        anim_list.append(anim)
    self.play(*anim_list, run_time=rt)

def anim_trace_path(self, rt=3):

    path_forward = TracedPath(
        point.get_center, stroke_color=point.color, stroke_width=6
    )
    self.add(path_forward)

    self.play(
        dot.animate.shift(RIGHT * length),
        Rotate(dashed_circle, -2 * TAU),
        run_time=rt,
        rate_func=linear,
    )
    self.wait(0.5)
    path_forward.clear_updaters()
    path_return = path_forward.copy()
    self.play(path_forward.animate(run_time=1.5).fade(2 / 3))
    path_forward.clear_updaters()
    self.wait(0.5)

    path_backward = TracedPath(
        point.get_center,
        dissipating_time=1 / 3,
        stroke_color=point.color,
        stroke_width=6,
    )
    self.add(path_backward)

    self.play(
        FadeOut(path_forward),
        dot.animate.shift(LEFT * length),
        Rotate(dashed_circle, 2 * TAU),
        rate_func=linear,
        run_time=rt,
    )
    self.wait(0.5)
    path_backward.clear_updaters()
    self.remove(path_backward)
    return path_return

```
## Animation Scenes

### Cycloid Scene
Learn more from **MathWorld** — A Wolfram Web Resource.\
[mathworld.wolfram.com/Cycloid.html](https://mathworld.wolfram.com/Cycloid.html)

https://github.com/user-attachments/assets/f09a9ff0-2023-4548-87e3-4358a6c4eb08

```python
%%manim CycloidScene

class CycloidScene(Scene):

    def construct(self):

        self.add(mobjects)

        txt = Text("Cycloid").to_edge(UP, buff=1)

        path_color = "#7B00FF"

        anim_point_radius(self, r=1, color=path_color, anim=Write(txt))

        self.wait()

        anim_trace_path(self)

        self.wait()

        anim_point_radius(self, r=-1, color=path_color)

        self.wait()

        anim_trace_path(self)

        self.wait()

        anim_point_radius(self, r=0, anim=Unwrite(txt))

        self.wait(0.5)
```

### Prolate Cycloid Scene
Learn more from **MathWorld** — A Wolfram Web Resource.\
[mathworld.wolfram.com/ProlateCycloid.html](https://mathworld.wolfram.com/ProlateCycloid.html)

https://github.com/user-attachments/assets/240ba4ab-e1a3-4df0-819d-259de08018e2

```python
%%manim ProlateCycloidScene

class ProlateCycloidScene(Scene):

    def construct(self):

        self.add(mobjects)

        txt = Text("Prolate Cycloid").to_edge(UP, buff=1)

        path_color = "#FF0004"

        anim_point_radius(self, r=1.75, color=path_color, anim=Write(txt))

        self.wait()

        anim_trace_path(self)

        self.wait()

        anim_point_radius(self, r=-2, color=path_color)

        self.wait()

        anim_trace_path(self)

        self.wait()

        anim_point_radius(self, r=0, anim=Unwrite(txt))

        self.wait(0.5)
```

### Curtate Cycloid Scene
Learn more from **MathWorld** — A Wolfram Web Resource.\
[mathworld.wolfram.com/CurtateCycloid.html](https://mathworld.wolfram.com/CurtateCycloid.html)

https://github.com/user-attachments/assets/bdc06918-dfda-4af3-9aaa-d7572bb6c7e3

```python
%%manim CurtateCycloidScene

class CurtateCycloidScene(Scene):

    def construct(self):

        self.add(mobjects)

        txt = Text("Curtate Cycloid").to_edge(UP, buff=1)

        path_color= "#84FF00"

        anim_point_radius(self, r=0.5, color=path_color, anim=Write(txt))

        self.wait()

        anim_trace_path(self)

        self.wait()

        anim_point_radius(self, r=-0.375, color=path_color)

        self.wait()

        anim_trace_path(self)

        self.wait()

        anim_point_radius(self, r=0, anim=Unwrite(txt))

        self.wait(0.5)
```

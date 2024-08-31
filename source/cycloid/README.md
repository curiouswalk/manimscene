# Cycloid

A cycloid is a mathematical curve traced by a point on the circumference of a circle as it rolls along a straight line. A prolate cycloid, also known as an extended cycloid, is traced by a point at a radius greater than the radius of the rolling circle. A curtate cycloid, also known as a contracted cycloid, is traced by a point at a radius smaller than the radius of the rolling circle. Cycloids have significant applications in various fields, including mathematics, physics, and engineering.

https://github.com/user-attachments/assets/994d9d55-bf86-4893-802f-79fd635cc27c

>[!TIP]
> This project is done in Jupyter Notebook on Google Colab.
>
> <a href="https://colab.research.google.com/github/curiouswalk/manimscene/blob/main/source/cycloid/cycloid.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height="23px" alt="Open In Colab"/></a>
>




# Animation Script

## Setup

[Installation Guide](https://docs.manim.community/en/stable/installation.html)

**Manim in Colab**<br>[`colab.curiouswalk.com/manim`](https://colab.curiouswalk.com/manim)

```python
from manim import *

config.disable_caching = True
config.verbosity = "WARNING"
config.media_embed = True
```

## Initialization

Run this code cell to begin, and rerun it if anything goes wrong.

```python
length = config.frame_width * 0.8

num_line = NumberLine(
    x_range=[-TAU, TAU, PI], length=length, color=ManimColor("#A8ABAE")
).to_edge(DOWN, buff=2)

circle_radius = length / (TAU * 2)

circle = Circle(radius=circle_radius, color=ManimColor("#199CE3")).next_to(
    num_line.get_start(), UP, buff=0.25
)
dashed_circle = DashedVMobject(circle)

dot = Dot(color=circle.color).move_to(circle)

point = Dot(radius=0.1, color=circle.color).move_to(circle)

line = Line(dot, point, color=circle.color)

update_mob = VGroup(dashed_circle, line, point)

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

    mob[1].set_points_by_ends(dot.get_center(), pos)

    mob[2].move_to(pos)

mobjects = VGroup(update_mob, num_line, dot)

def anim_point_radius(self, r=0, color=circle.color, anim=None, rt=1.5):

    update_mob.add_updater(updater_function)

    anim_list = [
        radius.animate.set_value(r * circle_radius),
        point.animate.set_color(color),
        line.animate.set_color(average_color(circle.color, color)),
    ]
    if anim:
        anim_list.append(anim)

    self.play(*anim_list, run_time=rt)

def anim_trace_path(self, rt=3):

    trail = TracedPath(
        dot.get_center,
        dissipating_time=rt * 0.06,
        stroke_color=dot.color,
        stroke_width=4,
    )
    path_forward = TracedPath(
        point.get_center, stroke_color=point.color, stroke_width=6
    )
    self.add(trail, path_forward)

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
    self.wait(0.5)

    path_backward = TracedPath(
        point.get_center,
        dissipating_time=rt * 0.25,
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
    self.wait()

    path_backward.clear_updaters()
    self.remove(trail, path_backward)

    return path_return

```

## Animation Scenes

### Cycloid Scene
Learn more from **MathWorld** — A Wolfram Web Resource.<br>
[mathworld.wolfram.com/Cycloid.html](https://mathworld.wolfram.com/Cycloid.html)

https://github.com/user-attachments/assets/1b12438e-b67f-4561-bc4e-a93ec978a675

```python
%%manim CycloidScene

class CycloidScene(Scene):

    def construct(self):

        self.add(mobjects)

        txt = Text("Cycloid").to_edge(UP, buff=1)

        path_color = ManimColor("#6019E3")

        anim_point_radius(self, r=1, color=path_color, anim=Write(txt))

        self.wait()

        anim_trace_path(self, rt=4)

        self.wait()

        anim_point_radius(self, r=-1, color=path_color)

        self.wait()

        anim_trace_path(self, rt=4)

        self.wait()

        anim_point_radius(self, r=0, anim=Unwrite(txt))

        self.wait(0.5)

```

### Prolate Cycloid Scene
Learn more from **MathWorld** — A Wolfram Web Resource.<br>
[mathworld.wolfram.com/ProlateCycloid.html](https://mathworld.wolfram.com/ProlateCycloid.html)

https://github.com/user-attachments/assets/1ef19a2a-993b-4c12-b0fe-7ecf763aa1a1

```python
%%manim ProlateCycloidScene

class ProlateCycloidScene(Scene):

    def construct(self):

        self.add(mobjects)

        txt = Text("Prolate Cycloid").to_edge(UP, buff=1)

        path_color = ManimColor("#E31937")

        anim_point_radius(self, r=1.75, color=path_color, anim=Write(txt))

        self.wait()

        anim_trace_path(self, rt=4)

        self.wait()

        anim_point_radius(self, r=-2, color=path_color)

        self.wait()

        anim_trace_path(self, rt=4)

        self.wait()

        anim_point_radius(self, r=0, anim=Unwrite(txt))

        self.wait(0.5)

```

### Curtate Cycloid Scene
Learn more from **MathWorld** — A Wolfram Web Resource.<br>
[mathworld.wolfram.com/CurtateCycloid.html](https://mathworld.wolfram.com/CurtateCycloid.html)

https://github.com/user-attachments/assets/30ca6ddb-ebda-4601-8499-0c2ba4726aa1

```python
%%manim CurtateCycloidScene

class CurtateCycloidScene(Scene):

    def construct(self):

        self.add(mobjects)

        txt = Text("Curtate Cycloid").to_edge(UP, buff=1)

        path_color= ManimColor("#19E360")

        anim_point_radius(self, r=0.5, color=path_color, anim=Write(txt))

        self.wait()

        anim_trace_path(self, rt=4)

        self.wait()

        anim_point_radius(self, r=-0.375, color=path_color)

        self.wait()

        anim_trace_path(self, rt=4)

        self.wait()

        anim_point_radius(self, r=0, anim=Unwrite(txt))

        self.wait(0.5)

```

## Cycloid Animation

Here is the complete animation. If anything goes wrong, please reinitialize (rerun initialization).

https://github.com/user-attachments/assets/2d960ae8-e16f-4a1a-9cdb-0cf163f4d4dd

```python
%%manim Cycloid

class Cycloid(Scene):

    def construct(self):

        vgroup = VGroup(VGroup(dashed_circle, point), num_line)

        vgroup_copy = vgroup.copy()

        vgroup.save_state()

        vgroup.arrange(DOWN, buff=1)

        self.play(
            Create(dashed_circle), GrowFromCenter(point), Create(num_line, lag_ratio=0)
        )

        self.wait(1.5)

        self.play(Restore(vgroup))

        self.add(mobjects)

        text = [
            Text(txt).to_edge(UP, buff=1)
            for txt in ("Cycloid", "Prolate Cycloid", "Curtate Cycloid")
        ]

        self.wait(0.5)

        anim_point_radius(self, r=1, color=ManimColor("#6019E3"), anim=Write(text[0]))

        self.wait(1.5)

        cycloid_path = anim_trace_path(self)

        self.wait()

        anim_point_radius(
            self, r=5/3, color=ManimColor("#E31937"), anim=ReplacementTransform(text[0], text[1])
        )

        self.wait(1.5)

        prolate_cycloid_path = anim_trace_path(self)

        self.wait()

        anim_point_radius(
            self, r=1/3, color=ManimColor("#19E360"), anim=ReplacementTransform(text[1], text[2])
        )
        self.wait(1.5)

        curtate_cycloid_path = anim_trace_path(self)

        self.wait()

        anim_point_radius(self, r=0, anim=Unwrite(text[2]))

        self.wait()

        self.remove(mobjects)

        self.add(vgroup_copy)

        dashed_circle_copy, point_copy = vgroup_copy[0]
        num_line_copy = vgroup_copy[1]

        cycloids = VGroup(cycloid_path, prolate_cycloid_path, curtate_cycloid_path)

        anim_one = AnimationGroup(
            Uncreate(dashed_circle_copy, run_time=1.5),
            ShrinkToCenter(point_copy, run_time=1.5),
            Create(cycloids, lag_ratio=0, rate_func=linear, run_time=3),
        )
        anim_two = AnimationGroup(
            Uncreate(cycloids, lag_ratio=0, rate_func=linear, run_time=3),
            Uncreate(num_line_copy, lag_ratio=0, run_time=1.5),
            lag_ratio=0.5,
        )

        self.play(anim_one)

        self.wait(2)

        self.play(anim_two)

        self.wait(0.5)

```
---

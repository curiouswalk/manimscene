# Koch Snowflake

In mathematics, the intriguing concept of self-similarity emerges, wherein an object bears resemblance, either entirety or partially, to a smaller iteration of itself. A remarkable illustration of this phenomenon is the Koch Snowflake, showcasing the beauty of complexity inherent in self-similar geometric patterns. It is created by repeatedly dividing each side of an equilateral triangle into three segments and replacing the middle segment with a smaller equilateral triangle. This process leads to a shape with an infinite perimeter enclosing a finite area.

https://github.com/user-attachments/assets/6208abcb-9d67-4fec-889c-eaff45afd811

>[!TIP]
> This project is done in Jupyter Notebook on Google Colab.
>
> <a href="https://colab.research.google.com/github/curiouswalk/manim/blob/main/source/koch_snowflake/koch_snowflake.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" height="23px" alt="Open In Colab"/></a>

## Setup

⦿ [Installation Guide](https://docs.manim.community/en/stable/installation.html) ⦿ [Configuration](https://docs.manim.community/en/stable/guides/configuration.html)

>[!TIP]
> **Manim in Colab**
>
> [`colab.curiouswalk.com/manim`](https://colab.curiouswalk.com/manim)


```python
from manim import *

config.disable_caching = True
config.verbosity = "WARNING"
config.media_embed = True
```

## Animation Script

```python
class KochSnowflake(Polygram):
    """A Koch Snowflake at the given level of complexity.

    Source:
      https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html

    Args:
      level (int): The recursion depth (level of complexity). Defaults to 0.
      scale (float): The extent of the snowflake (edge length of the base triangle). Defaults to 4.0.
      **kwargs: Additional keyword arguments passed to the Polygram constructor.
    """

    def __init__(self, level=0, scale=4, **kwargs) -> None:

        def _koch_snowflake_complex(level):
            if level == 0:
                # initial triangle
                angles = np.array([0, 120, 240]) + 90
                return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
            else:
                ZR = 0.5 - 0.5j * np.sqrt(3) / 3

                p1 = _koch_snowflake_complex(level - 1)  # start points
                p2 = np.roll(p1, shift=-1)  # end points
                dp = p2 - p1  # connection vectors

                new_points = np.empty(len(p1) * 4, dtype=np.complex128)
                new_points[::4] = p1
                new_points[1::4] = p1 + dp / 3
                new_points[2::4] = p1 + dp * ZR
                new_points[3::4] = p1 + dp / 3 * 2
                return new_points

        points = _koch_snowflake_complex(level)
        x, y = points.real, points.imag
        z = np.zeros(points.size)
        vertices = np.stack((x, y, z), axis=-1)

        super().__init__(vertices, **kwargs)
```

### Default Setting

```python
color = (ManimColor("#0ADBEF"), ManimColor("#0A68EF"), ManimColor("#1F0AEF"))
KochSnowflake.set_default(fill_color=color, fill_opacity=1, stroke_width=0, scale=5)
```

### Koch Snowflake Images

#### Single Koch Snowflake

![koch_snowflake_single](https://github.com/user-attachments/assets/bcac4182-1790-4cae-9ebd-6a001f35be40)

```python
%%manim KochSnowflakeSingle

class KochSnowflakeSingle(Scene):
    def construct(self):

        n = 3  # level of complexity

        title = Text("Koch Snowflake")

        level = Text("Level: %d" % n)

        text_group = VGroup(title, level)

        text_group.arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        koch_snowflake = KochSnowflake(level=n)

        self.add(text_group, koch_snowflake)
```

#### Multiple Koch Snowflakes

![koch_snowflake_multiple](https://github.com/user-attachments/assets/be4fe0b5-778b-4012-bb67-a1c50cf3d4dd)

```python
%%manim KochSnowflakeMultiple

class KochSnowflakeMultiple(Scene):
    def construct(self):

        title = Text("Koch Snowflake").to_edge(UP, buff=1)

        koch_snowflake_group = VGroup()

        for i in range(1, 5):
            koch_snowflake = KochSnowflake(level=i, scale=2.75)
            level = Text(str(i), color=BLACK, font_size=72)
            koch_snowflake.add(level)
            koch_snowflake_group.add(koch_snowflake)

        koch_snowflake_group.arrange(RIGHT, buff=0.5)

        self.add(title, koch_snowflake_group)
```

### Koch Snowflake Scene

https://github.com/user-attachments/assets/6208abcb-9d67-4fec-889c-eaff45afd811

```python
%%manim KochSnowflakeScene

class KochSnowflakeScene(Scene):
    def construct(self):

        title = Text("Koch Snowflake")

        level = VGroup(Text("Level:"), Text("0")).arrange(RIGHT, aligned_edge=DOWN)

        text_group = VGroup(title, level).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        koch_snowflake = KochSnowflake(level=0)

        def koch_snowflake_anim(n):
            next_level = Text(str(n)).next_to(level[0], RIGHT, aligned_edge=DOWN)
            next_koch_snowflake = KochSnowflake(level=n)
            anim = AnimationGroup(
                Transform(
                    koch_snowflake, next_koch_snowflake, run_time=2.5, rate_func=linear
                ),
                Transform(level[1], next_level),
            )
            return anim

        self.play(Write(text_group), GrowFromEdge(koch_snowflake, DR), run_time=1.5)
        self.wait()

        for i in range(1, 5):
            self.play(koch_snowflake_anim(i))
            self.wait(1.5)

        for i in range(3, -1, -1):
            self.play(koch_snowflake_anim(i))
            self.wait(1.5)

        self.play(
            Unwrite(text_group),
            GrowFromEdge(koch_snowflake, DR, reverse_rate_function=True),
            run_time=1.5,
        )
        self.wait(0.5)
```
---

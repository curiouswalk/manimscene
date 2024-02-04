# Koch Snowflake

In mathematics, the intriguing concept of self-similarity emerges, wherein an object bears resemblance, either entirety or partially, to a smaller iteration of itself. A remarkable illustration of this phenomenon is the Koch Snowflake, showcasing the beauty and complexity inherent in self-replicating geometric patterns.

https://github.com/curiouswalk/manim/assets/157306209/aa06927a-fe4d-4dab-aeb9-cccc1e3ae733

>[!TIP]
> This project is done in Jupyter Notebook on Google Colab.
>
> <a href="https://colab.research.google.com/github/curiouswalk/manim/blob/main/source/cycloid/cycloid.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Scene Script 

>[!NOTE]
> Save the KochSnowflake class below as `fractal.py` script.

```python
from manim import Polygram
import numpy as np

class KochSnowflake(Polygram):
    """A Koch Snowflake. It inherits from Polygram class.

    Source:
      https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html

    Args:
      level (int): The recursion depth (level of complexity). Defaults to 0.
      scale (float): The extent of the snowflake (edge length of the base triangle). Defaults to 4.0.
      **kwargs: Arbitrary keyword arguments.
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
        vertex_groups = np.stack((x, y, z), axis=-1)

        super().__init__(vertex_groups, **kwargs)

```
## Koch Snowflake Image

![cw_koch_snowflake_image](https://github.com/curiouswalk/manim/assets/157306209/d0f3fee4-8075-4e1a-b902-85c984adb063)

```python
from manim import *
from fractal import KochSnowflake
 
config.disable_caching = True

# Changing default font typeface in LaTeX.
config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class KochSnowflakeImage(Scene):

    def construct(self):

        n = 3  # level of complexity

        sw = 4  # stroke width (decrease for greater n)

        color = ("#0A68EF", "#4AF1F2")

        txt = Tex("Koch Snowflake")

        level = Tex("Level: %d" % n)

        tex_group = VGroup(txt, level).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        koch_snowflake = (
            KochSnowflake(n, scale=5, stroke_width=sw, fill_opacity=0.25)
            .set_color(color)
            .center()
        )

        self.add(tex_group, koch_snowflake)
```
## Koch Snowflake Scene 1

https://github.com/curiouswalk/manim/assets/157306209/59669c40-fce6-4469-950a-32d8a464198a

```python
from manim import *
from fractal import KochSnowflake
 
config.disable_caching = True

config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class KochSnowflakeScene1(Scene):

    def construct(self):

        txt = Tex("Koch Snowflake")
        level = Variable(0, Tex("Level"), var_type=Integer)

        tex_group = VGroup(txt, level).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        color = ("#0A68EF", "#4AF1F2")

        ks = KochSnowflake(0, scale=5, stroke_width=6, fill_opacity=0.25).set_color(
            color
        )

        sw = np.linspace(6, 1, 6)  # thinning stroke width

        self.wait(0.25)

        self.play(FadeIn(tex_group, ks), run_time=1.5)

        self.wait(1.5)

        for i in range(1, 6):

            ks_next_level = KochSnowflake(
                i, scale=5, stroke_width=sw[i], fill_opacity=0.25
            ).set_color(color)

            self.play(
                level.tracker.animate.set_value(i),
                ks.animate.become(ks_next_level),
                run_time=1.5,
            )
            self.wait(1.5)

        self.wait(0.5)

        self.play(FadeOut(tex_group, ks), run_time=1.5)

        self.wait(0.25)

```
## Koch Snowflake Scene 2

https://github.com/curiouswalk/manim/assets/157306209/4096b057-4416-41e9-9cc4-1c06f898a677

```python
from manim import *
from fractal import KochSnowflake
 
config.disable_caching = True

config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class KochSnowflakeScene2(Scene):

    def construct(self):

        txt = Tex("Koch Snowflake").to_edge(UP)

        color = ("#0A68EF", "#4AF1F2")

        ks_grp = VGroup()

        sw = np.linspace(6, 2, 4)  # thinning stroke width

        for i in range(4):

            ks_grp.add(
                VGroup(
                    KochSnowflake(
                        i, scale=3, stroke_width=sw[i], fill_opacity=0.25
                    ).set_color(color),
                    Tex("Level: %d" % i),
                ).arrange(UP, buff=0.5)
            )

        ks_grp.arrange(RIGHT, aligned_edge=UP)

        self.wait(0.25)

        self.play(FadeIn(txt, ks_grp[0]))

        self.wait()

        for i in range(1, 4):

            self.play(TransformFromCopy(ks_grp[i - 1], ks_grp[i], run_time=1.5))

            self.wait()

        self.wait()

        self.play(FadeOut(txt, ks_grp))

```
-----


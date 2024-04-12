# CuriousWalk
#### [`www.curiouswalk.com`](https://www.curiouswalk.com)
#### [`link.curiouswalk.com/manim`](https://link.curiouswalk.com/manim)

# Manim

Manim is an engine for precise programmatic animations, designed for creating explanatory math videos.

> [!NOTE]
> The Manim Community Developers. (2024). Manim – Mathematical Animation Framework (Version v0.18.0) [Computer software].  [www.manim.community](https://www.manim.community/)

# Setup

[Installation Guide](https://docs.manim.community/en/stable/installation.html)

Run this cell to get started.


```python
from IPython.display import clear_output

!sudo apt update

!sudo apt install libcairo2-dev libpango1.0-dev ffmpeg

# LaTeX installation
!sudo apt install texlive texlive-latex-extra

# LaTeX additional packages
!sudo apt install texlive-science texlive-fonts-extra

!pip install manim

clear_output() # clears cell output

!manim --version

exit() # restarts runtime
```

# Imports


```python
from manim import *
config.disable_caching = True
config.verbosity = "WARNING"
```


# Fibonacci Spiral

## Functions


```python
def fib_seq(n, a=1, b=1):
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def seq_print(seq, string="Fibonacci Sequence"):
    string += ": " + ", ".join(map(str, seq)) + ", ..."
    return print(string)

```


```python
fib_seq_20 = fib_seq(20, 0, 1)
seq_print(fib_seq_20)
```


```python
def fib_spiral_mobj(seq):
    """Returns mobjects for Fibonacci Spiral.

    Args:
        seq (list[int]): List of Fibonacci numbers.

    Returns:
        VGroup: A group of mobjects:
                Square, MathTex, ArcBetweenPoints and Dot.
    """

    mobjects = VGroup()
    squares = VGroup()
    direction = (UP, RIGHT, DOWN, LEFT)
    corner = (DL, UL)
    dot_index = (0, 0, -1, -1)

    for i, n in enumerate(seq):
        square = Square(n).next_to(squares, direction[i % 4], buff=0)
        dots = VGroup(
            Dot(square.get_corner(corner[i % 2]), color="#cfff04"),
            Dot(square.get_corner(-corner[i % 2]), color="#cfff04"),
        )
        spiral = ArcBetweenPoints(
            dots[dot_index[i % 4]].get_center(),
            dots[dot_index[i % 4] + 1].get_center(),
            angle=-PI / 2,
            color="#04d9ff",
            stroke_width=5,
        )
        num = (
            MathTex(rf"{n}^2")
            .scale_to_fit_height(square.height * 0.3)
            .move_to(square)
        )
        squares.add(square)
        mobjects.add(VGroup(square, num, spiral, dots))
        mobjects.center()

    return mobjects

```


```python
def spiral_animation(self, mobjects):
    """Animation for Fibonacci Spiral.

    Args:
        mobjects (VGroup): A group of mobjects to animate.
    """

    width = config.frame_width * 0.8

    height = config.frame_height * 0.8

    def scale_width(idx, width=width):
        mobjects.scale_to_fit_width(width * (mobjects.width / mobjects[:idx].width))

    def scale_height(idx, height=height):
        mobjects.scale_to_fit_height(height * (mobjects.height / mobjects[:idx].height))

    def recenter(idx):
        mobjects.move_to(mobjects.get_center() - mobjects[:idx].get_center())

    scale_height(1, config.frame_height * 0.3)

    for i, mobj in enumerate(mobjects, 1):

        if mobjects[:i].width > width:

            scale_width(i, width)

        elif mobjects[:i].height > height:

            scale_height(i, height)

        square, num, spiral, dots = mobj

        recenter(i)

        self.bring_to_back(square)

        self.play(Create(square), Write(num))

        self.play(Create(spiral, rate_func=linear), FadeIn(dots))
        self.wait()
        self.play(FadeToColor(square, "#7a687f"), FadeToColor(num, "#7a687f"))
        self.wait()

```

## Manim Scene


```python
%%manim -qh FibonacciSpiralImg

# changes LaTeX font typeface
config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class FibonacciSpiralImg(Scene):
    def construct(self):

        # first 6 terms of Fibonacci sequence
        fib_seq_6 = fib_seq(6)

        fib_spiral = fib_spiral_mobj(fib_seq_6)

        fib_spiral.scale_to_fit_width(config.frame_width * 0.75)

        tex_width = fib_spiral[-1][0].width * 0.75

        fib_spiral_tex = Tex("Fibonacci Spiral")

        fib_spiral_tex.scale_to_fit_width(tex_width).next_to(
            fib_spiral[-1][0], DOWN, buff=-1
        )

        self.add(fib_spiral_tex, fib_spiral)

        for i in fib_spiral:
            self.bring_to_front(i[-2], i[-1])

        seq_print(fib_seq_6)

```
![fibonacci_spiral_img](https://github.com/curiouswalk/manim/assets/157306209/1a316880-63f8-4c2f-b08e-77169dfdfe98)

---

```python
%%manim -qh FibonacciSpiralSceneOne

# changes LaTeX font typeface
config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class FibonacciSpiralSceneOne(Scene):
    def construct(self):

        # first 6 terms of Fibonacci sequence
        fib_seq_6 = fib_seq(6)

        fib_spiral = fib_spiral_mobj(fib_seq_6)

        fib_spiral.scale_to_fit_width(config.frame_width * 0.75)

        tex_width = fib_spiral[-1][0].width * 0.75

        fib_spiral_tex = Tex("Fibonacci Spiral")

        fib_spiral_tex.scale_to_fit_width(tex_width).next_to(
            fib_spiral[-1][0], DOWN, buff=-1
        )

        vgrp = [VGroup() for _ in range(4)]

        square, num, spiral, dots = vgrp

        for mobj in fib_spiral:
            for a, b in zip(vgrp, mobj):
                a.add(b)

        for s, n, d in zip(square, num, dots):
            self.play(Create(s), Write(n))
            self.play(*[FadeIn(i, scale=3) for i in d])

        self.wait(2)

        self.bring_to_front(spiral, dots)
        self.play(
            Create(spiral, rate_func=linear, run_time=4),
            Write(fib_spiral_tex, run_time=2),
        )

        self.wait()

```

https://github.com/curiouswalk/manim/assets/157306209/21e47d3b-087e-4edf-8bfe-43abab752726

---

```python
def text_anim(self):

    tex_width = config.frame_width * 0.5

    fib_spiral_tex = VGroup(
        Tex("Fibonacci").scale_to_fit_width(tex_width),
        Tex("Spiral").scale_to_fit_width(tex_width),
    ).arrange(DOWN)

    tex_group = VGroup(*fib_spiral_tex[0][0], *fib_spiral_tex[1][0])

    self.play(SpiralIn(tex_group, scale_factor=1))

    self.wait(2)

    self.play(
        SpiralIn(
            tex_group,
            scale_factor=1,
            rate_func=lambda t: smooth(1 - t),
            remover=True,
        )
    )


```

```python
%%manim -qh FibonacciSpiralSceneTwo

config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class FibonacciSpiralSceneTwo(Scene):
    def construct(self):

        text_anim(self)
        self.wait()

        # first 10 terms of Fibonacci sequence
        fib_seq_10 = fib_seq(10)

        seq_print(fib_seq_10)

        fib_spiral = fib_spiral_mobj(fib_seq_10)

        spiral_animation(self, fib_spiral)
        self.wait()

```

https://github.com/curiouswalk/manim/assets/157306209/d33cef31-ce3d-468e-a299-ac212183a397


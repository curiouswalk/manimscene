from manim import *
from fractal import KochSnowflake
 
config.disable_caching = True

# Changes the default font typeface in LaTeX.
config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class KochSnowflakeImage(Scene):

    def construct(self):

        n = 3 # level of complexity

        sw = 4 # stroke width (decrease for greater n)

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

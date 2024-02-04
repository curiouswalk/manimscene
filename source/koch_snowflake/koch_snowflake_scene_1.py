from manim import *
from fractal import KochSnowflake
 
config.disable_caching = True

# Changes the default font typeface in LaTeX.
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

        sw = np.linspace(6, 1, 6) # thinning stroke width

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

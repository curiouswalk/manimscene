from manim import *
from fractal import KochSnowflake
 
config.disable_caching = True

# Changes the default font typeface in LaTeX.
config.tex_template.add_to_preamble(r"\usepackage{fourier}")

class KochSnowflakeScene2(Scene):

    def construct(self):

        txt = Tex("Koch Snowflake").to_edge(UP)

        color = ("#0A68EF", "#4AF1F2")

        ks_grp = VGroup()

        sw = np.linspace(6, 2, 4) # thinning stroke width

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

        self.wait(0.5)

        self.play(FadeOut(txt, ks_grp))

        self.wait(0.25)

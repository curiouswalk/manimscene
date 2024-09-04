from manim import Polygram
import numpy as np

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

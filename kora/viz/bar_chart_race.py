import os
from matplotlib.animation import FuncAnimation

os.system("pip install bar_chart_race")
from bar_chart_race import *      # replaced
from bar_chart_race._make_chart import _BarChartRace


def anim(df, **kwargs):
    """ Show animation in Colab (with slider) """
    kw = dict(filename=None, orientation='h', sort='desc', n_bars=None, 
                   fixed_order=False, fixed_max=False, steps_per_period=10, 
                   period_length=500, interpolate_period=False, label_bars=True, 
                   bar_size=.95, period_label=True, period_fmt=None, 
                   period_summary_func=None, perpendicular_bar_func=None, figsize=(5, 3),
                   cmap=None, title=None, title_size=None, bar_label_size=7, 
                   tick_label_size=7, shared_fontdict=None, scale='linear', writer=None, 
                   fig=None, dpi=144, bar_kwargs=None, filter_column_colors=False)
    kw.update(kwargs)
    return _BarChartRace(df, **kw)

_BarChartRace._repr_html_ = lambda self: (
    FuncAnimation(self.fig, 
                  self.anim_func, 
                  range(len(self.df_values)), 
                  interval=self.period_length / self.steps_per_period
    ).to_jshtml() + 
    """<script>
      document.querySelector('.anim-state').state.value='once'
      document.querySelector('.fa-play').click() // autoplay not working?
      </script>
    """
)

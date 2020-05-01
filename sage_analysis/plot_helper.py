from typing import List, Optional, Tuple
import os

import matplotlib

class PlotHelper():
    """
    This class contains a number of useful attributes and methods to assist with creating good looking plots.
    """

    def __init__(
        self,
        colors: Optional[List[str]] = None,
        markers: Optional[List[str]] = None,
        linestyles: Optional[List[str]] = None,
        output_format: str = "png",
        output_path: str = "./plots",
        figsize: List[float] = None,
    ) -> None:
        """
        plot_output_format : string, optional
            The format of the saved plots.

        plot_output_path : string, optional
            The path where the plots will be saved. If the base directory does not exist, it will be created.
        """

        if colors is None:
            colors = ["r", "g", "b", "c", "m"]
        self._colors = colors

        if markers is None:
            markers = ["x", "o"]
        self._markers = markers

        if linestyles is None:
            linestyles = ["--", "-.", "."]
        self._linestyles = linestyles

        self._output_format = output_format
        self._output_path = output_path

        if figsize is None:
            figsize = [12.0, 12.0]
        self._figsize = figsize

        # Check to see if the directory exists. If ``output_path`` is "directory/tag" then we create "directory/".
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))

    @property
    def colors(self) -> List[str]:
        """
        list of str : the colours that will be used for plotting.
        """
        return self._colors

    @property
    def markers(self) -> List[str]:
        """
        list of str : the markers that will be used for plotting.
        """
        return self._markers

    @property
    def linestyles(self) -> List[str]:
        """
        list of str : the linestyles that will be used for plotting.
        """
        return self._linestyles

    @property
    def output_format(self) -> str:
        """
        str : the format plots will be saved as.
        """
        return self._output_format

    @property
    def output_path(self) -> str:
        """
        str : the path the plots will be saved to.
        """
        return self._output_path

    @property
    def figsize(self) -> List[float]:
        """
        str(float, float) : the size of the figures that are created.
        """
        return self._figsize

    def setup_matplotlib_options(self):
        """
        Set the default plotting parameters.
        """

        matplotlib.rcdefaults()
        plt.rc('xtick', labelsize='x-large')
        plt.rc('ytick', labelsize='x-large')
        plt.rc('lines', linewidth='2.0')
        plt.rc('legend', numpoints=1, fontsize='x-large')


    def adjust_legend(self, ax, location="upper right", scatter_plot=0):
        """
        Adjusts the legend of a specified axis.

        Parameters
        ----------
        ax : ``matplotlib`` axes object
            The axis whose legend we're adjusting

        location : String, default "upper right". See ``matplotlib`` docs for full options
            Location for the legend to be placed.

        scatter_plot : {0, 1}
            For plots involved scattered-plotted data, we adjust the size and alpha of the
            legend points.

        Returns
        -------
        None. The legend is placed directly onto the axis.
        """

        legend = ax.legend(loc=location)
        handles = legend.legendHandles

        legend.draw_frame(False)

        # First adjust the text sizes.
        for t in legend.get_texts():
            t.set_fontsize("medium")

        # For scatter plots, we want to increase the marker size.
        if scatter_plot:
            for handle in handles:
                # We may have lines in the legend which we don't want to touch here.
                if isinstance(handle, matplotlib.collections.PathCollection):
                    handle.set_alpha(1.0)
                    handle.set_sizes([10.0])

        return ax
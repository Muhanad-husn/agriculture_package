import seaporn as sns

def ar_text(text):
    """
    Convert Arabic text to a format suitable for display in environments that do not support Arabic script natively.
    
    This function reshapes Arabic text and applies Bi-directional (BiDi) algorithm to ensure that the Arabic text is 
    displayed correctly in environments that are not designed to handle right-to-left (RTL) scripts. This is particularly 
    useful for displaying Arabic text in graphical user interfaces or plots that do not natively support RTL languages.
    
    Parameters:
    text (str): The Arabic text string to be reshaped and processed for correct display.
    
    Returns:
    str: The processed text string ready for display in non-Arabic script supporting environments.
    """
    from arabic_reshaper import arabic_reshaper
    from bidi.algorithm import get_display
    # Reshape the Arabic text to handle characters connection correctly
    reshaped_text = arabic_reshaper.reshape(text)
    # Apply the BiDi algorithm to ensure correct display order
    bidi_text = get_display(reshaped_text)
    return bidi_text


def set_arabic(ax, trees_dict, title, xlabel, ylabel):
    """
    Sets the title, x-label, y-label, and x-axis tick labels of a given Axes object
    to Arabic text. The x-axis tick labels are determined by matching the original
    x-axis labels with values in a dictionary and applying the ar_text function to
    the corresponding keys.

    Parameters:
    ax (matplotlib.axes.Axes): The Axes object to modify.
    trees_dict (dict): A dictionary to match the x-axis labels against its values
                       and use its keys for the new labels.
    title (str): The title text to set on the Axes object.
    xlabel (str): The text for the x-axis label.
    ylabel (str): The text for the y-axis label.
    """
    # Apply ar_text to title, xlabel, and ylabel
    ar_title = ar_text(title)
    ar_xlabel = ar_text(xlabel)
    ar_ylabel = ar_text(ylabel)
    
    # Set the processed texts on the Axes object
    ax.set_title(ar_title)
    ax.set_xlabel(ar_xlabel)
    ax.set_ylabel(ar_ylabel)
    
    # Get the tick labels for the x-axis
    x_ticks = [tick.get_text() for tick in ax.get_xticklabels()]
    
    # Match the x-axis labels with values in trees_dict to find corresponding keys
    matched_keys = [key for value in x_ticks for key, dict_value in trees_dict.items() if dict_value == value]
    
    # Apply ar_text to these keys for Arabic text labels
    ar_xticks = [ar_text(i) for i in matched_keys]
    
    # Set the new x-axis tick labels
    ax.set_xticklabels(ar_xticks)


def set_arabic_long(ax, trees_dict, title, xlabel, ylabel):
    """
    Sets the title, x-label, y-label, and x-axis tick labels of a given Axes object
    to Arabic text. The x-axis tick labels are determined by matching the original
    x-axis labels with values in a dictionary and applying the ar_text function to
    the corresponding keys.

    Parameters:
    ax (matplotlib.axes.Axes): The Axes object to modify.
    trees_dict (dict): A dictionary to match the x-axis labels against its values
                       and use its keys for the new labels.
    title (str): The title text to set on the Axes object.
    xlabel (str): The text for the x-axis label.
    ylabel (str): The text for the y-axis label.
    """
    # Apply ar_text to title, xlabel, and ylabel
    ar_title = ar_text(title)
    ar_xlabel = ar_text(xlabel)
    ar_ylabel = ar_text(ylabel)
    
    # Set the processed texts on the Axes object
    ax.set_title(ar_title)
    ax.set_xlabel(ar_xlabel)
    ax.set_ylabel(ar_ylabel)
    
    # Get the tick labels for the x-axis
    y_ticks = [tick.get_text() for tick in ax.get_yticklabels()]
    
    # Match the x-axis labels with values in trees_dict to find corresponding keys
    matched_keys = [key for value in y_ticks for key, dict_value in trees_dict.items() if dict_value == value]
    
    # Apply ar_text to these keys for Arabic text labels
    ar_yticks = [ar_text(i) for i in matched_keys]
    
    # Set the new x-axis tick labels
    ax.set_yticklabels(ar_yticks)
    

def my_plot_start(figsize=(10, 8), style='darkgrid', context='notebook',
                  grid_color='grey', grid_linestyle='-.', subtitle= None):
    """
    Initializes the plotting environment with customizable options for size,
    style, and context.

    Parameters:
    - figsize: tuple, optional
        Size of the figure (width, height in inches).
    - style: str, optional
        The aesthetic style of the plots (e.g., 'darkgrid', 'whitegrid',
        'dark', 'white', and 'ticks').
    - context: str, optional
        The plotting context parameters (e.g., 'paper', 'notebook', 'talk',
        'poster').
    - grid_color: str, optional
        Color of the grid lines (applicable if style includes a grid).
    - grid_linestyle: str, optional
        Style of the grid lines (e.g., '-', '--', '-.', ':').

    Returns:
    - fig, ax: Matplotlib figure and axes objects.
    """
    sns.set_style(style)
    sns.set_context(context)
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = grid_color
    plt.rcParams['grid.linestyle'] = grid_linestyle

    fig, ax = plt.subplots(figsize=figsize)
    
    if subtitle:
        # Adjust the figure's layout to create more space at the bottom
        plt.subplots_adjust(bottom=0.6)  # Increase the bottom margin
        fig.text(0.5, 0.001, subtitle, ha='center', fontsize=12)
    
    return fig, ax


def my_plot_end(ax, title=None, xlabel=None, ylabel=None, xticks_rot=0, 
                yticks_rot=0, save_figure=False, filename='plot.jpg'):
    """
    Finalizes the plot by setting titles, labels, tick rotations, and optionally saving the figure.

    Parameters:
    - ax: Matplotlib.axes.Axes
        The axes object to customize.
    - title: str, optional
        Title for the plot.
    - xlabel: str, optional
        Label for the x-axis.
    - ylabel: str, optional
        Label for the y-axis.
    - xticks_rot: int or float, optional
        Rotation angle for x-axis tick labels.
    - yticks_rot: int or float, optional
        Rotation angle for y-axis tick labels.
    - save_figure: bool, optional
        If True, the figure will be saved to the specified filename.
    - filename: str, optional
        The path and filename to save the figure to if save_figure is True.
    """
    if title:
        ax.set_title(title, fontsize=14)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12)
    
    # Setting tick rotation if specified
    if xticks_rot != 0:
        ax.tick_params(axis='x', rotation=xticks_rot)
    if yticks_rot != 0:
        ax.tick_params(axis='y', rotation=yticks_rot)
    
    plt.tight_layout()

    if save_figure:
        ax.figure.savefig(filename, dpi=300)
    plt.show()
    

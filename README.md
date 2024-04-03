# agriculture_package

agriculture_package is a Python library designed to simplify the handling and visualization of Arabic text in data analysis and plotting contexts. This package provides a set of tools to reshape Arabic text for display in environments not natively supporting right-to-left (RTL) scripts and to integrate Arabic text into `matplotlib` plots seamlessly.

## Installation

Install agriculture_package directly from GitHub using pip:

```bash
pip install git+https:https://github.com/Muhanad-husn/agriculture_package
```

## Features

- **Arabic Text Reshaping**: Convert Arabic text into a format suitable for display in environments that do not support Arabic script natively.
- **Arabic Text Integration with Matplotlib**: Easily set plot titles, labels, and tick labels in Arabic, ensuring correct display in plots.

## Usage

Below are examples showing how to use the key functionalities of the package.

### Reshape Arabic Text for Display

```python
from agriculture_package.module1 import ar_text

reshaped_text = ar_text("النص العربي")
print(reshaped_text)
```

### Integrate Arabic Text in Matplotlib Plots

Ensure you have `matplotlib` and `seaborn` installed as they are prerequisites for these functions.

#### Setting Plot Texts in Arabic

```python
import matplotlib.pyplot as plt
from agriculture_package.module1 import set_arabic, my_plot_start, my_plot_end

# Example data
trees_dict = {'شجرة 1': 10, 'شجرة 2': 15, 'شجرة 3': 7}

# Start a plot
fig, ax = my_plot_start()

# Plotting data
ax.bar(trees_dict.values())

# Using set_arabic to set titles and labels in Arabic
set_arabic(ax, trees_dict, title="عنوان", xlabel="محور السينات", ylabel="محور الصادات")

# Finalizing and showing the plot
my_plot_end(ax)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# 23-24: 8632 -- PROGRAMMING AND SCRIPTING. 

# Introduction

This repository contains the final project for the Programming and Scripting (23-24: 8632 -- PROGRAMMING AND SCRIPTING) module for the Higher Diploma in Science in Data Analytics at Atlantic Technological University.

# Instructions

This project contains an executable Python file with will produce text and image files summarising and visualising the variables of the Iris dataset. 

To run this file, navigate to the `pands-project` directory and run the following code: 

``` python 
python analysis.py
```

You will need a modern version of Python installed on your machine to run this code.

To install Python, you can download a copy of Python from [Python.org](https://www.python.org/) or download a more full-featured collection of Python-related programs from [Anaconda.com](https://www.anaconda.com/).

# Overview

The Iris data set is a famous collection of data often used to demonstrate statistical and machine learning concepts. It contains the measurements of fifty samples of three species of Iris flower and was popularised by statistician and biologist Ronald Fischer through his work on linear discriminant analysis, although the data was originally collected by botanist Edgar Anderson in the Gaspé Peninsula. 

The three species of flowers examined in the data set are:
* Iris setosa 
* Iris virginica 
* Iris versicolor

The measurements collected are:
* Length of sepal
* Width of sepal
* Length of petal 
* Width of petal

# Summary of Variables

The `summary/iris_summary.txt' contains summary of the variables contained with the data set. From this, we can draw some initial conclusions. 

In general, the lengths of the sepal and petals are greater than their widths, with sepal and petal length means of 5.84cm and 3.76cm and width means of 3.05cm and 1.20cm respectively. Similarly, we can draw from this that sepals and generally longer than petals, although petals have higher standard deviations than sepals despite their shorter mean lengths, with sepal and petal length standard deviations of 0.83cm and 1.76cm and width standard deviations of 0.43cm and 0.76cm respectively.

Looking at the medians and modes, we can see that the sepal and petal lengths have medians of 5.80 and 4.35, the sepal and petal widths have medians of 3.00 and 1.30, the sepal and petal lengths have modes of 5.0 and 1.5 and sepal and petal widths have modes of 3.0 and 0.2. An interesting observation here is that the sepals have medians that are relatively similar to their modes, implying a symmetrical distribution. The petals on the other hand have medians that are quite different from their modes. 

# Visual Analysis

Charts provide a visual way of analysing a data set, and can provide insights that might otherwise be difficult to infer. There are a number of different charts that we can use to represent the variables in the Iris data set. The ones that we will examine are histograms, KDE plots, scatter plots, and a pair plot. 

## Histograms

Histograms are used to display continuous data. Values are grouped into buckets, which are represented on the x-axis, and each occurrence of a value in a particular bucket (range) is represented by a unit on the y-axis. 

We have four continuous variables in our data (sepal_length, sepal_width, petal_length, and petal_width) and we can examine them next to eachother on a 2x2 grid. 

<p align="center">
  <img src = "./plots/histograms/petal_length_histogram.png" alt = "Petal Length" width="45%" />
  <img src = "./plots/histograms/sepal_length_histogram.png" alt = "Sepal Length" width="45%" />
</p>
<p align="center">
  <img src="./plots/histograms/petal_width_histogram.png" alt="Petal Width" width="45%" />
  <img src="./plots/histograms/sepal_width_histogram.png" alt="Sepal Width" width="45%" />
</p>

From this visual representation, we can confirm our earlier conclusion that the distributions of the sepal lengths and widths are more symmetrical than those of the petals. From looking the petal distributions, it's clear that there is some factor that is responsible for groupings of the data observations. Standard histograms treat all values the same, and while it is possible to add hues to represent multiple dimensions within the data, there are other charts that perform a similar analysis but allow for more effectively visualising multiple dimensions. 

## KDE Plots

KDE (Kernel Density Estimation) plots are analogous to histograms in that they represent the distribution of values in a data set, but their methods of representation are very different. A KDE plot visualises the continuous probability density curve of a variable, and since multiple curves can be more easily displayed overlapping on a single plot, we can separate variables into different dimensions and display their continuous probability density curves on one on one plot. In our case, we will examine four plots (one for each measurement type) and separate the plots into three dimensions (one for each species type). 

<p align="center">
  <img src = "./plots/kde_plots/petal_length_kde_plot.png" alt = "Petal Length" width="45%" />
  <img src = "./plots/kde_plots/sepal_length_kde_plot.png" alt = "Sepal Length" width="45%" />
</p>
<p align="center">
  <img src="./plots/kde_plots/petal_width_kde_plot.png" alt="Petal Width" width="45%" />
  <img src="./plots/kde_plots/sepal_width_kde_plot.png" alt="Sepal Width" width="45%" />
</p>

From this view, we can clearly see how the distribution of lengths and widths is different depending on the species width. If we focus on petal_length, we can see how the Iris-setosa is responsible for the dense grouping of values in the 1-2cm range, and Iris-versicolor and Iris-virginica correspond with the two other peaks. Similar groups of density can be seen in the other measurements which were not as obvious with histograms. 

## Scatter Plots & Pair Plots

Scatter plots visualise the relationship between two numerical variables. Observations are plotted as points on a two dimensional cartesian plane, with one variable represented by the x-axis and another variable represented on the y-axis. A third, categorical variable, can be represented by the colour of each point. 

In our case, we will plot each unordered pair of variables. Since we have six pairs of unordered variables, we could display these plots on a 4x grid, similar to how we displayed 2x2 grids of histograms and KDE plots. 

<p align="center">
  <img src = "./plots/scatter_plots/petal_length_vs_petal_width_scatter_plot.png" alt = "Petal Length vs Petal Width" width="22%" />
  <img src = "./plots/scatter_plots/petal_length_vs_sepal_length_scatter_plot.png" alt = "Petal Length vs Sepal Length" width="22%" />
  <img src = "./plots/scatter_plots/petal_length_vs_sepal_width_scatter_plot.png" alt = "Petal Length vs Sepal Width" width="22%" />
  <img src = "./plots/scatter_plots/petal_width_vs_petal_length_scatter_plot.png" alt = "Petal Width vs Petal Length" width="22%" />
</p>
<p align="center">
  <img src = "./plots/scatter_plots/petal_width_vs_sepal_length_scatter_plot.png" alt = "Petal Width vs Sepal Length" width="22%" />
  <img src = "./plots/scatter_plots/petal_width_vs_sepal_width_scatter_plot.png" alt = "Petal Width vs Sepal Width" width="22%" />
  <img src = "./plots/scatter_plots/sepal_length_vs_petal_length_scatter_plot.png" alt = "Sepal Length vs Petal Length" width="22%" />
  <img src = "./plots/scatter_plots/sepal_length_vs_petal_width_scatter_plot.png" alt = "Sepal Length vs Petal Width" width="22%" />
</p>
<p align="center">
  <img src = "./plots/scatter_plots/sepal_length_vs_sepal_width_scatter_plot.png" alt = "Sepal Length vs Sepal Width" width="22%" />
  <img src = "./plots/scatter_plots/sepal_width_vs_petal_length_scatter_plot.png" alt = "Sepal Width vs Petal Length" width="22%" />
  <img src = "./plots/scatter_plots/sepal_width_vs_petal_width_scatter_plot.png" alt = "Sepal Width vs Petal Width" width="22%" />
  <img src = "./plots/scatter_plots/sepal_width_vs_sepal_length_scatter_plot.png" alt = "Sepal Width vs Sepal Length" width="22%" />
</p>

An alternative way to display groups of related scatter plots however is through a pair plot, which plots scatter plots of all pairs of variables on one graph along with their corresponding KDE plots. Each scatter plot and its inverse is displayed symmetrically across the top left to bottom right diagonal. 

<p align="center">
  <img src = "./plots/pair_plots/iris_pair_plot.png" alt = "Pair Plot" width="90%" />
</p>



# References

## General

- [https://en.wikipedia.org/wiki/Iris_flower_data_set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
- [https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)
- [https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis](https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis)
- [https://www.statistics.com/historical-spotlight-iris-dataset/](https://www.statistics.com/historical-spotlight-iris-dataset/)
- [https://courses.lumenlearning.com/introstats1/chapter/skewness-and-the-mean-median-and-mode](https://courses.lumenlearning.com/introstats1/chapter/skewness-and-the-mean-median-and-mode)
- [https://statisticsbyjim.com/basics/histograms/](https://statisticsbyjim.com/basics/histograms/)
- [https://en.wikipedia.org/wiki/Kernel_density_estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation)
- [https://en.wikipedia.org/wiki/Scatter_plot](https://en.wikipedia.org/wiki/Scatter_plot)

## Code

- [https://realpython.com/python-f-strings/](https://realpython.com/python-f-strings/)
- [https://realpython.com/pandas-python-explore-dataset/](https://realpython.com/pandas-python-explore-dataset/)
- [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [https://www.w3schools.com/python/python_file_write.asp](https://www.w3schools.com/python/python_file_write.asp)
- [https://realpython.com/defining-your-own-python-function/](https://realpython.com/defining-your-own-python-function/)
- [https://www.geeksforgeeks.org/python-for-loops/](https://www.geeksforgeeks.org/python-for-loops/)
- [https://seaborn.pydata.org/generated/seaborn.pairplot.html](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
- [https://seaborn.pydata.org/generated/seaborn.histplot.html](https://seaborn.pydata.org/generated/seaborn.histplot.html)
- [https://seaborn.pydata.org/generated/seaborn.scatterplot.html](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)
- [https://www.w3schools.com/python/matplotlib_labels.asp](https://www.w3schools.com/python/matplotlib_labels.asp)
- [https://www.atlassian.com/data/notebook/how-to-save-a-plot-to-a-file-using-matplotlib](https://www.atlassian.com/data/notebook/how-to-save-a-plot-to-a-file-using-matplotlib)
- [https://www.geeksforgeeks.org/python-pair-iteration-in-list/](https://www.geeksforgeeks.org/python-pair-iteration-in-list/)
- [https://seaborn.pydata.org/generated/seaborn.kdeplot.html](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)
- [https://www.geeksforgeeks.org/seaborn-kdeplot-a-comprehensive-guide/](https://www.geeksforgeeks.org/seaborn-kdeplot-a-comprehensive-guide/)
- [https://seaborn.pydata.org/tutorial/color_palettes.html](https://seaborn.pydata.org/tutorial/color_palettes.html)
- [https://seaborn.pydata.org/generated/seaborn.kdeplot.html](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)

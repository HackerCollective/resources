
Getting Started with R for Statistical Programming
============================
[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/ages-12.svg)](http://forthebadge.com)

So you wanna learn R eh? Well, what is R?

"R is a tool for statistics and data modeling. The R programming language is elegant, versatile, and has a highly expressive syntax designed around working with data. R is more than that, though — it also includes extremely powerful graphics capabilities. If you want to easily manipulate your data and present it in compelling ways, R is the tool for you." -- Code School

Feel free to share this guide! [http://bit.ly/learn-r](http://bit.ly/learn-r)

## <a name='toc'>Table of Contents</a>
  1. [An Introduction to R](#intro)
  2. [Notes](#notes)



## [[⬆]](#toc) <a name='intro'>An Introduction to R</a>
1. [Try R -- Code School](http://tryr.codeschool.com/) | If you're new to R, this is the place to start. In this course, you'll take a look at some of the most common and important bits of the language, how to use them, and then put them together into several different handy functions, and analysis patterns.

## [[⬆]](#toc) <a name='intro'>Notes</a>
### <a name='toc'>Notes TOC</a>
  1. [R Syntax: A gentle introduction to R expressions, variables, and functions](#syntax)
  2. [Vectors: Grouping values into vectors, then doing arithmetic and graphs with them](#vectors)
  3. [Matrices: Creating and graphing two-dimensional data sets](#matrices)
  4. [Summary Statistics: Calculating and plotting some basic statistics: mean, median, and standard deviation](#summaryStat)
  5. [Factors: Creating and plotting categorized data](#factors)
  6. [Data Frames: Organizing values into data frames, loading frames from files and merging them](#dataFrames)
  7. [Working With Real-World Data: Testing for correlation between data sets, linear models and installing additional packages](#realWorldData)

### [[⬆]](#toc) <a name='syntax'>R Syntax
A gentle introduction to R expressions, variables, and functions


### [[⬆]](#toc) <a name='vectors'>Vectors</a>
Grouping values into vectors, then doing arithmetic and graphs with them


### [[⬆]](#toc) <a name='matrices'>Matricies</a>
Matrices: Creating and graphing two-dimensional data sets

#### Matrix Plotting

Generate a 10 by 10 matrix named elevation with all its values initialized to 1:

```R
> elevation <- matrix(1, 10, 10)
```

You can now do a contour map of the values simply by passing the matrix to the contour function:
```R
> contour(elevation)
```
Or you can create a 3D perspective plot with the persp function:

```R
persp(elevation)
```
The perspective plot will look a little odd, though. This is because persp automatically expands the view so that your highest value (the beach surface) is at the very top.
```R
persp(elevation, expand=.2)
```


To make your surface a particular **size**  you must add it to your surface object. If you do not specify, the surface inherits the size of its parent--the context.
```javascript
var firstSurface = new Surface({
  size: [200, 400],
  content: 'hello world',
  properties: {
    color: 'white',
    textAlign: 'center',
    backgroundColor: '#FA5C4F'
  }
});

mainContext.add(firstSurface);
```
##### Surface Size:
- In pixels with [x, y]
- In only one dimension with [undefined, y] or [x, undefined]. For example,  [undefined, 200] will span the entire length of the x-direction, while only 200 pixles in the y direction. [, ] also works. 
- Have the surface auto-size according to the content with [true, true]. You can put in any statement that evaluates to [true, true]. For example, [1>3, 1>3], [false, false], and [null, null] all work.












### [[⬆]](#toc) <a name='summaryStat'>Summary Statistics</a>
Calculating and plotting some basic statistics: mean, median, and standard deviation

Simply throwing a bunch of numbers at your audience will only confuse them. Part of a statistician's job is to explain their data. In this chapter, we'll show you some of the tools R offers to let you do so, with minimum fuss.

#### Mean
***
Determining the health of the crew is an important part of any inventory of the ship. Here's a vector containing the number of limbs each member has left, along with their names.
```R
limbs <- c(4, 3, 4, 3, 2, 4, 4, 4)
names(limbs) <- c('One-Eye', 'Peg-Leg', 'Smitty', 'Hook', 'Scooter', 'Dan', 'Mikey', 'Blackbeard')
```

A quick way to assess our battle-readiness would be to get the average of the crew's appendage counts. Statisticians call this the "mean". Call the mean function with the ```limbs``` vector. To do this we employ our call function ```mean(limbs)```. The mean of the aformentioned data would be **3.5**

Now, to visually represent this data we can pull it into  a bar chart via ```barplot(limbs)```. 

To make our data set clearer we can we draw a line on the plot representing the mean. The **abline** function can take an *h* parameter with a value at which to draw a horizontal line, or a v parameter for a vertical line. When it's called, it updates the previous plot.

Draw a horizontal line 
```R
abline(h = mean(limbs))
```

### [[⬆]](#toc) <a name='factors'>Factors</a>
Factors: Creating and plotting categorized data


### [[⬆]](#toc) <a name='dataFrames'>Data Frames </a>
Data Frames: Organizing values into data frames, loading frames from files and merging them

### [[⬆]](#toc) <a name='realWorldData'>Working With Real-World Data: </a>
Testing for correlation between data sets, linear models and installing additional packages

<script type="text/javascript" src="//api.filestackapi.com/filestack.js"></script>

<input type="filepicker" data-fp-apikey="AzdDJg6OPRbil7ZRpeY9iz"
onchange="alert(event.fpfile.url)">

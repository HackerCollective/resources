
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

#### Median
***
The median is calculated by sorting the values and choosing the middle one (for sets with an even number of values, the middle two values are averaged). This can help if we're intrepreting data that hold outliers that may skew our data set. 

For example, Let's say we gain a crew member that completely skews the mean.
```R
> limbs <- c(4, 3, 4, 3, 2, 4, 4, 14)
> names(limbs) <- c('One-Eye', 'Peg-Leg', 'Smitty', 'Hook', 
                    'Scooter', 'Dan', 'Mikey', 'Davy Jones')
> mean(limbs)
[1] 4.75
```
While we can say we have our crew has a mean of 4.75 limbs, it's not entirely accurate. For this, median to the rescue. 

Call the median function on the vector:
```R
median(limbs)
```
This gives us a median of 4, which is a much more realistic view our our data set. 

#### Standard Deviation
***
Statisticians use the concept of **"standard deviation"** from the mean to describe the range of typical values for a data set. For a group of numbers, it shows how much they typically vary from the average value. To calculate the standard deviation, you calculate the mean of the values, then subtract the mean from each number and square the result, then average those squares, and take the square root of that average.

If that sounds like a lot of work, don't worry. You're using R, and all you have to do is pass a vector to the sd function. Try calling sd on the pounds vector now, and assign the result to the deviation variable:

Now to the example!
Some of the plunder from our recent raids has been worth less than what we're used to. Here's a vector with the values of our latest hauls:

```R
> pounds <- c(45000, 50000, 35000, 40000, 35000, 45000, 10000, 15000)
> barplot(pounds)
> meanValue <- mean(pounds)
```

Creating the deviation variable:
```R
deviation <- sd(pounds)
```
### [[⬆]](#toc) <a name='factors'>Factors</a>
#### Creating and plotting categorized data

Often your data needs to be grouped by category: blood pressure by age range, accidents by auto manufacturer, and so forth. R has a special collection type called a factor to track these categorized values.

#### Creating Factors
***
It's time to take inventory of the ship's hold. We'll make a vector for you with the type of booty in each chest.

To categorize the values, simply pass the vector to the factor function:

RedoComplete
```R
> chests <- c('gold', 'silver', 'gems', 'gold', 'gems')
> types <- factor(chests)
```
There are a couple differences between the original vector and the new factor that are worth noting. Print the chests vector:

```R
> print(chests)
[1] "gold"   "silver" "gems"   "gold"   "gems"
```
You see the raw list of strings, repeated values and all. Now print the types factor:

```R
> print(types)
[1] gold   silver gems   gold   gems  
Levels: gems gold silver
```
Printed at the bottom, you'll see the factor's "levels" - groups of unique values. Notice also that there are no quotes around the values. That's because they're not strings; they're actually integer references to one of the factor's levels.

Let's take a look at the underlying integers. Pass the factor to the ```as.integer``` function:
```R
> as.integer(types)
[1] 2 3 1 2 1
```
You can get only the factor levels with the **levels** function:

#### Plots With Factors
***
You can use a factor to separate plots into categories. Let's graph our five chests by weight and value, and show their type as well. We'll create two vectors for you; weights will contain the weight of each chest, and prices will track how much the chests are worth.

Now, try calling plot to graph the chests by weight and value.
```R
> weights <- c(300, 200, 100, 250, 150)
> prices <- c(9000, 5000, 12000, 7500, 18000)
> plot(weights, prices)
```
We can't tell which chest is which, though. Fortunately, we can use different plot characters for each type by converting the factor to integers, and passing it to the **pch** argument of **plot**.

```R
 plot(weights, prices, pch=as.integer(types))
```

"Circle", "Triangle", and "Plus Sign" still aren't great descriptions for treasure, though. Let's add a legend to show what the symbols mean.





### [[⬆]](#toc) <a name='dataFrames'>Data Frames </a>
Data Frames: Organizing values into data frames, loading frames from files and merging them

The **weights**, **prices**, and **types** data structures are all deeply tied together, if you think about it. If you add a new weight sample, you need to remember to add a new price and type, or risk everything falling out of sync. To avoid trouble, it would be nice if we could tie all these variables together in a single data structure.

Fortunately, R has a structure for just this purpose: the data frame. You can think of a data frame as something akin to a database table or an Excel spreadsheet. It has a specific number of columns, each of which is expected to contain values of a particular type. It also has an indeterminate number of rows - sets of related values for each column.

#### Data Frame Access

Just like matrices, it's easy to access individual portions of a data frame.

You can get individual columns by providing their index number in double-brackets. Try getting the second column (prices) of treasure:
```R
treasure[[2]]
```
You could instead provide a column name as a string in double-brackets. (This is often more readable.) Retrieve the "weights" column:

```R
> treasure[["weights"]]
[1] 300 200 100 250 150
```
**Shorthand for Dataframes**
Typing all those brackets can get tedious, so there's also a shorthand notation: the data frame name, a dollar sign, and the column name (without quotes). Try using it to get the "prices" column:

```R
treasure$prices
```

#### Loading Data Frames

Typing in all your data by hand only works up to a point, obviously, which is why R was given the capability to easily load data in from external files.

You can load a CSV file's content into a data frame by passing the file name to the read.csv function. Try it with the "targets.csv" file:
```R
read.csv("targets.csv")
```

For files that use separator strings other than commas, you can use the ```read.table``` function. The **sep** argument defines the separator character, and you can specify a tab character with **"\t"**.

Call ```read.table``` on "infantry.txt", using tab separators:

```R
read.table("infantry.txt", sep="\t")
```

In this case you'll get "V1" and "V2" column headers. The first line is not automatically treated as column headers with ```read.table```. This behavior is controlled by the header argument. To fix this, you can call  ```read.table``` and set the header to TRUE:
```R
read.table("infantry.txt", sep="\t", header=TRUE)
```
#### Merging Data Frames
We want to loot the city with the most treasure and the fewest guards. Right now, though, we have to look at both files and match up the rows. It would be nice if all the data for a port were in one place...

R's merge function can accomplish precisely that. It joins two data frames together, using the contents of one or more columns. First, we're going to store those file contents in two data frames for you, **targets** and **infantry**.

The merge function takes arguments with an **x** frame (**targets**) and a **y** frame (**infantry**). By default, it joins the frames on columns with the same name (the two Port columns). See if you can merge the two frames:

```R
merge(x = targets, y = infantry)
```

### Notes
R can test for correlation between two vectors with the ```cor.test``` function. 

```R
cor.test(countries$GDP, countries$Piracy)
```
```R
> cor.test(countries$GDP, countries$Piracy)

	Pearson's product-moment correlation

data:  countries$GDP and countries$Piracy 
t = -14.8371, df = 107, p-value < 2.2e-16
alternative hypothesis: true correlation is not equal to 0 
95 percent confidence interval:
 -0.8736179 -0.7475690 
sample estimates:
       cor 
-0.8203183 
```
The key result we're interested in is the **"p-value"**. Conventionally, any correlation with a p-value less than **0.05** is considered statistically significant, and this sample data's p-value is definitely below that threshold. In other words, yes, these data do show a statistically significant negative correlation between GDP and software piracy.

We have more countries represented in our GDP data than we do our piracy rate data. If we know a country's GDP, can we use that to estimate its piracy rate?

We can, if we calculate the linear model that best represents all our data points (with a certain degree of error). The **lm** function takes a model formula, which is represented by a response variable (piracy rate), a tilde character (**~**), and a predictor variable (GDP). (Note that the response variable comes first.)

Try calculating the linear model for piracy rate by GDP, and assign it to the line variable:

```R
line <- lm(countries$Piracy ~ countries$GDP)
```
Sort of like a trend line! We can now plot it by calling our handy dandy abline!
```R
abline(line)
```

#### 
The functionality we've shown you so far is all included with R by default. (And it's pretty powerful, isn't it?) But in case the default installation doesn't include that function you need, there are still more libraries available on the servers of the Comprehensive R Archive Network, or CRAN. They can add anything from new statistical functions to better graphics capabilities. Better yet, installing any of them is just a command away.

Let's install the popular ggplot2 graphics package. Call the install.packages function with the package name in a string:

```R
> install.packages("ggplot2")
```R
You can get help for a package by calling the help function and passing the package name in the package argument. Try displaying help for the "ggplot2" package:

```R
help(package = "ggplot2")
```
## Appendix
***
Straight to business
# Notes
#### Plating with Variables 
```R
x = 11
> x
[1] 11
> print(x)
[1] 11
> rm(x)
> x <- 192
> y = 9
> sqrt(y)
[1] 3
> exp(y)
[1] 8103.084
> e^y
Error: object 'e' not found
> log(y)
[1] 2.197225
> y^y^y
[1] Inf
> y^y
[1] 387420489
> y^(sqrt(y))
[1] 729
> x = 11
> rm(y)
```
#### Creating Vectors, Matricies, Sequences 
```R
> x1 <- x(1,3,5,6,9)
Error: could not find function "x"
> x1 <- c(1,3,5,6,9)
> gender <- c("male", "female")
```
Creating a sequence from 2 to 7
```R
> 2:7
[1] 2 3 4 5 6 7
```
Creating a sequence with specified indexing. 
```R
> seq(from=1, to=7, by=.25)
 [1] 1.00 1.25 1.50 1.75 2.00 2.25 2.50 2.75 3.00
[10] 3.25 3.50 3.75 4.00 4.25 4.50 4.75 5.00 5.25
[19] 5.50 5.75 6.00 6.25 6.50 6.75 7.00
> rep(1, times=10)
 [1] 1 1 1 1 1 1 1 1 1 1
> rep(1:3. times=5)
Error: unexpected symbol in "rep(1:3. times"
> rep(1:3, times=5)
 [1] 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3
 ```
 
 Repeating a sequence x number of times
 ```R
  rep(seq(from=2, to-5, by=.25), times=3)
Error in seq.default(from = 2, to - 5, by = 0.25) : object 'to' not found
> rep(seq(from=2, to=5, by=.25), times=3)
 [1] 2.00 2.25 2.50 2.75 3.00 3.25 3.50 3.75 4.00 4.25 4.50 4.75 5.00 2.00 2.25 2.50 2.75 3.00 3.25 3.50 3.75 4.00 4.25
[24] 4.50 4.75 5.00 2.00 2.25 2.50 2.75 3.00 3.25 3.50 3.75 4.00 4.25 4.50 4.75 5.00
> 
```
You can see that I orginally had an error due to putting t = 5, and not to = 5.

Creating vectors and playing with them

```R
> x <- 1:5
> x+10
[1] 11 12 13 14 15
> x - 10
[1] -9 -8 -7 -6 -5
> x *10
[1] 10 20 30 40 50
> x/2
[1] 0.5 1.0 1.5 2.0 2.5
> # if two vectors are of the same length, we may add/subtract/mult/div 
> # corresponding elements
> y <- c(1,3,5,7,9)
> x+y
[1]  2  5  8 11 14
> x*y
[1]  1  6 15 28 45
> x/y
[1] 1.0000000 0.6666667 0.6000000 0.5714286 0.5555556
```

Extracting elements in a matrix
```R
> y[3]
[1] 5
```
Extracting all elements except specified one in a matrix
```R
> y[-3]
[1] 1 3 7 9
```
Different methods to create a matrix
```R
> y[1:3]
[1] 1 3 5
> y[c(1,5)]
[1] 1 9
```
Extrcting elements only less than 6
```R
> y[y<6]
[1] 1 3 5
```
creating a matrix
```R
> matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, byrow=TRUE)
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9
```

Creating a matrix while specifying that these are entered in a row fashion
Setting byrow = FALSE produces a matrix, now set up by a column fashion
```R
> matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, byrow=FALSE)
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
> 
```

```R
> mat <- matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, byrow=TRUE)
> mat
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9
> mat[1,2]
[1] 2
> #first row second column
> 
> mat[c(1,3), 2]
[1] 2 8
> #extracted everything in row 1/3 and column 2
> mat[2]
[1] 4
> mat[2,]
[1] 4 5 6
> #extract all columns in row 2
> mat[,1]
[1] 1 4 7
> #extracting everything in row one
```

> ### How to import from excel into r
> #save as a csv or a txt
> #can ask for help with a function via help(read.csv) or ?read.csv
> 
> 

```R
> data1 <-read.csv(file.choose(),header=T)
> #using file.choose() allows you to choose the document via a pop up
> # instead of having to type the file path
> #header = T or header = TRUE, tells R that there are headers in the first row
> data1
   LungCap Age Height Smoke Gender Caesarean
1    6.475   6   62.1    no   male        no
2   10.125  18   74.7   yes female        no
3    9.550  16   69.7    no female       yes
4   11.125  14   71.0    no   male        no
5    4.800   5   56.9    no   male        no
6    6.225  11   58.7    no female        no
7    4.950   8   63.3    no   male       yes
8    7.325  11   70.4    no   male        no
9    8.875  15   70.5    no   male        no
10   6.800  11   59.2    no   male        no
> # we can see that R has properly read our data
> 
> 
> # We can also pull in files via the read.table method
> data2 <- read.table(file.choose(), header=T, sep=",")
> # this way we can read in other delineated types of values
> 
> data2
   LungCap Age Height Smoke Gender Caesarean
1    6.475   6   62.1    no   male        no
2   10.125  18   74.7   yes female        no
3    9.550  16   69.7    no female       yes
4   11.125  14   71.0    no   male        no
5    4.800   5   56.9    no   male        no
6    6.225  11   58.7    no female        no
7    4.950   8   63.3    no   male       yes
8    7.325  11   70.4    no   male        no
9    8.875  15   70.5    no   male        no
10   6.800  11   59.2    no   male        no
> 
> 
> #Now we're going to read in a tab delimited text file
> data3 <- read.delim(file.choose(), header=T)
> data3
   LungCap Age Height Smoke Gender Caesarean
1    6.475   6   62.1    no   male        no
2   10.125  18   74.7   yes female        no
3    9.550  16   69.7    no female       yes
4   11.125  14   71.0    no   male        no
5    4.800   5   56.9    no   male        no
6    6.225  11   58.7    no female        no
7    4.950   8   63.3    no   male       yes
8    7.325  11   70.4    no   male        no
9    8.875  15   70.5    no   male        no
10   6.800  11   59.2    no   male        no
> 
> 
> #can also do it with the read.table command
> data4 <- read.table(file.choose(), header=T, sep="\t")
> # we had to specify the special character \t for tab
> data4
   LungCap Age Height Smoke Gender Caesarean
1    6.475   6   62.1    no   male        no
2   10.125  18   74.7   yes female        no
3    9.550  16   69.7    no female       yes
4   11.125  14   71.0    no   male        no
5    4.800   5   56.9    no   male        no
6    6.225  11   58.7    no female        no
7    4.950   8   63.3    no   male       yes
8    7.325  11   70.4    no   male        no
9    8.875  15   70.5    no   male        no
10   6.800  11   59.2    no   male        no
```


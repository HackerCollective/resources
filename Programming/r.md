
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

```R
> #Reading larger data sets and working with data
> rm(data1)
> rm(data2)
> rm(data3)
> rm(data4)
> rm(mat)
> rm(gender)
> data1 <- read.table(file.choose(), header=T, sep="\t")
> find dimension of data
Error: unexpected symbol in "find dimension"
> # find dimension of data
> dim(data1)
[1] 725   6
> head(data1)
  LungCap Age Height Smoke Gender Caesarean
1   6.475   6   62.1    no   male        no
2  10.125  18   74.7   yes female        no
3   9.550  16   69.7    no female       yes
4  11.125  14   71.0    no   male        no
5   4.800   5   56.9    no   male        no
6   6.225  11   58.7    no female        no
> #shows the first siz rows
> tail(data1)
    LungCap Age Height Smoke Gender Caesarean
720   7.325   9   66.3    no   male        no
721   5.725   9   56.0    no female        no
722   9.050  18   72.0   yes   male       yes
723   3.850  11   60.5   yes female        no
724   9.825  15   64.9    no female        no
725   7.100  10   67.7    no   male        no
> #shows the last 6 rows
> 
> 
> data1[c(5,6,7,8,8), ]
    LungCap Age Height Smoke Gender Caesarean
5     4.800   5   56.9    no   male        no
6     6.225  11   58.7    no female        no
7     4.950   8   63.3    no   male       yes
8     7.325  11   70.4    no   male        no
8.1   7.325  11   70.4    no   male        no
> # we can also use the colon! 
> data1[5:0,]
  LungCap Age Height Smoke Gender Caesarean
5   4.800   5   56.9    no   male        no
4  11.125  14   71.0    no   male        no
3   9.550  16   69.7    no female       yes
2  10.125  18   74.7   yes female        no
1   6.475   6   62.1    no   male        no
> names(data1) #this should give us the headers
[1] "LungCap"   "Age"       "Height"    "Smoke"     "Gender"    "Caesarean"
```
### Working with variables and Data in R
> mean(Age)
Error in mean(Age) : object 'Age' not found
> # this is because R does not recognize age as it is part of the object data1
> # we can extract it by using the $ to parse our object
> 
> mean(data1$Age)
[1] 12.3269
> 
> # we can use the dollar sign to extract variables, or we can attach the data
> 
> 
> attach(data1)
> # now r recognizes the headers as variables
> mean(Age)
[1] 12.3269
> # we can unattach using detach command
> detach(data1)
> age
Error: object 'age' not found
> # we can re attach it to make it easier
> attach(data1)
> Age
  [1]  6 18 16 14  5 11  8 11 15 11 19 17 12 10 10 13 15  8 11 14  6  8 16 11 11 12 12  9  4 18  4 13 13 13 12 10  6  9 11
 [40] 17 14 17  8 12  6 11 11 12 17  7 15 15 11 10 18  6 13 19  9 12 12 14  9 13 13 13 11 11 11 12 14 11 11 13 13 12 14  9
 [79] 17 11 12 16 17 19 14 12 19 11 15 19  9 14 13 14 19 18 16  7 16 10 13 14 13 16 16  5 16 12  7  7 15 18  8  3 15 15  7
[118] 18  8 17 16 12 17 16 19 12 17 19 12 12 15 17 13 12 16 13 15 15 14 13  6 18 18 18  9 17 14 14 14  3 11  8  9  8 16  7
[157] 11  5 16 11 16 10 12 19  7  8 13 17  9  8 15  6 14 10 17 15 10 16 17 17 13 17 15 16 18 10 16  8 14  4 17 15 10 13 16
[196] 17 19 11  8 12 13 16 15 18  8  5 10  8 13  7 11 15 10 15  8  7 10 18 15 19 14  3  6 12 14  8 15  5  3 11 11 13 18 19
[235] 15 18  8 11 17 14 12 14  8 12 11  6  9 11 18 18 19  9 18  9  7  8 18 11 12 11 14 14  5 12 19  9 17 10  9  9 10 14 14
[274] 12 17 10 12 13 11 12 17 14 15  8 13 11 10  6 10 18  6 18  3 15 13 19 11 13  5  8 18 13 10 18 12  9 15 14  8 19  7 13
[313] 14 19  9 12 10  3 13 16 13 10 15 11 11 19 15 11 19  8  7 10 13 14 14  9 11 13 15 18 15 13  9  8  7 17 11 12  9 14  8
[352] 16 17  9 12 19 17 15 12  7  8 15 18 11 10  9 11 16 16 18 16 10 13 16 18  9 13 11  5  6 12  9 15 13 16 18 11 13  7  4
[391] 13 16 17 10 11  7 11 16 13  8  3 12 15  8  4 13  7 15 15 18  7 13 18 19 10  6 13 14 15  5 12 17  8 12 12 12  7 19 17
[430] 16  6 12  6  6 14 15  7 14 16 11  9 19 17 15 13  5 11 11 10 13 10  9 15 13 17  5 14 10 13  8 17 13 10 10 16  5 15 11
[469] 12 19 10 18 13 15 16 17 14  9 16 16 16 16 12 16  7 18  4 19 11 15  8 15  5  6 19 14 14  7 15 13  9 13 18  5 14  7 18
[508] 17 14 13 11 12 18  3 14  9 10  9 15 14 16 12  9 13 15 11  6 12 17 12  3 12  7 12  8  9 15 11 15 12  9 10  6 12 14 15
[547]  8 19 12  7 17  7 12 13 15 15  6 13 19 12  9 17 19 10 12 14 12 18  5 19 17 13  9  7 16 16 17 17 18  7  7 12 12  8  8
[586] 14 11 17 13 13 15  5 10 15 11  3  6  7 12 14 13 19 15 14  7 16 16 16  7  7 16 15 12  6 11 13 15 13 18 15  3 16 12 12
[625]  5 12 14  6 19  9 11 10  7 16  5  8 15 10 10 13 18 12 13 19 10 19 16 13 13 14  9  8 10 13 12  6 14 18 14  3 16 10 12
[664] 10 16 10  8 10  5  8  8 18  6 10 14 17 18 14 14 10 13 18 11 15 19 16 16 15  8  7 12 10 13  7 13 14  9 16 15 13 10 14
[703] 12  7 15 19 15 12 15 10 17  5  3 14 16 19 11 16 17  9  9 18 11 15 10
> 
> 
> names(data1)
[1] "LungCap"   "Age"       "Height"    "Smoke"     "Gender"    "Caesarean"
> class(data1)
[1] "data.frame"
> class(Age)
[1] "integer"
> class(Height)
[1] "numeric"
> class(Smoke)
[1] "factor"
> class(gender)
Error: object 'gender' not found
> 
> class(gender)
Error: object 'gender' not found
> # these classify what type of object each of our classes in our data is, whether integer or factor, or data.frame
> 
> 
> levels(smoke)
Error in levels(smoke) : object 'smoke' not found
> levels(Smoke)
[1] "no"  "yes"
> levels(Gender)
[1] "female" "male"  
> #levesl gives us a quick breakdown of the different types of data
> 
> 
> summary(data1)
    LungCap            Age            Height      Smoke        Gender    Caesarean
 Min.   : 0.507   Min.   : 3.00   Min.   :45.30   no :648   female:358   no :561  
 1st Qu.: 6.150   1st Qu.: 9.00   1st Qu.:59.90   yes: 77   male  :367   yes:164  
 Median : 8.000   Median :13.00   Median :65.40                                   
 Mean   : 7.863   Mean   :12.33   Mean   :64.84                                   
 3rd Qu.: 9.800   3rd Qu.:15.00   3rd Qu.:70.30                                   
 Max.   :14.675   Max.   :19.00   Max.   :81.80                                   
> 
> #r provides summary data that it thinks is useful depending on the type of object, whether it's a number or string
> 
> 
> x <- c(0,1,1,1,0,0,0,0,0)
> class(x)
[1] "numeric"
> summary(x)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
 0.0000  0.0000  0.0000  0.3333  1.0000  1.0000 
> # we wanted x to represent yes or no fi someone is a smoker like lots of data sets
> # we can see by default R categorizes it not as a category/factor but rather as numeric
> # and it gives us summary details that are indicative of numeric analysis
> # however if we'd like, we can change this manually
> 
> 
> x <- as.factor(x)
> # store in the object x, x as a factor
> class(x)
[1] "factor"
> summary(x)
0 1 
6 3 


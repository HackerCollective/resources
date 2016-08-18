Quick Notes on R
============================
[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/ages-12.svg)](http://forthebadge.com)

Below is a detailed brief of my notes, thoughts, and experiences from a plethora of tutorials, examples, and practical work. 


View the guide that details where to start, and which tutorials to use here ! [http://bit.ly/learn-r](http://bit.ly/learn-r)
Feel free to share this guide! [R Notes ](https://github.com/HackerCollective/resources/edit/gh-pages/Programming/r-notes.md)
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


# Straight to business
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

### How to import from excel into r
You can save as a csv or a txt
can ask for help with a function via help(read.csv) or ?read.csv

Download the data set 
http://www.statslectures.com/index.php/r-stats-datasets



```R
> data1 <-read.csv(file.choose(),header=T)
```

using file.choose() allows you to choose the document via a pop up
instead of having to type the file path
header = T or header = TRUE, tells R that there are headers in the first row

```R
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
```R
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
```

## Bar Charts and Pie Charts in R 
```R
> # A BArchart is a visual display of the frequency for each category of a categorical variable or the relative frequency (%) for each category
> # We can get help on bar charts via the help command and barplot
> help("barplot")
> # Thi should pull up a description in the right window
> 
> 
> # The frequency command can be pulled up using the table command
> table(Gender)
Gender
female   male 
   358    367 
> count <- table(Gender)
> count
Gender
female   male 
   358    367 
> table(Gender)/725
Gender
   female      male 
0.4937931 0.5062069 
> perent <- table(Gender)/725
> barplot(count)
> barplot(percent)
Error in barplot(percent) : object 'percent' not found
> percent <- table(Gender)/725
> rm(perent)
> barplot(percent)
> 
> # we can add information such as the title, and the axis information via the following
> barplot(percent, main="TITLE", xlab="Gender", ylab="%")
> 
> # I however like to rotate the values on the y-axis to be more human readable
> barplot(percent, main="TITLE", xlab="Gender", ylab="%", las=1)
> 
> # To change the names and labels that appear under the bars we can use the names.arg argument
> barplot(percent, main="TITLE", xlab="Gender", ylab="%", las=1, names.arg=c("Female", "Male"))
> 
> 
> #Finally if you want the bars to appear horizontally, and not vertically, we can add the horiz attribute
> barplot(percent, main="TITLE", ylab="Gender", xlab="%", las=1, names.arg=c("Female", "Male"), horiz=TRUE)
> #Note, we must change our x and y label, so we don't get confused 
> 
> 
> ### Pie Charts
> # We can produce a Pie Chart using the Pie Command
> pie(count)
> pie(count, main="TITLE HERE")
> box()
> # we used the box command to add a nice box to our pie chart
```

### Boxplots and Boxplots With Groups in R

```R
> boxplot(LungCap)
> 
> # The blox plot is a visual display of the 5 number summary, and we can get those details easily
> # min, 1'st quartile, median, 2nd quartile, max
> 
> quantile(LungCap, probs=c(0, 0.25, 0.5, 0.75, 1))
    0%    25%    50%    75%   100% 
 0.507  6.150  8.000  9.800 14.675 
> # this produces the results for data that appears at that probability
> 
> #time to pretty it up
> boxplot(LungCap, main="Boxplot", ylab="Lung Capacity")
> 
> # we can now set the limits to make it easier to see and view
> boxplot(LungCap, main="Boxplot", ylab="Lung Capacity", ylim = c(0,16))
> 
> # and again, rotating the values to make it look snazzy
> boxplot(LungCap, main="Boxplot", ylab="Lung Capacity", ylim = c(0,16), las=1)
> 
> 
> # Now comparing 2 or more box plots on the same scale, going to compare different groups based on their category
> boxplot(LungCap ~ Gender)
> boxplot(LungCap ~ Gender, main="Boxplot by Gender")
> 
> 
> # We can do the same thing using the square bracket method
> boxplot(LungCap[Gender=="female"], LungCap[Gender=="male"])
```

### Stratified Boxplots in R


Stratified boxplots are useful for examining the relationship between a categorical variable and a numeric variable, within strata or groups defined by a third categorical variable

In the following example we'll examine the relationship between Smoking & Lung Capacity within age groups or Age Strata and make sure you've already loaded the data and attached it

Now we will make an "AgeGroups" Vatiable, this will split the age into sertain sections per our liking

```R
> AgeGroups <- cut(Age, breaks=c(0,13,15,17,25), labels=c("<13", "14/15", "16/17", "18+"))
```

Now we will check the first 5 ages, and age groups

```R
> Age[1:5]
[1]  6 18 16 14  5
> AgeGroups[1:5]
[1] <13   18+   16/17 14/15 <13  
Levels: <13 14/15 16/17 18+
> levels("AgeGroups")
NULL
> levels(AgeGroups)
[1] "<13"   "14/15" "16/17" "18+"  
```

Puuuuuuuurfeeeeect
We'll elarn more about cut and numric to categorical variables later


```R
> boxplot(LungCap, ylab="Lung Capacity", main="Boxplot of Lung Cap", las=1)
> boxplot(LungCap~Smoke, ylab="Lung Capacity", main="LungCap vs Smoking", las=1)
```

The smokign effect is confounded with the Age effect (we'll talk about counfounded laterrrrrs)
* On average smokers are older than non smokers, and older children have bigger bodies hence the bigger lung capacities of the smokers
One option we consider is to look at smoking and lung capcity within age strata

```R
> boxplot(LungCap[Age>=18]~Smoke[Age>=18], ylab="Lung Capacity", main="LungCap vs Smoking", las=1)
> boxplot(LungCap[Age>=18]~Smoke[Age>=18], ylab="Lung Capacity", main="LungCap vs Smoking for 18+", las=1)
```

Now we want to visualize the relationship between LungCapacity and SMoking within each of the Age Strate
We'll do this by creating BoxPlots of lung capacity for smokers and for non smokers of different age strata

```R
> boxplot(LungCap[Age>=18]~Smoke*AgeGroups, ylab="Lung Capacity", main="LungCap vs Smoking by age group", las=1)
Error in model.frame.default(formula = LungCap[Age >= 18] ~ Smoke * AgeGroups) : 
  variable lengths differ (found for 'Smoke')
> boxplot(LungCap~Smoke*AgeGroups, ylab="Lung Capacity", main="LungCap vs Smoking by age group", las=1)
```

oops, litte typo, but what did we just do?
when we multipled Smoke by AgeGroups, we created a box plot for each of the age groups (there are 4) and under both conditions, smoking = yes, and smoking = no, creating 8 different plots the x-axis values are kind of overlapping but we can fix that with the las command

```R
> boxplot(LungCap~Smoke*AgeGroups, ylab="Lung Capacity", main="LungCap vs Smoking by age group", las=2)
> boxplot(LungCap~Smoke*AgeGroups, ylab="Lung Capacity", main="LungCap vs Smoking by age group", las=2, col=c(4,2))
```




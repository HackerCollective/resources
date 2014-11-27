#Elixir
wont run out of stack levels unless you run out of memory

works with OTP
##Elixir
elixir built on erlang vm
compiles to BEAM bytecode
Erlang has fault-tolerant ("let it crash" error)
Pattern matching
Recursion
Immutable Data Structures
Adds more data types to erlang
All data is immutable

##Atoms
atms are just Sybmols in Ruby
`:hello_world`
`:a`
`true #booleans are also atoms`

##Tuples
Ordered collection of elements

```
#tuple
{:one, :two, :three}


elem({1, 2, 3}, 0) # => 1

```

##Lists
No array type, only linked lists
Each item in the list contains value, along with pointer

```
letters = [:a, :b, :c]

[:d | letters] #=> [:d, :a, :b, c:]
```
##String(ish) Types
No true string type
represents strings as binaries
Lists can be used to represent string data
```
"" # = utf-8 binary
'' # = char list
?a # = character code
```

##Modules
everything is stored in modules

```
def moduleping do
  #todo
end
```

##Functions
In elixir function are identified by name and arity

```
#add/2 has two clauses
def add(0, 0) do: 0
def add(x, y) do: x + y

#add/3 has one clause
def add(x, y, z) do
  x +y +z
end
```

##Pattern Matching
The equal sign isn't assignment, it's a challenge to make both sides equal

```
:a = :a #=> a
:a = :b #=> ** (MethError) match of right hand side value: :b

letter = :a #=> :a
letter #=> :a
```

matching tuples

```
{:ok, foo} = {:ok, "foo bar baz"}
foo #=> "foo bar baz"

{:ok, foo} = {:error, :crashed} #=> ** (MatchError) no match of right hand side value: {:error, crashed}
```

matching lists
```
[head|tail] = [1,2,3]
head #=> 1
tail #=>[2,3]

[first, second, third] = [1,2,3]
second #=> 2

[one, two] = [1,2,3] #=> ** (MatchError) no match of right hand side value: [1,2,3]

[first, second |rest] = [1, 2, 3]
second #=> 2
```

###functions
```
def fib(0) do 0 end
def fib(1) do 1 end
def fib(n) do fib(n-1) + fib(n-2) end
```

##Variables
variables cannot be re-bound to new values during a match

```
{num, num} = {1, 1}
{num, num} = {1, 2} #=> ** No match of right hand value
```

###underscore variable can be used in place of a normal variable in a pattern

```
{_, _} = {1, 1}
{_, _} = {1, 2}
{num, num} = {1, 2}
```

###the ^ Variable prefix
```
username = "Jose"

{:name, ^username} = {:name, "Joe"} #forces it to retain Jose and not be re-assigned, throws error
{:name, ^username} {:name, "Jose"}
```

##First Class Functions
Two Types
 - Names -- does not inherit scope
 - Anonymous -- inherits the scope of wherever it was defined functions
Both can be referenced and passed around

####Named
```
defmodule Hello
  def greet("SunJug") do "hello everyone!" end
  def greet(name) do "hello " <> name end
end

#references the function
hello = &hello.greet/1 #=> #function<6.90072147/1 in :erl_eval.expr/5>

hello.("SunJUG") #=> hello everyone!
Hello.greet("Jose") #=> hello Jose
```

####Anonymous
```
special_greetings = "Hello everyone!"

#inherits scope creating closure

greet = fn
  "SunJug" -> special_greeting
  name -> "hello " <> name
end

greet #=> #Function...

greet.("SunJug")
```

##Recursion
No iteration so use recursion

####Recursion Step by Step in Elixir

```
def sum_list([head | tai;], acc) do
  sum_list( tail, acc+head)
end

def sum_list([], acc) do
  acc
end
```

##Concurrency
Each instance of the Erlang VM is called a node
You can have one or more nodes on a physical machine
Can spread nodes through a network
Can rate limit the VM on amount of threads
Erlang processes are not OS processes
Within the VM you can have multiple Erlang processes
There is no "main" process, everything is a process and there are not special types of processes
No shared data amongst processes - Make a copy and work on their own
Processing done via message passing
Can pass a message to another VM
Lazy copying
Processes can be linked together, processes can also be monitored by other processes
#####Processes are Actors
Implements the actor model
Processes encapsulate state
Elixir's processes are more object-oriented than objects in object-oriented languages

######Processes Example
Messages are stored in the mailbox
All messages are async, if it receives messages during work it gets next message
Can put limitations on the mailbox
```
#Message being sent to a process
#pid is a process
message = {:add, 1, 2}
send pid, message

#process receiving
#listens for message
receive do
  {:add, x, y} ->
    x +y
  {:subtract, x, y} ->
    x -y
  _->
    :error
end # would call this again to implement a server
```

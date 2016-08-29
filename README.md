<h1 id="sololearn-python-notes"><strong><em>PYTHON NOTES</em></strong></h1>

<hr>



<h2 id="table-of-contents"><strong>Table of Contents</strong></h2>

<p><div class="toc">
<ul>
<li><a href="#sololearn-python-notes">PYTHON NOTES</a><ul>
<li><a href="#table-of-contents">Table of Contents</a></li>
<li><a href="#functional-programming">FUNCTIONAL PROGRAMMING</a></li>
<li><a href="#lambdas">Lambdas</a></li>
<li><a href="#map">Map</a></li>
<li><a href="#filter">Filter</a></li>
<li><a href="#generators-1">Generators-1</a></li>
<li><a href="#generators-2">Generators-2</a></li>
<li><a href="#generators-3">Generators-3</a></li>
<li><a href="#decorators-1">Decorators-1</a></li>
<li><a href="#decorators-2">Decorators-2</a></li>
<li><a href="#recursion-1">Recursion-1</a></li>
<li><a href="#recursion-2">Recursion-2</a></li>
<li><a href="#recursion-3">Recursion-3</a></li>
<li><a href="#sets-1">Sets-1</a></li>
<li><a href="#sets-2">Sets-2</a></li>
<li><a href="#sets-3">Sets-3</a></li>
<li><a href="#data-structures">Data Structures</a></li>
<li><a href="#itertools-1">itertools-1</a></li>
<li><a href="#itertools-2">itertools-2</a></li>
<li><a href="#itertools-3">itertools-3</a></li>
</ul>
</li>
</ul>
</div>
</p>

<h2 id="functional-programming"><strong><em>Functional Programming</em></strong></h2>
[Source: SoloLearn Python Tutorial](http://www.sololearn.com/Play/Python)
<h3 id="lambdas"><strong>Lambdas</strong></h3>

<hr>

<p>Creating a function normally (using def) assigns it to a variable automatically.  <br>
This is different from the creation of other objects - such as strings and integers - which can be created on the fly, without assigning them to a variable.  <br>
The same is possible with functions, provided that they are created using lambda syntax. Functions created this way are known as <strong>anonymous</strong>. <br>
This approach is most commonly used when passing a simple function as an argument to another function. The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.</p>

<pre><code>def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)
</code></pre>

<blockquote>
  <p><strong>Note:</strong> Lambda functions get their name from lambda calculus, which is a model of computation invented by Alonzo Church.</p>
</blockquote>

<h3 id="map"><strong>Map</strong></h3>

<hr>

<p>The built-in functions <strong>map</strong> and <strong>filter</strong> are very useful <strong>higher-order functions</strong> that operate on <strong>lists</strong> (or similar objects called iterables).  <br>
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.</p>

<p><strong>Example</strong>:</p>

<pre><code>def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[16, 27, 38, 49, 60]</p>
</blockquote>

<p>We could have achieved the same result more easily by using <strong>lambda syntax</strong>.</p>

<pre><code>nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)
</code></pre>

<blockquote>
  <p><strong>Note:</strong> To convert the result into a list, we used list explicitly.</p>
</blockquote>

<h3 id="filter"><strong>Filter</strong></h3>

<hr>

<p>The function <strong>filter</strong> filters an iterable by removing items that don’t match a predicate (a function that returns a Boolean).  <br>
<strong>Example:</strong></p>

<pre><code>nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[22, 44]</p>
  
  <p><strong>Note:</strong> Like map, the result has to be explicitly converted to a list if you want to print it.</p>
</blockquote>

<p><strong>Example:</strong> <br>
Fill in the blanks to remove all items that are greater than 4 from the list.</p>

<pre><code>nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x &lt; 5, nums))
print(res)
</code></pre>

<h3 id="generators-1"><strong>Generators-1</strong></h3>

<hr>

<p><strong>Generators</strong> are a type of iterable, like lists or tuples.  <br>
Unlike lists, they don’t allow indexing with arbitrary indices, but they can still be iterated through with <strong>for</strong> loops.  <br>
They can be created using functions and the <strong>yield</strong> statement. <br>
<strong>Example:</strong></p>

<pre><code>def countdown():
  i=5
  while i &gt; 0:
    yield i
    i -= 1

for i in countdown():
  print(i)
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>5 <br>
  4 <br>
  3 <br>
  2 <br>
  1</p>
</blockquote>

<p>The <strong>yield</strong> statement is used to define a <strong>generator</strong>, replacing the return of a function to provide a result to its caller without destroying local variables.</p>

<h3 id="generators-2"><strong>Generators-2</strong></h3>

<hr>

<p>Due to the fact that they <strong>yield</strong> one item at a time, generators don’t have the memory restrictions of lists.  <br>
In fact, they can be <strong>infinite</strong>!</p>

<pre><code>def infinite_sevens():
  while True:
    yield 7

for i in infinite_sevens():
  print(i)
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>7 <br>
  7 <br>
  7 <br>
  7 <br>
  7 <br>
  7 <br>
  7 <br>
  …</p>
</blockquote>

<p><strong>Note:</strong> In short, <strong>generators</strong> allow you to declare a <strong>function</strong> that behaves like an iterator, i.e. it can be used in a <strong>for</strong> loop.</p>

<p><strong>Example:</strong> <br>
Fill in the blanks to create a prime number generator, that yields all prime numbers in a loop. (Consider having an is_prime function already defined):</p>

<pre><code> def get_primes():
  num = 2
  while True:
    if is_prime(num):
      yield num
    num += 1
</code></pre>

<h3 id="generators-3"><strong>Generators-3</strong></h3>

<hr>

<p>Finite generators can be converted into lists by passing them as arguments to the <strong>list</strong> function.</p>

<pre><code>def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[0, 2, 4, 6, 8, 10]</p>
</blockquote>

<p><strong>Note:</strong> Using <strong>generators</strong> results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been generated before we start to use them.</p>

<h3 id="decorators-1"><strong>Decorators-1</strong></h3>

<hr>

<p><strong>Decorators</strong> provide a way to modify functions using other functions.  <br>
This is ideal when you need to extend the functionality of functions that you don’t want to modify. <br>
<strong>Example:</strong></p>

<pre><code>def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()
</code></pre>

<p>We defined a function named <strong>decor</strong> that has a single parameter <strong>func</strong>. Inside <strong>decor</strong>, we defined a nested function named <strong>wrap</strong>. The <strong>wrap</strong> function will print a string, then call <strong>func()</strong>, and print another string. The <strong>decor</strong> function returns the <strong>wrap</strong> function as its result. <br>
We could say that the variable <strong>decorated</strong> is a decorated version of <strong>print_text</strong> - it’s <strong>print_text</strong> plus something.  <br>
In fact, if we wrote a useful <strong>decorator</strong> we might want to replace <strong>print_text</strong> with the decorated version altogether so we always got our “plus something” version of <strong>print_text</strong>.  <br>
This is done by re-assigning the variable that contains our function:</p>

<pre><code>print_text = decor(print_text)
print_text()
</code></pre>

<blockquote>
  <p>Now print_text corresponds to our decorated version.</p>
</blockquote>

<h3 id="decorators-2"><strong>Decorators-2</strong></h3>

<hr>

<p>In our previous example, we decorated our function by replacing the variable containing the function with a wrapped version.</p>

<pre><code>def print_text():
  print("Hello world!")

print_text = decor(print_text)
</code></pre>

<p>This pattern can be used at any time, to wrap any function.  <br>
Python provides support to wrap a function in a decorator by pre-pending the function definition with a <strong>decorator</strong> name and the <strong>@ symbol</strong>.  <br>
If we are defining a function we can “decorate” it with the @ symbol like:</p>

<pre><code>@decor
def print_text():
  print("Hello world!")
Try It Yourself
</code></pre>

<p>This will have the same result as the above code.</p>

<blockquote>
  <p><strong>Note:</strong> A single function can have multiple decorators.</p>
</blockquote>

<h3 id="recursion-1"><strong>Recursion-1</strong></h3>

<hr>

<p><strong>Recursion</strong> is a very important concept in functional programming.  <br>
The fundamental part of recursion is <strong>self-reference - functions calling</strong> themselves. It is used to solve problems that can be broken up into easier sub-problems of the same type.</p>

<p>A classic example of a function that is implemented recursively is the <strong>factorial function</strong>, which finds the product of all positive integers below a specified number.  <br>
For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.  <br>
Furthermore, 1! = 1. This is known as the <strong>base case</strong>, as it can be calculated without performing any more factorials.  <br>
Below is a recursive implementation of the factorial function.</p>

<pre><code>def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)

print(factorial(5))
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>120</p>
</blockquote>

<p><strong>Note:</strong> <em>The base case acts as the exit condition of the recursion.</em></p>

<h3 id="recursion-2"><strong>Recursion-2</strong></h3>

<hr>

<p>Recursive functions can be <strong>infinite</strong>, just like infinite <strong>while</strong> loops. These often occur when you forget to implement the base case.  <br>
Below is an <strong>incorrect</strong> version of the factorial function. It has <strong>no base case</strong>, so it runs until the interpreter runs out of memory and crashes.</p>

<pre><code>def factorial(x):
  return x * factorial(x-1)

print(factorial(5))
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>RuntimeError: maximum recursion depth exceeded</p>
</blockquote>

<h3 id="recursion-3"><strong>Recursion-3</strong></h3>

<hr>

<p>Recursion can also be <strong>indirect</strong>. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions. <br>
<strong>Example:</strong></p>

<pre><code>def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))
</code></pre>

<p><strong>Result</strong>:</p>

<blockquote>
  <p>True <br>
  False</p>
</blockquote>

<h3 id="sets-1"><strong>Sets-1</strong></h3>

<hr>

<p><strong>Sets</strong> are data structures, similar to <strong>lists</strong> or <strong>dictionaries</strong>. They are created using curly braces, or the <strong>set</strong> function. They share some functionality with lists, such as the use of <strong>in</strong> to check whether they contain a particular item.</p>

<pre><code>num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>True <br>
  False</p>
</blockquote>

<p><strong>Note:</strong> <em>To create an empty set, you must use <strong>set()</strong>, as <strong>{}</strong> creates an empty dictionary.</em></p>

<h3 id="sets-2"><strong>Sets-2</strong></h3>

<hr>

<p>Sets differ from lists in several ways, but share several list operations such as <strong>len</strong>.  <br>
They are unordered, which means that they can’t be indexed.  <br>
They <strong>cannot contain duplicate</strong> elements.  <br>
Due to the way they’re stored, it’s <strong>faster</strong> to check whether an item is part of a set, rather than part of a list. <br>
Instead of using <strong>append</strong> to add to a set, use <strong>add</strong>.  <br>
The method <strong>remove</strong> removes a specific element from a set; <strong>pop</strong> removes an arbitrary element.</p>

<pre><code>nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
</code></pre>

<p>Result:</p>

<blockquote>
  <p>{1, 2, 3, 4, 5, 6} <br>
  {1, 2, 4, 5, 6, -7}</p>
</blockquote>

<p><strong>Note</strong>: <em>Basic uses of <strong>sets</strong> include membership testing and the <strong>elimination of duplicate entries</strong>.</em></p>

<h3 id="sets-3"><strong>Sets-3</strong></h3>

<hr>

<p>Sets can be combined using mathematical operations. <br>
The <strong>union</strong> operator <strong>|</strong> combines two sets to form a new one containing items in either.  <br>
The <strong>intersection</strong> operator <strong>&amp;</strong> gets items only in both.  <br>
The <strong>difference</strong> operator <strong>-</strong> gets items in the first set but not in the second.  <br>
The <strong>symmetric</strong> <strong>difference</strong> operator <strong>^</strong> gets items in either set, but not both.</p>

<pre><code>first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first &amp; second)
print(first - second)
print(second - first)
print(first ^ second)
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>{1, 2, 3, 4, 5, 6, 7, 8, 9} <br>
  {4, 5, 6} <br>
  {1, 2, 3} <br>
  {8, 9, 7} <br>
  {1, 2, 3, 7, 8, 9}</p>
</blockquote>

<p>StackEdit stores your documents in your browser, which means all your documents are automatically saved locally and are accessible <strong>offline!</strong></p>

<h3 id="data-structures"><strong>Data Structures</strong></h3>

<hr>

<p>As we have seen in the previous lessons, Python supports the following data structures: <strong>lists</strong>, <strong>dictionaries</strong>, <strong>tuples</strong>, <strong>sets</strong>.</p>

<p><strong>When to use a dictionary:</strong></p>

<ul>
<li>When you need a logical association between a <strong>key:value pair</strong>.</li>
<li>When you need <strong>fast lookup</strong> for your data, based on a custom <strong>key</strong>.</li>
<li>When your data is being constantly modified. Remember, dictionaries are <strong>mutable</strong>.</li>
</ul>

<p><strong>When to use the other types:</strong></p>

<ul>
<li>Use <strong>lists</strong> if you have a collection of data that does <strong>not need random access</strong>. Try to choose lists when you need a simple, iterable collection that is modified frequently.</li>
<li>Use a <strong>set</strong> if you need <strong>uniqueness</strong> for the elements. </li>
<li>Use <strong>tuples</strong> when your data cannot change. </li>
</ul>

<blockquote>
  <p>Many times, a <strong>tuple</strong> is used in combination with a <strong>dictionary</strong>, for example, a <strong>tuple</strong> might represent a key, because it’s <strong>immutable</strong>.</p>
</blockquote>

<h3 id="itertools-1"><strong>itertools-1</strong></h3>

<hr>

<p>The module <strong>itertools</strong> is a standard library that contains several functions that are useful in functional programming.  <br>
One type of function it produces is <strong>infinite</strong> iterators.  <br>
The function <strong>count</strong> counts up infinitely from a value.  <br>
The function <strong>cycle</strong> infinitely iterates through an iterable (for instance a list or string).  <br>
The function <strong>repeat</strong> repeats an object, either infinitely or a specific number of times. <br>
<strong>Example:</strong></p>

<pre><code>from itertools import count

for i in count(3):
  print(i)
  if i &gt;=11:
    break
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>3 <br>
  4 <br>
  5 <br>
  6 <br>
  7 <br>
  8 <br>
  9 <br>
  10 <br>
  11</p>
</blockquote>

<h3 id="itertools-2"><strong>itertools-2</strong></h3>

<hr>

<p>There are many functions in <strong>itertools</strong> that operate on iterables, in a similar way to <strong>map</strong> and <strong>filter</strong>.  <br>
<strong>Some examples:</strong> <br>
<strong>takewhile</strong> - takes items from an iterable while a predicate function remains true; <br>
<strong>chain</strong> - combines several iterables into one long one;  <br>
<strong>accumulate</strong> - returns a running total of values in an iterable.</p>

<pre><code>from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x&lt;= 6, nums)))
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[0, 1, 3, 6, 10, 15, 21, 28] <br>
  [0, 1, 3, 6]</p>
</blockquote>

<h3 id="itertools-3"><strong>itertools-3</strong></h3>

<hr>

<p>There are also several combinatoric functions in <strong>itertool</strong>, such as <strong>product</strong> and <strong>permutation</strong>. <br>
These are used when you want to accomplish a task with all possible combinations of some items. <br>
<strong>Example:</strong></p>

<pre><code>from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[(‘A’, 0), (‘A’, 1), (‘B’, 0), (‘B’, 1)] <br>
  [(‘A’, ‘B’), (‘B’, ‘A’)]</p>
</blockquote>

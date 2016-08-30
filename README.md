<h1 id="python-notes"><strong><em>PYTHON NOTES</em></strong></h1>

<hr>



<h2 id="table-of-contents"><strong>Table of Contents</strong></h2>

<p><div class="toc">
<ul>
<li><a href="#python-notes">PYTHON NOTES</a><ul>
<li><a href="#table-of-contents">Table of Contents</a></li>
<li><a href="#functional-programming">Functional Programming</a><ul>
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
<li><a href="#object-oriented-programming">Object-Oriented Programming</a><ul>
<li><a href="#classes-1">Classes-1</a><ul>
<li><a href="#init">__init__</a></li>
<li><a href="#methods">Methods</a></li>
</ul>
</li>
<li><a href="#classes-2">Classes-2</a></li>
<li><a href="#inheritance-1">Inheritance-1</a></li>
<li><a href="#inheritance-2">Inheritance-2</a></li>
<li><a href="#inheritance-3">Inheritance-3</a></li>
<li><a href="#inheritance-4">Inheritance-4</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</p>

<p>Source: <a href="http://www.sololearn.com/Play/Python">SoloLearn Python Tutorial</a></p>



<h2 id="functional-programming"><strong><em>Functional Programming</em></strong></h2>



<h3 id="lambdas"><strong>Lambdas</strong></h3>

<hr>

<p>Creating a function normally (using <strong>def</strong>) assigns it to a variable automatically.  <br>
This is different from the creation of other objects - such as <strong>strings</strong> and <strong>integers</strong> - which can be created on the fly, without assigning them to a variable.  <br>
The same is possible with <strong>functions</strong>, provided that they are created using <strong>lambda syntax</strong>. Functions created this way are known as <strong>anonymous</strong>. <br>
This approach is most commonly used when passing a simple function as an argument to another function. The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a <strong>colon</strong>, and the <strong>expression</strong> to <strong>evaluate</strong> and <strong>return</strong>.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">my_func</span><span class="hljs-params">(f, arg)</span>:</span>
  <span class="hljs-keyword">return</span> f(arg)

my_func(<span class="hljs-keyword">lambda</span> x: <span class="hljs-number">2</span>*x*x, <span class="hljs-number">5</span>)</code></pre>

<blockquote>
  <p><strong>Note:</strong> Lambda functions get their name from lambda calculus, which is a model of computation invented by Alonzo Church.</p>
</blockquote>



<h3 id="map"><strong>Map</strong></h3>

<hr>

<p>The built-in functions <strong>map</strong> and <strong>filter</strong> are very useful <strong>higher-order functions</strong> that operate on <strong>lists</strong> (or similar objects called iterables).  <br>
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.</p>

<p><strong>Example</strong>:</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">add_five</span><span class="hljs-params">(x)</span>:</span>
  <span class="hljs-keyword">return</span> x + <span class="hljs-number">5</span>

nums = [<span class="hljs-number">11</span>, <span class="hljs-number">22</span>, <span class="hljs-number">33</span>, <span class="hljs-number">44</span>, <span class="hljs-number">55</span>]
result = list(map(add_five, nums))
print(result)
</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[16, 27, 38, 49, 60]</p>
</blockquote>

<p>We could have achieved the same result more easily by using <strong>lambda syntax</strong>.</p>



<pre class="prettyprint"><code class=" hljs applescript">nums = [<span class="hljs-number">11</span>, <span class="hljs-number">22</span>, <span class="hljs-number">33</span>, <span class="hljs-number">44</span>, <span class="hljs-number">55</span>]

<span class="hljs-constant">result</span> = <span class="hljs-type">list</span>(map(lambda x: x+<span class="hljs-number">5</span>, nums))
print(<span class="hljs-constant">result</span>)</code></pre>

<blockquote>
  <p><strong>Note:</strong> To convert the result into a list, we used list explicitly.</p>
</blockquote>



<h3 id="filter"><strong>Filter</strong></h3>

<hr>

<p>The function <strong>filter</strong> filters an iterable by removing items that don’t match a predicate (a function that returns a Boolean).  <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs mel">nums = [<span class="hljs-number">11</span>, <span class="hljs-number">22</span>, <span class="hljs-number">33</span>, <span class="hljs-number">44</span>, <span class="hljs-number">55</span>]
res = list(<span class="hljs-keyword">filter</span>(lambda x: x<span class="hljs-variable">%2</span>==<span class="hljs-number">0</span>, nums))
<span class="hljs-keyword">print</span>(res)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[22, 44]</p>
  
  <p><strong>Note:</strong> Like map, the result has to be explicitly converted to a list if you want to print it.</p>
</blockquote>

<p><strong>Example:</strong> <br>
Fill in the blanks to remove all items that are greater than 4 from the list.</p>



<pre class="prettyprint"><code class=" hljs php">nums = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">5</span>, <span class="hljs-number">8</span>, <span class="hljs-number">3</span>, <span class="hljs-number">0</span>, <span class="hljs-number">7</span>]
res = <span class="hljs-keyword">list</span>(filter(lambda x: x &lt; <span class="hljs-number">5</span>, nums))
<span class="hljs-keyword">print</span>(res)</code></pre>



<h3 id="generators-1"><strong>Generators-1</strong></h3>

<hr>

<p><strong>Generators</strong> are a type of iterable, like lists or tuples.  <br>
Unlike lists, they don’t allow indexing with arbitrary indices, but they can still be iterated through with <strong>for</strong> loops.  <br>
They can be created using functions and the <strong>yield</strong> statement. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">countdown</span><span class="hljs-params">()</span>:</span>
  i=<span class="hljs-number">5</span>
  <span class="hljs-keyword">while</span> i &gt; <span class="hljs-number">0</span>:
    <span class="hljs-keyword">yield</span> i
    i -= <span class="hljs-number">1</span>

<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> countdown():
  print(i)</code></pre>

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



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">infinite_sevens</span><span class="hljs-params">()</span>:</span>
  <span class="hljs-keyword">while</span> <span class="hljs-keyword">True</span>:
    <span class="hljs-keyword">yield</span> <span class="hljs-number">7</span>

<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> infinite_sevens():
  print(i)</code></pre>

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



<pre class="prettyprint"><code class=" hljs python"> <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_primes</span><span class="hljs-params">()</span>:</span>
  num = <span class="hljs-number">2</span>
  <span class="hljs-keyword">while</span> <span class="hljs-keyword">True</span>:
    <span class="hljs-keyword">if</span> is_prime(num):
      <span class="hljs-keyword">yield</span> num
    num += <span class="hljs-number">1</span></code></pre>



<h3 id="generators-3"><strong>Generators-3</strong></h3>

<hr>

<p>Finite generators can be converted into lists by passing them as arguments to the <strong>list</strong> function.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">numbers</span><span class="hljs-params">(x)</span>:</span>
  <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(x):
    <span class="hljs-keyword">if</span> i % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>:
      <span class="hljs-keyword">yield</span> i

print(list(numbers(<span class="hljs-number">11</span>)))</code></pre>

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



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">decor</span><span class="hljs-params">(func)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">wrap</span><span class="hljs-params">()</span>:</span>
    print(<span class="hljs-string">"============"</span>)
    func()
    print(<span class="hljs-string">"============"</span>)
  <span class="hljs-keyword">return</span> wrap

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print_text</span><span class="hljs-params">()</span>:</span>
  print(<span class="hljs-string">"Hello world!"</span>)

decorated = decor(print_text)
decorated()</code></pre>

<p>We defined a function named <strong>decor</strong> that has a single parameter <strong>func</strong>. Inside <strong>decor</strong>, we defined a nested function named <strong>wrap</strong>. The <strong>wrap</strong> function will print a string, then call <strong>func()</strong>, and print another string. The <strong>decor</strong> function returns the <strong>wrap</strong> function as its result. <br>
We could say that the variable <strong>decorated</strong> is a decorated version of <strong>print_text</strong> - it’s <strong>print_text</strong> plus something.  <br>
In fact, if we wrote a useful <strong>decorator</strong> we might want to replace <strong>print_text</strong> with the decorated version altogether so we always got our “plus something” version of <strong>print_text</strong>.  <br>
This is done by re-assigning the variable that contains our function:</p>



<pre class="prettyprint"><code class=" hljs fix"><span class="hljs-attribute">print_text </span>=<span class="hljs-string"> decor(print_text)
print_text()</span></code></pre>

<blockquote>
  <p>Now print_text corresponds to our decorated version.</p>
</blockquote>



<h3 id="decorators-2"><strong>Decorators-2</strong></h3>

<hr>

<p>In our previous example, we decorated our function by replacing the variable containing the function with a wrapped version.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print_text</span><span class="hljs-params">()</span>:</span>
  print(<span class="hljs-string">"Hello world!"</span>)

print_text = decor(print_text)</code></pre>

<p>This pattern can be used at any time, to wrap any function.  <br>
Python provides support to wrap a function in a decorator by pre-pending the function definition with a <strong>decorator</strong> name and the <strong>@ symbol</strong>.  <br>
If we are defining a function we can “decorate” it with the @ symbol like:</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-decorator">@decor</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print_text</span><span class="hljs-params">()</span>:</span>
  print(<span class="hljs-string">"Hello world!"</span>)
Try It Yourself</code></pre>

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



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">factorial</span><span class="hljs-params">(x)</span>:</span>
  <span class="hljs-keyword">if</span> x == <span class="hljs-number">1</span>:
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
  <span class="hljs-keyword">else</span>: 
    <span class="hljs-keyword">return</span> x * factorial(x-<span class="hljs-number">1</span>)

print(factorial(<span class="hljs-number">5</span>))</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>120</p>
</blockquote>

<p><strong>Note:</strong> <em>The base case acts as the exit condition of the recursion.</em></p>



<h3 id="recursion-2"><strong>Recursion-2</strong></h3>

<hr>

<p>Recursive functions can be <strong>infinite</strong>, just like infinite <strong>while</strong> loops. These often occur when you forget to implement the base case.  <br>
Below is an <strong>incorrect</strong> version of the factorial function. It has <strong>no base case</strong>, so it runs until the interpreter runs out of memory and crashes.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">factorial</span><span class="hljs-params">(x)</span>:</span>
  <span class="hljs-keyword">return</span> x * factorial(x-<span class="hljs-number">1</span>)

print(factorial(<span class="hljs-number">5</span>))</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>RuntimeError: maximum recursion depth exceeded</p>
</blockquote>



<h3 id="recursion-3"><strong>Recursion-3</strong></h3>

<hr>

<p>Recursion can also be <strong>indirect</strong>. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">is_even</span><span class="hljs-params">(x)</span>:</span>
  <span class="hljs-keyword">if</span> x == <span class="hljs-number">0</span>:
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">True</span>
  <span class="hljs-keyword">else</span>:
    <span class="hljs-keyword">return</span> is_odd(x-<span class="hljs-number">1</span>)

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">is_odd</span><span class="hljs-params">(x)</span>:</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">not</span> is_even(x)


print(is_odd(<span class="hljs-number">17</span>))
print(is_even(<span class="hljs-number">23</span>))</code></pre>

<p><strong>Result</strong>:</p>

<blockquote>
  <p>True <br>
  False</p>
</blockquote>



<h3 id="sets-1"><strong>Sets-1</strong></h3>

<hr>

<p><strong>Sets</strong> are data structures, similar to <strong>lists</strong> or <strong>dictionaries</strong>. They are created using curly braces, or the <strong>set</strong> function. They share some functionality with lists, such as the use of <strong>in</strong> to check whether they contain a particular item.</p>



<pre class="prettyprint"><code class=" hljs bash">num_<span class="hljs-keyword">set</span> = {<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>}
word_<span class="hljs-keyword">set</span> = <span class="hljs-keyword">set</span>([<span class="hljs-string">"spam"</span>, <span class="hljs-string">"eggs"</span>, <span class="hljs-string">"sausage"</span>])

print(<span class="hljs-number">3</span> <span class="hljs-keyword">in</span> num_<span class="hljs-keyword">set</span>)
print(<span class="hljs-string">"spam"</span> not <span class="hljs-keyword">in</span> word_<span class="hljs-keyword">set</span>)</code></pre>

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



<pre class="prettyprint"><code class=" hljs erlang">nums = <span class="hljs-tuple">{<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>}</span>
<span class="hljs-function"><span class="hljs-title">print</span><span class="hljs-params">(nums)</span>
<span class="hljs-title">nums</span>.<span class="hljs-title">add</span><span class="hljs-params">(-<span class="hljs-number">7</span>)</span>
<span class="hljs-title">nums</span>.<span class="hljs-title">remove</span><span class="hljs-params">(<span class="hljs-number">3</span>)</span>
<span class="hljs-title">print</span><span class="hljs-params">(nums)</span></span></code></pre>

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



<pre class="prettyprint"><code class=" hljs livecodeserver"><span class="hljs-keyword">first</span> = {<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>}
<span class="hljs-keyword">second</span> = {<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>}

print(<span class="hljs-keyword">first</span> | <span class="hljs-keyword">second</span>)
print(<span class="hljs-keyword">first</span> &amp; <span class="hljs-keyword">second</span>)
print(<span class="hljs-keyword">first</span> - <span class="hljs-keyword">second</span>)
print(<span class="hljs-keyword">second</span> - <span class="hljs-keyword">first</span>)
print(<span class="hljs-keyword">first</span> ^ <span class="hljs-keyword">second</span>)</code></pre>

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



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-keyword">from</span> itertools <span class="hljs-keyword">import</span> count

<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> count(<span class="hljs-number">3</span>):
  print(i)
  <span class="hljs-keyword">if</span> i &gt;=<span class="hljs-number">11</span>:
    <span class="hljs-keyword">break</span></code></pre>

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



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-keyword">from</span> itertools <span class="hljs-keyword">import</span> accumulate, takewhile

nums = list(accumulate(range(<span class="hljs-number">8</span>)))
print(nums)
print(list(takewhile(<span class="hljs-keyword">lambda</span> x: x&lt;= <span class="hljs-number">6</span>, nums)))</code></pre>

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



<pre class="prettyprint"><code class=" hljs php">from itertools import product, permutations

letters = (<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>)
<span class="hljs-keyword">print</span>(<span class="hljs-keyword">list</span>(product(letters, range(<span class="hljs-number">2</span>))))
<span class="hljs-keyword">print</span>(<span class="hljs-keyword">list</span>(permutations(letters))) </code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>[(‘A’, 0), (‘A’, 1), (‘B’, 0), (‘B’, 1)] <br>
  [(‘A’, ‘B’), (‘B’, ‘A’)]</p>
</blockquote>



<h2 id="object-oriented-programming"><strong><em>Object-Oriented Programming</em></strong></h2>



<h3 id="classes-1"><strong>Classes-1</strong></h3>

<hr>

<p>We have previously looked at two paradigms of programming - <strong>imperative</strong> (using statements, loops, and functions as subroutines), and <strong>functional</strong> (using pure functions, higher-order functions, and recursion).</p>

<p>Another very popular paradigm is <strong>object**</strong>-<strong>**oriented</strong> <strong>programming</strong> (<strong>OOP</strong>). <br>
Objects are created using <strong>classes</strong>, which are actually the focal point of OOP. <br>
The <strong>class</strong> describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object’s blueprint, description, or definition. <br>
You can use the same class as a blueprint for creating multiple different objects. </p>

<p>Classes are created using the keyword <strong>class</strong> and an indented block, which contains class <strong>methods</strong> (which are functions).  <br>
Below is an example of a simple class and its objects.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, color, legs)</span>:</span>
    self.color = color
    self.legs = legs

felix = Cat(<span class="hljs-string">"ginger"</span>, <span class="hljs-number">4</span>)
rover = Cat(<span class="hljs-string">"dog-colored"</span>, <span class="hljs-number">4</span>)
stumpy = Cat(<span class="hljs-string">"brown"</span>, <span class="hljs-number">3</span>)</code></pre>

<blockquote>
  <p><strong>Note:</strong> This code defines a class named <strong>Cat</strong>, which has two attributes: <strong>color</strong> and <strong>legs</strong>. <br>
  Then the class is used to create 3 separate objects of that class.</p>
</blockquote>



<h4 id="init"><strong><code>__init__</code></strong></h4>

<hr>

<p>The <strong>init</strong> method is the most important method in a class.  <br>
This is called when an instance (object) of the class is created, using the class name as a function.</p>

<p>All methods must have <strong>self</strong> as their first parameter, although it isn’t explicitly passed, Python adds the <strong>self</strong> argument to the list for you; you do not need to include it when you call the methods. Within a method definition, <strong>self</strong> refers to the instance calling the method.</p>

<p>Instances of a class have <strong>attributes</strong>, which are pieces of data associated with them. <br>
In this example, <strong>Cat</strong> instances have attributes <strong>color</strong> and <strong>legs</strong>. These can be accessed by putting a <strong>dot</strong>, and the attribute name after an instance.  <br>
In an <strong>init</strong> method, <strong>self.attribute</strong> can therefore be used to set the initial value of an instance’s attributes. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, color, legs)</span>:</span>
    self.color = color
    self.legs = legs

felix = Cat(<span class="hljs-string">"ginger"</span>, <span class="hljs-number">4</span>)
print(felix.color)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p><strong>Note:</strong> ginger</p>
</blockquote>

<p><strong>Note:</strong> In the example above, the <strong>init</strong> method takes two arguments and assigns them to the object’s attributes. The <strong>init</strong> method is called the class <strong>constructor</strong>.</p>



<h4 id="methods"><strong>Methods</strong></h4>

<hr>

<p>Classes can have other <strong>methods</strong> defined to add functionality to them.  <br>
Remember, that all methods must have <strong>self</strong> as their first <strong>parameter</strong>. <br>
These methods are accessed using the same <strong>dot syntax</strong> as attributes.  <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, name, color)</span>:</span>
    self.name = name
    self.color = color

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">bark</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"Woof!"</span>)

fido = Dog(<span class="hljs-string">"Fido"</span>, <span class="hljs-string">"brown"</span>)
print(fido.name)
fido.bark()</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>Fido <br>
  Woof!</p>
</blockquote>

<p>Classes can also have <strong>class attributes</strong>, created by assigning variables within the body of the class. These can be accessed either from instances of the class, or the class itself. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span>:</span>
  legs = <span class="hljs-number">4</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, name, color)</span>:</span>
    self.name = name
    self.color = color

fido = Dog(<span class="hljs-string">"Fido"</span>, <span class="hljs-string">"brown"</span>)
print(fido.legs)
print(Dog.legs)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>4 <br>
  4</p>
</blockquote>

<p><strong>NOTE:</strong> Class attributes are shared by all instances of the class.</p>



<h3 id="classes-2"><strong>Classes-2</strong></h3>

<hr>

<p>Trying to access an attribute of an instance that isn’t defined causes an <strong>AttributeError</strong>. This also applies when you call an <strong>undefined</strong> method.</p>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rectangle</span>:</span> 
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, width, height)</span>:</span>
    self.width = width
    self.height = height

rect = Rectangle(<span class="hljs-number">7</span>, <span class="hljs-number">8</span>)
print(rect.color)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>AttributeError: ‘Rectangle’ object has no attribute ‘color’</p>
</blockquote>



<h3 id="inheritance-1"><strong>Inheritance-1</strong></h3>

<hr>

<p><strong>Inheritance</strong> provides a way to share functionality between classes.  <br>
Imagine several classes, <strong>Cat</strong>, <strong>Dog</strong>, <strong>Rabbit</strong> and so on. Although they may differ in some ways (only <strong>Dog</strong> might have the method <strong>bark</strong>), they are likely to be similar in others (all having the attributes <strong>color</strong> and <strong>name</strong>).  <br>
This similarity can be expressed by making them all inherit from a <strong>superclass</strong> <strong>Animal</strong>, which contains the shared functionality.  <br>
To inherit a class from another class, put the superclass name in parentheses after the class name. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span>:</span> 
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, name, color)</span>:</span>
    self.name = name
    self.color = color

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span><span class="hljs-params">(Animal)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">purr</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"Purr..."</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span><span class="hljs-params">(Animal)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">bark</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"Woof!"</span>)

fido = Dog(<span class="hljs-string">"Fido"</span>, <span class="hljs-string">"brown"</span>)
print(fido.color)
fido.bark()</code></pre>

<p><strong>Result</strong>:</p>

<blockquote>
  <p>brown <br>
  Woof!</p>
</blockquote>



<h3 id="inheritance-2"><strong>Inheritance-2</strong></h3>

<hr>

<p>A class that inherits from another class is called a <strong>subclass</strong>. <br>
A class that is inherited from is called a <strong>superclass</strong>. <br>
If a class inherits from another with the same attributes or methods, it overrides them.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Wolf</span>:</span> 
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, name, color)</span>:</span>
    self.name = name
    self.color = color

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">bark</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"Grr..."</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span><span class="hljs-params">(Wolf)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">bark</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"Woof"</span>)

husky = Dog(<span class="hljs-string">"Max"</span>, <span class="hljs-string">"grey"</span>)
husky.bark()</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>Woof</p>
</blockquote>

<p><strong>Note:</strong> In the example above, Wolf is the superclass, Dog is the subclass.</p>



<h3 id="inheritance-3"><strong>Inheritance-3</strong></h3>

<hr>

<p>Inheritance can also be <strong>indirect</strong>. One class can inherit from another, and that class can inherit from a third class.  <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">method</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"A method"</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span><span class="hljs-params">(A)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">another_method</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"B method"</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span><span class="hljs-params">(B)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">third_method</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-string">"C method"</span>)

c = C()
c.method()
c.another_method()
c.third_method()</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>A method <br>
  B method <br>
  C method</p>
</blockquote>

<p><strong>Note:</strong> However, circular inheritance is not possible.</p>



<h3 id="inheritance-4"><strong>Inheritance-4</strong></h3>

<hr>

<p>The function <strong>super</strong> is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object’s superclass. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">spam</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-number">1</span>)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span><span class="hljs-params">(A)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">spam</span><span class="hljs-params">(self)</span>:</span>
    print(<span class="hljs-number">2</span>)
    super().spam()

B().spam()</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>2 <br>
  1    </p>
</blockquote>

<p><strong>Note:</strong> <strong><em>super().spam()</em></strong> calls the <strong>spam</strong> method of the superclass.</p>



<h3 id="magic-methods-1"><strong>Magic Methods-1</strong></h3>

<hr>

<p><strong>Magic methods</strong> are special methods which have <strong>double underscores</strong> at the beginning and end of their names.  <br>
They are also known as <strong>dunders.</strong>  <br>
So far, the only one we have encountered is <code>__init__</code>, but there are several others.  <br>
They are used to create functionality that can’t be represented as a normal method. </p>

<p>One common use of them is <strong>operator overloading</strong>.  <br>
This means defining operators for custom classes that allow operators such as <strong>+ and *</strong> to be used on them. <br>
An example magic method is <code>__add__</code> for <strong>+</strong>.</p>

<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vector2D</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, x, y)</span>:</span>
    self.x = x
    self.y = y
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__add__</span><span class="hljs-params">(self, other)</span>:</span>
    <span class="hljs-keyword">return</span> Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(<span class="hljs-number">5</span>, <span class="hljs-number">7</span>)
second = Vector2D(<span class="hljs-number">3</span>, <span class="hljs-number">9</span>)
result = first + second
print(result.x)
print(result.y)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>8 <br>
  16    </p>
</blockquote>

<p>The <code>__add__</code> method allows for the definition of a custom behavior for the <strong>+ operator</strong> in our class.  <br>
As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result. <br>
Once it’s defined, we can add two objects of the class together.</p>



<h3 id="magic-methods-2"><strong>Magic Methods-2</strong></h3>

<hr>

<p>More magic methods for common operators: <br>
<code>__sub__</code> for <strong>-</strong> <br>
<code>__mul__</code> for <strong>*</strong> <br>
<code>__truediv__</code> for <strong>/</strong> <br>
<code>__floordiv__</code> for <strong>//</strong> <br>
<code>__mod__</code> for <strong>%</strong> <br>
<code>__pow__</code> for <strong>**</strong> <br>
<code>__and__</code> for <strong>&amp;</strong> <br>
<code>__xor__</code> for <strong>^</strong> <br>
<code>__or__</code> for <strong>|</strong></p>

<p>The expression <code>x + y</code> is translated into <code>x.__add__(y)</code>.  <br>
However, if x hasn’t implemented <code>__add__</code>, and x and y are of different types, then <code>y.__radd__(x)</code> is called.  <br>
There are equivalent r methods for all magic methods just mentioned. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpecialString</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, cont)</span>:</span>
    self.cont = cont

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__truediv__</span><span class="hljs-params">(self, other)</span>:</span>
    line = <span class="hljs-string">"="</span> * len(other.cont)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"\n"</span>.join([self.cont, line, other.cont])

spam = SpecialString(<span class="hljs-string">"spam"</span>)
hello = SpecialString(<span class="hljs-string">"Hello world!"</span>)
print(spam / hello)</code></pre>

<p><strong>Result:</strong>  </p>



<pre class="prettyprint"><code class=" hljs asciidoc"><span class="hljs-header">spam
============</span>
Hello world!</code></pre>

<p><strong>Note:</strong> In the example above, we defined the <strong>division</strong> operation for our class <strong>SpecialString</strong>.</p>

<h3 id="magic-methods-3"><strong>Magic Methods-3</strong></h3>

<hr>

<p>Python also provides magic methods for comparisons. <br>
<code>__lt__</code> for <strong>&lt;</strong> <br>
<code>__le__</code> for <strong>&lt;=</strong> <br>
<code>__eq__</code> for <strong>==</strong> <br>
<code>__ne__</code> for <strong>!=</strong> <br>
<code>__gt__</code> for <strong>&gt;</strong> <br>
<code>__ge__</code> for <strong>&gt;=</strong></p>

<p>If <code>__ne__</code> is not implemented, it returns the opposite of <code>__eq__</code>.  <br>
<strong>Note:</strong> There are no other relationships between the other operators. <br>
<strong>Example:</strong></p>

<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpecialString</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, cont)</span>:</span>
    self.cont = cont

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__gt__</span><span class="hljs-params">(self, other)</span>:</span>
    <span class="hljs-keyword">for</span> index <span class="hljs-keyword">in</span> range(len(other.cont)+<span class="hljs-number">1</span>):
      result = other.cont[:index] + <span class="hljs-string">"&gt;"</span> + self.cont
      result += <span class="hljs-string">"&gt;"</span> + other.cont[index:]
      print(result)

spam = SpecialString(<span class="hljs-string">"spam"</span>)
eggs = SpecialString(<span class="hljs-string">"eggs"</span>)
spam &gt; eggs</code></pre>

<p><strong>Result:</strong></p>



<pre class="prettyprint"><code class=" hljs ">&gt;spam&gt;eggs
e&gt;spam&gt;ggs
eg&gt;spam&gt;gs
egg&gt;spam&gt;s
eggs&gt;spam&gt;</code></pre>

<p><strong>Note:</strong> As you can see, you can define any custom behavior for the overloaded operators.</p>



<h3 id="magic-methods-4"><strong>Magic Methods-4</strong></h3>

<hr>

<p>There are several magic methods for making classes act like containers. <br>
<code>__len__</code> for <strong>len()</strong> <br>
<code>__getitem__</code> for <strong>indexing</strong> <br>
<code>__setitem__</code> for <strong>assigning</strong> to indexed values <br>
<code>__delitem__</code> for <strong>deleting</strong> indexed values <br>
<code>__iter__</code> for <strong>iteration</strong> over objects (e.g., in for loops) <br>
<code>__contains__</code> for <strong>in</strong></p>

<p>There are many other magic methods that we won’t cover here, such as <code>__call__</code> for calling objects as functions, and <code>__int__</code>, <code>__str__</code>, and the like, for converting objects to built-in types.  <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-keyword">import</span> random

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VagueList</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, cont)</span>:</span>
    self.cont = cont

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__getitem__</span><span class="hljs-params">(self, index)</span>:</span>
    <span class="hljs-keyword">return</span> self.cont[index + random.randint(-<span class="hljs-number">1</span>, <span class="hljs-number">1</span>)]

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__len__</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">return</span> random.randint(<span class="hljs-number">0</span>, len(self.cont)*<span class="hljs-number">2</span>)

vague_list = VagueList([<span class="hljs-string">"A"</span>, <span class="hljs-string">"B"</span>, <span class="hljs-string">"C"</span>, <span class="hljs-string">"D"</span>, <span class="hljs-string">"E"</span>])
print(len(vague_list))
print(len(vague_list))
print(vague_list[<span class="hljs-number">2</span>])
print(vague_list[<span class="hljs-number">2</span>])</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>6 <br>
  7 <br>
  D <br>
  C</p>
</blockquote>

<p><strong>Note:</strong> We have overridden the <strong>len()</strong> function for the class VagueList to return a random number. <br>
The indexing function also returns a random item in a range from the list, based on the expression.</p>



<h3 id="object-lifecycle-1"><strong>Object Lifecycle-1</strong></h3>

<hr>

<p>The lifecycle of an object is made up of its <strong>creation</strong>, <strong>manipulation</strong>, and <strong>destruction</strong>.</p>

<p>The first stage of the life-cycle of an object is the <strong>definition</strong> of the class to which it belongs. <br>
The next stage is the <strong>instantiation</strong> of an instance, when <code>__init__</code> is called. Memory is allocated to store the instance. Just before this occurs, the <code>__new__</code> method of the class is called. This is usually overridden only in special cases.</p>

<blockquote>
  <p><strong>Note:</strong> After this has happened, the object is ready to be used. Other code can then interact with the object, by calling functions on <br>
  it and accessing its attributes.  Eventually, it will finish being <br>
  used, and can be <strong>destroyed</strong>.</p>
</blockquote>



<h3 id="object-lifecycle-2"><strong>Object Lifecycle-2</strong></h3>

<hr>

<p>When an object is <strong>destroyed</strong>, the memory allocated to it is freed up, and can be used for other purposes. <br>
Destruction of an object occurs when its <strong>reference count</strong> reaches zero. Reference count is the number of variables and other elements that refer to an object. <br>
If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted.</p>

<p>In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well.  <br>
The del statement reduces the reference count of an object by one, and this often leads to its deletion. <br>
The magic method for the <strong>del</strong> statement is <code>__del__</code>.  <br>
The process of deleting objects when they are no longer needed is called <strong>garbage collection</strong>. <br>
In summary, an object’s reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object’s reference count decreases when it’s deleted with <strong>del</strong>, its reference is reassigned, or its reference goes out of scope. When an object’s reference count reaches zero, Python automatically deletes it. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs sql">a = 42  # <span class="hljs-operator"><span class="hljs-keyword">Create</span> object &lt;<span class="hljs-number">42</span>&gt;
b = a  # Increase ref. <span class="hljs-aggregate">count</span>  <span class="hljs-keyword">of</span> &lt;<span class="hljs-number">42</span>&gt; 
c = [a]  # Increase ref. <span class="hljs-aggregate">count</span>  <span class="hljs-keyword">of</span> &lt;<span class="hljs-number">42</span>&gt; 

del a  # Decrease ref. <span class="hljs-aggregate">count</span>  <span class="hljs-keyword">of</span> &lt;<span class="hljs-number">42</span>&gt;
b = <span class="hljs-number">100</span>  # Decrease ref. <span class="hljs-aggregate">count</span>  <span class="hljs-keyword">of</span> &lt;<span class="hljs-number">42</span>&gt; 
c[<span class="hljs-number">0</span>] = -<span class="hljs-number">1</span>  # Decrease ref. <span class="hljs-aggregate">count</span>  <span class="hljs-keyword">of</span> &lt;<span class="hljs-number">42</span>&gt;</span></code></pre>

<blockquote>
  <p><strong>Note:</strong> Lower level languages like C don’t have this kind of automatic memory management.</p>
</blockquote>



<h3 id="data-hiding-1"><strong>Data Hiding-1</strong></h3>

<hr>

<p>A key part of object-oriented programming is <strong>encapsulation</strong>, which involves packaging of related variables and functions into a single easy-to-use object - an instance of a class. <br>
A related concept is <strong>data hiding</strong>, which states that implementation details of a class should be hidden, and a clean standard interface be presented for those who want to use the class.  <br>
In other programming languages, this is usually done with private methods and attributes, which block external access to certain methods and attributes in a class.</p>

<p>The Python philosophy is slightly different. It is often stated as <strong>“we are all consenting adults here”</strong>, meaning that you shouldn’t put arbitrary restrictions on accessing parts of a class. Hence there are no ways of enforcing a method or attribute be strictly private. </p>

<blockquote>
  <p><strong>Note:</strong> However, there are ways to discourage people from accessing parts of a class, such as by denoting that it is an implementation <br>
  detail, and should be used at their own risk.</p>
</blockquote>



<h3 id="data-hiding-2"><strong>Data Hiding-2</strong></h3>

<hr>

<p><strong>Weakly private</strong> methods and attributes have a <strong>single underscore</strong> at the beginning. <br>
This signals that they are private, and shouldn’t be used by external code. However, it is mostly only a convention, and does not stop external code from accessing them.  <br>
Its only actual effect is that <strong>from module_name import *</strong> won’t import variables that start with a single underscore. <br>
<strong>Example:</strong></p>

<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Queue</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, contents)</span>:</span>
    self._hiddenlist = list(contents)

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">push</span><span class="hljs-params">(self, value)</span>:</span>
    self._hiddenlist.insert(<span class="hljs-number">0</span>, value)

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pop</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">return</span> self._hiddenlist.pop(-<span class="hljs-number">1</span>)

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__repr__</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Queue({})"</span>.format(self._hiddenlist)

queue = Queue([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>])
print(queue)
queue.push(<span class="hljs-number">0</span>)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>Queue([1, 2, 3]) <br>
  Queue([0, 1, 2, 3]) <br>
  Queue([0, 1, 2]) <br>
  [0, 1, 2]</p>
</blockquote>

<p><strong>Note:</strong> In the code above, the attribute <code>_hiddenlist</code> is marked as private, but it can still be accessed in the outside code. <br>
The <code>__repr__</code> magic method is used for string representation of the instance.</p>



<h3 id="data-hiding-3"><strong>Data Hiding-3</strong></h3>

<hr>

<p><strong>Strongly private</strong> methods and attributes have a <strong>double underscore</strong> at the beginning of their names. This causes their names to be mangled, which means that they can’t be accessed from outside the class.  <br>
The purpose of this isn’t to ensure that they are kept private, but to avoid bugs if there are subclasses that have methods or attributes with the same names. <br>
Name mangled methods can still be accessed externally, but by a different name. The method <code>__privatemethod</code> of class <strong>Spam</strong> could be accessed externally with <code>_Spam__privatemethod</code>. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Spam</span>:</span>
  __egg = <span class="hljs-number">7</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print_egg</span><span class="hljs-params">(self)</span>:</span>
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>7 <br>
  7 <br>
  AttributeError: ‘Spam’ object has no attribute ‘__egg’</p>
</blockquote>

<p><strong>Note:</strong> Basically, Python protects those members by internally changing the name to include the class name.</p>



<h3 id="class-methods"><strong>Class Methods</strong></h3>

<hr>

<p>Methods of objects we’ve looked at so far are called by an instance of a class, which is then passed to the <strong>self</strong> parameter of the method. <br>
<strong>Class methods</strong> are different - they are called by a class, which is passed to the <strong>cls</strong> parameter of the method.  <br>
A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.  <br>
Class methods are marked with a <strong>classmethod</strong> <strong>decorator</strong>. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rectangle</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, width, height)</span>:</span>
    self.width = width
    self.height = height

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">calculate_area</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">return</span> self.width * self.height

  <span class="hljs-decorator">@classmethod</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">new_square</span><span class="hljs-params">(cls, side_length)</span>:</span>
    <span class="hljs-keyword">return</span> cls(side_length, side_length)

square = Rectangle.new_square(<span class="hljs-number">5</span>)
print(square.calculate_area())</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>25</p>
</blockquote>

<p><strong>new_square</strong> is a class method and is called on the class, rather than on an instance of the class. It returns a new object of the class <strong>cls</strong>. <br>
Technically, the parameters <strong>self</strong> and <strong>cls</strong> are just conventions; they could be changed to anything else. However, they are universally followed, so it is wise to stick to using them.</p>



<h3 id="static-methods"><strong>Static Methods</strong></h3>

<hr>

<p><strong>Static methods</strong> are similar to class methods, except they don’t receive any additional arguments; they are identical to normal functions that belong to a class.  <br>
They are marked with the <strong>staticmethod decorator.</strong> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Pizza</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, toppings)</span>:</span>
    self.toppings = toppings

  <span class="hljs-decorator">@staticmethod</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">validate_topping</span><span class="hljs-params">(topping)</span>:</span>
    <span class="hljs-keyword">if</span> topping == <span class="hljs-string">"pineapple"</span>:
      <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">"No pineapples!"</span>)
    <span class="hljs-keyword">else</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">True</span>

ingredients = [<span class="hljs-string">"cheese"</span>, <span class="hljs-string">"onions"</span>, <span class="hljs-string">"spam"</span>]
<span class="hljs-keyword">if</span> all(Pizza.validate_topping(i) <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> ingredients):
  pizza = Pizza(ingredients) </code></pre>

<blockquote>
  <p><strong>Note:</strong> Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.</p>
</blockquote>



<h3 id="properties-1"><strong>Properties-1</strong></h3>

<hr>

<p><strong>Properties</strong> provide a way of customizing access to instance attributes.  <br>
They are created by putting the <strong>property decorator</strong> above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead.  <br>
One common use of a property is to make an attribute <strong>read-only</strong>. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Pizza</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, toppings)</span>:</span>
    self.toppings = toppings

  <span class="hljs-decorator">@property</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pineapple_allowed</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">False</span>

pizza = Pizza([<span class="hljs-string">"cheese"</span>, <span class="hljs-string">"tomato"</span>])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = <span class="hljs-keyword">True</span></code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>False</p>
  
  <p>AttributeError: can’t set attribute</p>
</blockquote>



<h3 id="properties-2"><strong>Properties-2</strong></h3>

<hr>

<p>Properties can also be set by defining <strong>setter/getter</strong> functions. <br>
The <strong>setter</strong> function sets the corresponding property’s value. <br>
The <strong>getter</strong> gets the value. <br>
To define a <strong>setter</strong>, you need to use a <strong>decorator</strong> of the same name as the property, followed by a <strong>dot</strong> and the <strong>setter</strong> keyword. <br>
The same applies to defining <strong>getter</strong> functions. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Pizza</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, toppings)</span>:</span>
    self.toppings = toppings
    self._pineapple_allowed = <span class="hljs-keyword">False</span>

  <span class="hljs-decorator">@property</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pineapple_allowed</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">return</span> self._pineapple_allowed

  <span class="hljs-decorator">@pineapple_allowed.setter</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pineapple_allowed</span><span class="hljs-params">(self, value)</span>:</span>
    <span class="hljs-keyword">if</span> value:
      password = input(<span class="hljs-string">"Enter the password: "</span>)
      <span class="hljs-keyword">if</span> password == <span class="hljs-string">"Sw0rdf1sh!"</span>:
        self._pineapple_allowed = value
      <span class="hljs-keyword">else</span>:
        <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">"Alert! Intruder!"</span>)

pizza = Pizza([<span class="hljs-string">"cheese"</span>, <span class="hljs-string">"tomato"</span>])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = <span class="hljs-keyword">True</span>
print(pizza.pineapple_allowed)</code></pre>

<p><strong>Result:</strong></p>

<blockquote>
  <p>False <br>
  Enter the password to permit pineapple: Sw0rdf1sh! <br>
  True</p>
</blockquote>



<h3 id="a-simple-game"><strong>A Simple Game</strong></h3>

<hr>

<p>Object-orientation is very useful when managing different objects and their relations. That is especially useful when you are developing games with different characters and features.</p>

<p>Let’s look at an example project that shows how classes are used in game development. <br>
The game to be developed is an old fashioned text-based adventure game. <br>
Below is the function handling input and simple parsing.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_input</span><span class="hljs-params">()</span>:</span>
  command = input(<span class="hljs-string">": "</span>).split()
  verb_word = command[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">if</span> verb_word <span class="hljs-keyword">in</span> verb_dict:
    verb = verb_dict[verb_word]
  <span class="hljs-keyword">else</span>:
    print(<span class="hljs-string">"Unknown verb {}"</span>. format(verb_word))
    <span class="hljs-keyword">return</span>

  <span class="hljs-keyword">if</span> len(command) &gt;= <span class="hljs-number">2</span>:
    noun_word = command[<span class="hljs-number">1</span>]
    <span class="hljs-keyword">print</span> (verb(noun_word))
  <span class="hljs-keyword">else</span>:
    print(verb(<span class="hljs-string">"nothing"</span>))

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">say</span><span class="hljs-params">(noun)</span>:</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">'You said "{}"'</span>.format(noun)

verb_dict = {
  <span class="hljs-string">"say"</span>: say,
}

<span class="hljs-keyword">while</span> <span class="hljs-keyword">True</span>:
  get_input()</code></pre>

<p><strong>Result:</strong></p>

<pre><code>: say Hello!
You said "Hello!"
: say Goodbye!
You said "Goodbye!"

: test
Unknown verb test
</code></pre>

<blockquote>
  <p><strong>Note:</strong> The code above takes input from the user, and tries to match the first word with a command in <strong>verb_dict</strong>. If a match is found, the <br>
  corresponding function is called.</p>
</blockquote>

<p>The next step is to use classes to represent game objects.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GameObject</span>:</span>
  class_name = <span class="hljs-string">""</span>
  desc = <span class="hljs-string">""</span>
  objects = {}

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, name)</span>:</span>
    self.name = name
    GameObject.objects[self.class_name] = self

  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get_desc</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">return</span> self.class_name + <span class="hljs-string">"\n"</span> + self.desc

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Goblin</span><span class="hljs-params">(GameObject)</span>:</span>
  class_name = <span class="hljs-string">"goblin"</span>
  desc = <span class="hljs-string">"A foul creature"</span>

goblin = Goblin(<span class="hljs-string">"Gobbly"</span>)

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">examine</span><span class="hljs-params">(noun)</span>:</span>
  <span class="hljs-keyword">if</span> noun <span class="hljs-keyword">in</span> GameObject.objects:
    <span class="hljs-keyword">return</span> GameObject.objects[noun].get_desc()
  <span class="hljs-keyword">else</span>:
    <span class="hljs-keyword">return</span> <span class="hljs-string">"There is no {} here."</span>.format(noun)</code></pre>

<p>We created a <strong>Goblin</strong> class, which inherits from the <strong>GameObjects</strong> class. <br>
We also created a new function <strong>examine</strong>, which returns the objects description. <br>
Now we can add a new “examine” verb to our dictionary and try it out!</p>



<pre class="prettyprint"><code class=" hljs perl">verb_dict = {
  <span class="hljs-string">"say"</span>: <span class="hljs-keyword">say</span>,
  <span class="hljs-string">"examine"</span>: examine,
}</code></pre>

<p>Combine this code with the one in our previous example, and run the program.</p>

<pre><code>&gt;&gt;&gt;
: say Hello!
You said "Hello!"

: examine goblin
goblin
A foul creature

: examine elf
There is no elf here.
:
</code></pre>

<p>This code adds more detail to the <strong>Goblin</strong> class and allows you to <strong>fight</strong> goblins.</p>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Goblin</span><span class="hljs-params">(GameObject)</span>:</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span><span class="hljs-params">(self, name)</span>:</span>
    self.class_name = <span class="hljs-string">"goblin"</span>
    self.health = <span class="hljs-number">3</span>
    self._desc = <span class="hljs-string">" A foul creature"</span>
    super().__init__(name)

  <span class="hljs-decorator">@property</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">desc</span><span class="hljs-params">(self)</span>:</span>
    <span class="hljs-keyword">if</span> self.health &gt;=<span class="hljs-number">3</span>:
      <span class="hljs-keyword">return</span> self._desc
    <span class="hljs-keyword">elif</span> self.health == <span class="hljs-number">2</span>:
      health_line = <span class="hljs-string">"It has a wound on its knee."</span>
    <span class="hljs-keyword">elif</span> self.health == <span class="hljs-number">1</span>:
      health_line = <span class="hljs-string">"Its left arm has been cut off!"</span>
    <span class="hljs-keyword">elif</span> self.health &lt;= <span class="hljs-number">0</span>:
      health_line = <span class="hljs-string">"It is dead."</span>
    <span class="hljs-keyword">return</span> self._desc + <span class="hljs-string">"\n"</span> + health_line

  <span class="hljs-decorator">@desc.setter</span>
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">desc</span><span class="hljs-params">(self, value)</span>:</span>
    self._desc = value

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">hit</span><span class="hljs-params">(noun)</span>:</span>
  <span class="hljs-keyword">if</span> noun <span class="hljs-keyword">in</span> GameObject.objects:
    thing = GameObject.objects[noun]
    <span class="hljs-keyword">if</span> type(thing) == Goblin:
      thing.health = thing.health - <span class="hljs-number">1</span>
      <span class="hljs-keyword">if</span> thing.health &lt;= <span class="hljs-number">0</span>:
        msg = <span class="hljs-string">"You killed the goblin!"</span>
      <span class="hljs-keyword">else</span>: 
        msg = <span class="hljs-string">"You hit the {}"</span>.format(thing.class_name)
  <span class="hljs-keyword">else</span>:
    msg =<span class="hljs-string">"There is no {} here."</span>.format(noun) 
  <span class="hljs-keyword">return</span> msg</code></pre>

<p><strong>Result:</strong></p>

<pre><code>&gt;&gt;&gt;
: hit goblin
You hit the goblin

: examine goblin
goblin
 A foul creature
It has a wound on its knee.

: hit goblin
You hit the goblin

: hit goblin
You killed the goblin!

: examine goblin
A goblin

goblin
 A foul creature
It is dead.
:
</code></pre>

<blockquote>
  <p><strong>Note:</strong> This was just a simple sample. You could create different classes <br>
  (e.g., elves, orcs, humans), fight them, make them fight each other, <br>
  and so on.</p>
</blockquote>
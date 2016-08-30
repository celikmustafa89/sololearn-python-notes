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
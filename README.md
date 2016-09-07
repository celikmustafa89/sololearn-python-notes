<style>
 #preview-box {
     background-color: rgba(1,1,1,0.1);
     padding: 1px 10px;
     border-radius: 10px;
 }
</style>
<link id="linkstyle" rel='stylesheet' href='theme1.css'/>

<script>
 var linkstyle = document.getElementById('linkstyle');
 var themes = document.getElementById('themes');

 themes.onchange = function(e) {
     linkstyle.href = themes.value;
 };
</script>

<h1 id="shell-scripting"><strong>SHELL SCRIPTING</strong></h1>

<hr>



<h2 id="table-of-contents"><strong>Table of Contents</strong></h2>

<p><div class="toc">
<ul>
<li><a href="#shell-scripting">SHELL SCRIPTING</a><ul>
<li><a href="#table-of-contents">Table of Contents</a></li>
<li><a href="#shell-scripting-tutorial-1-introduction">Shell Scripting Tutorial-1: Introduction</a></li>
<li><a href="#shell-scripting-tutorial-2-shell-kernel-terminal-and-more">Shell Scripting Tutorial-2: Shell, Kernel, Terminal and More</a></li>
<li><a href="#shell-scripting-tutorial-3-view-system-date-calender">Shell Scripting Tutorial-3: View System Date, Calender</a><ul>
<li><a href="#calender">Calender</a></li>
<li><a href="#date">Date</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-4-create-files-directories">Shell Scripting Tutorial-4: Create Files &amp; Directories</a></li>
<li><a href="#shell-scripting-tutorial-5-text-files-create-merge-play">Shell Scripting Tutorial-5: Text Files: Create, Merge &amp; Play</a></li>
<li><a href="#shell-scripting-tutorial-6-rename-delete-files-directories">Shell Scripting Tutorial-6: Rename &amp; Delete Files &amp; Directories</a><ul>
<li><a href="#rename-files-directories">Rename Files &amp; Directories</a></li>
<li><a href="#delete-files-directories">Delete Files &amp; Directories</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-7-create-copies-links-to-files-directories">Shell Scripting Tutorial-7: Create Copies, Links to Files &amp; Directories</a><ul>
<li><a href="#copy-files">Copy Files</a></li>
<li><a href="#links">Links</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-8-file-permissions">Shell Scripting Tutorial-8: File Permissions</a><ul>
<li><a href="#file-permission">File Permission</a></li>
<li><a href="#umask-usage">“umask” Usage</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-9-see-whats-using-in-ls">Shell Scripting Tutorial-9: See What’s Using in ‘ls’</a><ul>
<li><a href="#usage-of-ls">Usage of ‘ls’</a></li>
<li><a href="#hidden-files-and-ls-a">Hidden files and ‘ls -a’</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-10-change-file-permissions-using-chmod">Shell Scripting Tutorial-10: Change File Permissions Using ‘chmod’</a><ul>
<li><a href="#usage-of-chmod">Usage of ‘chmod’</a></li>
<li><a href="#usage-of-uname">Usage of ‘uname’</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-11-count-lines-words-characters-using-wc">Shell Scripting Tutorial-11: Count Lines, Words &amp; Characters Using ‘wc’</a><ul>
<li><a href="#usage-of-file">Usage of ‘file’</a></li>
<li><a href="#usage-of-wc">Usage of ‘wc’</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-12-sort">Shell Scripting Tutorial-12: Sort</a><ul>
<li><a href="#usage-of-sort">Usage of ‘sort’</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-13-cut-through-your-files">Shell Scripting Tutorial-13: Cut Through Your Files</a><ul>
<li><a href="#usage-of-cut">Usage of ‘cut’</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-14-convert-copy-files-with-dd">Shell Scripting Tutorial-14: Convert &amp; Copy Files with ‘dd’</a><ul>
<li><a href="#usage-of-dd">Usage of ‘dd’</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-15-get-help-view-fancy-text-reduce-file-size">Shell Scripting Tutorial-15: Get Help, View Fancy Text &amp; Reduce File Size</a><ul>
<li><a href="#getting-help">Getting Help</a></li>
<li><a href="#view-fancy-text">View Fancy Text</a></li>
<li><a href="#reduce-file-size">Reduce File Size</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-16-hello-world">Shell Scripting Tutorial-16: Hello World!</a></li>
<li><a href="#shell-scripting-tutorial-17-use-command-in-your-script">Shell Scripting Tutorial-17: Use Command in Your Script</a></li>
<li><a href="#shell-scripting-tutorial-18-shell-variables-grab-user-input-using-read">Shell Scripting Tutorial-18: Shell Variables, Grab User Input Using ‘read’</a><ul>
<li><a href="#shell-variables">Shell Variables</a></li>
<li><a href="#grab-user-input-using-read">Grab User Input Using ‘read’</a></li>
</ul>
</li>
<li><a href="#shell-scripting-tutorial-19-positional-parameters">Shell Scripting Tutorial-19: Positional Parameters</a></li>
<li><a href="#shell-scripting-tutorial-20-more-on-positional-parameters">Shell Scripting Tutorial-20: More on Positional Parameters</a></li>
<li><a href="#shell-scripting-tutorial-21-reverse-quotes-accent-graves">Shell Scripting Tutorial-21: Reverse Quotes &amp; Accent Graves</a></li>
<li><a href="#shell-scripting-tutorial-22-count-the-number-of-command-line-arguments-using">Shell Scripting Tutorial-22: Count the Number of Command Line Arguments Using ‘$#’</a></li>
<li><a href="#shell-scripting-tutorial-23-math-on-integers-using-expr">Shell Scripting Tutorial-23: Math on Integers Using ‘expr’</a></li>
<li><a href="#shell-scripting-tutorial-24-operator-precedence">Shell Scripting Tutorial-24: Operator Precedence</a></li>
<li><a href="#shell-scripting-tutorial-25-math-on-real-numbers">Shell Scripting Tutorial-25: Math on Real Numbers</a></li>
<li><a href="#shell-scripting-tutorial-26-escape-sequences">Shell Scripting Tutorial-26: Escape Sequences</a></li>
<li><a href="#shell-scripting-tutorial-27-do-cool-things-with-tput">Shell Scripting Tutorial-27: Do Cool Things with ‘tput’</a></li>
<li><a href="#shell-scripting-tutorial-28-if-then-statement-in-action">Shell Scripting Tutorial-28: ‘if-then’ Statement in Action</a></li>
<li><a href="#shell-scripting-tutorial-29-the-if-then-else-statement">Shell Scripting Tutorial-29: The ‘if-then-else’ Statement</a></li>
<li><a href="#shell-scripting-tutorial-30-run-checks-on-numbers">Shell Scripting Tutorial-30: Run Checks on Numbers</a></li>
<li><a href="#shell-scripting-tutorial-31-run-checks-on-files">Shell Scripting Tutorial-31: Run Checks on Files</a></li>
<li><a href="#shell-scripting-tutorial-32-append-text-to-a-file-through-shell-script">Shell Scripting Tutorial-32: Append Text to a File Through Shell Script</a></li>
<li><a href="#shell-scripting-tutorial-33-run-checks-on-strings">Shell Scripting Tutorial-33: Run Checks on Strings</a></li>
<li><a href="#shell-scripting-tutorial-34-run-checks-on-stringthe-and-logical-operator">Shell Scripting Tutorial-34: Run Checks on StringThe ‘AND’ Logical Operator</a></li>
<li><a href="#shell-scripting-tutorial-35-count-the-number-of-characters-in-users-input-in-your-script">Shell Scripting Tutorial-35: Count the Number of Characters in User’s Input in Your Script</a></li>
<li><a href="#shell-scripting-tutorial-36-the-or-logical-operator">Shell Scripting Tutorial-36: The ‘OR’ Logical Operator</a></li>
<li><a href="#shell-scripting-tutorial-38-another-date-with-case-statement">Shell Scripting Tutorial-38: Another Date with ‘case’ Statement</a></li>
<li><a href="#shell-scripting-tutorial-39-the-while-loop">Shell Scripting Tutorial-39: The ‘while’ Loop</a></li>
<li><a href="#shell-scripting-tutorial-40-the-until-loop">Shell Scripting Tutorial-40: The ‘until’ Loop</a></li>
<li><a href="#shell-scripting-tutorial-41-the-for-loop">Shell Scripting Tutorial-41: The ‘for’ Loop</a></li>
<li><a href="#shell-scripting-tutorial-42-rant-little-work">Shell Scripting Tutorial-42: Rant &amp; Little Work</a></li>
<li><a href="#shell-scripting-tutorial-43-search-patterns-using-grep">Shell Scripting Tutorial-43: Search Patterns Using ‘grep’</a></li>
<li><a href="#shell-scripting-tutorial-44-the-passwd-file-explained">Shell Scripting Tutorial-44: The ‘passwd’ File Explained</a></li>
<li><a href="#shell-scripting-tutorial-45-the-internal-field-separator">Shell Scripting Tutorial-45: The Internal Field Separator</a></li>
<li><a href="#shell-scripting-tutorial-46-passwd-file-revisited">Shell Scripting Tutorial-46: ‘passwd’ File Revisited</a></li>
<li><a href="#shell-scripting-tutorial-47-reading-from-a-file">Shell Scripting Tutorial-47: Reading From a File</a></li>
<li><a href="#shell-scripting-tutorial-48-sleep-while-you-are-at-work">Shell Scripting Tutorial-48: Sleep While You are at Work</a></li>
<li><a href="#shell-scripting-tutorial-49-count-the-number-of-words-sentences-in-a-text-file-without-using-wc">Shell Scripting Tutorial-49: Count the number of words &amp; sentences in a text file without using ‘wc’</a></li>
<li><a href="#shell-scripting-tutorial-50-fetch-redirect-man-pages-of-commands-using-for-loop">Shell Scripting Tutorial-50: Fetch &amp; Redirect Man Pages of commands using ‘for loop’</a></li>
<li><a href="#shell-scripting-tutorial-51-nested-loops">Shell Scripting Tutorial-51: Nested Loops</a></li>
<li><a href="#shell-scripting-tutorial-52-the-break-statement">Shell Scripting Tutorial-52: The ‘break’ Statement</a></li>
<li><a href="#shell-scripting-tutorial-53-the-continue-statement">Shell Scripting Tutorial-53: The ‘continue’ Statement</a></li>
<li><a href="#shell-scripting-tutorial-54-more-on-metacharacters">Shell Scripting Tutorial-54: More on Metacharacters</a></li>
<li><a href="#shell-scripting-tutorial-55-adding-removing-users">Shell Scripting Tutorial-55: Adding &amp; Removing Users</a></li>
<li><a href="#shell-scripting-tutorial-56-know-when-users-log-in-part-one">Shell Scripting Tutorial-56: Know when users log in Part One</a></li>
<li><a href="#shell-scripting-tutorial-57-know-when-users-log-in-part-two">Shell Scripting Tutorial-57: Know when users log in Part Two</a></li>
<li><a href="#shell-scripting-tutorial-58-know-when-users-log-in-final-part">Shell Scripting Tutorial-58: Know when users log in Final Part</a></li>
<li><a href="#shell-scripting-tutorial-59-communicate-with-other-users-using-write">Shell Scripting Tutorial-59: Communicate with other users using ‘write’</a></li>
<li><a href="#shell-scripting-tutorial-60-create-your-own-commands-using-functions">Shell Scripting Tutorial-60: Create Your Own Commands Using Functions</a></li>
<li><a href="#shell-scripting-tutorial-61-executing-multiple-scripts">Shell Scripting Tutorial-61: Executing Multiple Scripts</a></li>
</ul>
</li>
</ul>
</div>
</p>



<h2 id="shell-scripting-tutorial-1-introduction"><strong>Shell Scripting Tutorial-1:</strong> <em>Introduction</em></h2>

<p>Install a linux distribution.</p>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/nVt3Rst-2H8" frameborder="0" allowfullscreen></iframe>



<h2 id="shell-scripting-tutorial-2-shell-kernel-terminal-and-more"><strong>Shell Scripting Tutorial-2:</strong> <em>Shell, Kernel, Terminal and More</em></h2>

<p><strong>Shell</strong> is an interface between user and the UNIX Kernel. <br>
<strong>UNIX Kernel</strong> manages the resources and hardware. <br>
<strong>Terminal</strong> provides access to shell.  </p>

<p>\@\:~$ terminal commands must be lowercase.  </p>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
who am i
whoami
<span class="hljs-built_in">pwd</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">joker    pts/3        2016-08-31 16:40 (:0.0) joker /home/joker/PycharmProjects/bash_script</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>who am i</code></td>
  <td>shows user name, terminal number, date</td>
</tr>
<tr>
  <td><code>whoami</code></td>
  <td>shows only user name</td>
</tr>
<tr>
  <td><code>pwd</code></td>
  <td>prints the working directory</td>
</tr>
</tbody></table>
<br><iframe width="560" height="315" src="https://www.youtube.com/embed/Y5mnE64WEDA" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-3-view-system-date-calender"><strong>Shell Scripting Tutorial-3:</strong> <em>View System Date, Calender</em></h2>



<h3 id="calender">Calender</h3>

<p>calender commands:  </p>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>cal</code></td>
  <td>prints the calender</td>
</tr>
<tr>
  <td><code>cal 7 2006</code></td>
  <td>prints july 2006</td>
</tr>
<tr>
  <td><code>cal feb 2033</code></td>
  <td>prints february 2033</td>
</tr>
</tbody></table>




<h3 id="date">Date</h3>

<p><strong>date</strong> command prints date as <em><strong>Mon Aug  8 14:37:04 EEST 2016</strong></em>.  </p>

<p>Output of date command can be customized. <br>
$ date ‘+DATE: %m-%y%nTIME: %H:%M:%S’ <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
cal <span class="hljs-comment"># prints the calender</span>
cal <span class="hljs-number">7</span> <span class="hljs-number">2006</span> <span class="hljs-comment"># prints july 2006</span>
cal feb <span class="hljs-number">2033</span>

date <span class="hljs-comment"># prints date, time and year</span>
date <span class="hljs-string">'+DATE: %m-%y%nTIME: %H:%M:%S'</span> <span class="hljs-comment"># customized date print</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs css">    <span class="hljs-tag">August</span> 2016       
<span class="hljs-tag">Su</span> <span class="hljs-tag">Mo</span> <span class="hljs-tag">Tu</span> <span class="hljs-tag">We</span> <span class="hljs-tag">Th</span> <span class="hljs-tag">Fr</span> <span class="hljs-tag">Sa</span>  
    1  2  3  4  5  6  
 7  8  9 10 11 12 13  
14 15 16 17 18 19 20  
21 22 23 24 25 26 27  
28 29 30 31           

     <span class="hljs-tag">July</span> 2006        
<span class="hljs-tag">Su</span> <span class="hljs-tag">Mo</span> <span class="hljs-tag">Tu</span> <span class="hljs-tag">We</span> <span class="hljs-tag">Th</span> <span class="hljs-tag">Fr</span> <span class="hljs-tag">Sa</span>  
                   1  
 2  3  4  5  6  7  8  
 9 10 11 12 13 14 15  
16 17 18 19 20 21 22  
23 24 25 26 27 28 29  
30 31                 
   <span class="hljs-tag">February</span> 2033      
<span class="hljs-tag">Su</span> <span class="hljs-tag">Mo</span> <span class="hljs-tag">Tu</span> <span class="hljs-tag">We</span> <span class="hljs-tag">Th</span> <span class="hljs-tag">Fr</span> <span class="hljs-tag">Sa</span>  
       1  2  3  4  5  
 6  7  8  9 10 11 12  
13 14 15 16 17 18 19  
20 21 22 23 24 25 26  
27 28                 

<span class="hljs-tag">Wed</span> <span class="hljs-tag">Aug</span> 31 16<span class="hljs-pseudo">:43</span><span class="hljs-pseudo">:35</span> <span class="hljs-tag">EEST</span> 2016
<span class="hljs-tag">DATE</span>: 08<span class="hljs-tag">-16</span>
<span class="hljs-tag">TIME</span>: 16<span class="hljs-pseudo">:43</span><span class="hljs-pseudo">:35</span></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>date</code></td>
  <td>prints date as “Mon Aug  8 14:37:04 EEST 2016”</td>
</tr>
<tr>
  <td><code>date '+DATE: %m-%y%nTIME: %H:%M:%S'</code></td>
  <td>prints date as “DATE: 08-16 TIME: 14:40:33”</td>
</tr>
</tbody></table>
<br><iframe width="560" height="315" src="https://www.youtube.com/embed/ThQ6R1EM0e8" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-4-create-files-directories"><strong>Shell Scripting Tutorial-4:</strong> <em>Create Files &amp; Directories</em></h2>

<p><strong>touch</strong> is used to create empty files. <br>
<strong>mkdir</strong> is used to create empty folder. <br>
<strong>cd</strong> is used to navigate inside folders. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
touch empty_file1 empty_file2 empty_file3 <span class="hljs-comment"># creates empty file</span>

mkdir folder1 folder2 folder3 <span class="hljs-comment"># creates folder</span>
mkdir Documents/folder1 <span class="hljs-comment"># creates folder in a specific path</span>

<span class="hljs-built_in">cd</span> Documents/folder1</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs "></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>touch empty_file1 empty_file2</code></td>
  <td>creates two empty files</td>
</tr>
<tr>
  <td><code>mkdir folder1</code></td>
  <td>creates a folder in working directory</td>
</tr>
<tr>
  <td><code>mkdir Documents/folder1</code></td>
  <td>creates a folder in Documents directory</td>
</tr>
</tbody></table>
<br><iframe width="560" height="315" src="https://www.youtube.com/embed/0csDVuBloIQ" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-5-text-files-create-merge-play"><strong>Shell Scripting Tutorial-5:</strong> <em>Text Files: Create, Merge &amp; Play</em></h2>

<p><strong>cat</strong> creates file with text. <br>
<code>$ cat &gt; test_file</code> <br>
<code>test_file content bla bla..</code>  </p>

<p><strong>cat</strong> shows content of the file. <br>
<code>$ cat test_file</code> <br>
<code>$ cat &lt; test_file</code>  </p>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
cat &gt; test_file <span class="hljs-comment"># creates file with text</span>
<span class="hljs-comment"># test_file content is entered here...</span>

cat &lt; test_file <span class="hljs-comment"># prints the content</span>
cat test_file <span class="hljs-comment"># prints the content</span>

cat &gt; test_file2 <span class="hljs-comment"># creates file with text</span>
<span class="hljs-comment"># test_file2 content is entered here..</span>

cat test_file test_file2 &gt; merged_test_files <span class="hljs-comment"># merge two files</span>

cat &lt; merged_test_files <span class="hljs-comment"># shows both test files' content</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">test_file_content <span class="hljs-number">1</span> <span class="hljs-constant">EOF</span>
test_file_content <span class="hljs-number">1</span> <span class="hljs-constant">EOF</span>
test_file_content <span class="hljs-number">1</span> <span class="hljs-constant">EOF</span>
test_file2_content <span class="hljs-number">2</span> <span class="hljs-constant">EOF</span>
test_file_content <span class="hljs-number">1</span> <span class="hljs-constant">EOF</span>
test_file2_content <span class="hljs-number">2</span> <span class="hljs-constant">EOF</span></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>cat &gt; test_file</code></td>
  <td>creates file with text</td>
</tr>
<tr>
  <td><code>cat &lt; test_file</code></td>
  <td>prints the content</td>
</tr>
<tr>
  <td><code>cat test_file</code></td>
  <td>prints the content</td>
</tr>
<tr>
  <td><code>cat &gt; test_file2</code></td>
  <td>creates file with text</td>
</tr>
<tr>
  <td><code>cat test_file test_file2 &gt; merged_test_files</code></td>
  <td>merge two files</td>
</tr>
<tr>
  <td><code>cat &lt; merged_test_files</code></td>
  <td>shows both test files’ content</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/viEmljLt-Fo" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-6-rename-delete-files-directories"><strong>Shell Scripting Tutorial-6:</strong> <em>Rename &amp; Delete Files &amp; Directories</em></h2>



<h3 id="rename-files-directories">Rename Files &amp; Directories</h3>

<p><strong>mv</strong> renames files and directories <br>
<code>mv file1 file2</code>  </p>



<h3 id="delete-files-directories">Delete Files &amp; Directories</h3>

<p><strong>rm</strong> deletes file <br>
<code>rm file</code>  </p>

<p><strong>rm -r</strong> deletes directory <br>
<code>rm -r directory/</code>  </p>

<p><strong>rmdir</strong> deletes empty directory <br>
<code>rmdir empty_directory</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
touch farm_village
mv farm_village red_cliff <span class="hljs-comment"># renames the file</span>
rm red_cliff <span class="hljs-comment"># deletes the file</span>

mkdir new
rm -r new <span class="hljs-comment"># deletes the directory</span>

mkdir test
rmdir test <span class="hljs-comment"># deletes the directory</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs "></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>mv file1 file2</code></td>
  <td>renames the file</td>
</tr>
<tr>
  <td><code>mv directory1 directory2</code></td>
  <td>renames the directory</td>
</tr>
<tr>
  <td><code>rm file2</code></td>
  <td>deletes the file</td>
</tr>
<tr>
  <td><code>rm -r directory2</code></td>
  <td>deletes the directory</td>
</tr>
<tr>
  <td><code>rmdir empty_directory</code></td>
  <td>deletes the empty directory</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/4r2r9HNCm0o" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-7-create-copies-links-to-files-directories"><strong>Shell Scripting Tutorial-7:</strong> <em>Create Copies, Links to Files &amp; Directories</em></h2>



<h3 id="copy-files">Copy Files</h3>

<p><strong>cp</strong> is used to copy files from one location to other. <br>
<strong>cp</strong> copies the file <strong>mv</strong> cuts and pastes the file. <br>
<code>cp file /home/Music/file_new_name</code>  </p>



<h3 id="links">Links</h3>

<p><strong>ln</strong> creates hard link for a file. <br>
<strong>Hard link</strong> is replica of original one. <br>
Any changes from old file, also exists in new one. <br>
Removing the original one does not effect new one. <br>
<code>ln old_file new_file</code>  </p>

<p><strong>ln -s</strong> creates soft link. <br>
Any changes from old file, also exists in new one. <br>
Removing the original makes soft link useless. <br>
<code>ln -s old old_soft</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
touch old
cp old /home/Music/new_file <span class="hljs-comment"># copy files with new name</span>

ln old new <span class="hljs-comment"># creates hard links</span>
<span class="hljs-comment"># any changes from old file, also exists in new one (HARD link)</span>

ln <span class="hljs-operator">-s</span>  old old_soft <span class="hljs-comment"># creates soft  link</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs "></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>cp old_file /home/Music/new_file</code></td>
  <td>copy files to new location with new name</td>
</tr>
<tr>
  <td><code>ln file hard_file</code></td>
  <td>creates a hard link</td>
</tr>
<tr>
  <td><code>ln -s file soft_file</code></td>
  <td>creates a soft link</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/8CEpUQCJKhc" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-8-file-permissions"><strong>Shell Scripting Tutorial-8:</strong> <em>File Permissions</em></h2>



<h3 id="file-permission">File Permission</h3>

<p><strong>owner</strong>, <strong>group</strong> and <strong>other</strong> are 3 permission part.  </p>

<p><strong>read</strong>, <strong>write</strong> and <strong>execute</strong> are 3 type of permission. <br>
- <strong>read</strong>: has numeric value “<strong>4</strong>“. <br>
- <strong>write</strong>: has numeric value “<strong>2</strong>“. <br>
- <strong>execute</strong>: has numeric value “<strong>1</strong>“.  </p>



<h3 id="umask-usage">“umask” Usage</h3>

<p><strong>umask</strong> is used to specify permission values. <br>
Assume <strong>umask</strong> value is <strong><em>0022</em></strong>. <br>
<code>file permission = 666 - 022 = 644</code> which means owner(read, write=6), group(read=4), other(read=4) <br>
<code>directory permission = 777 - 022 = 755</code> which means owner(read, write, execute=7), group/other(read, execute=5) <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
umask <span class="hljs-comment"># shows the number that is used to create defaul file permission.</span>
<span class="hljs-comment"># output: 0022</span>
<span class="hljs-comment"># which means:</span>
<span class="hljs-comment"># - file permissions will be     = 666-022 = 644 (owner-&gt;read,write group/other-&gt;read)</span>
<span class="hljs-comment"># - directory permission will be = 777-022 = 755 (owner-&gt;r,w,e group/other-&gt;r,e)</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">0022</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>umask</code></td>
  <td>shows file and directory permission creation base number</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/jID3dFxuFR8" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-9-see-whats-using-in-ls"><strong>Shell Scripting Tutorial-9:</strong> <em>See What’s Using in ‘ls’</em></h2>



<h3 id="usage-of-ls">Usage of ‘ls’</h3>

<p><strong>ls</strong> shows the list of files and directories. <br>
<code>ls -l</code> shows the following <br>
<code>total 4</code> <br>
<code>-rw-r--r-- 2 joker joker    0 Aug  9 13:58 forrest_village</code> <br>
<code>-rw-r--r-- 2 joker joker    0 Aug  9 13:58 new</code> <br>
<code>-rw-r--r-- 1 joker joker    0 Aug  9 15:10 sample</code> <br>
<code>drwxr-xr-x 2 joker joker 4096 Aug  9 14:05 sdf</code>    </p>

<p><strong>“d”</strong> letter at the beginnig of the last line shows that it is a <strong>directory</strong>. <br>
Any <strong>“l”</strong> letter at the beginning of the line shows that it is a <strong>soft link</strong>.  </p>

<p>Next characters shows the permissions owner(read,write,execute)group(read,write,execute)other(read,write,execute)  </p>



<h3 id="hidden-files-and-ls-a">Hidden files and ‘ls -a’</h3>

<p>Hidden files are created using . at the beginning of the file name. <br>
<code>touch .test</code>  </p>

<p><code>ls -a</code> shows all files in the directory, inclued hidden files. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
cat &gt; test
<span class="hljs-comment"># random text in test file...</span>

ls <span class="hljs-comment"># lists the files and directories</span>

ls <span class="hljs-operator">-l</span> <span class="hljs-comment"># lists the file permissions.</span>

touch .test <span class="hljs-comment"># creates a hidden files</span>
ls <span class="hljs-operator">-a</span> <span class="hljs-comment"># lists all files and directories including hidden ones.</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">list <span class="hljs-operator">of</span> all <span class="hljs-built_in">files</span> will be printed.</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>ls</code></td>
  <td>lists files and directories</td>
</tr>
<tr>
  <td><code>ls -l</code></td>
  <td>lists files and directories with permissions</td>
</tr>
<tr>
  <td><code>touch .test</code></td>
  <td>creates a hidden file</td>
</tr>
<tr>
  <td><code>ls -a</code></td>
  <td>list all files and directories including hidden ones</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/bFL05iO9k2M" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-10-change-file-permissions-using-chmod"><strong>Shell Scripting Tutorial-10:</strong> <em>Change File Permissions Using ‘chmod’</em></h2>



<h3 id="usage-of-chmod">Usage of ‘chmod’</h3>

<p><code>**chmod**</code> changes file permissions. <br>
<code>chmod 777 test</code> gives read, write and execute permissions to owner,group and other  </p>



<h3 id="usage-of-uname">Usage of ‘uname’</h3>

<p><code>**uname**</code> shows all about machine. <br>
<code>$ uname -a</code>  <br>
output: <br>
<code>**Linux joker 3.16.0-38-generic #52~14.04.1-Ubuntu SMP Fri May 8 09:43:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux**</code>  </p>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
touch test
ls <span class="hljs-operator">-l</span>

chmod <span class="hljs-number">777</span> test <span class="hljs-comment"># gives all permissions to owner, group and others.</span>
ls <span class="hljs-operator">-l</span>

uname <span class="hljs-operator">-a</span> <span class="hljs-comment"># shows all about machine</span>
<span class="hljs-comment"># output:</span>
<span class="hljs-comment"># Linux joker 3.16.0-38-generic #52~14.04.1-Ubuntu SMP Fri May 8 09:43:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-comment">####file list will be printed here.</span>
Linux joker <span class="hljs-number">3.16</span>.<span class="hljs-number">0</span>-<span class="hljs-number">38</span>-generic <span class="hljs-comment">#52~14.04.1-Ubuntu SMP Fri May 8 09:43:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>chmod 777 test</code></td>
  <td>gives all permissions to all users</td>
</tr>
<tr>
  <td><code>uname -a</code></td>
  <td>shows all details about machine and kernel</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/QBlENrp2wns" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-11-count-lines-words-characters-using-wc"><strong>Shell Scripting Tutorial-11:</strong> <em>Count Lines, Words &amp; Characters Using ‘wc’</em></h2>



<h3 id="usage-of-file">Usage of ‘file’</h3>

<p><strong><code>file</code></strong> shows the type of files. <br>
<code>file *</code> <br>
output: <br>
<code>aaa:             symbolic link to 'new'</code> <br>
<code>bbb:             empty</code> <br>
<code>forrest_village: empty</code> <br>
<code>jazz:            ASCII text</code> <br>
<code>new:             empty</code> <br>
<code>sdf:             directory</code>  </p>



<h3 id="usage-of-wc">Usage of ‘wc’</h3>

<p><code>wc file</code> <br>
output: <br>
<code>4  7 48 file</code> <br>
4 : number of lines <br>
7 : number of words <br>
48: number of characters  </p>

<p><code>wc -l file</code> show line count <br>
<code>wc -w file</code> show word count <br>
<code>wc -c file</code> show character count <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs vhdl">#!/usr/bin/env bash

<span class="hljs-keyword">file</span> * # shows the <span class="hljs-keyword">type</span> <span class="hljs-keyword">of</span> files
<span class="hljs-keyword">file</span> test # shows the <span class="hljs-keyword">type</span> <span class="hljs-keyword">of</span> <span class="hljs-keyword">file</span> test

wc test # shows the number <span class="hljs-keyword">of</span> lines,words <span class="hljs-keyword">and</span> chracters <span class="hljs-keyword">of</span> <span class="hljs-keyword">file</span> test
wc -l test # shows the number <span class="hljs-keyword">of</span> lines <span class="hljs-keyword">of</span> <span class="hljs-keyword">file</span> test
wc -w test # shows the number <span class="hljs-keyword">of</span> words <span class="hljs-keyword">of</span> <span class="hljs-keyword">file</span> test
wc -c test # shows the number <span class="hljs-keyword">of</span> characters <span class="hljs-keyword">of</span> <span class="hljs-keyword">file</span> test</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">commandlist_tutorial_50:     ASCII <span class="hljs-keyword">text</span>
create_consecutive_files.sh: Bourne-Again <span class="hljs-built_in">shell</span> script, ASCII <span class="hljs-keyword">text</span> executable
empty_file1:                 <span class="hljs-constant">empty</span> 
empty_file2:                 <span class="hljs-constant">empty</span> 
empty_file3:                 <span class="hljs-constant">empty</span> 
folder1:                     <span class="hljs-built_in">directory</span> 
test: ASCII <span class="hljs-keyword">text</span>
 <span class="hljs-number">1</span>  <span class="hljs-number">2</span> <span class="hljs-number">10</span> test
<span class="hljs-number">1</span> test
<span class="hljs-number">2</span> test
<span class="hljs-number">10</span> test
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>file *</code></td>
  <td>shows file types of all files</td>
</tr>
<tr>
  <td><code>wc file</code></td>
  <td>shows number of lines, words and chracters of file</td>
</tr>
<tr>
  <td><code>wc -l file</code></td>
  <td>shows number of lines</td>
</tr>
<tr>
  <td><code>wc -w file</code></td>
  <td>shows number of words</td>
</tr>
<tr>
  <td><code>wc -c file</code></td>
  <td>shows number of chracters</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/Ex-mzjPwrmo" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-12-sort"><strong>Shell Scripting Tutorial-12:</strong> <em>Sort</em></h2>



<h3 id="usage-of-sort">Usage of ‘sort’</h3>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs vala"><span class="hljs-preprocessor">#!/usr/bin/env bash</span>

cat &gt; animals
<span class="hljs-preprocessor"># dogs</span>
<span class="hljs-preprocessor"># cats</span>
<span class="hljs-preprocessor"># birds</span>
<span class="hljs-preprocessor"># monkeys</span>
<span class="hljs-preprocessor"># elephants</span>

sort animals # sort lines alphabetically

cat &gt; sports
<span class="hljs-preprocessor"># cricet</span>
<span class="hljs-preprocessor"># tennis</span>
<span class="hljs-preprocessor"># football</span>
<span class="hljs-preprocessor"># basketball</span>
<span class="hljs-preprocessor"># wrestling</span>

sort sports # sort lines alphabetically

sort
<span class="hljs-preprocessor"># Apocalypse</span>
<span class="hljs-preprocessor"># Avatar</span>
<span class="hljs-preprocessor"># Forrest Gump</span>
<span class="hljs-preprocessor"># Saving Private Ryan</span>

<span class="hljs-preprocessor"># hit "ctrl+d" sorts the lines</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs php">dogs
cats
birds
monkeys
elephants
birds
cats
dogs
elephants
monkeys
cricet
tennis
football
basketball
wrestling
basketball
cricet
football
tennis
wrestling
Apocalypse
Avatar
Forrest Gump
Saving <span class="hljs-keyword">Private</span> Ryan
Apocalypse
Avatar
Forrest Gump
Saving <span class="hljs-keyword">Private</span> Ryan
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>sort animals</code></td>
  <td>sorts alphabetically the lines of file</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/kL08uSQZbHA" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-13-cut-through-your-files"><strong>Shell Scripting Tutorial-13:</strong> <em>Cut Through Your Files</em></h2>



<h3 id="usage-of-cut">Usage of ‘cut’</h3>

<p><strong><code>cut</code></strong> uses - as default saperater. <br>
<code>cut -d"-" -f 1,3 file_name</code>  </p>

<p><strong><em>-d</em></strong>: specify the delimeter character <br>
<strong><em>-f</em></strong>: specify the fields that will be printed <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
cat &gt; players
<span class="hljs-comment"># Name-Sport-Age</span>
<span class="hljs-comment"># Roger-Tennis-30</span>
<span class="hljs-comment"># Rafel-Tennis-25</span>
<span class="hljs-comment"># Tiger-Golf-27</span>
<span class="hljs-comment"># Michael-Swimmer-27</span>
<span class="hljs-comment"># Kobe-Basketball-34</span>

cut <span class="hljs-operator">-d</span><span class="hljs-string">"-"</span> <span class="hljs-operator">-f</span> <span class="hljs-number">1</span>,<span class="hljs-number">3</span> players <span class="hljs-comment"># prints 1 and 3 column of players file using - delimeter</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs lasso">Name<span class="hljs-attribute">-Sport</span><span class="hljs-attribute">-Age</span>
Roger<span class="hljs-attribute">-Tennis</span><span class="hljs-subst">-</span><span class="hljs-number">30</span>
Rafel<span class="hljs-attribute">-Tennis</span><span class="hljs-subst">-</span><span class="hljs-number">25</span>
Tiger<span class="hljs-attribute">-Golf</span><span class="hljs-subst">-</span><span class="hljs-number">27</span>
Michael<span class="hljs-attribute">-Swimmer</span><span class="hljs-subst">-</span><span class="hljs-number">27</span>
Kobe<span class="hljs-attribute">-Basketball</span><span class="hljs-subst">-</span><span class="hljs-number">34</span>

Name<span class="hljs-attribute">-Age</span>
Roger<span class="hljs-subst">-</span><span class="hljs-number">30</span>
Rafel<span class="hljs-subst">-</span><span class="hljs-number">25</span>
Tiger<span class="hljs-subst">-</span><span class="hljs-number">27</span>
Michael<span class="hljs-subst">-</span><span class="hljs-number">27</span>
Kobe<span class="hljs-subst">-</span><span class="hljs-number">34</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>cut -d"-" 1,3 file_name</code></td>
  <td>prints the 1 and 3 column of the file, and - is delimeter</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/CA00GqJibZA" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-14-convert-copy-files-with-dd"><strong>Shell Scripting Tutorial-14:</strong> <em>Convert &amp; Copy Files with ‘dd’</em></h2>



<h3 id="usage-of-dd">Usage of ‘dd’</h3>

<p>converts all characters from lowercase to uppercase in a file. <br>
<code>dd if=test of=test1 conv=ucase</code>  </p>

<p>converts encoding to european based encoding. <br>
<code>dd if=test of=test2 conv=ebcdic</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
cat &gt; test
<span class="hljs-comment"># this is a test file.</span>

dd <span class="hljs-keyword">if</span>=test of=test1 conv=ucase <span class="hljs-comment"># converts all lowercase character to uppercase with in a new file.</span>
cat test
cat test1

dd <span class="hljs-keyword">if</span>=test of=test2 conv=ebcdic <span class="hljs-comment"># conerts encoding to european based encoding.</span>
cat test
cat test2
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vhdl">this <span class="hljs-keyword">is</span> a test <span class="hljs-keyword">file</span>.
<span class="hljs-number">0</span>+<span class="hljs-number">1</span> records <span class="hljs-keyword">in</span>
<span class="hljs-number">0</span>+<span class="hljs-number">1</span> records <span class="hljs-keyword">out</span>
<span class="hljs-number">21</span> bytes (<span class="hljs-number">21</span> B) copied, <span class="hljs-number">0.000277341</span> s, <span class="hljs-number">75.7</span> kB/s
this <span class="hljs-keyword">is</span> a test <span class="hljs-keyword">file</span>.
THIS <span class="hljs-keyword">IS</span> A TEST <span class="hljs-keyword">FILE</span>.
<span class="hljs-number">0</span>+<span class="hljs-number">1</span> records <span class="hljs-keyword">in</span>
<span class="hljs-number">0</span>+<span class="hljs-number">1</span> records <span class="hljs-keyword">out</span>
<span class="hljs-number">21</span> bytes (<span class="hljs-number">21</span> B) copied, <span class="hljs-number">0.000301356</span> s, <span class="hljs-number">69.7</span> kB/s
this <span class="hljs-keyword">is</span> a test <span class="hljs-keyword">file</span>.
����@��@�@����@����K%</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>dd if=test of=test1 conv=ucase</code></td>
  <td>converts all lowercase to uppercase in a new file</td>
</tr>
<tr>
  <td><code>dd if=test of=test2 conv=ebcdic</code></td>
  <td>converts encoding to european based encoding</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/6N4HyE11UFs" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-15-get-help-view-fancy-text-reduce-file-size"><strong>Shell Scripting Tutorial-15:</strong> <em>Get Help, View Fancy Text &amp; Reduce File Size</em></h2>



<h3 id="getting-help">Getting Help</h3>

<p><code>man &lt;command name&gt;</code> shows the help manual of the command. <br>
<code>man cat</code>  </p>

<p>exiting manual page by using Q key.  </p>



<h3 id="view-fancy-text">View Fancy Text</h3>

<p><code>banner my name is mustafa celik</code> <br>
<code>banner "my name is mustafa celik"</code> banner shows 10 character in one line.    </p>



<h3 id="reduce-file-size">Reduce File Size</h3>

<p>reducing the size of a file. <br>
<code>compress -v test</code>  </p>

<p>printing compressed file in a readable format. <br>
<code>zcat -v test.Z</code>  </p>

<p>uncompressing the compressed file. <br>
<code>uncompress test.Z</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
man cat

banner my name is mustafa celik <span class="hljs-comment"># prints fancy text</span>
banner <span class="hljs-string">"my name is mustafa celik"</span> <span class="hljs-comment"># prints fancy text in one line</span>

compress -v test <span class="hljs-comment"># compress the file</span>
zcat -v test.Z  <span class="hljs-comment"># prints compressed file readable.</span>

uncompress -v test.Z <span class="hljs-comment"># uncompress the compresed file.</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ruleslanguage">Whole Man Page of cat command will be printed.

 <span class="hljs-array">#    </span><span class="hljs-array">#   </span><span class="hljs-array">#   </span>#
 #<span class="hljs-array">#  </span>#<span class="hljs-array">#    </span><span class="hljs-array"># </span>#
 <span class="hljs-array"># </span>#<span class="hljs-array"># </span><span class="hljs-array">#     </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#     </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#     </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#     </span>#


 <span class="hljs-array">#    </span><span class="hljs-array">#    </span>#<span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>######
 #<span class="hljs-array">#   </span><span class="hljs-array">#   </span><span class="hljs-array">#  </span><span class="hljs-array">#   </span>#<span class="hljs-array">#  </span>#<span class="hljs-array">#  </span>#
 <span class="hljs-array"># </span><span class="hljs-array">#  </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array"># </span>#<span class="hljs-array"># </span><span class="hljs-array">#  </span>#####
 <span class="hljs-array">#  </span><span class="hljs-array"># </span><span class="hljs-array">#  </span>#####<span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#
 <span class="hljs-array">#   </span>#<span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>######


    <span class="hljs-array">#     </span>####
    <span class="hljs-array">#    </span>#
    <span class="hljs-array">#     </span>####
    <span class="hljs-array">#         </span>#
    <span class="hljs-array">#    </span><span class="hljs-array">#    </span>#
    <span class="hljs-array">#     </span>####


 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#   </span>###<span class="hljs-array">#    </span>####<span class="hljs-array">#    </span>#<span class="hljs-array">#    </span>#####<span class="hljs-array">#    </span>##
 #<span class="hljs-array">#  </span>#<span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#          </span><span class="hljs-array">#     </span><span class="hljs-array">#  </span><span class="hljs-array">#   </span><span class="hljs-array">#        </span><span class="hljs-array">#  </span>#
 <span class="hljs-array"># </span>#<span class="hljs-array"># </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#   </span>###<span class="hljs-array">#      </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>####<span class="hljs-array">#   </span><span class="hljs-array">#    </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#       </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span>#####<span class="hljs-array">#  </span><span class="hljs-array">#       </span>######
 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#       </span><span class="hljs-array">#    </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#   </span>###<span class="hljs-array">#    </span>###<span class="hljs-array">#      </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#       </span><span class="hljs-array">#    </span>#


  ###<span class="hljs-array">#   </span>#####<span class="hljs-array">#  </span><span class="hljs-array">#          </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#       </span><span class="hljs-array">#          </span><span class="hljs-array">#    </span><span class="hljs-array">#   </span>#
 <span class="hljs-array">#       </span>####<span class="hljs-array">#   </span><span class="hljs-array">#          </span><span class="hljs-array">#    </span>####
 <span class="hljs-array">#       </span><span class="hljs-array">#       </span><span class="hljs-array">#          </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#       </span><span class="hljs-array">#          </span><span class="hljs-array">#    </span><span class="hljs-array">#   </span>#
  ###<span class="hljs-array">#   </span>#####<span class="hljs-array">#  </span>#####<span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span>#


 <span class="hljs-array">#    </span><span class="hljs-array">#   </span><span class="hljs-array">#   </span><span class="hljs-array">#          </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span>#<span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#####<span class="hljs-array">#             </span><span class="hljs-array">#     </span>####
 #<span class="hljs-array">#  </span>#<span class="hljs-array">#    </span><span class="hljs-array"># </span><span class="hljs-array">#           </span>#<span class="hljs-array">#   </span><span class="hljs-array">#   </span><span class="hljs-array">#  </span><span class="hljs-array">#   </span>#<span class="hljs-array">#  </span>#<span class="hljs-array">#  </span><span class="hljs-array">#                  </span><span class="hljs-array">#    </span>#
 <span class="hljs-array"># </span>#<span class="hljs-array"># </span><span class="hljs-array">#     </span><span class="hljs-array">#            </span><span class="hljs-array"># </span><span class="hljs-array">#  </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array"># </span>#<span class="hljs-array"># </span><span class="hljs-array">#  </span>####<span class="hljs-array">#              </span><span class="hljs-array">#     </span>####
 <span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#            </span><span class="hljs-array">#  </span><span class="hljs-array"># </span><span class="hljs-array">#  </span>#####<span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#                  </span><span class="hljs-array">#         </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#            </span><span class="hljs-array">#   </span>#<span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#                  </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#            </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#####<span class="hljs-array">#             </span><span class="hljs-array">#     </span>####

test: No compression -- test unchanged
gzip: test.Z: No such file or directory
gzip: test.Z: No such file or directory
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>man &lt;command&gt;</code></td>
  <td>shows the manuel of the command. Note: use Q key to quit.</td>
</tr>
<tr>
  <td><code>banner some text</code></td>
  <td>prints fancy text</td>
</tr>
<tr>
  <td><code>banner "some text"</code></td>
  <td>prints fancy text in one line. Note: limited to 10 character.</td>
</tr>
<tr>
  <td><code>compress -v test</code></td>
  <td>compresses the test file.</td>
</tr>
<tr>
  <td><code>zcat -v test.Z</code></td>
  <td>prints the readable version of the compressed file.</td>
</tr>
<tr>
  <td><code>uncompress test.Z</code></td>
  <td>uncompress the compressed file.</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/R9qkOKZoYWc" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-16-hello-world"><strong>Shell Scripting Tutorial-16:</strong> <em>Hello World!</em></h2>

<p>hello world example is implemented using <code>echo</code> command. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Hello World!"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs erlang-repl"><span class="hljs-variable">Hello</span> <span class="hljs-variable">World</span><span class="hljs-exclamation_mark">!</span></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>echo "Hello World!"</code></td>
  <td>prints hello world to terminal.</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/PLzZ0OjeCrE" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-17-use-command-in-your-script"><strong>Shell Scripting Tutorial-17:</strong> <em>Use Command in Your Script</em></h2>

<p>Use commands in the script. <br>
<code>pwd</code> <br>
<code>ls -l</code> <br>
<code>banner "The End"</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># Shell_scripting_tutorial_17: Use Command in Your Script</span>

<span class="hljs-built_in">pwd</span>
ls <span class="hljs-operator">-l</span>
banner <span class="hljs-string">"The End"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ruleslanguage">/home/joker/PycharmProjects/bash_script
total <span class="hljs-number">348</span>
-rw-r--r-- <span class="hljs-number">1</span> joker joker    <span class="hljs-number">34</span> Aug <span class="hljs-number">31</span> <span class="hljs-number">17</span>:<span class="hljs-number">11</span> animals
-rw-r--r-- <span class="hljs-number">1</span> joker joker    <span class="hljs-number">18</span> Aug <span class="hljs-number">27</span> <span class="hljs-number">21</span>:<span class="hljs-number">07</span> commandlist_tutorial_50
-rw-r--r-- <span class="hljs-number">1</span> joker joker   <span class="hljs-number">507</span> Aug <span class="hljs-number">27</span> <span class="hljs-number">21</span>:<span class="hljs-number">07</span> create_consecutive_files.sh
-rw-r--r-- <span class="hljs-number">1</span> joker joker     <span class="hljs-number">0</span> Aug <span class="hljs-number">31</span> <span class="hljs-number">16</span>:<span class="hljs-number">59</span> empty_file1
-rw-r--r-- <span class="hljs-number">1</span> joker joker     <span class="hljs-number">0</span> Aug <span class="hljs-number">31</span> <span class="hljs-number">16</span>:<span class="hljs-number">59</span> empty_file2
-rw-r--r-- <span class="hljs-number">1</span> joker joker     <span class="hljs-number">0</span> Aug <span class="hljs-number">31</span> <span class="hljs-number">16</span>:<span class="hljs-number">59</span> empty_file3
drwxr-xr-x <span class="hljs-number">2</span> joker joker  <span class="hljs-number">4096</span> Aug <span class="hljs-number">31</span> <span class="hljs-number">16</span>:<span class="hljs-number">59</span> folder1

######<span class="hljs-array">#                         </span>#######
   <span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#####<span class="hljs-array">#         </span><span class="hljs-array">#        </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#####
   <span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#              </span><span class="hljs-array">#        </span>#<span class="hljs-array">#   </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span>#
   <span class="hljs-array">#     </span>#####<span class="hljs-array">#  </span>####<span class="hljs-array">#          </span>####<span class="hljs-array">#    </span><span class="hljs-array"># </span><span class="hljs-array">#  </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span>#
   <span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#              </span><span class="hljs-array">#        </span><span class="hljs-array">#  </span><span class="hljs-array"># </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span>#
   <span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#              </span><span class="hljs-array">#        </span><span class="hljs-array">#   </span>#<span class="hljs-array">#  </span><span class="hljs-array">#    </span>#
   <span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#####<span class="hljs-array">#         </span>######<span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span>#####

</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/Jh9h52BQ5VA" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-18-shell-variables-grab-user-input-using-read"><strong>Shell Scripting Tutorial-18:</strong> <em>Shell Variables, Grab User Input Using ‘read’</em></h2>



<h3 id="shell-variables">Shell Variables</h3>

<p>Shell scripting has some rules for variables. <br>
- variable names starts with an <strong>alphabet</strong> or <strong>underscore</strong> symbol. <br>
- variables are case sensitive. <code>my_var</code> and <code>MY_VAR</code> are different variables.  </p>



<h3 id="grab-user-input-using-read">Grab User Input Using ‘read’</h3>

<p><strong>read</strong> is used to get user input from terminal. <br>
<code>echo "Enter your name: "</code> <br>
<code>read name</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Please enter your name: "</span>
<span class="hljs-built_in">read</span> my_name
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Hello <span class="hljs-variable">$my_name</span>"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs applescript">Please enter your <span class="hljs-property">name</span>: 
mustafa celik
Hello mustafa celik
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>read name</code></td>
  <td>reads input from user and assign it to name variable</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/x6hRT1VppAc" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-19-positional-parameters"><strong>Shell Scripting Tutorial-19:</strong> <em>Positional Parameters</em></h2>

<p>Renaming a file using one positional parameter. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># This file takes a file name as an argument and renames it.</span>
<span class="hljs-comment"># run following commands for the script:</span>
<span class="hljs-comment"># cat &gt; test</span>
<span class="hljs-comment"># this is a test file.</span>
<span class="hljs-comment"># ctrl+d</span>
<span class="hljs-comment"># sh video_tutorial_19.sh test</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"provide a file name to change: "</span>
<span class="hljs-built_in">read</span> name
mv <span class="hljs-variable">$1</span> <span class="hljs-variable">$name</span>
cat <span class="hljs-variable">$name</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">provide <span class="hljs-operator">a</span> <span class="hljs-built_in">file</span> name <span class="hljs-built_in">to</span> change: 
new_name
falkdsjflad sgadg
</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/lADppydI1EA" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-20-more-on-positional-parameters"><strong>Shell Scripting Tutorial-20:</strong> <em>More on Positional Parameters</em></h2>

<p>setting positional parameters from the content of a file. <br>
<code>set cat test</code> this usage is wrong which assigns <script type="math/tex" id="MathJax-Element-1">1:cat and </script>2:test <br>
<code>echo $*</code> <br>
“set `cat test`”  this assigns file content as parameters <br>
<code>cat test</code> <br>
<code>echo $*</code>  </p>

<p>özetle <br>
reverse quotes: ters tirnak isareti <br>
accent grave: tirnak arasinda komut calistirilan kisim <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
chmod <span class="hljs-number">744</span> <span class="hljs-variable">$1</span>
ls <span class="hljs-operator">-l</span> <span class="hljs-variable">$1</span>

<span class="hljs-keyword">set</span> word1 word2 word3
<span class="hljs-built_in">echo</span> $*</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs brainfuck"><span class="hljs-literal">-</span><span class="hljs-comment">rw</span><span class="hljs-literal">-</span><span class="hljs-comment">r</span><span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">r</span><span class="hljs-literal">-</span><span class="hljs-literal">-</span> <span class="hljs-comment">1</span> <span class="hljs-comment">joker</span> <span class="hljs-comment">joker</span>   <span class="hljs-comment">375</span> <span class="hljs-comment">Aug</span> <span class="hljs-comment">27</span> <span class="hljs-comment">21:07</span> <span class="hljs-comment">video_tutorial_60</span><span class="hljs-string">.</span><span class="hljs-comment">sh</span>
<span class="hljs-literal">-</span><span class="hljs-comment">rw</span><span class="hljs-literal">-</span><span class="hljs-comment">r</span><span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">r</span><span class="hljs-literal">-</span><span class="hljs-literal">-</span> <span class="hljs-comment">1</span> <span class="hljs-comment">joker</span> <span class="hljs-comment">joker</span>   <span class="hljs-comment">201</span> <span class="hljs-comment">Aug</span> <span class="hljs-comment">27</span> <span class="hljs-comment">21:07</span> <span class="hljs-comment">video_tutorial_61</span><span class="hljs-string">.</span><span class="hljs-comment">sh</span>
<span class="hljs-literal">-</span><span class="hljs-comment">rw</span><span class="hljs-literal">-</span><span class="hljs-comment">r</span><span class="hljs-literal">-</span><span class="hljs-literal">-</span><span class="hljs-comment">r</span><span class="hljs-literal">-</span><span class="hljs-literal">-</span> <span class="hljs-comment">1</span> <span class="hljs-comment">joker</span> <span class="hljs-comment">joker</span>     <span class="hljs-comment">0</span> <span class="hljs-comment">Aug</span> <span class="hljs-comment">26</span> <span class="hljs-comment">02:08</span> <span class="hljs-comment">video_tutorial_62</span><span class="hljs-string">.</span><span class="hljs-comment">sh</span>
<span class="hljs-comment">word1</span> <span class="hljs-comment">word2</span> <span class="hljs-comment">word3</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td>set <code>cat test</code></td>
  <td>assigns content of test file to positional parameters</td>
</tr>
<tr>
  <td>set <code>who am i</code></td>
  <td>assigns output of the command to positional parameters</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/3JyuX6ncPDs" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-21-reverse-quotes-accent-graves"><strong>Shell Scripting Tutorial-21:</strong> <em>Reverse Quotes &amp; Accent Graves</em></h2>

<p><code>set shell scripting is cool</code> <br>
<code>echo $1</code> <br>
<code>echo $2</code> <br>
<code>echo $3</code> <br>
<code>echo $4</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># Renames a file to file.name</span>
<span class="hljs-comment"># Where name is the login name of the user executing the script</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># run following commands before the script:</span>
<span class="hljs-comment"># cat &gt; test</span>
<span class="hljs-comment"># my neighbour's dog is annoying.</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># set cat test</span>
<span class="hljs-comment"># echo $*</span>
<span class="hljs-comment"># set `cat test`</span>
<span class="hljs-comment"># echo $*</span>

name=<span class="hljs-variable">$1</span>
<span class="hljs-keyword">set</span> `who am i`
mv <span class="hljs-variable">$name</span> <span class="hljs-variable">$name</span>.<span class="hljs-variable">$1</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vhdl"># name <span class="hljs-keyword">of</span> the <span class="hljs-keyword">file</span> should be changed. <span class="hljs-keyword">type</span> ls <span class="hljs-keyword">to</span> observe.</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>set word1 word2 word3</code></td>
  <td>assigns <script type="math/tex" id="MathJax-Element-2">1: word1 </script>2: word2 and $3: word3</td>
</tr>
<tr>
  <td><code>echo $*</code></td>
  <td>prints all positional parameters</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/gh0Ms3YRQzM" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-22-count-the-number-of-command-line-arguments-using"><strong>Shell Scripting Tutorial-22:</strong> <em>Count the Number of Command Line Arguments Using ‘$#’</em></h2>

<p>Finding number of positional parameters that comes from <strong>command line</strong> and <strong><code>set</code></strong> command. <br>
<code>set this is video tutorial about shell scripting</code> <br>
<code>echo $#</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># Run following command before the script:</span>
<span class="hljs-comment"># sh vidoe_tutorial_22.sh *</span>

<span class="hljs-built_in">echo</span> The total number of items <span class="hljs-keyword">in</span> current directory is=<span class="hljs-variable">$#</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">The total <span class="hljs-built_in">number</span> <span class="hljs-operator">of</span> <span class="hljs-keyword">items</span> <span class="hljs-operator">in</span> current <span class="hljs-built_in">directory</span> is=<span class="hljs-number">91</span></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>echo $#</code></td>
  <td>prints the number of parameter.</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/WtEwpiLVs54" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-23-math-on-integers-using-expr"><strong>Shell Scripting Tutorial-23:</strong> <em>Math on Integers Using ‘expr’</em></h2>

<p>arithmetic operations on shell script. <br>
“a=30 b=15” <br>
“echo <code>expr $a + $b</code>” <br>
“echo <code>expr $a - $b</code>” <br>
“echo <code>expr $a \* $b</code>” <br>
“echo <code>expr $a / $b</code>” <br>
“echo <code>expr $a % $b</code>” <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># Arithmetic operations</span>

a=<span class="hljs-number">30</span> b=<span class="hljs-number">15</span>
<span class="hljs-built_in">echo</span> `expr <span class="hljs-variable">$a</span> + <span class="hljs-variable">$b</span>`
<span class="hljs-built_in">echo</span> `expr <span class="hljs-variable">$a</span> - <span class="hljs-variable">$b</span>`
<span class="hljs-built_in">echo</span> `expr <span class="hljs-variable">$a</span> \* <span class="hljs-variable">$b</span>`
<span class="hljs-built_in">echo</span> `expr <span class="hljs-variable">$a</span> / <span class="hljs-variable">$b</span>`
<span class="hljs-built_in">echo</span> `expr <span class="hljs-variable">$a</span> % <span class="hljs-variable">$b</span>`</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">45
15
450
2
0
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td>echo <code>expr $a + $b</code></td>
  <td>addition</td>
</tr>
<tr>
  <td>echo <code>expr $a - $b</code></td>
  <td>substraction</td>
</tr>
<tr>
  <td>echo <code>expr $a \* $b</code></td>
  <td>multiplication</td>
</tr>
<tr>
  <td>echo <code>expr $a / $b</code></td>
  <td>division</td>
</tr>
<tr>
  <td>echo <code>expr $a % $b</code></td>
  <td>modular division</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/dRNcGgAYF5o" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-24-operator-precedence"><strong>Shell Scripting Tutorial-24:</strong> <em>Operator Precedence</em></h2>

<p>/, *, % operations have first priority. <br>
+, - operations have second priority.  </p>

<p>echo <code>expr $a \* \( $b + $c \) / $d</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># Arithmetic Operation Precedence</span>

a=<span class="hljs-number">30</span> b=<span class="hljs-number">15</span> c=<span class="hljs-number">2</span> d=<span class="hljs-number">5</span>
<span class="hljs-built_in">echo</span> `expr <span class="hljs-variable">$a</span> \* \( <span class="hljs-variable">$b</span> + <span class="hljs-variable">$c</span> \) / <span class="hljs-variable">$d</span>`</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">102</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td>echo <code>expr $a \* \( $b + $c \) / $d</code></td>
  <td>operation precedence using \</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/nqn2NLwb8cI" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-25-math-on-real-numbers"><strong>Shell Scripting Tutorial-25:</strong> <em>Math on Real Numbers</em></h2>

<p><strong>bc</strong> usage is explained in this tutorial. <br>
<code>echo $a + $b | bc</code> <br>
<code>echo $a - $b | bc</code> <br>
<code>echo $a \* $b | bc</code> <br>
<code>echo $a / $b | bc</code>  </p>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># Floating Point Arithmetic Operations</span>

a=<span class="hljs-number">10.5</span>
b=<span class="hljs-number">3.5</span>

c=`<span class="hljs-built_in">echo</span> <span class="hljs-variable">$a</span> + <span class="hljs-variable">$b</span> | bc`
d=`<span class="hljs-built_in">echo</span> <span class="hljs-variable">$a</span> - <span class="hljs-variable">$b</span> | bc`
e=`<span class="hljs-built_in">echo</span> <span class="hljs-variable">$a</span> \* <span class="hljs-variable">$b</span> | bc`
f=`<span class="hljs-built_in">echo</span> <span class="hljs-variable">$a</span> / <span class="hljs-variable">$b</span> | bc`

<span class="hljs-built_in">echo</span> <span class="hljs-variable">$c</span> <span class="hljs-variable">$d</span> <span class="hljs-variable">$e</span> <span class="hljs-variable">$f</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">14.0 7.0 36.7 3
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>echo $a + $b (or) bc</code></td>
  <td>bs is used for floating point operations with pipe or</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/qCXjZ0xa-lM" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-26-escape-sequences"><strong>Shell Scripting Tutorial-26:</strong> <em>Escape Sequences</em></h2>

<p>customizing(text color, border etc.) the <strong>echo</strong> outputs. <br>
- new line: <strong>\n</strong> -&gt; <code>echo "hello \nworld"</code> <br>
- return: <strong>\r</strong> -&gt; <code>echo "hello \rworld"</code> basa donerek üzerine yazar. <br>
- tab: <strong>\t</strong> -&gt; <code>echo "hello \tworld"</code> <br>
- backspace:  <strong>\b</strong> -&gt; <code>echo "Hey World, \b\b\b\b\b\b\bwhat's up?"</code> bir onceki karakterin uzerine yaziyor. <br>
- bold: <strong>\033[1m</strong> <strong>\033[0m</strong> -&gt; <code>echo "\033[1mHey World, what's up?\033[0m"</code> writes the text in bold format <br>
- black background: <strong>\033[7m</strong> <strong>\033[0m</strong> -&gt; <code>echo "\033[7mHey World, what's up?\033[0m"</code> prints black background <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># Escape Sequences</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Hey World, \nwhat's up?"</span> <span class="hljs-comment"># new line</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Hey World, \rwhat's"</span> <span class="hljs-comment"># starts from beginning and prints on the previos one</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Hey World, \twhat's up?"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Hey World, \b\b\b\b\b\b\bwhat's up?"</span> <span class="hljs-comment"># comes back one character</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"\033[1mHey World, what's up?\033[0m"</span> <span class="hljs-comment"># writes the text in bold format</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"\033[7mHey World, what's up?\033[0m"</span> <span class="hljs-comment"># writes the text with black background</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vbnet">Hey World, 
what<span class="hljs-comment">'s up?</span>
what<span class="hljs-comment">'srld, </span>
Hey World,  what<span class="hljs-comment">'s up?</span>
Hey what<span class="hljs-comment">'s up?</span>
Hey World, what<span class="hljs-comment">'s up?</span>
Hey World, what<span class="hljs-comment">'s up?</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>echo "hello \nworld"</code></td>
  <td>new line</td>
</tr>
<tr>
  <td><code>echo "hello \rworld"</code></td>
  <td>return character writes from the beginning over the previous print</td>
</tr>
<tr>
  <td><code>echo "hello \tworld"</code></td>
  <td>tab character</td>
</tr>
<tr>
  <td><code>echo "Hey World, \b\b\b\b\b\b\bwhat's up?"</code></td>
  <td>backspace comes 1 character back</td>
</tr>
<tr>
  <td><code>echo "\033[1mHey World, what's up?\033[0m"</code></td>
  <td>bold character</td>
</tr>
<tr>
  <td><code>echo "\033[7mHey World, what's up?\033[0m"</code></td>
  <td>black background</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/M6sPYzHhask" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-27-do-cool-things-with-tput"><strong>Shell Scripting Tutorial-27:</strong> <em>Do Cool Things with ‘tput’</em></h2>

<p>clearing terminal. <br>
<code>tput clear</code> <br>
determining the number of rows and  columns of the terminal. <br>
<code>tput lines</code> shows number of rows. <br>
<code>tput cols</code> shows number of columns. <br>
printing character in bold. <br>
<code>tput bold</code> <br>
positioning the cursor to a specific row and column. <br>
<code>tput cup 15 20</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># tput-in action</span>

tput clear
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Total number of rows on screen=\c"</span>
tput lines
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Total number of columns on screen=\c"</span>
tput cols
tput cup <span class="hljs-number">15</span> <span class="hljs-number">20</span> <span class="hljs-comment"># cursor position row, column</span>
tput bold
<span class="hljs-built_in">echo</span> <span class="hljs-string">"This is a bold text"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"\033[0mbye bye"</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Total <span class="hljs-built_in">number</span> <span class="hljs-operator">of</span> rows <span class="hljs-command"><span class="hljs-keyword">on</span> <span class="hljs-title">screen</span>=<span class="hljs-title">35</span></span>
Total <span class="hljs-built_in">number</span> <span class="hljs-operator">of</span> columns <span class="hljs-command"><span class="hljs-keyword">on</span> <span class="hljs-title">screen</span>=<span class="hljs-title">134</span></span>













                    This is <span class="hljs-operator">a</span> bold <span class="hljs-keyword">text</span>
bye bye
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>tput clear</code></td>
  <td>clear the terminal</td>
</tr>
<tr>
  <td><code>tput lines</code></td>
  <td>Total number of rows on screen</td>
</tr>
<tr>
  <td><code>tput cols</code></td>
  <td>Total number of columns on screen</td>
</tr>
<tr>
  <td><code>tput cup 15 20</code></td>
  <td>position cursor to new row and column</td>
</tr>
<tr>
  <td><code>tput bold</code></td>
  <td>print in bold format</td>
</tr>
<tr>
  <td><code>echo "\033[0mbye bye"</code></td>
  <td>ends printing in bold</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/9WisxGxVzgM" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-28-if-then-statement-in-action"><strong>Shell Scripting Tutorial-28:</strong> <em>‘if-then’ Statement in Action</em></h2>

<p>terminalde her komut calistiktan sonra, komutun basarili olup olmadigini gosteren bir sayi doner. <br>
bu ciktiyi gormek icin su komut kullanilir: <br>
<code>mkdir new</code> <br>
<code>echo $?</code>  </p>

<p>renaming a file using if statement. <br>
<code>if mv source.txt target.txt</code> <br>
<code>then</code> <br>
<code>echo "Your file has been succesfully renamed."</code> <br>
<code>fi</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># if-then statement in action</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># touch test</span>
<span class="hljs-comment"># sh video_tutorial_28.sh </span>
<span class="hljs-comment"># sh video_tutorial_28.sh</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter source and target file names:"</span>
<span class="hljs-built_in">read</span> <span class="hljs-built_in">source</span> target
<span class="hljs-keyword">if</span> mv <span class="hljs-variable">$source</span> <span class="hljs-variable">$target</span>
<span class="hljs-keyword">then</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Your file has been successfully renamed."</span>
<span class="hljs-keyword">fi</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Enter source <span class="hljs-operator">and</span> target <span class="hljs-built_in">file</span> names:
test new_name     
Your <span class="hljs-built_in">file</span> has been successfully renamed.
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
</tr>
</thead>
<tbody><tr>
  <td>usage of if-then statement</td>
</tr>
<tr>
  <td><code>if something_true</code></td>
</tr>
<tr>
  <td><code>then</code></td>
</tr>
<tr>
  <td><code>echo "condition is correct"</code></td>
</tr>
<tr>
  <td><code>fi</code></td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/elN9wmcIumE" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-29-the-if-then-else-statement"><strong>Shell Scripting Tutorial-29:</strong> <em>The ‘if-then-else’ Statement</em></h2>

<p>renaming a file using if statement. <br>
<code>if mv source.txt target.txt</code> <br>
<code>then</code> <br>
<code>echo "Your file has been successfully renamed."</code> <br>
<code>else</code> <br>
<code>echo "file has NOT been  renamed."</code> <br>
<code>fi</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># if-then-else statement in action</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># touch test</span>
<span class="hljs-comment"># sh video_tutorial_29.sh</span>
<span class="hljs-comment"># sh video_tutorial_29.sh</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter source and target file names."</span>
<span class="hljs-built_in">read</span> <span class="hljs-built_in">source</span> target
<span class="hljs-keyword">if</span> mv <span class="hljs-variable">$source</span> <span class="hljs-variable">$target</span>
<span class="hljs-keyword">then</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Your file has been successfully renamed."</span>
<span class="hljs-keyword">else</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Your file has NOT been successfully renamed."</span>
<span class="hljs-keyword">fi</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">bash_script@pc $ sh video_tutorial_29.sh 
Enter source <span class="hljs-operator">and</span> target <span class="hljs-built_in">file</span> names.
test new_name
Your <span class="hljs-built_in">file</span> has been successfully renamed.
bash_script@pc $ sh video_tutorial_29.sh 
Enter source <span class="hljs-operator">and</span> target <span class="hljs-built_in">file</span> names.
test new_name
mv: cannot stat ‘test’: No such <span class="hljs-built_in">file</span> <span class="hljs-operator">or</span> <span class="hljs-built_in">directory</span>
Your <span class="hljs-built_in">file</span> has NOT been successfully renamed.</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
</tr>
</thead>
<tbody><tr>
  <td>usage of if-then statement</td>
</tr>
<tr>
  <td><code>if something_true_or_false</code></td>
</tr>
<tr>
  <td><code>then</code></td>
</tr>
<tr>
  <td><code>echo "condition is true"</code></td>
</tr>
<tr>
  <td><code>else</code></td>
</tr>
<tr>
  <td><code>echo "condition is false"</code></td>
</tr>
<tr>
  <td><code>fi</code></td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/1s3r0Cnsy3U" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-30-run-checks-on-numbers"><strong>Shell Scripting Tutorial-30:</strong> <em>Run Checks on Numbers</em></h2>

<p>if checks statements are following: <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a number between 10 and 20: \c"</span>
<span class="hljs-built_in">read</span> num

<span class="hljs-keyword">if</span> [ <span class="hljs-variable">$num</span> <span class="hljs-operator">-lt</span> <span class="hljs-number">10</span> ]
<span class="hljs-keyword">then</span> 
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"That was under the belt partner."</span>
<span class="hljs-keyword">elif</span> [ <span class="hljs-variable">$num</span> <span class="hljs-operator">-gt</span> <span class="hljs-number">20</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"That went over my head."</span>
<span class="hljs-keyword">elif</span> [ <span class="hljs-variable">$num</span> <span class="hljs-operator">-eq</span> <span class="hljs-number">10</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"That is equal to 10."</span>
<span class="hljs-keyword">elif</span> [ <span class="hljs-variable">$num</span> -le <span class="hljs-number">10</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"That is less than and equal to 10."</span>
<span class="hljs-keyword">elif</span> [ <span class="hljs-variable">$num</span> -ge <span class="hljs-number">10</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"That is greater than and equal to 10."</span>
<span class="hljs-keyword">elif</span> [ <span class="hljs-variable">$num</span> <span class="hljs-operator">-ne</span> <span class="hljs-number">10</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"That is not equal to 10."</span>
<span class="hljs-keyword">else</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"Now you are making sense."</span>
<span class="hljs-keyword">fi</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs applescript">Enter a <span class="hljs-type">number</span> <span class="hljs-keyword">between</span> <span class="hljs-number">10</span> <span class="hljs-keyword">and</span> <span class="hljs-number">20</span>: <span class="hljs-number">12</span>
That <span class="hljs-keyword">is</span> <span class="hljs-keyword">greater than</span> <span class="hljs-keyword">and</span> <span class="hljs-keyword">equal</span> <span class="hljs-keyword">to</span> <span class="hljs-number">10.</span></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>-eq</code></td>
  <td>equal</td>
</tr>
<tr>
  <td><code>-lt</code></td>
  <td>less than</td>
</tr>
<tr>
  <td><code>-gt</code></td>
  <td>greater than</td>
</tr>
<tr>
  <td><code>-le</code></td>
  <td>less than and equal</td>
</tr>
<tr>
  <td><code>-ge</code></td>
  <td>greater than and equal</td>
</tr>
<tr>
  <td><code>-ne</code></td>
  <td>not equal</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/YhtHm9gyMxE" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-31-run-checks-on-files"><strong>Shell Scripting Tutorial-31:</strong> <em>Run Checks on Files</em></h2>

<p><strong>character space file</strong>: text files <br>
<strong>block space file</strong>: video and image files which can not be displayed by text editor <br>
<strong>directory space file</strong>: folders are also a file  </p>

<p><code>if [ -f $fname ]</code> checks is it file or not.  </p>

<p><strong>-f</strong>: checks for file <br>
<strong>-d</strong>: checks for directory <br>
<strong>-c</strong>: checks for character space file(text file) <br>
<strong>-b</strong>: checks for block space file(image, video) <br>
<strong>-r</strong>: checks read permission <br>
<strong>-w</strong>: checks write permission <br>
<strong>-x</strong>: checks execute permission <br>
<strong>-s</strong>: checks if the file size is greater 0 or not <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a name: \c"</span>
<span class="hljs-built_in">read</span> fname
<span class="hljs-keyword">if</span> [ <span class="hljs-operator">-f</span> <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks file</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You indeed entered a file name."</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ <span class="hljs-operator">-d</span> <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks directory</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You indeed entered a folder name."</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ -c <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks character space file</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You indeed entered a character space(text) file name."</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ -b <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks block space file</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You indeed entered a block space(image,videp) file name."</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ -r <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks read permission</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"File has read permission."</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ -w <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks write permission</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"File has write permission."</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ -x <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks execute permission</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"File has execute permission."</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ <span class="hljs-operator">-s</span> <span class="hljs-variable">$fname</span> ] <span class="hljs-comment"># checks size is greater than 0 or not</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"File size is gretaer than zero."</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Enter <span class="hljs-operator">a</span> name: new_name
You indeed entered <span class="hljs-operator">a</span> <span class="hljs-built_in">file</span> name.
File has <span class="hljs-built_in">read</span> permission.
File has <span class="hljs-built_in">write</span> permission.
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>if [ -f $fname ]</code></td>
  <td>checks file or not</td>
</tr>
<tr>
  <td><code>if [ -d $fname ]</code></td>
  <td>checks directory or not</td>
</tr>
<tr>
  <td><code>if [ -c $fname ]</code></td>
  <td>checks character space file or not</td>
</tr>
<tr>
  <td><code>if [ -b $fname ]</code></td>
  <td>checks block space file or not</td>
</tr>
<tr>
  <td><code>if [ -r $fname ]</code></td>
  <td>checks has read permission or not</td>
</tr>
<tr>
  <td><code>if [ -w $fname ]</code></td>
  <td>checks has write permission or not</td>
</tr>
<tr>
  <td><code>if [ -x $fname ]</code></td>
  <td>checks has execute permission or not</td>
</tr>
<tr>
  <td><code>if [ -s $fname ]</code></td>
  <td>checks size is greater than 0 or not</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/LGT3HaKg4lU" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-32-append-text-to-a-file-through-shell-script"><strong>Shell Scripting Tutorial-32:</strong> <em>Append Text to a File Through Shell Script</em></h2>

<p>usage of the if else statement and file checks command. <br>
example code: <br>
<code>echo "Enter file name:\c"</code> <br>
<code>read fname</code> <br>
<code>if [ -f $fname ]</code> <br>
<code>then</code> <br>
<code>if [ -w $fname ]</code> <br>
<code>then</code> <br>
<code>echo "Type matter to append. To quit press ctrl+d."</code> <br>
<code>cat &gt;&gt; $fname</code> <br>
<code>else</code> <br>
<code>echo "You do not have permission to write."</code> <br>
<code>fi</code> <br>
<code>fi</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># 1. script ask users to enter a name.</span>
<span class="hljs-comment"># 2. check the folder exist or not</span>
<span class="hljs-comment"># 3. if file exists check the user has write permission.</span>
<span class="hljs-comment"># 4. if the user has write permission, presents append option to user.</span>
<span class="hljs-comment"># 5. if the user has not write permission, display message show not permitted.</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter file name:\c"</span>
<span class="hljs-built_in">read</span> fname
<span class="hljs-keyword">if</span> [ <span class="hljs-operator">-f</span> <span class="hljs-variable">$fname</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-keyword">if</span> [ -w <span class="hljs-variable">$fname</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"Type matter to append. To quit press ctrl+d."</span>
        cat &gt;&gt; <span class="hljs-variable">$fname</span>
    <span class="hljs-keyword">else</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"You do not have permission to write."</span>
    <span class="hljs-keyword">fi</span>
<span class="hljs-keyword">fi</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vhdl">Enter <span class="hljs-keyword">file</span> name:new_name
<span class="hljs-keyword">Type</span> matter <span class="hljs-keyword">to</span> append. <span class="hljs-keyword">To</span> quit press ctrl+d.
skdg
ssdgfs
</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/VOAVGwPbwlI" frameborder="0" allowfullscreen></iframe>





<h2 id="shell-scripting-tutorial-33-run-checks-on-strings"><strong>Shell Scripting Tutorial-33:</strong> <em>Run Checks on Strings</em></h2>

<p>string checks: <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># comparison of the strings (string checks)</span>

str1=<span class="hljs-string">"Hey You!"</span>
str2=<span class="hljs-string">"What's up?"</span>
str3=<span class="hljs-string">""</span> <span class="hljs-comment"># null variable</span>
str3=   <span class="hljs-comment"># null variable</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"str1: <span class="hljs-variable">$str1</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"str2: <span class="hljs-variable">$str2</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"str3: <span class="hljs-variable">$str3</span>"</span>


[ <span class="hljs-string">"<span class="hljs-variable">$str1</span>"</span> = <span class="hljs-string">"<span class="hljs-variable">$str2</span>"</span> ] <span class="hljs-comment"># equal</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"str1 = str2 \t-&gt; $?"</span>

[ <span class="hljs-string">"<span class="hljs-variable">$str1</span>"</span> != <span class="hljs-string">"<span class="hljs-variable">$str2</span>"</span> ] <span class="hljs-comment"># not equal</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"str1 != str2 \t-&gt; $?"</span>

[ -n <span class="hljs-string">"<span class="hljs-variable">$str1</span>"</span> ] <span class="hljs-comment"># greater than zero</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"[ -n str1 ] \t-&gt; $?"</span>

[ -n <span class="hljs-string">"<span class="hljs-variable">$str3</span>"</span> ] <span class="hljs-comment"># greater than zero</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"[ -n str3 ] \t-&gt; $?"</span>

[ -z <span class="hljs-string">"<span class="hljs-variable">$str1</span>"</span> ] <span class="hljs-comment"># length of string is zero or not?</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"[ -z str1 ] \t-&gt; $?"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs erlang-repl"><span class="hljs-function_or_atom">str1</span>: <span class="hljs-variable">Hey</span> <span class="hljs-variable">You</span><span class="hljs-exclamation_mark">!</span>
<span class="hljs-function_or_atom">str2</span>: <span class="hljs-variable">What's</span> <span class="hljs-function_or_atom">up</span>?
<span class="hljs-function_or_atom">str3</span>: 
<span class="hljs-function_or_atom">str1</span> = <span class="hljs-function_or_atom">str2</span>     <span class="hljs-arrow">-&gt;</span> <span class="hljs-number">1</span>
<span class="hljs-function_or_atom">str1</span> <span class="hljs-exclamation_mark">!</span>= <span class="hljs-function_or_atom">str2</span>    <span class="hljs-arrow">-&gt;</span> <span class="hljs-number">0</span>
[ -<span class="hljs-function_or_atom">n</span> <span class="hljs-function_or_atom">str1</span> ]     <span class="hljs-arrow">-&gt;</span> <span class="hljs-number">0</span>
[ -<span class="hljs-function_or_atom">n</span> <span class="hljs-function_or_atom">str3</span> ]     <span class="hljs-arrow">-&gt;</span> <span class="hljs-number">1</span>
[ -<span class="hljs-function_or_atom">z</span> <span class="hljs-function_or_atom">str1</span> ]     <span class="hljs-arrow">-&gt;</span> <span class="hljs-number">1</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>[ "$str1" = "$str2" ]</code></td>
  <td>checks if string are equal</td>
</tr>
<tr>
  <td><code>[ "$str1" != "$str2" ]</code></td>
  <td>checks if string are not equal</td>
</tr>
<tr>
  <td><code>[ -n "$str1"</code></td>
  <td>checks if string length is greater than zero</td>
</tr>
<tr>
  <td><code>[ -z "$str1" ]</code></td>
  <td>checks if string length is zero</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/IIhh1e1fURU" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-34-run-checks-on-stringthe-and-logical-operator"><strong>Shell Scripting Tutorial-34:</strong> <em>Run Checks on StringThe ‘AND’ Logical Operator</em></h2>

<p><strong>-a</strong> is the ‘AND’ operator for shell scripting. <br>
Following if statement checks the variable if it is between 50 and 100. <br>
<code>if [ $num -le 100 -a $num -ge 50 ]</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># 1. script ask users to enter a number between 50-100</span>
<span class="hljs-comment"># 2. store input</span>
<span class="hljs-comment"># 3. check the input between 50-100</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a number between 50 and 100:\c"</span>
<span class="hljs-built_in">read</span> num

<span class="hljs-keyword">if</span> [ <span class="hljs-variable">$num</span> -le <span class="hljs-number">100</span> <span class="hljs-operator">-a</span> <span class="hljs-variable">$num</span> -ge <span class="hljs-number">50</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"The number is between 50 and 100."</span>
<span class="hljs-keyword">else</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"The number is not between 50 and 100."</span>
<span class="hljs-keyword">fi</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs applescript">Enter a <span class="hljs-type">number</span> <span class="hljs-keyword">between</span> <span class="hljs-number">50</span> <span class="hljs-keyword">and</span> <span class="hljs-number">100</span>:<span class="hljs-number">54</span>
The <span class="hljs-type">number</span> <span class="hljs-keyword">is</span> <span class="hljs-keyword">between</span> <span class="hljs-number">50</span> <span class="hljs-keyword">and</span> <span class="hljs-number">100.</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>if [ $num -le 100 -a $num -ge 50 ]</code></td>
  <td>usage of AND operator</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/t7pJDlAkgy4" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-35-count-the-number-of-characters-in-users-input-in-your-script"><strong>Shell Scripting Tutorial-35:</strong> <em>Count the Number of Characters in User’s Input in Your Script</em></h2>

<p>checking the number of the character of the variable. <br>
<code>if [ 'echo $var | wc -c' -eq 2 ]</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># 1. script ask users to enter a character</span>
<span class="hljs-comment"># 2. check if one character is entered or not</span>
<span class="hljs-comment"># 3. if not print invalid input</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter  a character:\c"</span>
<span class="hljs-built_in">read</span> var

<span class="hljs-keyword">if</span> [ `<span class="hljs-built_in">echo</span> <span class="hljs-variable">$var</span> | wc -c` <span class="hljs-operator">-eq</span> <span class="hljs-number">2</span> ] <span class="hljs-comment"># check if there is one character or not. 2 because of enter character.</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You entered a character."</span>
<span class="hljs-keyword">else</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"Invalid input."</span>
<span class="hljs-keyword">fi</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Enter  <span class="hljs-operator">a</span> <span class="hljs-keyword">character</span>:d
You entered <span class="hljs-operator">a</span> <span class="hljs-keyword">character</span>.</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td>`if [ ‘echo $var</td>
  <td>wc -c’ -eq 2 ]`</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/B0tiwZQYBQA" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-36-the-or-logical-operator"><strong>Shell Scripting Tutorial-36:</strong> <em>The ‘OR’ Logical Operator</em></h2>

<p><strong>-0</strong> is the ‘OR’ operator for shell scripting. <br>
Following if statement checks the variable if it is vowel or not. <br>
<code>if [ $var  = a -o $var  = e -o $var  = i -o $var  = u -o $var  = o ]</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># 1. script ask users to enter a character</span>
<span class="hljs-comment"># 2. check if one character is entered or more than character</span>
<span class="hljs-comment"># 3. if one character is input, check if it is vowel or not</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a lowercase character:\c"</span>
<span class="hljs-built_in">read</span> var

<span class="hljs-keyword">if</span> [ `<span class="hljs-built_in">echo</span> <span class="hljs-variable">$var</span> | wc -c` <span class="hljs-operator">-eq</span> <span class="hljs-number">2</span> ] <span class="hljs-comment"># check if there is one character or not. 2 because of enter character.</span>
<span class="hljs-keyword">then</span>
    <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$var</span>  = a -o <span class="hljs-variable">$var</span>  = e -o <span class="hljs-variable">$var</span>  = i -o <span class="hljs-variable">$var</span>  = u -o <span class="hljs-variable">$var</span>  = o ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"You entered a vowel."</span>
    <span class="hljs-keyword">else</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"You did not enter a vowel."</span>
    <span class="hljs-keyword">fi</span>
<span class="hljs-keyword">else</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"Invalid input."</span>
<span class="hljs-keyword">fi</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Enter <span class="hljs-operator">a</span> lowercase <span class="hljs-keyword">character</span>:m
You did <span class="hljs-operator">not</span> enter <span class="hljs-operator">a</span> vowel.

Enter <span class="hljs-operator">a</span> lowercase <span class="hljs-keyword">character</span>:<span class="hljs-operator">a</span>
You entered <span class="hljs-operator">a</span> vowel.</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>if [ $var  = a -o $var  = e -o $var  = i -o $var  = u -o $var  = o ]</code></td>
  <td>usage of OR operator</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/vP8yT1Ni9JY" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-37-the-case-statement"></h2><strong>Shell Scripting Tutorial-37:</strong> <em>The ‘case’ Statement</em> ##</h2>

<p>The case statement is the fourth version of the condition statements. <br>
1. if <br>
2. if else <br>
3. elif <br>
4. case</p>

<p>usage of case statement: <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># 1. script ask users to enter a character</span>
<span class="hljs-comment"># 2. check whether the character is lowercase or uppercase or digit or special character</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a character:\c"</span>
<span class="hljs-built_in">read</span> var

<span class="hljs-keyword">case</span> <span class="hljs-variable">$var</span> <span class="hljs-keyword">in</span>
[a-z])
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You entered a lowercase character."</span>
    ;;
[A-Z])
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You entered an uppercase character."</span>
    ;;
[<span class="hljs-number">0</span>-<span class="hljs-number">9</span>])
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You entered a digit."</span>
    ;;
?)
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You entered a special character."</span>
    ;;
*)
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"You entered more than one character."</span>
    ;;
<span class="hljs-keyword">esac</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Enter <span class="hljs-operator">a</span> <span class="hljs-keyword">character</span>:d
You entered <span class="hljs-operator">a</span> lowercase <span class="hljs-keyword">character</span>.

Enter <span class="hljs-operator">a</span> <span class="hljs-keyword">character</span>:D
You entered <span class="hljs-operator">an</span> uppercase <span class="hljs-keyword">character</span>.

Enter <span class="hljs-operator">a</span> <span class="hljs-keyword">character</span>:ad
You entered more than <span class="hljs-constant">one</span> <span class="hljs-keyword">character</span>.

Enter <span class="hljs-operator">a</span> <span class="hljs-keyword">character</span>:<span class="hljs-number">4</span>
You entered <span class="hljs-operator">a</span> digit.</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/bVL9pDfvAMc" frameborder="0" allowfullscreen></iframe>



<h2 id="shell-scripting-tutorial-38-another-date-with-case-statement"><strong>Shell Scripting Tutorial-38:</strong> <em>Another Date with ‘case’ Statement</em></h2>

<p>Another example of case statement. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># 1. script ask users to enter a word</span>
<span class="hljs-comment"># 2. 1 check if word starts a vowel character or not</span>
<span class="hljs-comment"># 3. 2 check if the word starts with a digit</span>
<span class="hljs-comment"># 4. 3 check if the word ends with a digit</span>
<span class="hljs-comment"># 5. 4 check if the word s 3-letter word</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a word:\c"</span>
<span class="hljs-built_in">read</span> word

<span class="hljs-keyword">case</span> <span class="hljs-variable">$word</span> <span class="hljs-keyword">in</span>
[aeiou]* | [AEIOU]*)
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"The words begins with a vowel."</span>
    ;;
[<span class="hljs-number">0</span>-<span class="hljs-number">9</span>]*)
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"The words begins with a digit."</span>
    ;;
*[<span class="hljs-number">0</span>-<span class="hljs-number">9</span>])
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"The words ends with a digit."</span>
    ;;
???)
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"The words is a 3-letter word."</span>
    ;;
*)
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"Something else."</span>
    ;;
<span class="hljs-keyword">esac</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Enter <span class="hljs-operator">a</span> <span class="hljs-built_in">word</span>:mustafa
Something <span class="hljs-keyword">else</span>.

Enter <span class="hljs-operator">a</span> <span class="hljs-built_in">word</span>:<span class="hljs-number">234</span>
The <span class="hljs-keyword">words</span> <span class="hljs-operator">begins</span> <span class="hljs-operator">with</span> <span class="hljs-operator">a</span> digit.

Enter <span class="hljs-operator">a</span> <span class="hljs-built_in">word</span>:msd 
The <span class="hljs-keyword">words</span> is <span class="hljs-operator">a</span> <span class="hljs-number">3</span>-letter <span class="hljs-built_in">word</span>.

Enter <span class="hljs-operator">a</span> <span class="hljs-built_in">word</span>:asasdf3
The <span class="hljs-keyword">words</span> <span class="hljs-operator">begins</span> <span class="hljs-operator">with</span> <span class="hljs-operator">a</span> vowel.

Enter <span class="hljs-operator">a</span> <span class="hljs-built_in">word</span>:dfds3
The <span class="hljs-keyword">words</span> <span class="hljs-operator">ends</span> <span class="hljs-operator">with</span> <span class="hljs-operator">a</span> digit.
</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/pyhzv8XZnww" frameborder="0" allowfullscreen></iframe>



<h2 id="shell-scripting-tutorial-39-the-while-loop"><strong>Shell Scripting Tutorial-39:</strong> <em>The ‘while’ Loop</em></h2>

<p>usage of ‘while’ loop. <br>
display the number 1 to 10. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># while loop in action</span>

<span class="hljs-comment"># 1. display number 1 to 10.</span>

count=<span class="hljs-number">1</span>
<span class="hljs-keyword">while</span> [ <span class="hljs-variable">$count</span> -le <span class="hljs-number">10</span> ]
<span class="hljs-keyword">do</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-variable">$count</span>
    count=`expr <span class="hljs-variable">$count</span> + <span class="hljs-number">1</span>`
<span class="hljs-keyword">done</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">1
2
3
4
5
6
7
8
9
10
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>while [ $count -le 10 ]</code></td>
  <td>usage of while loop</td>
</tr>
<tr>
  <td><code>do</code></td>
  <td></td>
</tr>
<tr>
  <td><code>echo $count</code></td>
  <td></td>
</tr>
<tr>
  <td><code>done</code></td>
  <td></td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/50UH6IPM1KE" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-40-the-until-loop"><strong>Shell Scripting Tutorial-40:</strong> <em>The ‘until’ Loop</em></h2>

<p>usage of until loop. <br>
display the numbers 1 to 9. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># until loop in action</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># 1. display number 1 to 9.</span>

count=<span class="hljs-number">1</span>
until [ <span class="hljs-variable">$count</span> -ge <span class="hljs-number">10</span> ]
<span class="hljs-keyword">do</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$count</span>"</span>
    count=`expr <span class="hljs-variable">$count</span> + <span class="hljs-number">1</span>`
<span class="hljs-keyword">done</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">1
2
3
4
5
6
7
8
9</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>until [ $count -gt 10 ]</code></td>
  <td>usage of until loop</td>
</tr>
<tr>
  <td><code>do</code></td>
  <td></td>
</tr>
<tr>
  <td><code>echo $count</code></td>
  <td></td>
</tr>
<tr>
  <td><code>done</code></td>
  <td></td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/UYjodeCOQRo" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-41-the-for-loop"><strong>Shell Scripting Tutorial-41:</strong> <em>The ‘for’ Loop</em></h2>

<p>usage of for loop. <br>
for loop is pretty different than until and while loop. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. display folders in the directory not the files</span>

<span class="hljs-comment"># list the directories</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"\ndirectories: "</span>
<span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> * <span class="hljs-comment"># asterics means all the items in the current directory</span>
<span class="hljs-keyword">do</span>
    <span class="hljs-keyword">if</span> [ <span class="hljs-operator">-d</span> <span class="hljs-variable">$item</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$item</span>"</span>
    <span class="hljs-keyword">fi</span>
<span class="hljs-keyword">done</span>

<span class="hljs-comment"># list the files</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"\nfiles:"</span>
<span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> * <span class="hljs-comment"># asterics means all the items in the current directory</span>
<span class="hljs-keyword">do</span>
    <span class="hljs-keyword">if</span> [ <span class="hljs-operator">-f</span> <span class="hljs-variable">$item</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$item</span>"</span>
    <span class="hljs-keyword">fi</span>
<span class="hljs-keyword">done</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs avrasm"><span class="hljs-label">directories:</span> 
folder1
folder2
folder3
sandbox

<span class="hljs-label">files:</span>
animals
commandlist_tutorial_50
create_consecutive_files<span class="hljs-preprocessor">.sh</span>
empty_file1
empty_file2
empty_file3
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>for item in *</code></td>
  <td>usage of for loop. * means all items in current directory</td>
</tr>
<tr>
  <td><code>do</code></td>
  <td></td>
</tr>
<tr>
  <td><code>...</code></td>
  <td></td>
</tr>
<tr>
  <td><code>done</code></td>
  <td></td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/sIYmF32Ic8s" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-42-rant-little-work"><strong>Shell Scripting Tutorial-42:</strong> <em>Rant &amp; Little Work</em></h2>

<p>comparison of real number.  </p>

<p>another comparison for floating point numbers. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. comparison of the real numbers</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"following method is for integers and not working for real numbers: "</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"a=4.5
b=4.5
[ a -eq b ]
echo ?
"</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"change real numbers to string to compare"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"a=4.5
b=4.5
[ "</span>a<span class="hljs-string">" = "</span>b<span class="hljs-string">" ]
echo ?
"</span>

a=<span class="hljs-number">4.5</span>
b=<span class="hljs-number">4.5</span>
[ <span class="hljs-string">"<span class="hljs-variable">$a</span>"</span> = <span class="hljs-string">"<span class="hljs-variable">$b</span>"</span> ]
<span class="hljs-built_in">echo</span> $?

<span class="hljs-comment"># another comparison example</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"\nanother comparison example:"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"min=12.45
val=10.35

if [ 1 -eq (echo {val} &lt; {min}| bc) ]
then
    min={val}
fi

echo min"</span>

min=<span class="hljs-number">12.45</span>
val=<span class="hljs-number">10.35</span>

<span class="hljs-keyword">if</span> [ <span class="hljs-number">1</span> <span class="hljs-operator">-eq</span> <span class="hljs-string">"<span class="hljs-variable">$(echo "${val} &lt; ${min}" | bc)</span>"</span> ]
<span class="hljs-keyword">then</span>
    min=<span class="hljs-variable">${val}</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$min</span>"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs oxygene">following <span class="hljs-function"><span class="hljs-keyword">method</span> <span class="hljs-title">is</span> <span class="hljs-title">for</span> <span class="hljs-title">integers</span> <span class="hljs-title">and</span> <span class="hljs-title">not</span> <span class="hljs-title">working</span> <span class="hljs-title">for</span> <span class="hljs-title">real</span> <span class="hljs-title">numbers</span>:</span> 
a=<span class="hljs-number">4.5</span>
b=<span class="hljs-number">4.5</span>
[ a -eq b ]
echo ?

change real numbers <span class="hljs-keyword">to</span> string <span class="hljs-keyword">to</span> compare
a=<span class="hljs-number">4.5</span>
b=<span class="hljs-number">4.5</span>
[ a = b ]
echo ?

<span class="hljs-number">0</span>

another comparison example:
min=<span class="hljs-number">12.45</span>
val=<span class="hljs-number">10.35</span>

<span class="hljs-keyword">if</span> [ <span class="hljs-number">1</span> -eq (echo <span class="hljs-comment">{val}</span> &lt; <span class="hljs-comment">{min}</span>| bc) ]
<span class="hljs-keyword">then</span>
    min=<span class="hljs-comment">{val}</span>
fi

echo min
<span class="hljs-number">10.35</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>[ $a -eq $b ]</code></td>
  <td>this is for integers and not working for real numbers</td>
</tr>
<tr>
  <td><code>[ "$a" = "$b" ]</code></td>
  <td>this converts number to string and compares them</td>
</tr>
<tr>
  <td><code>min=12.45</code></td>
  <td>another comparison example for floating point numbers</td>
</tr>
<tr>
  <td><code>val=10.35</code></td>
  <td></td>
</tr>
<tr>
  <td>`if [ 1 -eq “<script type="math/tex" id="MathJax-Element-3">(echo “</script>{val} &lt; ${min}”</td>
  <td>bc)” ]`</td>
</tr>
<tr>
  <td><code>then</code></td>
  <td></td>
</tr>
<tr>
  <td><code>min=${val}</code></td>
  <td></td>
</tr>
<tr>
  <td><code>fi</code></td>
  <td></td>
</tr>
<tr>
  <td><code>echo "$min"</code></td>
  <td></td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/H-QPEjNri1U" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-43-search-patterns-using-grep"><strong>Shell Scripting Tutorial-43:</strong> <em>Search Patterns Using ‘grep’</em></h2>

<p>Usage of ‘grep’ command. <br>
<strong>grep</strong> is same as using <strong>ctrl+f</strong> option in a file.  </p>

<p><strong>grep -i</strong>: ignores case sensitivity <br>
<strong>grep -n</strong>: shows line numbers for search results. <br>
<strong>grep -c</strong>: shows the total number of the line that has money. <br>
<strong>grep -v</strong>: shows the grep result for not matching lines. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. search text in file text_tutorial_43</span>

<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># create a file name text_tutorial_43 with text contains money word.</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Search money in the file with case sensitivity:"</span>
grep money text_tutorial_43

<span class="hljs-built_in">echo</span> <span class="hljs-string">"\nSearch money in the file without case sensitivity:"</span>
grep -i money text_tutorial_43

<span class="hljs-built_in">echo</span> <span class="hljs-string">"\nSearch money in the file with case sensitivity and line numbers:"</span>
grep -i -n money text_tutorial_43

<span class="hljs-built_in">echo</span> <span class="hljs-string">"\nSearch money in the file with case sensitivity, line numbers and shows count:"</span>
grep -i -n -c money text_tutorial_43

<span class="hljs-built_in">echo</span> <span class="hljs-string">"\nSearch money in the file with case sensitivity, line numbers and shows count of money does not exist:"</span>
grep -i -n -c -v money text_tutorial_43</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs applescript">Search money <span class="hljs-keyword">in</span> <span class="hljs-keyword">the</span> <span class="hljs-type">file</span> <span class="hljs-keyword">with</span> case sensitivity:

Search money <span class="hljs-keyword">in</span> <span class="hljs-keyword">the</span> <span class="hljs-type">file</span> <span class="hljs-keyword">without</span> case sensitivity:
Money, <span class="hljs-keyword">get</span> away
Money, <span class="hljs-keyword">it</span>'s a gas
Money, <span class="hljs-keyword">get</span> <span class="hljs-keyword">back</span>
Money, <span class="hljs-keyword">it</span>'s a hit 
Money, <span class="hljs-keyword">it</span>'s a crime 
Money, so they <span class="hljs-command">say</span> 

Search money <span class="hljs-keyword">in</span> <span class="hljs-keyword">the</span> <span class="hljs-type">file</span> <span class="hljs-keyword">with</span> case sensitivity <span class="hljs-keyword">and</span> line numbers:
<span class="hljs-number">1</span>:Money, <span class="hljs-keyword">get</span> away
<span class="hljs-number">3</span>:Money, <span class="hljs-keyword">it</span>'s a gas
<span class="hljs-number">8</span>:Money, <span class="hljs-keyword">get</span> <span class="hljs-keyword">back</span>
<span class="hljs-number">10</span>:Money, <span class="hljs-keyword">it</span>'s a hit 
<span class="hljs-number">15</span>:Money, <span class="hljs-keyword">it</span>'s a crime 
<span class="hljs-number">17</span>:Money, so they <span class="hljs-command">say</span> 

Search money <span class="hljs-keyword">in</span> <span class="hljs-keyword">the</span> <span class="hljs-type">file</span> <span class="hljs-keyword">with</span> case sensitivity, line numbers <span class="hljs-keyword">and</span> shows <span class="hljs-command">count</span>:
<span class="hljs-number">6</span>

Search money <span class="hljs-keyword">in</span> <span class="hljs-keyword">the</span> <span class="hljs-type">file</span> <span class="hljs-keyword">with</span> case sensitivity, line numbers <span class="hljs-keyword">and</span> shows <span class="hljs-command">count</span> <span class="hljs-keyword">of</span> money <span class="hljs-keyword">does</span> <span class="hljs-keyword">not</span> exist:
<span class="hljs-number">16</span></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>grep money text_file</code></td>
  <td>search “money” in text_file</td>
</tr>
<tr>
  <td><code>grep -i money text_file</code></td>
  <td>search “money” in text_file by ignoring case sensitivity.</td>
</tr>
<tr>
  <td><code>grep -i -n money text_file</code></td>
  <td>search “money” in text_file by ignoring case sensitivity, and shows line numbers</td>
</tr>
<tr>
  <td><code>grep -i -c money text_file</code></td>
  <td>search “money” in text_file by ignoring case sensitivity, and shows count of money line</td>
</tr>
<tr>
  <td><code>grep -i -v money text_file</code></td>
  <td>search “money” in text_file by ignoring case sensitivity, and shows the lines that has no money</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/bQ_yxb25wEk" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-44-the-passwd-file-explained"><strong>Shell Scripting Tutorial-44:</strong> <em>The ‘passwd’ File Explained</em></h2>

<p>Usage of file “passwd”.  </p>

<p><code>cat /etc/passwd</code> command shows the content of passwd file. <br>
<strong>joker:x:1000:1000:joker,,,:/home/joker:/bin/bash</strong>  </p>

<p>filed 1 -&gt; <strong>joker</strong>: user name <br>
field 2 -&gt; <strong>x</strong>: password is encrypted for the user <br>
field 3 -&gt; <strong>1000</strong>: uid (userid). from 1 to 99 id are reserved for predefined accounts <br>
field 4 -&gt; <strong>1000</strong>: group id. <br>
field 5 -&gt; <strong>joker,,,</strong>: the name of the computer <br>
field 6 -&gt; <strong>/home/joker</strong>: home folder <br>
field 7 -&gt; <strong>/bin/bash</strong>: shell  <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs asciidoc">#!/usr/bin/env bash

cat /etc/passwd

echo "\n\nfiled 1 -&gt; *<span class="hljs-strong">*joker*</span><span class="hljs-strong">*: user name
field 2 -&gt; *</span><span class="hljs-strong">*x*</span><span class="hljs-strong">*: password is encrypted for the user
field 3 -&gt; *</span><span class="hljs-strong">*1000*</span><span class="hljs-strong">*: uid (userid). from 1 to 99 id are reserved for predefined accounts
field 4 -&gt; *</span><span class="hljs-strong">*1000*</span><span class="hljs-strong">*: group id.
field 5 -&gt; *</span><span class="hljs-strong">*joker,,,*</span><span class="hljs-strong">*: the name of the computer
field 6 -&gt; *</span><span class="hljs-strong">*/home/joker*</span><span class="hljs-strong">*: home folder
field 7 -&gt; *</span><span class="hljs-strong">*/bin/bash*</span><span class="hljs-strong">*: shell "</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ruby"><span class="hljs-symbol">root:</span><span class="hljs-symbol">x:</span><span class="hljs-number">0</span><span class="hljs-symbol">:</span><span class="hljs-number">0</span><span class="hljs-symbol">:root</span><span class="hljs-symbol">:/root</span><span class="hljs-symbol">:/bin/bash</span>
<span class="hljs-symbol">daemon:</span><span class="hljs-symbol">x:</span><span class="hljs-number">1</span><span class="hljs-symbol">:</span><span class="hljs-number">1</span><span class="hljs-symbol">:daemon</span><span class="hljs-symbol">:/usr/sbin</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">bin:</span><span class="hljs-symbol">x:</span><span class="hljs-number">2</span><span class="hljs-symbol">:</span><span class="hljs-number">2</span><span class="hljs-symbol">:bin</span><span class="hljs-symbol">:/bin</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">sys:</span><span class="hljs-symbol">x:</span><span class="hljs-number">3</span><span class="hljs-symbol">:</span><span class="hljs-number">3</span><span class="hljs-symbol">:sys</span><span class="hljs-symbol">:/dev</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">sync:</span><span class="hljs-symbol">x:</span><span class="hljs-number">4</span><span class="hljs-symbol">:</span><span class="hljs-number">65534</span><span class="hljs-symbol">:sync</span><span class="hljs-symbol">:/bin</span><span class="hljs-symbol">:/bin/sync</span>
<span class="hljs-symbol">games:</span><span class="hljs-symbol">x:</span><span class="hljs-number">5</span><span class="hljs-symbol">:</span><span class="hljs-number">60</span><span class="hljs-symbol">:games</span><span class="hljs-symbol">:/usr/games</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">man:</span><span class="hljs-symbol">x:</span><span class="hljs-number">6</span><span class="hljs-symbol">:</span><span class="hljs-number">12</span><span class="hljs-symbol">:man</span><span class="hljs-symbol">:/var/cache/man</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">lp:</span><span class="hljs-symbol">x:</span><span class="hljs-number">7</span><span class="hljs-symbol">:</span><span class="hljs-number">7</span><span class="hljs-symbol">:lp</span><span class="hljs-symbol">:/var/spool/lpd</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">mail:</span><span class="hljs-symbol">x:</span><span class="hljs-number">8</span><span class="hljs-symbol">:</span><span class="hljs-number">8</span><span class="hljs-symbol">:mail</span><span class="hljs-symbol">:/var/mail</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">news:</span><span class="hljs-symbol">x:</span><span class="hljs-number">9</span><span class="hljs-symbol">:</span><span class="hljs-number">9</span><span class="hljs-symbol">:news</span><span class="hljs-symbol">:/var/spool/news</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">uucp:</span><span class="hljs-symbol">x:</span><span class="hljs-number">10</span><span class="hljs-symbol">:</span><span class="hljs-number">10</span><span class="hljs-symbol">:uucp</span><span class="hljs-symbol">:/var/spool/uucp</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">proxy:</span><span class="hljs-symbol">x:</span><span class="hljs-number">13</span><span class="hljs-symbol">:</span><span class="hljs-number">13</span><span class="hljs-symbol">:proxy</span><span class="hljs-symbol">:/bin</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
www-<span class="hljs-symbol">data:</span><span class="hljs-symbol">x:</span><span class="hljs-number">33</span><span class="hljs-symbol">:</span><span class="hljs-number">33</span><span class="hljs-symbol">:www-data</span><span class="hljs-symbol">:/var/www</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">backup:</span><span class="hljs-symbol">x:</span><span class="hljs-number">34</span><span class="hljs-symbol">:</span><span class="hljs-number">34</span><span class="hljs-symbol">:backup</span><span class="hljs-symbol">:/var/backups</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">list:</span><span class="hljs-symbol">x:</span><span class="hljs-number">38</span><span class="hljs-symbol">:</span><span class="hljs-number">38</span><span class="hljs-symbol">:Mailing</span> <span class="hljs-constant">List</span> <span class="hljs-constant">Manager</span><span class="hljs-symbol">:/var/list</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">irc:</span><span class="hljs-symbol">x:</span><span class="hljs-number">39</span><span class="hljs-symbol">:</span><span class="hljs-number">39</span><span class="hljs-symbol">:ircd</span><span class="hljs-symbol">:/var/run/ircd</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">gnats:</span><span class="hljs-symbol">x:</span><span class="hljs-number">41</span><span class="hljs-symbol">:</span><span class="hljs-number">41</span><span class="hljs-symbol">:Gnats</span> <span class="hljs-constant">Bug</span>-<span class="hljs-constant">Reporting</span> <span class="hljs-constant">System</span> (admin)<span class="hljs-symbol">:/var/lib/gnats</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">nobody:</span><span class="hljs-symbol">x:</span><span class="hljs-number">65534</span><span class="hljs-symbol">:</span><span class="hljs-number">65534</span><span class="hljs-symbol">:nobody</span><span class="hljs-symbol">:/nonexistent</span><span class="hljs-symbol">:/usr/sbin/nologin</span>
<span class="hljs-symbol">libuuid:</span><span class="hljs-symbol">x:</span><span class="hljs-number">100</span><span class="hljs-symbol">:</span><span class="hljs-number">101</span><span class="hljs-symbol">:</span><span class="hljs-symbol">:/var/lib/libuuid</span><span class="hljs-symbol">:</span>
<span class="hljs-symbol">syslog:</span><span class="hljs-symbol">x:</span><span class="hljs-number">101</span><span class="hljs-symbol">:</span><span class="hljs-number">104</span><span class="hljs-symbol">:</span><span class="hljs-symbol">:/home/syslog</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">messagebus:</span><span class="hljs-symbol">x:</span><span class="hljs-number">102</span><span class="hljs-symbol">:</span><span class="hljs-number">106</span><span class="hljs-symbol">:</span><span class="hljs-symbol">:/var/run/dbus</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">usbmux:</span><span class="hljs-symbol">x:</span><span class="hljs-number">103</span><span class="hljs-symbol">:</span><span class="hljs-number">46</span><span class="hljs-symbol">:usbmux</span> daemon,,,<span class="hljs-symbol">:/home/usbmux</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">dnsmasq:</span><span class="hljs-symbol">x:</span><span class="hljs-number">104</span><span class="hljs-symbol">:</span><span class="hljs-number">65534</span><span class="hljs-symbol">:dnsmasq</span>,,,<span class="hljs-symbol">:/var/lib/misc</span><span class="hljs-symbol">:/bin/false</span>
avahi-<span class="hljs-symbol">autoipd:</span><span class="hljs-symbol">x:</span><span class="hljs-number">105</span><span class="hljs-symbol">:</span><span class="hljs-number">114</span><span class="hljs-symbol">:Avahi</span> autoip daemon,,,<span class="hljs-symbol">:/var/lib/avahi-autoipd</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">kernoops:</span><span class="hljs-symbol">x:</span><span class="hljs-number">106</span><span class="hljs-symbol">:</span><span class="hljs-number">65534</span><span class="hljs-symbol">:Kernel</span> <span class="hljs-constant">Oops</span> <span class="hljs-constant">Tracking</span> <span class="hljs-constant">Daemon</span>,,,<span class="hljs-symbol">:/</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">avahi:</span><span class="hljs-symbol">x:</span><span class="hljs-number">107</span><span class="hljs-symbol">:</span><span class="hljs-number">116</span><span class="hljs-symbol">:Avahi</span> mDNS daemon,,,<span class="hljs-symbol">:/var/run/avahi-daemon</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">colord:</span><span class="hljs-symbol">x:</span><span class="hljs-number">108</span><span class="hljs-symbol">:</span><span class="hljs-number">118</span><span class="hljs-symbol">:colord</span> colour management daemon,,,<span class="hljs-symbol">:/var/lib/colord</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">hplip:</span><span class="hljs-symbol">x:</span><span class="hljs-number">109</span><span class="hljs-symbol">:</span><span class="hljs-number">7</span><span class="hljs-symbol">:HPLIP</span> system user,,,<span class="hljs-symbol">:/var/run/hplip</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">pulse:</span><span class="hljs-symbol">x:</span><span class="hljs-number">110</span><span class="hljs-symbol">:</span><span class="hljs-number">119</span><span class="hljs-symbol">:PulseAudio</span> daemon,,,<span class="hljs-symbol">:/var/run/pulse</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">mdm:</span><span class="hljs-symbol">x:</span><span class="hljs-number">111</span><span class="hljs-symbol">:</span><span class="hljs-number">121</span><span class="hljs-symbol">:MDM</span> <span class="hljs-constant">Display</span> <span class="hljs-constant">Manager</span><span class="hljs-symbol">:/var/lib/mdm</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">rtkit:</span><span class="hljs-symbol">x:</span><span class="hljs-number">112</span><span class="hljs-symbol">:</span><span class="hljs-number">123</span><span class="hljs-symbol">:RealtimeKit</span>,,,<span class="hljs-symbol">:/proc</span><span class="hljs-symbol">:/bin/false</span>
<span class="hljs-symbol">saned:</span><span class="hljs-symbol">x:</span><span class="hljs-number">113</span><span class="hljs-symbol">:</span><span class="hljs-number">124</span><span class="hljs-symbol">:</span><span class="hljs-symbol">:/home/saned</span><span class="hljs-symbol">:/bin/false</span>
speech-<span class="hljs-symbol">dispatcher:</span><span class="hljs-symbol">x:</span><span class="hljs-number">114</span><span class="hljs-symbol">:</span><span class="hljs-number">29</span><span class="hljs-symbol">:Speech</span> <span class="hljs-constant">Dispatcher</span>,,,<span class="hljs-symbol">:/var/run/speech-dispatcher</span><span class="hljs-symbol">:/bin/sh</span>
<span class="hljs-symbol">joker:</span><span class="hljs-symbol">x:</span><span class="hljs-number">1000</span><span class="hljs-symbol">:</span><span class="hljs-number">1000</span><span class="hljs-symbol">:joker</span>,,,<span class="hljs-symbol">:/home/joker</span><span class="hljs-symbol">:/bin/bash</span>


filed <span class="hljs-number">1</span> -&gt; **joker**<span class="hljs-symbol">:</span> user name
field <span class="hljs-number">2</span> -&gt; **x**<span class="hljs-symbol">:</span> password is encrypted <span class="hljs-keyword">for</span> the user
field <span class="hljs-number">3</span> -&gt; **<span class="hljs-number">1000</span>**<span class="hljs-symbol">:</span> uid (userid). from <span class="hljs-number">1</span> to <span class="hljs-number">99</span> id are reserved <span class="hljs-keyword">for</span> predefined accounts
field <span class="hljs-number">4</span> -&gt; **<span class="hljs-number">1000</span>**<span class="hljs-symbol">:</span> group id.
field <span class="hljs-number">5</span> -&gt; **joker,,,**<span class="hljs-symbol">:</span> the name of the computer
field <span class="hljs-number">6</span> -&gt; **<span class="hljs-regexp">/home/joker</span>**<span class="hljs-symbol">:</span> home folder
field <span class="hljs-number">7</span> -&gt; **<span class="hljs-regexp">/bin/bash</span>**<span class="hljs-symbol">:</span> shell </code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>cat /etc/passwd</code></td>
  <td>shows info about the accounts of the computer</td>
</tr>
<tr>
  <td><code>joker:x:1000:1000:joker,,,:/home/joker:/bin/bash</code></td>
  <td>output of the file</td>
</tr>
<tr>
  <td><code>joker</code></td>
  <td>field 1: username</td>
</tr>
<tr>
  <td><code>x</code></td>
  <td>field 2: password</td>
</tr>
<tr>
  <td><code>1000</code></td>
  <td>field 3: user id</td>
</tr>
<tr>
  <td><code>1000</code></td>
  <td>field 4: group id</td>
</tr>
<tr>
  <td><code>joker,,,</code></td>
  <td>field 5: name of the computer</td>
</tr>
<tr>
  <td><code>/home/joker</code></td>
  <td>field 6: home folder of the user</td>
</tr>
<tr>
  <td><code>/bin/bash</code></td>
  <td>field 7: shell</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/rVcwqdG7a0s?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-45-the-internal-field-separator"><strong>Shell Scripting Tutorial-45:</strong> <em>The Internal Field Separator</em></h2>

<p>Usage of IFS (internal field separator)   </p>

<p><code>set this is the forty fifth tutorial.</code> sets the positional parameter  </p>

<p>default IFS character is space. It can be changed as following: <br>
<code>IFS=:</code> so, IFS is changed to : <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. change the value of the IFS and set will be changed.</span>

<span class="hljs-comment"># usage of default IFS</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"default IFS usage:"</span>
line=<span class="hljs-string">"Shell scripting is fun."</span>
<span class="hljs-keyword">set</span> <span class="hljs-variable">$line</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$1</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$2</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$3</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$4</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"\nIFS is changed to ':' and the result is:"</span>
IFS=: <span class="hljs-comment"># IFS is changed to :</span>
<span class="hljs-keyword">set</span> <span class="hljs-variable">$line</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$1</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$2</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$3</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$4</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"\ntext is separated using column character and IFS is column:"</span>
line=<span class="hljs-string">"Shell:scripting:is:fun."</span>
<span class="hljs-keyword">set</span> <span class="hljs-variable">$line</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$1</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$2</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$3</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$4</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs oxygene"><span class="hljs-keyword">default</span> IFS usage:
Shell
scripting
<span class="hljs-keyword">is</span>
fun.

IFS <span class="hljs-keyword">is</span> changed <span class="hljs-keyword">to</span> <span class="hljs-string">':'</span> <span class="hljs-keyword">and</span> the <span class="hljs-keyword">result</span> <span class="hljs-keyword">is</span>:
Shell scripting <span class="hljs-keyword">is</span> fun.




text <span class="hljs-keyword">is</span> separated <span class="hljs-keyword">using</span> column character <span class="hljs-keyword">and</span> IFS <span class="hljs-keyword">is</span> column:
Shell
scripting
<span class="hljs-keyword">is</span>
fun.
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>IFS=:</code></td>
  <td>Internal file separator is changed</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/zro2K3hay3Y?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-46-passwd-file-revisited"><strong>Shell Scripting Tutorial-46:</strong> <em>‘passwd’ File Revisited</em></h2>

<p>Example of using passwd file, IFS, grep and set command. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. shows some information from passwd file to users.</span>
<span class="hljs-comment"># 2. IFS is used.</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter Username:\c"</span>
<span class="hljs-built_in">read</span> logname

<span class="hljs-comment"># takes the line that is associated with the username</span>
line=`grep <span class="hljs-variable">$logname</span> /etc/passwd`

IFS=: <span class="hljs-comment"># the separator is : in passwd file</span>
<span class="hljs-keyword">set</span> <span class="hljs-variable">$line</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Username:<span class="hljs-variable">$1</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"User ID: <span class="hljs-variable">$3</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Group ID: <span class="hljs-variable">$4</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Comment Field: <span class="hljs-variable">$5</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Home Folder: <span class="hljs-variable">$6</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"Default shell: <span class="hljs-variable">$7</span>"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs autohotkey"><span class="hljs-label">Enter Username:</span>joker
<span class="hljs-label">Username:</span>joker
<span class="hljs-label">User ID:</span> <span class="hljs-number">1000</span>
<span class="hljs-label">Group ID:</span> <span class="hljs-number">1000</span>
<span class="hljs-label">Comment Field:</span> joker,,,
<span class="hljs-label">Home Folder:</span> /home/joker
<span class="hljs-label">Default shell:</span> /bin/bash</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/Htv2kkKe-_g?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>



<h2 id="shell-scripting-tutorial-47-reading-from-a-file"><strong>Shell Scripting Tutorial-47:</strong> <em>Reading From a File</em></h2>

<p>First, file should load to <strong>exec</strong>, at the same time current settings should be kept. <br>
<strong>terminal</strong> variable holds the current settings and it assigns back the settings after reading operation.  </p>

<p><code>terminal='tty'</code> <br>
<code>exec &lt; $fname</code>  </p>

<p><code>while read line</code> <br>
<code>do</code> <br>
<code>echo "$line"</code> <br>
<code>done</code>  </p>

<p><code>exec &lt; $terminal</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. script shows the line numbers of the text with the text</span>

<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># create text file name text_tutorial_47</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a file name(text_tutorial_47):\c"</span>
<span class="hljs-built_in">read</span> fname

<span class="hljs-keyword">if</span> [ -z <span class="hljs-string">"<span class="hljs-variable">$name</span>"</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"exit"</span>
<span class="hljs-keyword">fi</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"\ntty contains info about terminal setting."</span>
terminal=`tty`

<span class="hljs-keyword">exec</span> &lt; <span class="hljs-variable">$fname</span>

count=<span class="hljs-number">1</span>
<span class="hljs-keyword">while</span> <span class="hljs-built_in">read</span> line
<span class="hljs-keyword">do</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-variable">$count</span>.<span class="hljs-variable">$line</span>
    count=`expr <span class="hljs-variable">$count</span> + <span class="hljs-number">1</span>`
<span class="hljs-keyword">done</span>

<span class="hljs-keyword">exec</span> &lt; <span class="hljs-variable">$terminal</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs applescript">Enter a <span class="hljs-type">file</span> <span class="hljs-property">name</span>(text_tutorial_47):text_tutorial_47
<span class="hljs-keyword">exit</span>

tty <span class="hljs-keyword">contains</span> info <span class="hljs-keyword">about</span> terminal setting.
<span class="hljs-number">1.</span>Money, <span class="hljs-keyword">get</span> away
<span class="hljs-number">2.</span>Get a good job <span class="hljs-keyword">with</span> more pay <span class="hljs-keyword">and</span> you're okay
<span class="hljs-number">3.</span>Money, <span class="hljs-keyword">it</span>'s a gas
<span class="hljs-number">4.</span>Grab <span class="hljs-keyword">that</span> cash <span class="hljs-keyword">with</span> both hands <span class="hljs-keyword">and</span> make a stash
<span class="hljs-number">5.</span>New car, caviar, four star daydream
<span class="hljs-number">6.</span>Think I'll buy <span class="hljs-keyword">me</span> a football team
<span class="hljs-number">7.</span>
<span class="hljs-number">8.</span>Money, <span class="hljs-keyword">get</span> <span class="hljs-keyword">back</span>
<span class="hljs-number">9.</span>I'm all right Jack keep your hands off <span class="hljs-keyword">of</span> <span class="hljs-keyword">my</span> stack
<span class="hljs-number">10.</span>Money, <span class="hljs-keyword">it</span>'s a hit
<span class="hljs-number">11.</span>Don't give <span class="hljs-keyword">me</span> <span class="hljs-keyword">that</span> do goody good bullshit
<span class="hljs-number">12.</span>I'm <span class="hljs-keyword">in</span> <span class="hljs-keyword">the</span> high-fidelity <span class="hljs-keyword">first</span> <span class="hljs-type">class</span> traveling <span class="hljs-keyword">set</span>
<span class="hljs-number">13.</span>And I think I need a Lear jet
<span class="hljs-number">14.</span>
<span class="hljs-number">15.</span>Money, <span class="hljs-keyword">it</span>'s a crime
<span class="hljs-number">16.</span>Share <span class="hljs-keyword">it</span> fairly <span class="hljs-keyword">but</span> don't take a slice <span class="hljs-keyword">of</span> <span class="hljs-keyword">my</span> pie
<span class="hljs-number">17.</span>Money, so they <span class="hljs-command">say</span>
<span class="hljs-number">18.</span>Is <span class="hljs-keyword">the</span> root <span class="hljs-keyword">of</span> all evil today
<span class="hljs-number">19.</span>But <span class="hljs-keyword">if</span> you ask <span class="hljs-keyword">for</span> payrise <span class="hljs-keyword">it</span>'s no surprise
<span class="hljs-number">20.</span>That they're giving none away
<span class="hljs-number">21.</span>Away, away, way
<span class="hljs-number">22.</span>Away, away, away
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>terminal='tty'</code></td>
  <td>takes the current settings of the terminal</td>
</tr>
<tr>
  <td><code>exec &lt; $fname</code></td>
  <td>loads the file content</td>
</tr>
<tr>
  <td><code>while read line</code></td>
  <td>reads the line of the exec which is $fname in this case</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/DJAgtcB9V54?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-48-sleep-while-you-are-at-work"><strong>Shell Scripting Tutorial-48:</strong> <em>Sleep While You are at Work</em></h2>

<p>Usage of <strong>sleep</strong> command. Sleep makes a time delay on the execution of shell. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. ask user to enter a sentence</span>
<span class="hljs-comment"># 2. display one word at a time and use time delay</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a sentence:\c"</span>
<span class="hljs-built_in">read</span> str
<span class="hljs-keyword">for</span> word <span class="hljs-keyword">in</span> <span class="hljs-variable">$str</span>
<span class="hljs-keyword">do</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$word</span>"</span>
    sleep <span class="hljs-number">2</span>
<span class="hljs-keyword">done</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs applescript">Enter a sentence:shell <span class="hljs-keyword">script</span> tutorial <span class="hljs-keyword">is</span> cool :)
shell
<span class="hljs-keyword">script</span>
tutorial
<span class="hljs-keyword">is</span>
cool
:)</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>sleep 5</code></td>
  <td>shell execution sleeps 5 seconds</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/jFxLzOVPTBc?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-49-count-the-number-of-words-sentences-in-a-text-file-without-using-wc"><strong>Shell Scripting Tutorial-49:</strong> <em>Count the number of words &amp; sentences in a text file without using ‘wc’</em></h2>

<p>An example is ran.  </p>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. counts line number and word number</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># create text file name text_tutorial_49 with following content</span>
<span class="hljs-comment"># Money, get away</span>
<span class="hljs-comment"># Get a good job with more pay and you're okay </span>
<span class="hljs-comment"># Money, it's a gas</span>
<span class="hljs-comment"># Grab that cash with both hands and make a stash</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter a file name(text_tutorial_49):\c"</span>
<span class="hljs-built_in">read</span> fname 

terminal=`tty`

<span class="hljs-keyword">exec</span> &lt; <span class="hljs-variable">$fname</span>

nol=<span class="hljs-number">0</span> <span class="hljs-comment"># number of lines</span>
now=<span class="hljs-number">0</span> <span class="hljs-comment"># number of words</span>

<span class="hljs-keyword">while</span> <span class="hljs-built_in">read</span> line
<span class="hljs-keyword">do</span>
    nol=`expr <span class="hljs-variable">$nol</span> + <span class="hljs-number">1</span>`
    <span class="hljs-keyword">set</span> <span class="hljs-variable">$line</span>
    now=`expr <span class="hljs-variable">$now</span> + <span class="hljs-variable">$#</span>`
    <span class="hljs-comment"># for word in $line</span>
    <span class="hljs-comment"># do </span>
    <span class="hljs-comment">#   now=`expr $now + 1`</span>
    <span class="hljs-comment"># done</span>
<span class="hljs-keyword">done</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"number of lines: <span class="hljs-variable">$nol</span>"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"number of words: <span class="hljs-variable">$now</span>"</span>

<span class="hljs-keyword">exec</span> &lt; <span class="hljs-variable">$terminal</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs livecodeserver">Enter <span class="hljs-operator">a</span> <span class="hljs-built_in">file</span> name(text_tutorial_49):text_tutorial_49
<span class="hljs-built_in">number</span> <span class="hljs-operator">of</span> <span class="hljs-keyword">lines</span>: <span class="hljs-number">3</span>
<span class="hljs-built_in">number</span> <span class="hljs-operator">of</span> <span class="hljs-keyword">words</span>: <span class="hljs-number">17</span>
</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/vliYprapjXY?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-50-fetch-redirect-man-pages-of-commands-using-for-loop"><strong>Shell Scripting Tutorial-50:</strong> <em>Fetch &amp; Redirect Man Pages of commands using ‘for loop’</em></h2>

<p><strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. use the command in the commandlist_tutorial_50</span>
<span class="hljs-comment"># 2. iterate the commands using for loop</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># create a file name commandlist_tutorial_50 with the following content:</span>
<span class="hljs-comment"># cat</span>
<span class="hljs-comment"># date</span>
<span class="hljs-comment"># cal</span>
<span class="hljs-comment"># touch</span>
<span class="hljs-comment"># run command and check the file "helpfile"</span>

<span class="hljs-keyword">for</span> cmd <span class="hljs-keyword">in</span> `cat commandlist_tutorial_50`
<span class="hljs-keyword">do</span>
    man <span class="hljs-variable">$cmd</span> &gt;&gt; helpfile
<span class="hljs-keyword">done</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs oxygene"># <span class="hljs-keyword">take</span> a look <span class="hljs-keyword">to</span> content <span class="hljs-keyword">of</span> helpfile</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>man cat &gt;&gt; helpfile</code></td>
  <td>appends output of man command to helpfile</td>
</tr>
<tr>
  <td><code>for cmd in 'cat commandlist'</code></td>
  <td>for loop iteration of a file</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/RwDiD9Y4rB0?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-51-nested-loops"><strong>Shell Scripting Tutorial-51:</strong> <em>Nested Loops</em></h2>

<p>Example for nested loop. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. display all combination of  number 1 2 3</span>

a=<span class="hljs-number">1</span>
<span class="hljs-keyword">while</span> [ <span class="hljs-variable">$a</span> -le <span class="hljs-number">3</span> ]
<span class="hljs-keyword">do</span>
    b=<span class="hljs-number">1</span>
    <span class="hljs-keyword">while</span> [ <span class="hljs-variable">$b</span> -le <span class="hljs-number">3</span> ]
    <span class="hljs-keyword">do</span>
        c=<span class="hljs-number">1</span>
        <span class="hljs-keyword">while</span> [ <span class="hljs-variable">$c</span> -le <span class="hljs-number">3</span> ]
        <span class="hljs-keyword">do</span>
            <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$a</span><span class="hljs-variable">$b</span><span class="hljs-variable">$c</span>"</span>
            c=`expr <span class="hljs-variable">$c</span> + <span class="hljs-number">1</span>`
        <span class="hljs-keyword">done</span>
        b=`expr <span class="hljs-variable">$b</span> + <span class="hljs-number">1</span>`
    <span class="hljs-keyword">done</span>
    a=`expr <span class="hljs-variable">$a</span> + <span class="hljs-number">1</span>`
<span class="hljs-keyword">done</span>
</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ">111
112
113
121
122
123
131
132
133
211
212
213
221
222
223
231
232
233
311
312
313
321
322
323
331
332
333</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/WLoLcl1pTS0?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>



<h2 id="shell-scripting-tutorial-52-the-break-statement"><strong>Shell Scripting Tutorial-52:</strong> <em>The ‘break’ Statement</em></h2>

<p>break terminates the loop. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. generate 10 number using while loop</span>

count=<span class="hljs-number">1</span>
<span class="hljs-keyword">while</span> [ <span class="hljs-variable">$count</span> -le <span class="hljs-number">10</span> ]
<span class="hljs-keyword">do</span>
    <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$count</span> <span class="hljs-operator">-eq</span> <span class="hljs-number">6</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-keyword">break</span>
    <span class="hljs-keyword">fi</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-variable">$count</span>
    count=`expr <span class="hljs-variable">$count</span> + <span class="hljs-number">1</span>`
<span class="hljs-keyword">done</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"We are out of the loop"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vhdl"><span class="hljs-number">1</span>
<span class="hljs-number">2</span>
<span class="hljs-number">3</span>
<span class="hljs-number">4</span>
<span class="hljs-number">5</span>
We are <span class="hljs-keyword">out</span> <span class="hljs-keyword">of</span> the <span class="hljs-keyword">loop</span>
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>break</code></td>
  <td>ends the loop iteration</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/60kgR8mLac8?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-53-the-continue-statement"><strong>Shell Scripting Tutorial-53:</strong> <em>The ‘continue’ Statement</em></h2>

<p>continue sends execution the beginning of the loop. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. generate 10 number using while loop</span>

count=<span class="hljs-number">0</span>
<span class="hljs-keyword">while</span> [ <span class="hljs-variable">$count</span> -le <span class="hljs-number">9</span> ]
<span class="hljs-keyword">do</span>
    count=`expr <span class="hljs-variable">$count</span> + <span class="hljs-number">1</span>`
    <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$count</span> <span class="hljs-operator">-eq</span> <span class="hljs-number">5</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-keyword">continue</span>
    <span class="hljs-keyword">fi</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-variable">$count</span>
<span class="hljs-keyword">done</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"End of the loop"</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vbnet"><span class="hljs-number">1</span>
<span class="hljs-number">2</span>
<span class="hljs-number">3</span>
<span class="hljs-number">4</span>
<span class="hljs-number">6</span>
<span class="hljs-number">7</span>
<span class="hljs-number">8</span>
<span class="hljs-number">9</span>
<span class="hljs-number">10</span>
<span class="hljs-keyword">End</span> <span class="hljs-keyword">of</span> the <span class="hljs-keyword">loop</span></code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>continue</code></td>
  <td>returns back to start of loop</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/sx4_7-amjF0?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-54-more-on-metacharacters"><strong>Shell Scripting Tutorial-54:</strong> <em>More on Metacharacters</em></h2>

<p>Running more than one command a line. <br>
<code>ls ; cal ; banner "mustafa celik"</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash
</span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># create file text_tutorial_54 with some text</span>

ls ; cal ; banner <span class="hljs-string">"mustafa celik"</span>

grep -i money text_tutorial_54 &gt; pattern &amp;&amp; <span class="hljs-built_in">echo</span> <span class="hljs-string">"Task was completed."</span>

cat pattern</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs applescript">animals              script_2_tutorial_61  video_tutorial_10.sh  video_tutorial_29.sh  video_tutorial_48.sh
commandlist_tutorial_50      script_3_tutorial_61  video_tutorial_11.sh  video_tutorial_30.sh  video_tutorial_49.sh
create_consecutive_files.sh  sports        video_tutorial_12.sh  video_tutorial_31.sh  video_tutorial_50.sh
empty_file1          test1         video_tutorial_13.sh  video_tutorial_32.sh  video_tutorial_51.sh
empty_file2          test2         video_tutorial_14.sh  video_tutorial_33.sh  video_tutorial_52.sh
empty_file3          test_file         video_tutorial_15.sh  video_tutorial_34.sh  video_tutorial_53.sh
folder1              test_file2        video_tutorial_16.sh  video_tutorial_35.sh  video_tutorial_54.sh
folder2              text_tutorial_43      video_tutorial_17.sh  video_tutorial_36.sh  video_tutorial_55.sh
folder3              text_tutorial_47      video_tutorial_18.sh  video_tutorial_37.sh  video_tutorial_56.sh
helpfile             text_tutorial_49      video_tutorial_19.sh  video_tutorial_38.sh  video_tutorial_57.sh
merged_test_files        text_tutorial_54      video_tutorial_20.sh  video_tutorial_39.sh  video_tutorial_58.sh
<span class="hljs-keyword">my</span>.joker             video_tutorial_02.sh  video_tutorial_21.sh  video_tutorial_40.sh  video_tutorial_59.sh
new              video_tutorial_03.sh  video_tutorial_22.sh  video_tutorial_41.sh  video_tutorial_60.sh
new_name             video_tutorial_04.sh  video_tutorial_23.sh  video_tutorial_42.sh  video_tutorial_61.sh
old              video_tutorial_05.sh  video_tutorial_24.sh  video_tutorial_43.sh  video_tutorial_62.sh
old_soft             video_tutorial_06.sh  video_tutorial_25.sh  video_tutorial_44.sh
players              video_tutorial_07.sh  video_tutorial_26.sh  video_tutorial_45.sh
sandbox              video_tutorial_08.sh  video_tutorial_27.sh  video_tutorial_46.sh
script_1_tutorial_61         video_tutorial_09.sh  video_tutorial_28.sh  video_tutorial_47.sh
    August <span class="hljs-number">2016</span>       
Su Mo Tu We Th Fr Sa  
    <span class="hljs-number">1</span>  <span class="hljs-number">2</span>  <span class="hljs-number">3</span>  <span class="hljs-number">4</span>  <span class="hljs-number">5</span>  <span class="hljs-number">6</span>  
 <span class="hljs-number">7</span>  <span class="hljs-number">8</span>  <span class="hljs-number">9</span> <span class="hljs-number">10</span> <span class="hljs-number">11</span> <span class="hljs-number">12</span> <span class="hljs-number">13</span>  
<span class="hljs-number">14</span> <span class="hljs-number">15</span> <span class="hljs-number">16</span> <span class="hljs-number">17</span> <span class="hljs-number">18</span> <span class="hljs-number">19</span> <span class="hljs-number">20</span>  
<span class="hljs-number">21</span> <span class="hljs-number">22</span> <span class="hljs-number">23</span> <span class="hljs-number">24</span> <span class="hljs-number">25</span> <span class="hljs-number">26</span> <span class="hljs-number">27</span>  
<span class="hljs-number">28</span> <span class="hljs-number">29</span> <span class="hljs-number">30</span> <span class="hljs-number">31</span>           


 <span class="hljs-comment">#    #  #    #   ####    #####    ##    ######    ##             ####   ######</span>
 <span class="hljs-comment">##  ##  #    #  #          #     #  #   #        #  #           #    #  #</span>
 <span class="hljs-comment"># ## #  #    #   ####      #    #    #  #####   #    #          #       #####</span>
 <span class="hljs-comment">#    #  #    #       #     #    ######  #       ######          #       #</span>
 <span class="hljs-comment">#    #  #    #  #    #     #    #    #  #       #    #          #    #  #</span>
 <span class="hljs-comment">#    #   ####    ####      #    #    #  #       #    #           ####   ######</span>

Task was completed.
Money, <span class="hljs-keyword">get</span> away
Money, <span class="hljs-keyword">it</span>'s a gas
Money, <span class="hljs-keyword">get</span> <span class="hljs-keyword">back</span>
Money, <span class="hljs-keyword">it</span>'s a hit 
Money, <span class="hljs-keyword">it</span>'s a crime 
Money, so they <span class="hljs-command">say</span> 
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>ls ; cal ; banner "hello"</code></td>
  <td>running more than one command</td>
</tr>
<tr>
  <td><code>grep -i money text_tutorial_54 &gt; pattern &amp;&amp; echo "Task was completed."</code></td>
  <td>&amp;&amp; works if first part is ok</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/moRVYU-fpXw?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-55-adding-removing-users"><strong>Shell Scripting Tutorial-55:</strong> <em>Adding &amp; Removing Users</em></h2>

<p>by using GUI user can be added and deleted.  </p>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>sudo login</code></td>
  <td>change the user</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/kmDCgGk7P7k?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-56-know-when-users-log-in-part-one"><strong>Shell Scripting Tutorial-56:</strong> <em>Know when users log in Part One</em></h2>

<p>Login example. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. checks every minute the user login or not</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter username:\c"</span>
<span class="hljs-built_in">read</span> logname

time=<span class="hljs-number">0</span>

<span class="hljs-keyword">while</span> <span class="hljs-literal">true</span>
<span class="hljs-keyword">do</span>
    who | grep <span class="hljs-string">"<span class="hljs-variable">$logname</span>"</span> &gt; /dev/null
    <span class="hljs-keyword">if</span> [ $? <span class="hljs-operator">-eq</span> <span class="hljs-number">0</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$logname</span> has logged in."</span>
        <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$time</span> <span class="hljs-operator">-ne</span> <span class="hljs-number">0</span> ]
        <span class="hljs-keyword">then</span>
            <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$logname</span> was <span class="hljs-variable">$time</span> minutes late in logging in."</span>
        <span class="hljs-keyword">fi</span>
        <span class="hljs-keyword">exit</span>
    <span class="hljs-keyword">else</span>
        time=`expr <span class="hljs-variable">$time</span> + <span class="hljs-number">1</span>`
        sleep <span class="hljs-number">60</span>
    <span class="hljs-keyword">fi</span>
<span class="hljs-keyword">done</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs oxygene">Enter username:joker
joker <span class="hljs-keyword">has</span> logged <span class="hljs-keyword">in</span>.
</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/AfsCD_2HaYo?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>



<h2 id="shell-scripting-tutorial-57-know-when-users-log-in-part-two"><strong>Shell Scripting Tutorial-57:</strong> <em>Know when users log in Part Two</em></h2>

<p>example of login. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. checks every minute the user login or not</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter username:\c"</span>
<span class="hljs-built_in">read</span> logname

grep <span class="hljs-string">"<span class="hljs-variable">$logname</span>"</span> /etc/passwd &gt; /dev/null
<span class="hljs-keyword">if</span> [ $? <span class="hljs-operator">-eq</span> <span class="hljs-number">0</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"Wait..."</span>
<span class="hljs-keyword">else</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"User not found."</span>
<span class="hljs-keyword">fi</span>  

time=<span class="hljs-number">0</span>

<span class="hljs-keyword">while</span> <span class="hljs-literal">true</span>
<span class="hljs-keyword">do</span>
    who | grep <span class="hljs-string">"<span class="hljs-variable">$logname</span>"</span> &gt; /dev/null
    <span class="hljs-keyword">if</span> [ $? <span class="hljs-operator">-eq</span> <span class="hljs-number">0</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$logname</span> has logged in."</span>
        <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$time</span> <span class="hljs-operator">-ne</span> <span class="hljs-number">0</span> ]
        <span class="hljs-keyword">then</span>
            <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$logname</span> was <span class="hljs-variable">$time</span> minutes late in logging in."</span>
        <span class="hljs-keyword">fi</span>
        <span class="hljs-keyword">exit</span>
    <span class="hljs-keyword">else</span>
        time=`expr <span class="hljs-variable">$time</span> + <span class="hljs-number">1</span>`
        sleep <span class="hljs-number">60</span>
    <span class="hljs-keyword">fi</span>
<span class="hljs-keyword">done</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vhdl">Enter username:joker
<span class="hljs-keyword">Wait</span>...
joker has logged <span class="hljs-keyword">in</span>.
</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>grep "$logname" /etc/passwd &gt; /dev/null</code></td>
  <td>checking the user exists or not</td>
</tr>
<tr>
  <td><code>if [ $? -eq 0 ]</code></td>
  <td></td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/F9aqWi0bON0?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-58-know-when-users-log-in-final-part"><strong>Shell Scripting Tutorial-58:</strong> <em>Know when users log in Final Part</em></h2>

<p>loging example is implemented. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-comment">#!/usr/bin/env bas</span>
<span class="hljs-comment"># Shell_scripting_tutorial_58:  Know when users log in Final Part</span>
<span class="hljs-comment">#</span>
<span class="hljs-comment"># 1. checks every minute the user login or not</span>

<span class="hljs-built_in">echo</span> <span class="hljs-string">"Enter username:\c"</span>
<span class="hljs-built_in">read</span> logname

grep <span class="hljs-string">"<span class="hljs-variable">$logname</span>"</span> /etc/passwd &gt; /dev/null
<span class="hljs-keyword">if</span> [ $? <span class="hljs-operator">-eq</span> <span class="hljs-number">0</span> ]
<span class="hljs-keyword">then</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"Wait..."</span>
<span class="hljs-keyword">else</span>
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"User not found."</span>
<span class="hljs-keyword">fi</span>  

time=<span class="hljs-number">0</span>

<span class="hljs-keyword">while</span> <span class="hljs-literal">true</span>
<span class="hljs-keyword">do</span>
    who | grep <span class="hljs-string">"<span class="hljs-variable">$logname</span>"</span> &gt; /dev/null
    <span class="hljs-keyword">if</span> [ $? <span class="hljs-operator">-eq</span> <span class="hljs-number">0</span> ]
    <span class="hljs-keyword">then</span>
        <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$logname</span> has logged in."</span>
        <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$time</span> <span class="hljs-operator">-ne</span> <span class="hljs-number">0</span> ]
        <span class="hljs-keyword">then</span>
            <span class="hljs-keyword">if</span> [ <span class="hljs-variable">$time</span> <span class="hljs-operator">-gt</span> <span class="hljs-number">60</span> ]
            <span class="hljs-keyword">then</span>
                min=`expr <span class="hljs-variable">$time</span> / <span class="hljs-number">60</span>`
                sec=`expr <span class="hljs-variable">$time</span> % <span class="hljs-number">60</span>`
                <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$logname</span> was <span class="hljs-variable">$min</span> minutes and <span class="hljs-variable">$sec</span> seconds late in logging in."</span>
            <span class="hljs-keyword">else</span>
                sec=<span class="hljs-variable">$time</span>
                <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$logname</span> was <span class="hljs-variable">$sec</span> seconds late in logging in."</span>
            <span class="hljs-keyword">fi</span>
        <span class="hljs-keyword">fi</span>
        <span class="hljs-keyword">exit</span>
    <span class="hljs-keyword">else</span>
        time=`expr <span class="hljs-variable">$time</span> + <span class="hljs-number">1</span>`
        sleep <span class="hljs-number">1</span>
    <span class="hljs-keyword">fi</span>
<span class="hljs-keyword">done</span></code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs vhdl">Enter username:joker
<span class="hljs-keyword">Wait</span>...
joker has logged <span class="hljs-keyword">in</span>.
</code></pre>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/v9nZWXQCFcE?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>



<h2 id="shell-scripting-tutorial-59-communicate-with-other-users-using-write"><strong>Shell Scripting Tutorial-59:</strong> <em>Communicate with other users using ‘write’</em></h2>

<p>Both users must be logged in different terminals.  </p>

<p><code>write username</code>  the writer command. <br>
<code>mesg -y</code> the receiver command.  </p>

<p><code>finger</code> shows the terminal of other users. <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># 1. checks every minute the user login or not</span>
<span class="hljs-comment"># </span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># both users must be logged in different terminal.</span>

write newuser2

<span class="hljs-comment"># on the other terminal following command shoul be ran.</span>
mesg y

<span class="hljs-comment"># shows the terminal list of users to communicate.</span>
finger</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>write username</code></td>
  <td>message command</td>
</tr>
<tr>
  <td><code>mesg -y</code></td>
  <td>receiver command to take messages</td>
</tr>
<tr>
  <td><code>finger</code></td>
  <td>terminal list for messaging</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/BSFUJVHoJ7A?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-60-create-your-own-commands-using-functions"><strong>Shell Scripting Tutorial-60:</strong> <em>Create Your Own Commands Using Functions</em></h2>

<p>following is the function usage. <br>
run the following command to initialize the function:  </p>

<p>use following command to release the function: <br>
<code>$ unset youtube</code> <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash</span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># write functions</span>
<span class="hljs-comment"># change the permissions</span>
<span class="hljs-comment"># run the script</span>
<span class="hljs-comment"># $. video_tutorial_60.sh</span>
<span class="hljs-comment"># $ youtube</span>
<span class="hljs-comment"># $ byebye</span>
<span class="hljs-comment"># use unset to delete function</span>
<span class="hljs-comment"># $ unset youtube</span>

<span class="hljs-function"><span class="hljs-title">youtube</span></span>()
{
    <span class="hljs-built_in">echo</span> <span class="hljs-string">"Good Morning."</span>
}
<span class="hljs-function"><span class="hljs-title">byebye</span></span>()
{
    cal
}</code></pre>

<table>
<thead>
<tr>
  <th>Command</th>
  <th>Description</th>
</tr>
</thead>
<tbody><tr>
  <td><code>unset youtube</code></td>
  <td>removes the function</td>
</tr>
</tbody></table>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/Ho0sf54Kbr8?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>




<h2 id="shell-scripting-tutorial-61-executing-multiple-scripts"><strong>Shell Scripting Tutorial-61:</strong> <em>Executing Multiple Scripts</em></h2>

<p>Script should run at the last line of the previous script.  <br>
<strong>Example:</strong></p>



<pre class="prettyprint"><code class=" hljs bash"><span class="hljs-shebang">#!/usr/bin/env bash </span>
<span class="hljs-comment"># run the following command before the script:</span>
<span class="hljs-comment"># prepare 3 scripts which calls another consequently.</span>

sh script_1_tutorial_61</code></pre>

<p><strong>Output:</strong></p>



<pre class="prettyprint"><code class=" hljs ruleslanguage">                                                           #
  ###<span class="hljs-array">#    </span>###<span class="hljs-array">#   </span>####<span class="hljs-array">#      </span><span class="hljs-array">#    </span>####<span class="hljs-array">#    </span>####<span class="hljs-array">#           </span>##
 <span class="hljs-array">#       </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#            </span><span class="hljs-array"># </span>#
  ###<span class="hljs-array">#   </span><span class="hljs-array">#       </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#              </span>#
      <span class="hljs-array">#  </span><span class="hljs-array">#       </span>####<span class="hljs-array">#      </span><span class="hljs-array">#    </span>####<span class="hljs-array">#      </span><span class="hljs-array">#              </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#   </span><span class="hljs-array">#      </span><span class="hljs-array">#    </span><span class="hljs-array">#          </span><span class="hljs-array">#              </span>#
  ###<span class="hljs-array">#    </span>###<span class="hljs-array">#   </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#          </span><span class="hljs-array">#            </span>#####

                                                         #####
  ###<span class="hljs-array">#    </span>###<span class="hljs-array">#   </span>####<span class="hljs-array">#      </span><span class="hljs-array">#    </span>####<span class="hljs-array">#    </span>####<span class="hljs-array">#         </span><span class="hljs-array">#     </span>#
 <span class="hljs-array">#       </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#                 </span>#
  ###<span class="hljs-array">#   </span><span class="hljs-array">#       </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#            </span>#####
      <span class="hljs-array">#  </span><span class="hljs-array">#       </span>####<span class="hljs-array">#      </span><span class="hljs-array">#    </span>####<span class="hljs-array">#      </span><span class="hljs-array">#           </span>#
 <span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#   </span><span class="hljs-array">#      </span><span class="hljs-array">#    </span><span class="hljs-array">#          </span><span class="hljs-array">#           </span>#
  ###<span class="hljs-array">#    </span>###<span class="hljs-array">#   </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#          </span><span class="hljs-array">#           </span>#######

 ####<span class="hljs-array">#                                                   </span>#####
<span class="hljs-array">#     </span><span class="hljs-array">#   </span>###<span class="hljs-array">#   </span>####<span class="hljs-array">#      </span><span class="hljs-array">#    </span>####<span class="hljs-array">#    </span>####<span class="hljs-array">#         </span><span class="hljs-array">#     </span>#
<span class="hljs-array">#        </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#                 </span>#
 ####<span class="hljs-array">#   </span><span class="hljs-array">#       </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#            </span>#####
      <span class="hljs-array">#  </span><span class="hljs-array">#       </span>####<span class="hljs-array">#      </span><span class="hljs-array">#    </span>####<span class="hljs-array">#      </span><span class="hljs-array">#                 </span>#
<span class="hljs-array">#     </span><span class="hljs-array">#  </span><span class="hljs-array">#    </span><span class="hljs-array">#  </span><span class="hljs-array">#   </span><span class="hljs-array">#      </span><span class="hljs-array">#    </span><span class="hljs-array">#          </span><span class="hljs-array">#           </span><span class="hljs-array">#     </span>#
 ####<span class="hljs-array">#    </span>###<span class="hljs-array">#   </span><span class="hljs-array">#    </span><span class="hljs-array">#     </span><span class="hljs-array">#    </span><span class="hljs-array">#          </span><span class="hljs-array">#            </span>#####

</code></pre>

<blockquote>
  <p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>

<br><iframe width="560" height="315" src="https://www.youtube.com/embed/3dqR9W7FKB4?list=PL7B7FA4E693D8E790" frameborder="0" allowfullscreen></iframe>

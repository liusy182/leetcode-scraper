<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-using-language-builtins-accepted">Approach #1 Using Language Builtins [Accepted]</a></li>
<li><a href="#approach-2-in-place-accepted">Approach #2 In-place [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-using-language-builtins-accepted">Approach #1 Using Language Builtins [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>In a situation where raw efficiency is less important than code legibility,
it is likely better to use language-idiomatic builtin functions to solve this
problem.</p>
<p><strong>Algorithm</strong></p>
<p>There are a few corner cases that you can get snagged on in this problem, at
least in Java. First, one or more leading spaces will cause <code>split</code> to deduce
an erroneous <code>""</code> token at the beginning of the string, so we use the builtin
<code>trim</code> method to remove leading and trailing spaces. Then, if the resulting
string is the empty string, then we can simply output <code>0</code>. This is necessary due
to the following behavior of the <code>split</code> method:</p>
<div class="codehilite"><pre><span></span><span class="n">String</span><span class="o">[]</span> <span class="n">tokens</span> <span class="o">=</span> <span class="s">""</span><span class="o">.</span><span class="na">split</span><span class="o">(</span><span class="s">"\\s++"</span><span class="o">);</span>
<span class="n">tokens</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="c1">// 1</span>
<span class="n">tokens</span><span class="o">[</span><span class="mi">0</span><span class="o">];</span> <span class="c1">// ""</span>
</pre></div>


<p>If we reach the final return statement, we <code>split</code> the trimmed string on
sequences of one or more whitespace characters (<code>split</code> can take a regular
expression) and return the length of the resulting array.</p>
<p>The Python solution is trivially short because Python's <code>split</code> has a lot of
default behavior that makes it perfect for this sort of problem. Notably, it
returns an empty list when <code>split</code>ting an empty string, it splits on
whitespace by default, and it implicitly <code>trim</code>s (<code>strip</code>s, in Python lingo)
the string beforehand.</p>
<iframe src="https://leetcode.com/playground/FdCZomTr/shared" frameborder="0" width="100%" height="208" name="FdCZomTr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>All builtin language functionality used here (in both the Java and Python
examples) runs in either <script type="math/tex; mode=display">O(n)</script> or <script type="math/tex; mode=display">O(1)</script> time, so the entire algorithm
runs in linear time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p><code>split</code> (in both languages) returns an array/list of <script type="math/tex; mode=display">O(n)</script> length, so
the algorithm uses linear additional space.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-in-place-accepted">Approach #2 In-place [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If we cannot afford to allocate linear additional space, a fairly simple
algorithm can deduce the number of segments in linear time and constant
space.</p>
<p><strong>Algorithm</strong></p>
<p>To count the number of segments, it is equivalent to count the number of
string indices at which a segment begins. Therefore, by formally defining the
characteristics of such an index, we can simply iterate over the string and
test each index in turn. Such a definition is as follows: a string index
begins a segment if it is preceded by whitespace (or is the first index) and
is not whitespace itself, which can be checked in constant time. Finally, we
simply return the number of indices for which the condition is satisfied.</p>
<iframe src="https://leetcode.com/playground/XX7WFxaA/shared" frameborder="0" width="100%" height="276" name="XX7WFxaA"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>
</p>
<p>We do a constant time check for each of the string's <script type="math/tex; mode=display">n</script> indices, so the
runtime is overall linear.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>
</p>
<p>There are only a few integers allocated, so the memory footprint is
constant.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/emptyset">@emptyset</a></p>
          </div>
        
      </div>
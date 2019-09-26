<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sorting-accepted">Approach #1 (Sorting) [Accepted]</a></li>
<li><a href="#approach-2-hash-table-accepted">Approach #2 (Hash Table) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sorting-accepted">Approach #1 (Sorting) [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>An anagram is produced by rearranging the letters of <script type="math/tex; mode=display">s</script> into <script type="math/tex; mode=display">t</script>. Therefore, if <script type="math/tex; mode=display">t</script> is an anagram of <script type="math/tex; mode=display">s</script>, sorting both strings will result in two identical strings. Furthermore, if <script type="math/tex; mode=display">s</script> and <script type="math/tex; mode=display">t</script> have different lengths, <script type="math/tex; mode=display">t</script> must not be an anagram of <script type="math/tex; mode=display">s</script> and we can return early.</p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">isAnagram</span><span class="o">(</span><span class="n">String</span> <span class="n">s</span><span class="o">,</span> <span class="n">String</span> <span class="n">t</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">!=</span> <span class="n">t</span><span class="o">.</span><span class="na">length</span><span class="o">())</span> <span class="o">{</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kt">char</span><span class="o">[]</span> <span class="n">str1</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="na">toCharArray</span><span class="o">();</span>
    <span class="kt">char</span><span class="o">[]</span> <span class="n">str2</span> <span class="o">=</span> <span class="n">t</span><span class="o">.</span><span class="na">toCharArray</span><span class="o">();</span>
    <span class="n">Arrays</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">str1</span><span class="o">);</span>
    <span class="n">Arrays</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">str2</span><span class="o">);</span>
    <span class="k">return</span> <span class="n">Arrays</span><span class="o">.</span><span class="na">equals</span><span class="o">(</span><span class="n">str1</span><span class="o">,</span> <span class="n">str2</span><span class="o">);</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n \log n)</script>.
Assume that <script type="math/tex; mode=display">n</script> is the length of <script type="math/tex; mode=display">s</script>, sorting costs <script type="math/tex; mode=display">O(n \log n)</script> and comparing two strings costs <script type="math/tex; mode=display">O(n)</script>. Sorting time dominates and the overall time complexity is <script type="math/tex; mode=display">O(n \log n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
Space depends on the sorting implementation which, usually, costs <script type="math/tex; mode=display">O(1)</script> auxiliary space if <code>heapsort</code> is used. Note that in Java, <code>toCharArray()</code> makes a copy of the string so it costs <script type="math/tex; mode=display">O(n)</script> extra space, but we ignore this for complexity analysis because:</p>
<ul>
<li>It is a language dependent detail.</li>
<li>It depends on how the function is designed. For example, the function parameter types can be changed to <code>char[]</code>.</li>
</ul>
</li>
</ul>
<hr>
<h4 id="approach-2-hash-table-accepted">Approach #2 (Hash Table) [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>To examine if <script type="math/tex; mode=display">t</script> is a rearrangement of <script type="math/tex; mode=display">s</script>, we can count occurrences of each letter in the two strings and compare them. Since both <script type="math/tex; mode=display">s</script> and <script type="math/tex; mode=display">t</script> contain only letters from <script type="math/tex; mode=display">a-z</script>, a simple counter table of size 26 is suffice.</p>
<p>Do we need <em>two</em> counter tables for comparison? Actually no, because we could increment the counter for each letter in <script type="math/tex; mode=display">s</script> and decrement the counter for each letter in <script type="math/tex; mode=display">t</script>, then check if the counter reaches back to zero.</p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">isAnagram</span><span class="o">(</span><span class="n">String</span> <span class="n">s</span><span class="o">,</span> <span class="n">String</span> <span class="n">t</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">!=</span> <span class="n">t</span><span class="o">.</span><span class="na">length</span><span class="o">())</span> <span class="o">{</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kt">int</span><span class="o">[]</span> <span class="n">counter</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="mi">26</span><span class="o">];</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
        <span class="n">counter</span><span class="o">[</span><span class="n">s</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">-</span> <span class="sc">'a'</span><span class="o">]++;</span>
        <span class="n">counter</span><span class="o">[</span><span class="n">t</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">-</span> <span class="sc">'a'</span><span class="o">]--;</span>
    <span class="o">}</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">count</span> <span class="o">:</span> <span class="n">counter</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">count</span> <span class="o">!=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
        <span class="o">}</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p>Or we could first increment the counter for <script type="math/tex; mode=display">s</script>, then decrement the counter for <script type="math/tex; mode=display">t</script>. If at any point the counter drops below zero, we know that <script type="math/tex; mode=display">t</script> contains an extra letter not in <script type="math/tex; mode=display">s</script> and return false immediately.</p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">isAnagram</span><span class="o">(</span><span class="n">String</span> <span class="n">s</span><span class="o">,</span> <span class="n">String</span> <span class="n">t</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">!=</span> <span class="n">t</span><span class="o">.</span><span class="na">length</span><span class="o">())</span> <span class="o">{</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kt">int</span><span class="o">[]</span> <span class="n">table</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="mi">26</span><span class="o">];</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
        <span class="n">table</span><span class="o">[</span><span class="n">s</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">-</span> <span class="sc">'a'</span><span class="o">]++;</span>
    <span class="o">}</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">t</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
        <span class="n">table</span><span class="o">[</span><span class="n">t</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">-</span> <span class="sc">'a'</span><span class="o">]--;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">table</span><span class="o">[</span><span class="n">t</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">-</span> <span class="sc">'a'</span><span class="o">]</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
        <span class="o">}</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
Time complexity is <script type="math/tex; mode=display">O(n)</script> because accessing the counter table is a constant time operation.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
Although we do use extra space, the space complexity is <script type="math/tex; mode=display">O(1)</script> because the table's size stays constant no matter how large <script type="math/tex; mode=display">n</script> is.</p>
</li>
</ul>
<p><strong>Follow up</strong></p>
<p>What if the inputs contain unicode characters? How would you adapt your solution to such case?</p>
<p><strong>Answer</strong></p>
<p>Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to <a href="https://stackoverflow.com/a/5928054/490463">more than 1 million</a>. A hash table is a more generic solution and could adapt to any range of characters.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 (Brute Force) [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-caching-memory-limit-exceeded">Approach #2 (Caching) [Memory Limit Exceeded]</a></li>
<li><a href="#approach-3-caching-rows-accepted">Approach #3 (Caching Rows) [Accepted]</a></li>
<li><a href="#approach-4-caching-smarter-accepted">Approach #4 (Caching Smarter) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 (Brute Force) [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>Each time <em>sumRegion</em> is called, we use a double for loop to sum all elements from <script type="math/tex; mode=display">(row1, col1) \rightarrow (row2, col2)</script>.</p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="kt">int</span><span class="o">[][]</span> <span class="n">data</span><span class="o">;</span>

<span class="kd">public</span> <span class="nf">NumMatrix</span><span class="o">(</span><span class="kt">int</span><span class="o">[][]</span> <span class="n">matrix</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">matrix</span><span class="o">;</span>
<span class="o">}</span>

<span class="kd">public</span> <span class="kt">int</span> <span class="nf">sumRegion</span><span class="o">(</span><span class="kt">int</span> <span class="n">row1</span><span class="o">,</span> <span class="kt">int</span> <span class="n">col1</span><span class="o">,</span> <span class="kt">int</span> <span class="n">row2</span><span class="o">,</span> <span class="kt">int</span> <span class="n">col2</span><span class="o">)</span> <span class="o">{</span>
    <span class="kt">int</span> <span class="n">sum</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">r</span> <span class="o">=</span> <span class="n">row1</span><span class="o">;</span> <span class="n">r</span> <span class="o">&lt;=</span> <span class="n">row2</span><span class="o">;</span> <span class="n">r</span><span class="o">++)</span> <span class="o">{</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">c</span> <span class="o">=</span> <span class="n">col1</span><span class="o">;</span> <span class="n">c</span> <span class="o">&lt;=</span> <span class="n">col2</span><span class="o">;</span> <span class="n">c</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">sum</span> <span class="o">+=</span> <span class="n">data</span><span class="o">[</span><span class="n">r</span><span class="o">][</span><span class="n">c</span><span class="o">];</span>
        <span class="o">}</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="n">sum</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(mn)</script> time per query.
Assume that <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> represents the number of rows and columns respectively, each <em>sumRegion</em> query can go through at most <script type="math/tex; mode=display">m \times n</script> elements.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Note that <code>data</code> is a <em>reference</em> to <code>matrix</code> and is not a copy of it.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-caching-memory-limit-exceeded">Approach #2 (Caching) [Memory Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>Since <em>sumRegion</em> could be called many times, we definitely need to do some pre-processing.</p>
<p><strong>Algorithm</strong></p>
<p>We could trade in extra space for speed by pre-calculating all possible rectangular region sum and store them in a hash table. Each <em>sumRegion</em> query now takes only constant time complexity.</p>
<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script> time per query, <script type="math/tex; mode=display">O(m^2n^2)</script> time pre-computation.
Each <em>sumRegion</em> query takes <script type="math/tex; mode=display">O(1)</script> time as the hash table lookup's time complexity is constant. The pre-computation will take <script type="math/tex; mode=display">O(m^2n^2)</script> time as there are a total of <script type="math/tex; mode=display">m^2 \times n^2</script> possibilities need to be cached.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m^2n^2)</script>.
Since there are <script type="math/tex; mode=display">mn</script> different possibilities for both top left and bottom right points of the rectangular region, the extra space required is <script type="math/tex; mode=display">O(m^2n^2)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-caching-rows-accepted">Approach #3 (Caching Rows) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Remember from the <a href="https://leetcode.com/course/chapters/leetcode-101/range-sum-query-immutable/">1D version</a> where we used a cumulative sum array? Could we apply that directly to solve this 2D version?</p>
<p><strong>Algorithm</strong></p>
<p>Try to see the 2D matrix as <script type="math/tex; mode=display">m</script> rows of 1D arrays. To find the region sum, we just accumulate the sum in the region row by row.</p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="kt">int</span><span class="o">[][]</span> <span class="n">dp</span><span class="o">;</span>

<span class="kd">public</span> <span class="nf">NumMatrix</span><span class="o">(</span><span class="kt">int</span><span class="o">[][]</span> <span class="n">matrix</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">matrix</span><span class="o">.</span><span class="na">length</span> <span class="o">==</span> <span class="mi">0</span> <span class="o">||</span> <span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span><span class="o">;</span>
    <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">matrix</span><span class="o">.</span><span class="na">length</span><span class="o">][</span><span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">r</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">r</span> <span class="o">&lt;</span> <span class="n">matrix</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">r</span><span class="o">++)</span> <span class="o">{</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">c</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">c</span> <span class="o">&lt;</span> <span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span><span class="o">;</span> <span class="n">c</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">dp</span><span class="o">[</span><span class="n">r</span><span class="o">][</span><span class="n">c</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">=</span> <span class="n">dp</span><span class="o">[</span><span class="n">r</span><span class="o">][</span><span class="n">c</span><span class="o">]</span> <span class="o">+</span> <span class="n">matrix</span><span class="o">[</span><span class="n">r</span><span class="o">][</span><span class="n">c</span><span class="o">];</span>
        <span class="o">}</span>
    <span class="o">}</span>
<span class="o">}</span>

<span class="kd">public</span> <span class="kt">int</span> <span class="nf">sumRegion</span><span class="o">(</span><span class="kt">int</span> <span class="n">row1</span><span class="o">,</span> <span class="kt">int</span> <span class="n">col1</span><span class="o">,</span> <span class="kt">int</span> <span class="n">row2</span><span class="o">,</span> <span class="kt">int</span> <span class="n">col2</span><span class="o">)</span> <span class="o">{</span>
    <span class="kt">int</span> <span class="n">sum</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">row</span> <span class="o">=</span> <span class="n">row1</span><span class="o">;</span> <span class="n">row</span> <span class="o">&lt;=</span> <span class="n">row2</span><span class="o">;</span> <span class="n">row</span><span class="o">++)</span> <span class="o">{</span>
        <span class="n">sum</span> <span class="o">+=</span> <span class="n">dp</span><span class="o">[</span><span class="n">row</span><span class="o">][</span><span class="n">col2</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">-</span> <span class="n">dp</span><span class="o">[</span><span class="n">row</span><span class="o">][</span><span class="n">col1</span><span class="o">];</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="n">sum</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m)</script> time per query, <script type="math/tex; mode=display">O(mn)</script> time pre-computation.
The pre-computation in the constructor takes <script type="math/tex; mode=display">O(mn)</script> time. The <em>sumRegion</em> query takes <script type="math/tex; mode=display">O(m)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(mn)</script>.
The algorithm uses <script type="math/tex; mode=display">O(mn)</script> space to store the cumulative sum of all rows.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-caching-smarter-accepted">Approach #4 (Caching Smarter) [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We used a cumulative sum array in the <a href="https://leetcode.com/course/chapters/leetcode-101/range-sum-query-immutable/">1D version</a>. We notice that the cumulative sum is computed with respect to the origin at index 0. Extending this analogy to the 2D case, we could pre-compute a cumulative region sum with respect to the origin at <script type="math/tex; mode=display">(0, 0)</script>.</p>
<p><img alt="Sum OD" src="https://leetcode.com/static/images/courses/sum_od.png"><br>
<small>Sum(OD) is the cumulative region sum with respect to the origin at (0, 0).</small></p>
<p>How do we derive <script type="math/tex; mode=display">Sum(ABCD)</script> using the pre-computed cumulative region sum?</p>
<p><img alt="Sum OB" src="https://leetcode.com/static/images/courses/sum_ob.png"><br>
<small>Sum(OB) is the cumulative region sum on top of the rectangle.</small></p>
<p><img alt="Sum OC" src="https://leetcode.com/static/images/courses/sum_oc.png"><br>
<small>Sum(OC) is the cumulative region sum to the left of the rectangle.</small></p>
<p><img alt="Sum OA" src="https://leetcode.com/static/images/courses/sum_oa.png"><br>
<small>Sum(OA) is the cumulative region sum to the top left corner of the rectangle.</small></p>
<p>Note that the region <script type="math/tex; mode=display">Sum(OA)</script> is covered twice by both <script type="math/tex; mode=display">Sum(OB)</script> and <script type="math/tex; mode=display">Sum(OC)</script>. We could use the principle of inclusion-exclusion to calculate <script type="math/tex; mode=display">Sum(ABCD)</script> as following:</p>
<p>
<script type="math/tex; mode=display">
Sum(ABCD) = Sum(OD) - Sum(OB) - Sum(OC) + Sum(OA)
</script>
</p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="kt">int</span><span class="o">[][]</span> <span class="n">dp</span><span class="o">;</span>

<span class="kd">public</span> <span class="nf">NumMatrix</span><span class="o">(</span><span class="kt">int</span><span class="o">[][]</span> <span class="n">matrix</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">if</span> <span class="o">(</span><span class="n">matrix</span><span class="o">.</span><span class="na">length</span> <span class="o">==</span> <span class="mi">0</span> <span class="o">||</span> <span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span><span class="o">;</span>
    <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">matrix</span><span class="o">.</span><span class="na">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">r</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">r</span> <span class="o">&lt;</span> <span class="n">matrix</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">r</span><span class="o">++)</span> <span class="o">{</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">c</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">c</span> <span class="o">&lt;</span> <span class="n">matrix</span><span class="o">[</span><span class="mi">0</span><span class="o">].</span><span class="na">length</span><span class="o">;</span> <span class="n">c</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">dp</span><span class="o">[</span><span class="n">r</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">c</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">=</span> <span class="n">dp</span><span class="o">[</span><span class="n">r</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">c</span><span class="o">]</span> <span class="o">+</span> <span class="n">dp</span><span class="o">[</span><span class="n">r</span><span class="o">][</span><span class="n">c</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">+</span> <span class="n">matrix</span><span class="o">[</span><span class="n">r</span><span class="o">][</span><span class="n">c</span><span class="o">]</span> <span class="o">-</span> <span class="n">dp</span><span class="o">[</span><span class="n">r</span><span class="o">][</span><span class="n">c</span><span class="o">];</span>
        <span class="o">}</span>
    <span class="o">}</span>
<span class="o">}</span>

<span class="kd">public</span> <span class="kt">int</span> <span class="nf">sumRegion</span><span class="o">(</span><span class="kt">int</span> <span class="n">row1</span><span class="o">,</span> <span class="kt">int</span> <span class="n">col1</span><span class="o">,</span> <span class="kt">int</span> <span class="n">row2</span><span class="o">,</span> <span class="kt">int</span> <span class="n">col2</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">dp</span><span class="o">[</span><span class="n">row2</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">col2</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">-</span> <span class="n">dp</span><span class="o">[</span><span class="n">row1</span><span class="o">][</span><span class="n">col2</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">-</span> <span class="n">dp</span><span class="o">[</span><span class="n">row2</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">col1</span><span class="o">]</span> <span class="o">+</span> <span class="n">dp</span><span class="o">[</span><span class="n">row1</span><span class="o">][</span><span class="n">col1</span><span class="o">];</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script> time per query, <script type="math/tex; mode=display">O(mn)</script> time pre-computation.
The pre-computation in the constructor takes <script type="math/tex; mode=display">O(mn)</script> time. Each <em>sumRegion</em> query takes <script type="math/tex; mode=display">O(1)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(mn)</script>.
The algorithm uses <script type="math/tex; mode=display">O(mn)</script> space to store the cumulative region sum.</p>
</li>
</ul>
          </div>
        
      </div>
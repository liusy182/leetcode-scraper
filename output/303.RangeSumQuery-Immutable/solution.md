<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 (Brute Force) [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-caching-accepted">Approach #2 (Caching) [Accepted]</a></li>
<li><a href="#approach-3-caching-accepted">Approach #3 (Caching) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 (Brute Force) [Time Limit Exceeded]</h4>
<p>Each time <em>sumRange</em> is called, we use a for loop to sum each individual element from index <script type="math/tex; mode=display">i</script> to <script type="math/tex; mode=display">j</script>.</p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">data</span><span class="o">;</span>

<span class="kd">public</span> <span class="nf">NumArray</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">nums</span><span class="o">;</span>
<span class="o">}</span>

<span class="kd">public</span> <span class="kt">int</span> <span class="nf">sumRange</span><span class="o">(</span><span class="kt">int</span> <span class="n">i</span><span class="o">,</span> <span class="kt">int</span> <span class="n">j</span><span class="o">)</span> <span class="o">{</span>
    <span class="kt">int</span> <span class="n">sum</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">k</span> <span class="o">=</span> <span class="n">i</span><span class="o">;</span> <span class="n">k</span> <span class="o">&lt;=</span> <span class="n">j</span><span class="o">;</span> <span class="n">k</span><span class="o">++)</span> <span class="o">{</span>
        <span class="n">sum</span> <span class="o">+=</span> <span class="n">data</span><span class="o">[</span><span class="n">k</span><span class="o">];</span>
    <span class="o">}</span>
    <span class="k">return</span> <span class="n">sum</span><span class="o">;</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis:</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script> time per query.
Each <em>sumRange</em> query takes <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Note that <code>data</code> is a <em>reference</em> to <code>nums</code> and is not a copy of it.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-caching-accepted">Approach #2 (Caching) [Accepted]</h4>
<p>Imagine that <em>sumRange</em> is called one thousand times with the exact same arguments. How could we speed that up?</p>
<p>We could trade in extra space for speed. By pre-computing all range sum possibilities and store its results in a hash table, we can speed up the query to constant time.</p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="n">Map</span><span class="o">&lt;</span><span class="n">Pair</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">map</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">&lt;&gt;();</span>

<span class="kd">public</span> <span class="nf">NumArray</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">sum</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="n">i</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">j</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">sum</span> <span class="o">+=</span> <span class="n">nums</span><span class="o">[</span><span class="n">j</span><span class="o">];</span>
            <span class="n">map</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">Pair</span><span class="o">.</span><span class="na">create</span><span class="o">(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">),</span> <span class="n">sum</span><span class="o">);</span>
        <span class="o">}</span>
    <span class="o">}</span>
<span class="o">}</span>

<span class="kd">public</span> <span class="kt">int</span> <span class="nf">sumRange</span><span class="o">(</span><span class="kt">int</span> <span class="n">i</span><span class="o">,</span> <span class="kt">int</span> <span class="n">j</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">map</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">Pair</span><span class="o">.</span><span class="na">create</span><span class="o">(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">));</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script> time per query, <script type="math/tex; mode=display">O(n^2)</script> time pre-computation.
The pre-computation done in the constructor takes <script type="math/tex; mode=display">O(n^2)</script> time. Each <em>sumRange</em> query's time complexity is <script type="math/tex; mode=display">O(1)</script> as the hash table's look up operation is constant time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^2)</script>.
The extra space required is <script type="math/tex; mode=display">O(n^2)</script> as there are <script type="math/tex; mode=display">n</script> candidates for both <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-caching-accepted">Approach #3 (Caching) [Accepted]</h4>
<p>The above approach takes a lot of space, could we optimize it?</p>
<p>Imagine that we pre-compute the cummulative sum from index <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">k</script>. Could we use this information to derive <script type="math/tex; mode=display">Sum(i, j)</script>?</p>
<p>Let us define <script type="math/tex; mode=display">sum[k]</script> as the cumulative sum for <script type="math/tex; mode=display">nums[0 \cdots k-1]</script> (inclusive):</p>
<p>
<script type="math/tex; mode=display">
sum[k] = \left\{ \begin{array}{rl} \sum_{i=0}^{k-1}nums[i] & , k > 0 \\ 0 &, k = 0 \end{array} \right.
</script>
</p>
<p>Now, we can calculate <em>sumRange</em> as following:</p>
<p>
<script type="math/tex; mode=display">
sumRange(i, j) = sum[j + 1] - sum[i]
</script>
</p>
<div class="codehilite"><pre><span></span><span class="kd">private</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">sum</span><span class="o">;</span>

<span class="kd">public</span> <span class="nf">NumArray</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">sum</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">nums</span><span class="o">.</span><span class="na">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
    <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
        <span class="n">sum</span><span class="o">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">=</span> <span class="n">sum</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">+</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">];</span>
    <span class="o">}</span>
<span class="o">}</span>

<span class="kd">public</span> <span class="kt">int</span> <span class="nf">sumRange</span><span class="o">(</span><span class="kt">int</span> <span class="n">i</span><span class="o">,</span> <span class="kt">int</span> <span class="n">j</span><span class="o">)</span> <span class="o">{</span>
    <span class="k">return</span> <span class="n">sum</span><span class="o">[</span><span class="n">j</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">-</span> <span class="n">sum</span><span class="o">[</span><span class="n">i</span><span class="o">];</span>
<span class="o">}</span>
</pre></div>


<p>Notice in the code above we inserted a dummy 0 as the first element in the <em>sum</em> array. This trick saves us from an extra conditional check in <em>sumRange</em> function.</p>
<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script> time per query, <script type="math/tex; mode=display">O(n)</script> time pre-computation.
Since the cumulative sum is cached, each <em>sumRange</em> query can be calculated in <script type="math/tex; mode=display">O(1)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
</ul>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-binary-search-on-logarithms-accepted">Approach #1: Binary Search on Logarithms [Accepted]</a></li>
<li><a href="#approach-2-sliding-window-accepted">Approach #2: Sliding Window [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-binary-search-on-logarithms-accepted">Approach #1: Binary Search on Logarithms [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Because <script type="math/tex; mode=display">\log(\prod_i x_i) = \sum_i \log x_i</script>, we can reduce the problem to subarray <em>sums</em> instead of subarray products.  The motivation for this is that the product of some arbitrary subarray may be way too large (potentially <code>1000^50000</code>), and also dealing with sums gives us some more familiarity as it becomes similar to other problems we may have solved before.</p>
<p><strong>Algorithm</strong></p>
<p>After this transformation where every value <code>x</code> becomes <code>log(x)</code>, let us take prefix sums <code>prefix[i+1] = nums[0] + nums[1] + ... + nums[i]</code>.  Now we are left with the problem of finding, for each <code>i</code>, the largest <code>j</code> so that <code>nums[i] + ... + nums[j] = prefix[j] - prefix[i] &lt; k</code>.</p>
<p>Because <code>prefix</code> is a monotone increasing array, this can be solved with binary search.  We add the width of the interval <code>[i, j]</code> to our answer, which counts all subarrays <code>[i, k]</code> with <code>k &lt;= j</code>.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">numSubarrayProductLessThanK</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nums</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">k</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="mi">0</span>
        <span class="n">k</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>

        <span class="n">prefix</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">nums</span><span class="p">:</span>
            <span class="n">prefix</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">prefix</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="n">math</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>

        <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">prefix</span><span class="p">):</span>
            <span class="n">j</span> <span class="o">=</span> <span class="n">bisect</span><span class="o">.</span><span class="n">bisect</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">x</span> <span class="o">+</span> <span class="n">k</span> <span class="o">-</span> <span class="mf">1e-9</span><span class="p">,</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span>
            <span class="n">ans</span> <span class="o">+=</span> <span class="n">j</span> <span class="o">-</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">numSubarrayProductLessThanK</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">k</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="mi">0</span><span class="o">;</span>
        <span class="kt">double</span> <span class="n">logk</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">log</span><span class="o">(</span><span class="n">k</span><span class="o">);</span>
        <span class="kt">double</span><span class="o">[]</span> <span class="n">prefix</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">double</span><span class="o">[</span><span class="n">nums</span><span class="o">.</span><span class="na">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">prefix</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">]</span> <span class="o">=</span> <span class="n">prefix</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">+</span> <span class="n">Math</span><span class="o">.</span><span class="na">log</span><span class="o">(</span><span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">]);</span>
        <span class="o">}</span>

        <span class="kt">int</span> <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">prefix</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">lo</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="o">,</span> <span class="n">hi</span> <span class="o">=</span> <span class="n">prefix</span><span class="o">.</span><span class="na">length</span><span class="o">;</span>
            <span class="k">while</span> <span class="o">(</span><span class="n">lo</span> <span class="o">&lt;</span> <span class="n">hi</span><span class="o">)</span> <span class="o">{</span>
                <span class="kt">int</span> <span class="n">mi</span> <span class="o">=</span> <span class="n">lo</span> <span class="o">+</span> <span class="o">(</span><span class="n">hi</span> <span class="o">-</span> <span class="n">lo</span><span class="o">)</span> <span class="o">/</span> <span class="mi">2</span><span class="o">;</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">prefix</span><span class="o">[</span><span class="n">mi</span><span class="o">]</span> <span class="o">&lt;</span> <span class="n">prefix</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">+</span> <span class="n">logk</span> <span class="o">-</span> <span class="mf">1e-9</span><span class="o">)</span> <span class="n">lo</span> <span class="o">=</span> <span class="n">mi</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
                <span class="k">else</span> <span class="n">hi</span> <span class="o">=</span> <span class="n">mi</span><span class="o">;</span>
            <span class="o">}</span>
            <span class="n">ans</span> <span class="o">+=</span> <span class="n">lo</span> <span class="o">-</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N\log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  Inside our for loop, each binary search operation takes <script type="math/tex; mode=display">O(\log N)</script> time.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>prefix</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-sliding-window-accepted">Approach #2: Sliding Window [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>For each <code>right</code>, call <code>opt(right)</code> the smallest <code>left</code> so that the product of the subarray <code>nums[left] * nums[left + 1] * ... * nums[right]</code> is less than <code>k</code>.  <code>opt</code> is a monotone increasing function, so we can use a sliding window.</p>
<p><strong>Algorithm</strong></p>
<p>Our loop invariant is that <code>left</code> is the smallest value so that the product in the window <code>prod = nums[left] * nums[left + 1] * ... * nums[right]</code> is less than <code>k</code>.</p>
<p>For every right, we update <code>left</code> and <code>prod</code> to maintain this invariant.  Then, the number of intervals with subarray product less than <code>k</code> and with right-most coordinate <code>right</code>, is <code>right - left + 1</code>.  We'll count all of these for each value of <code>right</code>.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">numSubarrayProductLessThanK</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nums</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">k</span> <span class="o">&lt;=</span> <span class="mi">1</span><span class="p">:</span> <span class="k">return</span> <span class="mi">0</span>
        <span class="n">prod</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="n">ans</span> <span class="o">=</span> <span class="n">left</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">right</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nums</span><span class="p">):</span>
            <span class="n">prod</span> <span class="o">*=</span> <span class="n">val</span>
            <span class="k">while</span> <span class="n">prod</span> <span class="o">&gt;=</span> <span class="n">k</span><span class="p">:</span>
                <span class="n">prod</span> <span class="o">/=</span> <span class="n">nums</span><span class="p">[</span><span class="n">left</span><span class="p">]</span>
                <span class="n">left</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">ans</span> <span class="o">+=</span> <span class="n">right</span> <span class="o">-</span> <span class="n">left</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">numSubarrayProductLessThanK</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">k</span> <span class="o">&lt;=</span> <span class="mi">1</span><span class="o">)</span> <span class="k">return</span> <span class="mi">0</span><span class="o">;</span>
        <span class="kt">int</span> <span class="n">prod</span> <span class="o">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">left</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">right</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">right</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">right</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">prod</span> <span class="o">*=</span> <span class="n">nums</span><span class="o">[</span><span class="n">right</span><span class="o">];</span>
            <span class="k">while</span> <span class="o">(</span><span class="n">prod</span> <span class="o">&gt;=</span> <span class="n">k</span><span class="o">)</span> <span class="n">prod</span> <span class="o">/=</span> <span class="n">nums</span><span class="o">[</span><span class="n">left</span><span class="o">++];</span>
            <span class="n">ans</span> <span class="o">+=</span> <span class="n">right</span> <span class="o">-</span> <span class="n">left</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  <code>left</code> can only be incremented at most <code>N</code> times.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>prod</code>, <code>left</code>, and <code>ans</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
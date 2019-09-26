<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The largest value <code>v</code> used must be the root node in the tree.  Say <code>dp(v)</code> is the number of ways to make a tree with root node <code>v</code>.</p>
<p>If the root node of the tree (with value <code>v</code>) has children with values <code>x</code> and <code>y</code> (and <code>x * y == v</code>), then there are <code>dp(x) * dp(y)</code> ways to make this tree.</p>
<p>In total, there are <script type="math/tex; mode=display">\sum_{\substack{x * y = v}} \text{dp}(x) * \text{dp}(y)</script> ways to make a tree with root node <code>v</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Actually, let <code>dp[i]</code> be the number of ways to have a root node with value <code>A[i]</code>.</p>
<p>Since in the above example we always have <code>x &lt; v</code> and <code>y &lt; v</code>, we can calculate the values of <code>dp[i]</code> in increasing order using dynamic programming.</p>
<p>For some root value <code>A[i]</code>, let's try to find candidates for the children with values <code>A[j]</code> and <code>A[i] / A[j]</code> (so that evidently <code>A[j] * (A[i] / A[j]) = A[i]</code>).  To do this quickly, we will need <code>index</code> which looks up this value: if <code>A[k] = A[i] / A[j]</code>, then index[A[i] / A[j]] = k`.</p>
<p>After, we'll add all possible <code>dp[j] * dp[k]</code> (with <code>j &lt; i, k &lt; i</code>) to our answer <code>dp[i]</code>.  In our Java implementation, we carefully used <code>long</code> so avoid overflow issues.</p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">numFactoredBinaryTrees</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">A</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">MOD</span> <span class="o">=</span> <span class="mi">1_000_000_007</span><span class="o">;</span>
        <span class="kt">int</span> <span class="n">N</span> <span class="o">=</span> <span class="n">A</span><span class="o">.</span><span class="na">length</span><span class="o">;</span>
        <span class="n">Arrays</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">A</span><span class="o">);</span>
        <span class="kt">long</span><span class="o">[]</span> <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">long</span><span class="o">[</span><span class="n">N</span><span class="o">];</span>
        <span class="n">Arrays</span><span class="o">.</span><span class="na">fill</span><span class="o">(</span><span class="n">dp</span><span class="o">,</span> <span class="mi">1</span><span class="o">);</span>

        <span class="n">Map</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">index</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">N</span><span class="o">;</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span>
            <span class="n">index</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">A</span><span class="o">[</span><span class="n">i</span><span class="o">],</span> <span class="n">i</span><span class="o">);</span>

        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">N</span><span class="o">;</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">i</span><span class="o">;</span> <span class="o">++</span><span class="n">j</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">A</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">%</span> <span class="n">A</span><span class="o">[</span><span class="n">j</span><span class="o">]</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span> <span class="c1">// A[j] is left child</span>
                    <span class="kt">int</span> <span class="n">right</span> <span class="o">=</span> <span class="n">A</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">/</span> <span class="n">A</span><span class="o">[</span><span class="n">j</span><span class="o">];</span>
                    <span class="k">if</span> <span class="o">(</span><span class="n">index</span><span class="o">.</span><span class="na">containsKey</span><span class="o">(</span><span class="n">right</span><span class="o">))</span> <span class="o">{</span>
                        <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">=</span> <span class="o">(</span><span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">+</span> <span class="n">dp</span><span class="o">[</span><span class="n">j</span><span class="o">]</span> <span class="o">*</span> <span class="n">dp</span><span class="o">[</span><span class="n">index</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">right</span><span class="o">)])</span> <span class="o">%</span> <span class="n">MOD</span><span class="o">;</span>
                    <span class="o">}</span>
                <span class="o">}</span>
            <span class="o">}</span>

        <span class="kt">long</span> <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">long</span> <span class="n">x</span><span class="o">:</span> <span class="n">dp</span><span class="o">)</span> <span class="n">ans</span> <span class="o">+=</span> <span class="n">x</span><span class="o">;</span>
        <span class="k">return</span> <span class="o">(</span><span class="kt">int</span><span class="o">)</span> <span class="o">(</span><span class="n">ans</span> <span class="o">%</span> <span class="n">MOD</span><span class="o">);</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">numFactoredBinaryTrees</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">A</span><span class="p">):</span>
        <span class="n">MOD</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">**</span> <span class="mi">9</span> <span class="o">+</span> <span class="mi">7</span>
        <span class="n">N</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">)</span>
        <span class="n">A</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
        <span class="n">dp</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">*</span> <span class="n">N</span>
        <span class="n">index</span> <span class="o">=</span> <span class="p">{</span><span class="n">x</span><span class="p">:</span> <span class="n">i</span> <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">A</span><span class="p">)}</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">A</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="n">i</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">x</span> <span class="o">%</span> <span class="n">A</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c1">#A[j] will be left child</span>
                    <span class="n">right</span> <span class="o">=</span> <span class="n">x</span> <span class="o">/</span> <span class="n">A</span><span class="p">[</span><span class="n">j</span><span class="p">]</span>
                    <span class="k">if</span> <span class="n">right</span> <span class="ow">in</span> <span class="n">index</span><span class="p">:</span>
                        <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+=</span> <span class="n">dp</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">*</span> <span class="n">dp</span><span class="p">[</span><span class="n">index</span><span class="p">[</span><span class="n">right</span><span class="p">]]</span>
                        <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">%=</span> <span class="n">MOD</span>

        <span class="k">return</span> <span class="nb">sum</span><span class="p">(</span><span class="n">dp</span><span class="p">)</span> <span class="o">%</span> <span class="n">MOD</span>
</pre></div>


<p></p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.  This comes from the two for-loops iterating <code>i</code> and <code>j</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>dp</code> and <code>index</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
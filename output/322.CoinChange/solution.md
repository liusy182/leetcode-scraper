<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 (Brute force) [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-dynamic-programming-top-down-accepted">Approach #2 (Dynamic programming - Top down) [Accepted]</a></li>
<li><a href="#approach-3-dynamic-programming-bottom-up-accepted">Approach #3 (Dynamic programming - Bottom up) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for intermediate users. It introduces the following ideas:
Backtracking, Dynamic programming.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 (Brute force) [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>The problem could be modeled as the following optimization problem :
<script type="math/tex; mode=display">
\min_{x} \sum_{i=0}^{n - 1} x_i \\
\text{subject to} \sum_{i=0}^{n - 1} x_i*c_i = S
</script>
</p>
<p>, where <script type="math/tex; mode=display">S</script> is the amount,    <script type="math/tex; mode=display">c_i</script> is the coin denominations, <script type="math/tex; mode=display">x_i</script>  is the number of coins with denominations <script type="math/tex; mode=display">c_i</script> used in change of amount <script type="math/tex; mode=display">S</script>. We could easily see that <script type="math/tex; mode=display">x_i = [{0, \frac{S}{c_i}}]</script>.</p>
<p>A trivial solution is to enumerate all subsets of coin frequencies <script type="math/tex; mode=display">[x_0\dots\ x_{n - 1}]</script>  that satisfy the constraints above, compute their sums and return the minimum among them.</p>
<p><strong>Algorithm</strong></p>
<p>To apply this idea, the algorithm uses backtracking technique to generate all combinations of coin frequencies <script type="math/tex; mode=display">[x_0\dots\ x_{n-1}]</script> in the range <script type="math/tex">[{0, \frac{S}{c_i}}]</script> which satisfy the constraints above. It makes a sum of the combinations and returns their minimum or <script type="math/tex; mode=display">-1</script> in case there is no acceptable combination.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>    

    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">coinChange</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">coins</span><span class="o">,</span> <span class="kt">int</span> <span class="n">amount</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">return</span> <span class="n">coinChange</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">coins</span><span class="o">,</span> <span class="n">amount</span><span class="o">);</span>
    <span class="o">}</span>

    <span class="kd">private</span> <span class="kt">int</span> <span class="nf">coinChange</span><span class="o">(</span><span class="kt">int</span> <span class="n">idxCoin</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">coins</span><span class="o">,</span> <span class="kt">int</span> <span class="n">amount</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">amount</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span>
            <span class="k">return</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">idxCoin</span> <span class="o">&lt;</span> <span class="n">coins</span><span class="o">.</span><span class="na">length</span> <span class="o">&amp;&amp;</span> <span class="n">amount</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">maxVal</span> <span class="o">=</span> <span class="n">amount</span><span class="o">/</span><span class="n">coins</span><span class="o">[</span><span class="n">idxCoin</span><span class="o">];</span>
            <span class="kt">int</span> <span class="n">minCost</span> <span class="o">=</span> <span class="n">Integer</span><span class="o">.</span><span class="na">MAX_VALUE</span><span class="o">;</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">x</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">x</span> <span class="o">&lt;=</span> <span class="n">maxVal</span><span class="o">;</span> <span class="n">x</span><span class="o">++)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">amount</span> <span class="o">&gt;=</span> <span class="n">x</span> <span class="o">*</span> <span class="n">coins</span><span class="o">[</span><span class="n">idxCoin</span><span class="o">])</span> <span class="o">{</span>
                    <span class="kt">int</span> <span class="n">res</span> <span class="o">=</span> <span class="n">coinChange</span><span class="o">(</span><span class="n">idxCoin</span> <span class="o">+</span> <span class="mi">1</span><span class="o">,</span> <span class="n">coins</span><span class="o">,</span> <span class="n">amount</span> <span class="o">-</span> <span class="n">x</span> <span class="o">*</span> <span class="n">coins</span><span class="o">[</span><span class="n">idxCoin</span><span class="o">]);</span>
                    <span class="k">if</span> <span class="o">(</span><span class="n">res</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="o">)</span>
                        <span class="n">minCost</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">minCost</span><span class="o">,</span> <span class="n">res</span> <span class="o">+</span> <span class="n">x</span><span class="o">);</span>
                <span class="o">}</span>                    
            <span class="o">}</span>           
            <span class="k">return</span> <span class="o">(</span><span class="n">minCost</span> <span class="o">==</span> <span class="n">Integer</span><span class="o">.</span><span class="na">MAX_VALUE</span><span class="o">)?</span> <span class="o">-</span><span class="mi">1</span><span class="o">:</span> <span class="n">minCost</span><span class="o">;</span>
        <span class="o">}</span>        
        <span class="k">return</span> <span class="o">-</span><span class="mi">1</span><span class="o">;</span>
    <span class="o">}</span>  
<span class="o">}</span>

<span class="c1">// Time Limit Exceeded</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(S^n)</script>. In the worst case, complexity is exponential in the number of the coins <script type="math/tex; mode=display">n</script>. The reason is that every coin denomination <script type="math/tex; mode=display">c_i</script> could have at most <script type="math/tex; mode=display">\frac{S}{c_i}</script> values. Therefore the number of possible combinations is :</li>
</ul>
<p>
<script type="math/tex; mode=display">
\frac{S}{c_1}*\frac{S}{c_2}*\frac{S}{c_3}\ldots\frac{S}{c_n} = \frac{S^{n}}{{c_1}*{c_2}*{c_3}\ldots{c_n}}
</script>
</p>
<ul>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
In the worst case the maximum depth of recursion is <script type="math/tex; mode=display">n</script>. Therefore we need <script type="math/tex; mode=display">O( n)</script> space used by the system recursive stack.</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-top-down-accepted">Approach #2 (Dynamic programming - Top down) [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Could we improve the exponential solution above? Definitely! The problem could be solved with polynomial time using Dynamic programming technique. First, let's define:</p>
<blockquote>
<p>
<script type="math/tex; mode=display">F(S)</script> - minimum number of coins needed to make change for amount <script type="math/tex; mode=display">S</script> using coin denominations <script type="math/tex; mode=display">[{c_0\ldots c_{n-1}}]</script>
</p>
</blockquote>
<p>We note that this problem has an optimal substructure property, which is the key piece in solving any Dynamic Programming problems. In other words, the optimal solution can be constructed from optimal solutions of its subproblems.
How to split the problem into subproblems? Let's assume that we know <script type="math/tex; mode=display">F(S)</script> where some change <script type="math/tex; mode=display">val_1, val_2, \ldots</script> for <script type="math/tex; mode=display">S</script> which is optimal and the last coin's denomination is <script type="math/tex; mode=display">C</script>.
Then the following equation should be true because of optimal substructure of the problem:</p>
<p>
<script type="math/tex; mode=display">
F(S) = F(S - C) + 1
</script>
</p>
<p>But we don't know which is the denomination of the last coin <script type="math/tex; mode=display">C</script>. We compute  <script type="math/tex; mode=display">F(S - c_i)</script> for each possible denomination <script type="math/tex; mode=display">c_0, c_1, c_2 \ldots c_{n -1}</script> and choose the minimum among them. The following recurrence relation holds:</p>
<p>
<script type="math/tex; mode=display">
F(S) = \min_{i=0 ... n-1} { F(S - c_i) } + 1 \\
\text{subject to} \ \  S-c_i \geq 0 \\
</script>
</p>
<p>
<script type="math/tex; mode=display">
F(S) = 0 \ , \text{when} \ S = 0 \\
F(S) = -1 \ , \text{when} \ n = 0
</script>
</p>
<p align="center"><img alt="Recursion tree for finding coin change of amount 6 with coin denominations {1,2,3}." src="https://leetcode.com/media/original_images/322_coin_change_tree.png" width="100%"></p>
<p>In the recursion tree above, we could see that a lot of subproblems were calculated multiple times.  For example the problem <script type="math/tex; mode=display">F(1)</script> was calculated <script type="math/tex; mode=display">13</script> times. Therefore we should cache the solutions to the subproblems in a table and access them in constant time when necessary</p>
<p><strong>Algorithm</strong></p>
<p>The idea of the algorithm is to build the solution of the problem from top to bottom. It applies the idea described above. It use backtracking and cut the partial solutions in the recursive tree, which doesn't lead to a viable solution. Тhis happens when we try to make a change of a coin with a value greater than the amount <em><script type="math/tex; mode=display">S</script></em>. To improve  time complexity we should store the solutions of the already calculated subproblems in a table.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>

    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">coinChange</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">coins</span><span class="o">,</span> <span class="kt">int</span> <span class="n">amount</span><span class="o">)</span> <span class="o">{</span>        
        <span class="k">if</span> <span class="o">(</span><span class="n">amount</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="o">)</span> <span class="k">return</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">return</span> <span class="n">coinChange</span><span class="o">(</span><span class="n">coins</span><span class="o">,</span> <span class="n">amount</span><span class="o">,</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">amount</span><span class="o">]);</span>
    <span class="o">}</span>

    <span class="kd">private</span> <span class="kt">int</span> <span class="nf">coinChange</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">coins</span><span class="o">,</span> <span class="kt">int</span> <span class="n">rem</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">count</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">rem</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="o">-</span><span class="mi">1</span><span class="o">;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">rem</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">count</span><span class="o">[</span><span class="n">rem</span> <span class="o">-</span> <span class="mi">1</span><span class="o">]</span> <span class="o">!=</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="n">count</span><span class="o">[</span><span class="n">rem</span> <span class="o">-</span> <span class="mi">1</span><span class="o">];</span>
        <span class="kt">int</span> <span class="n">min</span> <span class="o">=</span> <span class="n">Integer</span><span class="o">.</span><span class="na">MAX_VALUE</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">coin</span> <span class="o">:</span> <span class="n">coins</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">res</span> <span class="o">=</span> <span class="n">coinChange</span><span class="o">(</span><span class="n">coins</span><span class="o">,</span> <span class="n">rem</span> <span class="o">-</span> <span class="n">coin</span><span class="o">,</span> <span class="n">count</span><span class="o">);</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">res</span> <span class="o">&gt;=</span> <span class="mi">0</span> <span class="o">&amp;&amp;</span> <span class="n">res</span> <span class="o">&lt;</span> <span class="n">min</span><span class="o">)</span>
                <span class="n">min</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">+</span> <span class="n">res</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="n">count</span><span class="o">[</span><span class="n">rem</span> <span class="o">-</span> <span class="mi">1</span><span class="o">]</span> <span class="o">=</span> <span class="o">(</span><span class="n">min</span> <span class="o">==</span> <span class="n">Integer</span><span class="o">.</span><span class="na">MAX_VALUE</span><span class="o">)</span> <span class="o">?</span> <span class="o">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">min</span><span class="o">;</span>
        <span class="k">return</span> <span class="n">count</span><span class="o">[</span><span class="n">rem</span> <span class="o">-</span> <span class="mi">1</span><span class="o">];</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(S*n)</script>. where S is the amount, n is denomination count.
In the worst case the recursive tree of the algorithm has height of <script type="math/tex; mode=display">S</script> and the algorithm  solves only <script type="math/tex; mode=display">S</script> subproblems because it caches precalculated solutions in a table. Each subproblem is computed with  <script type="math/tex; mode=display">n</script> iterations, one by coin denomination. Therefore there is <script type="math/tex; mode=display">O(S*n)</script> time complexity.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(S)</script>, where <script type="math/tex; mode=display">S</script> is the amount to change
We use extra space for the memoization table.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming-bottom-up-accepted">Approach #3 (Dynamic programming - Bottom up) [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>For the iterative solution, we think in bottom-up manner. Before calculating <em><script type="math/tex; mode=display">F(i)</script></em>, we have to compute all minimum counts for amounts up to <script type="math/tex; mode=display">i</script>. On each iteration <script type="math/tex; mode=display">i</script> of the algorithm <em><script type="math/tex; mode=display">F(i)</script></em> is computed as <script type="math/tex; mode=display">\min_{j=0 \ldots n-1}{F(i -c_j)} + 1</script>
</p>
<p align="center"><img alt="Bottom-up approach using a table to build up the solution to F6." src="https://leetcode.com/media/original_images/322_coin_change_table.png" width="539px"></p>
<p>In the example above you can see that:</p>
<p>
<script type="math/tex; mode=display">
\begin{align}
F(3) &= \min\{{F(3- c_1), F(3-c_2), F(3-c_3)}\} + 1 \\
&= \min\{{F(3- 1), F(3-2), F(3-3)}\} + 1 \\
&= \min\{{F(2), F(1), F(0)}\} + 1 \\
&= \min\{{1, 1, 0}\} + 1 \\
&= 1
\end{align}
</script>
</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">public</span> <span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">coinChange</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">coins</span><span class="o">,</span> <span class="kt">int</span> <span class="n">amount</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">max</span> <span class="o">=</span> <span class="n">amount</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>             
        <span class="kt">int</span><span class="o">[]</span> <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">amount</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>  
        <span class="n">Arrays</span><span class="o">.</span><span class="na">fill</span><span class="o">(</span><span class="n">dp</span><span class="o">,</span> <span class="n">max</span><span class="o">);</span>  
        <span class="n">dp</span><span class="o">[</span><span class="mi">0</span><span class="o">]</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>   
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">amount</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">coins</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">j</span><span class="o">++)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">coins</span><span class="o">[</span><span class="n">j</span><span class="o">]</span> <span class="o">&lt;=</span> <span class="n">i</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">],</span> <span class="n">dp</span><span class="o">[</span><span class="n">i</span> <span class="o">-</span> <span class="n">coins</span><span class="o">[</span><span class="n">j</span><span class="o">]]</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">dp</span><span class="o">[</span><span class="n">amount</span><span class="o">]</span> <span class="o">&gt;</span> <span class="n">amount</span> <span class="o">?</span> <span class="o">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">dp</span><span class="o">[</span><span class="n">amount</span><span class="o">];</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(S*n)</script>.
On each step the algorithm finds the next <em><script type="math/tex; mode=display">F(i)</script></em> in <script type="math/tex; mode=display">n</script> iterations, where <script type="math/tex; mode=display">1\leq i \leq S</script>. Therefore in total the iterations are <script type="math/tex; mode=display">S*n</script>.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(S)</script>.
We use extra space for the memoization table.</li>
</ul>
<p>Analysis written by: @elmirap.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>At the end of the <code>i</code>-th day, we maintain <code>cash</code>, the maximum profit we could have if we did not have a share of stock, and <code>hold</code>, the maximum profit we could have if we owned a share of stock.</p>
<p>To transition from the <code>i</code>-th day to the <code>i+1</code>-th day, we either sell our stock <code>cash = max(cash, hold + prices[i] - fee)</code> or buy a stock <code>hold = max(hold, cash - prices[i])</code>.  At the end, we want to return <code>cash</code>.  We can transform <code>cash</code> first without using temporary variables because selling and buying on the same day can't be better than just continuing to hold the stock.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">maxProfit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prices</span><span class="p">,</span> <span class="n">fee</span><span class="p">):</span>
        <span class="n">cash</span><span class="p">,</span> <span class="n">hold</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="n">prices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">prices</span><span class="p">)):</span>
            <span class="n">cash</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">cash</span><span class="p">,</span> <span class="n">hold</span> <span class="o">+</span> <span class="n">prices</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">-</span> <span class="n">fee</span><span class="p">)</span>
            <span class="n">hold</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">hold</span><span class="p">,</span> <span class="n">cash</span> <span class="o">-</span> <span class="n">prices</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">cash</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">maxProfit</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">prices</span><span class="o">,</span> <span class="kt">int</span> <span class="n">fee</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">cash</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">hold</span> <span class="o">=</span> <span class="o">-</span><span class="n">prices</span><span class="o">[</span><span class="mi">0</span><span class="o">];</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">prices</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">cash</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">max</span><span class="o">(</span><span class="n">cash</span><span class="o">,</span> <span class="n">hold</span> <span class="o">+</span> <span class="n">prices</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">-</span> <span class="n">fee</span><span class="o">);</span>
            <span class="n">hold</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">max</span><span class="o">(</span><span class="n">hold</span><span class="o">,</span> <span class="n">cash</span> <span class="o">-</span> <span class="n">prices</span><span class="o">[</span><span class="n">i</span><span class="o">]);</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">cash</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of prices.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>cash</code> and <code>hold</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
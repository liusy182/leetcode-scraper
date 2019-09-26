<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-left-and-right-index-accepted">Approach #1: Left and Right Index [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-left-and-right-index-accepted">Approach #1: Left and Right Index [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>An array that has degree <code>d</code>, must have some element <code>x</code> occur <code>d</code> times.  If some subarray has the same degree, then some element <code>x</code> (that occured <code>d</code> times), still occurs <code>d</code> times.  The shortest such subarray would be from the first occurrence of <code>x</code> until the last occurrence.</p>
<p>For each element in the given array, let's know <code>left</code>, the index of its first occurrence; and <code>right</code>, the index of its last occurrence.  For example, with <code>nums = [1,2,3,2,5]</code> we have <code>left[2] = 1</code> and <code>right[2] = 3</code>.</p>
<p>Then, for each element <code>x</code> that occurs the maximum number of times, <code>right[x] - left[x] + 1</code> will be our candidate answer, and we'll take the minimum of those candidates.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">findShortestSubArray</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nums</span><span class="p">):</span>
        <span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">,</span> <span class="n">count</span> <span class="o">=</span> <span class="p">{},</span> <span class="p">{},</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nums</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">x</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">left</span><span class="p">:</span> <span class="n">left</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span>
            <span class="n">right</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span>
            <span class="n">count</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">=</span> <span class="n">count</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span>

        <span class="n">ans</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">nums</span><span class="p">)</span>
        <span class="n">degree</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">count</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">count</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">count</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">==</span> <span class="n">degree</span><span class="p">:</span>
                <span class="n">ans</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">ans</span><span class="p">,</span> <span class="n">right</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">-</span> <span class="n">left</span><span class="p">[</span><span class="n">x</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">findShortestSubArray</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">left</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">(),</span>
            <span class="n">right</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">(),</span> <span class="n">count</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>

        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">x</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">];</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">left</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">==</span> <span class="kc">null</span><span class="o">)</span> <span class="n">left</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">i</span><span class="o">);</span>
            <span class="n">right</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">i</span><span class="o">);</span>
            <span class="n">count</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">count</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="mi">0</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
        <span class="o">}</span>

        <span class="kt">int</span> <span class="n">ans</span> <span class="o">=</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span>
        <span class="kt">int</span> <span class="n">degree</span> <span class="o">=</span> <span class="n">Collections</span><span class="o">.</span><span class="na">max</span><span class="o">(</span><span class="n">count</span><span class="o">.</span><span class="na">values</span><span class="o">());</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">:</span> <span class="n">count</span><span class="o">.</span><span class="na">keySet</span><span class="o">())</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">==</span> <span class="n">degree</span><span class="o">)</span> <span class="o">{</span>
                <span class="n">ans</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">ans</span><span class="o">,</span> <span class="n">right</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">-</span> <span class="n">left</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  Every loop is through <script type="math/tex; mode=display">O(N)</script> items with <script type="math/tex; mode=display">O(1)</script> work inside the for-block.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>left</code>, <code>right</code>, and <code>count</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
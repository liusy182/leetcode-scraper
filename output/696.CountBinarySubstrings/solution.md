<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-group-by-character-accepted">Approach #1: Group By Character [Accepted]</a></li>
<li><a href="#approach-2-linear-scan-accepted">Approach #2: Linear Scan [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-group-by-character-accepted">Approach #1: Group By Character [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can convert the string <code>s</code> into an array <code>groups</code> that represents the length of same-character contiguous blocks within the string.  For example, if <code>s = "110001111000000"</code>, then <code>groups = [2, 3, 4, 6]</code>.</p>
<p>For every binary string of the form <code>'0' * k + '1' * k</code> or <code>'1' * k + '0' * k</code>, the middle of this string must occur between two groups.  </p>
<p>Let's try to count the number of valid binary strings between <code>groups[i]</code> and <code>groups[i+1]</code>.  If we have <code>groups[i] = 2, groups[i+1] = 3</code>, then it represents either <code>"00111"</code> or <code>"11000"</code>.  We clearly can make <code>min(groups[i], groups[i+1])</code> valid binary strings within this string.  Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.</p>
<p><strong>Algorithm</strong></p>
<p>Let's create <code>groups</code> as defined above.  The first element of <code>s</code> belongs in it's own group.  From then on, each element either doesn't match the previous element, so that it starts a new group of size 1; or it does match, so that the size of the most recent group increases by 1.</p>
<p>Afterwards, we will take the sum of <code>min(groups[i-1], groups[i])</code>.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">countBinarySubstrings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">):</span>
        <span class="n">groups</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)):</span>
            <span class="k">if</span> <span class="n">s</span><span class="p">[</span><span class="n">i</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">!=</span> <span class="n">s</span><span class="p">[</span><span class="n">i</span><span class="p">]:</span>
                <span class="n">groups</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">groups</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>

        <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">groups</span><span class="p">)):</span>
            <span class="n">ans</span> <span class="o">+=</span> <span class="nb">min</span><span class="p">(</span><span class="n">groups</span><span class="p">[</span><span class="n">i</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">groups</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><em>Alternate Implentation</em></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">countBinarySubstrings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">):</span>
        <span class="n">groups</span> <span class="o">=</span> <span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">v</span><span class="p">))</span> <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">itertools</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">s</span><span class="p">)]</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">groups</span><span class="p">,</span> <span class="n">groups</span><span class="p">[</span><span class="mi">1</span><span class="p">:]))</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">countBinarySubstrings</span><span class="o">(</span><span class="n">String</span> <span class="n">s</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span><span class="o">[]</span> <span class="n">groups</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">()];</span>
        <span class="kt">int</span> <span class="n">t</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="n">groups</span><span class="o">[</span><span class="mi">0</span><span class="o">]</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">s</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">!=</span> <span class="n">s</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">))</span> <span class="o">{</span>
                <span class="n">groups</span><span class="o">[++</span><span class="n">t</span><span class="o">]</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span>
            <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
                <span class="n">groups</span><span class="o">[</span><span class="n">t</span><span class="o">]++;</span>
            <span class="o">}</span>
        <span class="o">}</span>

        <span class="kt">int</span> <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">t</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">ans</span> <span class="o">+=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">groups</span><span class="o">[</span><span class="n">i</span><span class="o">-</span><span class="mi">1</span><span class="o">],</span> <span class="n">groups</span><span class="o">[</span><span class="n">i</span><span class="o">]);</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>s</code>.  Every loop is through <script type="math/tex; mode=display">O(N)</script> items with <script type="math/tex; mode=display">O(1)</script> work inside the for-block.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>groups</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-linear-scan-accepted">Approach #2: Linear Scan [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can amend our <em>Approach #1</em> to calculate the answer on the fly.  Instead of storing <code>groups</code>, we will remember only <code>prev = groups[-2]</code> and <code>cur = groups[-1]</code>.  Then, the answer is the sum of <code>min(prev, cur)</code> over each different final <code>(prev, cur)</code> we see.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">countBinarySubstrings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">):</span>
        <span class="n">ans</span><span class="p">,</span> <span class="n">prev</span><span class="p">,</span> <span class="n">cur</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)):</span>
            <span class="k">if</span> <span class="n">s</span><span class="p">[</span><span class="n">i</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">!=</span> <span class="n">s</span><span class="p">[</span><span class="n">i</span><span class="p">]:</span>
                <span class="n">ans</span> <span class="o">+=</span> <span class="nb">min</span><span class="p">(</span><span class="n">prev</span><span class="p">,</span> <span class="n">cur</span><span class="p">)</span>
                <span class="n">prev</span><span class="p">,</span> <span class="n">cur</span> <span class="o">=</span> <span class="n">cur</span><span class="p">,</span> <span class="mi">1</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">cur</span> <span class="o">+=</span> <span class="mi">1</span>

        <span class="k">return</span> <span class="n">ans</span> <span class="o">+</span> <span class="nb">min</span><span class="p">(</span><span class="n">prev</span><span class="p">,</span> <span class="n">cur</span><span class="p">)</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">countBinarySubstrings</span><span class="o">(</span><span class="n">String</span> <span class="n">s</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">prev</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">cur</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">s</span><span class="o">.</span><span class="na">length</span><span class="o">();</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">s</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">!=</span> <span class="n">s</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">))</span> <span class="o">{</span>
                <span class="n">ans</span> <span class="o">+=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">prev</span><span class="o">,</span> <span class="n">cur</span><span class="o">);</span>
                <span class="n">prev</span> <span class="o">=</span> <span class="n">cur</span><span class="o">;</span>
                <span class="n">cur</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span>
            <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
                <span class="n">cur</span><span class="o">++;</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span> <span class="o">+</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">prev</span><span class="o">,</span> <span class="n">cur</span><span class="o">);</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>s</code>.  Every loop is through <script type="math/tex; mode=display">O(N)</script> items with <script type="math/tex; mode=display">O(1)</script> work inside the for-block.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>prev</code>, <code>cur</code>, and <code>ans</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <code>dp[i][j]</code> be the answer to the problem for the strings <code>s1[i:], s2[j:]</code>.</p>
<p>When one of the input strings is empty, the answer is the ASCII-sum of the other string.  We can calculate this cumulatively using code like <code>dp[i][s2.length()] = dp[i+1][s2.length()] + s1.codePointAt(i)</code>.</p>
<p>When <code>s1[i] == s2[j]</code>, we have <code>dp[i][j] = dp[i+1][j+1]</code> as we can ignore these two characters.</p>
<p>When <code>s1[i] != s2[j]</code>, we will have to delete at least one of them.  We'll have <code>dp[i][j]</code> as the minimum of the answers after both deletion options.</p>
<p>The solutions presented will use <em>bottom-up</em> dynamic programming.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">minimumDeleteSum</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s1</span><span class="p">,</span> <span class="n">s2</span><span class="p">):</span>
        <span class="n">dp</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s2</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s1</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)]</span>

        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s1</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
            <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="nb">len</span><span class="p">(</span><span class="n">s2</span><span class="p">)]</span> <span class="o">=</span> <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">][</span><span class="nb">len</span><span class="p">(</span><span class="n">s2</span><span class="p">)]</span> <span class="o">+</span> <span class="nb">ord</span><span class="p">(</span><span class="n">s1</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
        <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s2</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
            <span class="n">dp</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">s1</span><span class="p">)][</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="n">dp</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">s1</span><span class="p">)][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="nb">ord</span><span class="p">(</span><span class="n">s2</span><span class="p">[</span><span class="n">j</span><span class="p">])</span>

        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s1</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">s2</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">s1</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="n">s2</span><span class="p">[</span><span class="n">j</span><span class="p">]:</span>
                    <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">][</span><span class="n">j</span><span class="p">]</span> <span class="o">+</span> <span class="nb">ord</span><span class="p">(</span><span class="n">s1</span><span class="p">[</span><span class="n">i</span><span class="p">]),</span>
                                   <span class="n">dp</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="nb">ord</span><span class="p">(</span><span class="n">s2</span><span class="p">[</span><span class="n">j</span><span class="p">]))</span>

        <span class="k">return</span> <span class="n">dp</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">minimumDeleteSum</span><span class="o">(</span><span class="n">String</span> <span class="n">s1</span><span class="o">,</span> <span class="n">String</span> <span class="n">s2</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span><span class="o">[][]</span> <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">s1</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">s2</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>

        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="n">s1</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span><span class="o">--)</span> <span class="o">{</span>
            <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">s2</span><span class="o">.</span><span class="na">length</span><span class="o">()]</span> <span class="o">=</span> <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">][</span><span class="n">s2</span><span class="o">.</span><span class="na">length</span><span class="o">()]</span> <span class="o">+</span> <span class="n">s1</span><span class="o">.</span><span class="na">codePointAt</span><span class="o">(</span><span class="n">i</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="n">s2</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span> <span class="n">j</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span><span class="o">--)</span> <span class="o">{</span>
            <span class="n">dp</span><span class="o">[</span><span class="n">s1</span><span class="o">.</span><span class="na">length</span><span class="o">()][</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="n">dp</span><span class="o">[</span><span class="n">s1</span><span class="o">.</span><span class="na">length</span><span class="o">()][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="o">]</span> <span class="o">+</span> <span class="n">s2</span><span class="o">.</span><span class="na">codePointAt</span><span class="o">(</span><span class="n">j</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="n">s1</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span><span class="o">--)</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="n">s2</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span> <span class="n">j</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span><span class="o">--)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">s1</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">==</span> <span class="n">s2</span><span class="o">.</span><span class="na">charAt</span><span class="o">(</span><span class="n">j</span><span class="o">))</span> <span class="o">{</span>
                    <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="o">];</span>
                <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
                    <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">][</span><span class="n">j</span><span class="o">]</span> <span class="o">+</span> <span class="n">s1</span><span class="o">.</span><span class="na">codePointAt</span><span class="o">(</span><span class="n">i</span><span class="o">),</span>
                                        <span class="n">dp</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="o">]</span> <span class="o">+</span> <span class="n">s2</span><span class="o">.</span><span class="na">codePointAt</span><span class="o">(</span><span class="n">j</span><span class="o">));</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">dp</span><span class="o">[</span><span class="mi">0</span><span class="o">][</span><span class="mi">0</span><span class="o">];</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M*N)</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of the given strings.  We use nested for loops: each loop is <script type="math/tex; mode=display">O(M)</script> and <script type="math/tex; mode=display">O(N)</script> respectively.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M*N)</script>, the space used by <code>dp</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
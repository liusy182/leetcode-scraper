<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-increment-pointer-accepted">Approach #1: Increment Pointer [Accepted]</a></li>
<li><a href="#approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-increment-pointer-accepted">Approach #1: Increment Pointer [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>When reading from the <code>i</code>-th position, if <code>bits[i] == 0</code>, the next character must have 1 bit; else if <code>bits[i] == 1</code>, the next character must have 2 bits.  We increment our read-pointer <code>i</code> to the start of the next character appropriately.  At the end, if our pointer is at <code>bits.length - 1</code>, then the last character must have a size of 1 bit.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">isOneBitCharacter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bits</span><span class="p">):</span>
        <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">bits</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">i</span> <span class="o">+=</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">i</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">bits</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">isOneBitCharacter</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">bits</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">i</span> <span class="o">&lt;</span> <span class="n">bits</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">i</span> <span class="o">+=</span> <span class="n">bits</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">i</span> <span class="o">==</span> <span class="n">bits</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>bits</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>i</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>The second-last <code>0</code> must be the end of a character (or, the beginning of the array if it doesn't exist).  Looking from that position forward, the array <code>bits</code> takes the form <code>[1, 1, ..., 1, 0]</code> where there are zero or more <code>1</code>'s present in total.  It is easy to show that the answer is <code>true</code> if and only if there are an even number of ones present.</p>
<p>In our algorithm, we will find the second last zero by performing a linear scan from the right.  We present two slightly different approaches below.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">isOneBitCharacter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bits</span><span class="p">):</span>
        <span class="n">parity</span> <span class="o">=</span> <span class="n">bits</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
        <span class="k">while</span> <span class="n">bits</span> <span class="ow">and</span> <span class="n">bits</span><span class="o">.</span><span class="n">pop</span><span class="p">():</span> <span class="n">parity</span> <span class="o">^=</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">parity</span> <span class="o">==</span> <span class="mi">0</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">isOneBitCharacter</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">bits</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="n">bits</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">2</span><span class="o">;</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">i</span> <span class="o">&gt;=</span> <span class="mi">0</span> <span class="o">&amp;&amp;</span> <span class="n">bits</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="n">i</span><span class="o">--;</span>
        <span class="k">return</span> <span class="o">(</span><span class="n">bits</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="n">i</span><span class="o">)</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>bits</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>parity</code> (or <code>i</code>).</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-parsing-accepted">Approach #1: Parsing [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-parsing-accepted">Approach #1: Parsing [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We need to parse the <code>source</code> line by line.  Our state is that we either are in a block comment or not.</p>
<ul>
<li>
<p>If we start a block comment and we aren't in a block, then we will skip over the next two characters and change our state to be in a block.</p>
</li>
<li>
<p>If we end a block comment and we are in a block, then we will skip over the next two characters and change our state to be <em>not</em> in a block.</p>
</li>
<li>
<p>If we start a line comment and we aren't in a block, then we will ignore the rest of the line.</p>
</li>
<li>
<p>If we aren't in a block comment (and it wasn't the start of a comment), we will record the character we are at.</p>
</li>
<li>
<p>At the end of each line, if we aren't in a block, we will record the line.</p>
</li>
</ul>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">removeComments</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">source</span><span class="p">):</span>
        <span class="n">in_block</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="n">ans</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">source</span><span class="p">:</span>
            <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">in_block</span><span class="p">:</span>
                <span class="n">newline</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">line</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s1">'/*'</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">in_block</span><span class="p">:</span>
                    <span class="n">in_block</span> <span class="o">=</span> <span class="bp">True</span>
                    <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="k">elif</span> <span class="n">line</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s1">'*/'</span> <span class="ow">and</span> <span class="n">in_block</span><span class="p">:</span>
                    <span class="n">in_block</span> <span class="o">=</span> <span class="bp">False</span>
                    <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="k">elif</span> <span class="ow">not</span> <span class="n">in_block</span> <span class="ow">and</span> <span class="n">line</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s1">'//'</span><span class="p">:</span>
                    <span class="k">break</span>
                <span class="k">elif</span> <span class="ow">not</span> <span class="n">in_block</span><span class="p">:</span>
                    <span class="n">newline</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
                <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="n">newline</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">in_block</span><span class="p">:</span>
                <span class="n">ans</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">newline</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="nf">removeComments</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">source</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">boolean</span> <span class="n">inBlock</span> <span class="o">=</span> <span class="kc">false</span><span class="o">;</span>
        <span class="n">StringBuilder</span> <span class="n">newline</span> <span class="o">=</span> <span class="k">new</span> <span class="n">StringBuilder</span><span class="o">();</span>
        <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">ans</span> <span class="o">=</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">line</span><span class="o">:</span> <span class="n">source</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
            <span class="kt">char</span><span class="o">[]</span> <span class="n">chars</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="na">toCharArray</span><span class="o">();</span>
            <span class="k">if</span> <span class="o">(!</span><span class="n">inBlock</span><span class="o">)</span> <span class="n">newline</span> <span class="o">=</span> <span class="k">new</span> <span class="n">StringBuilder</span><span class="o">();</span>
            <span class="k">while</span> <span class="o">(</span><span class="n">i</span> <span class="o">&lt;</span> <span class="n">line</span><span class="o">.</span><span class="na">length</span><span class="o">())</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(!</span><span class="n">inBlock</span> <span class="o">&amp;&amp;</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span> <span class="o">&lt;</span> <span class="n">line</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&amp;&amp;</span> <span class="n">chars</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'/'</span> <span class="o">&amp;&amp;</span> <span class="n">chars</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'*'</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">inBlock</span> <span class="o">=</span> <span class="kc">true</span><span class="o">;</span>
                    <span class="n">i</span><span class="o">++;</span>
                <span class="o">}</span> <span class="k">else</span> <span class="k">if</span> <span class="o">(</span><span class="n">inBlock</span> <span class="o">&amp;&amp;</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span> <span class="o">&lt;</span> <span class="n">line</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&amp;&amp;</span> <span class="n">chars</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'*'</span> <span class="o">&amp;&amp;</span> <span class="n">chars</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'/'</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">inBlock</span> <span class="o">=</span> <span class="kc">false</span><span class="o">;</span>
                    <span class="n">i</span><span class="o">++;</span>
                <span class="o">}</span> <span class="k">else</span> <span class="k">if</span> <span class="o">(!</span><span class="n">inBlock</span> <span class="o">&amp;&amp;</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span> <span class="o">&lt;</span> <span class="n">line</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&amp;&amp;</span> <span class="n">chars</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'/'</span> <span class="o">&amp;&amp;</span> <span class="n">chars</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">]</span> <span class="o">==</span> <span class="sc">'/'</span><span class="o">)</span> <span class="o">{</span>
                    <span class="k">break</span><span class="o">;</span>
                <span class="o">}</span> <span class="k">else</span> <span class="k">if</span> <span class="o">(!</span><span class="n">inBlock</span><span class="o">)</span> <span class="o">{</span>
                    <span class="n">newline</span><span class="o">.</span><span class="na">append</span><span class="o">(</span><span class="n">chars</span><span class="o">[</span><span class="n">i</span><span class="o">]);</span>
                <span class="o">}</span>
                <span class="n">i</span><span class="o">++;</span>
            <span class="o">}</span>
            <span class="k">if</span> <span class="o">(!</span><span class="n">inBlock</span> <span class="o">&amp;&amp;</span> <span class="n">newline</span><span class="o">.</span><span class="na">length</span><span class="o">()</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span>
                <span class="n">ans</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="k">new</span> <span class="n">String</span><span class="o">(</span><span class="n">newline</span><span class="o">));</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(S)</script>, where <script type="math/tex; mode=display">S</script> is the total length of the source code.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(S)</script>, the space used by recording the source code into <code>ans</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-read-and-write-heads-accepted">Approach #1: Read and Write Heads [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-read-and-write-heads-accepted">Approach #1: Read and Write Heads [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We will use separate pointers <code>read</code> and <code>write</code> to mark where we are reading and writing from.  Both operations will be done left to right alternately:  we will read a contiguous group of characters, then write the compressed version to the array.  At the end, the position of the <code>write</code> head will be the length of the answer that was written.</p>
<p><strong>Algorithm</strong></p>
<p>Let's maintain <code>anchor</code>, the start position of the contiguous group of characters we are currently reading.</p>
<p>Now, let's read from left to right.  We know that we must be at the end of the block when we are at the last character, or when the next character is different from the current character.</p>
<p>When we are at the end of a group, we will write the result of that group down using our <code>write</code> head.  <code>chars[anchor]</code> will be the correct character, and the length (if greater than 1) will be <code>read - anchor + 1</code>.  We will write the digits of that number to the array.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">compress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">chars</span><span class="p">):</span>
        <span class="n">anchor</span> <span class="o">=</span> <span class="n">write</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">read</span><span class="p">,</span> <span class="n">c</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">chars</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">read</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">chars</span><span class="p">)</span> <span class="ow">or</span> <span class="n">chars</span><span class="p">[</span><span class="n">read</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span> <span class="o">!=</span> <span class="n">c</span><span class="p">:</span>
                <span class="n">chars</span><span class="p">[</span><span class="n">write</span><span class="p">]</span> <span class="o">=</span> <span class="n">chars</span><span class="p">[</span><span class="n">anchor</span><span class="p">]</span>
                <span class="n">write</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="k">if</span> <span class="n">read</span> <span class="o">&gt;</span> <span class="n">anchor</span><span class="p">:</span>
                    <span class="k">for</span> <span class="n">digit</span> <span class="ow">in</span> <span class="nb">str</span><span class="p">(</span><span class="n">read</span> <span class="o">-</span> <span class="n">anchor</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
                        <span class="n">chars</span><span class="p">[</span><span class="n">write</span><span class="p">]</span> <span class="o">=</span> <span class="n">digit</span>
                        <span class="n">write</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">anchor</span> <span class="o">=</span> <span class="n">read</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">write</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">compress</span><span class="o">(</span><span class="kt">char</span><span class="o">[]</span> <span class="n">chars</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">anchor</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">write</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">read</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">read</span> <span class="o">&lt;</span> <span class="n">chars</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">read</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">read</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">chars</span><span class="o">.</span><span class="na">length</span> <span class="o">||</span> <span class="n">chars</span><span class="o">[</span><span class="n">read</span> <span class="o">+</span> <span class="mi">1</span><span class="o">]</span> <span class="o">!=</span> <span class="n">chars</span><span class="o">[</span><span class="n">read</span><span class="o">])</span> <span class="o">{</span>
                <span class="n">chars</span><span class="o">[</span><span class="n">write</span><span class="o">++]</span> <span class="o">=</span> <span class="n">chars</span><span class="o">[</span><span class="n">anchor</span><span class="o">];</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">read</span> <span class="o">&gt;</span> <span class="n">anchor</span><span class="o">)</span> <span class="o">{</span>
                    <span class="k">for</span> <span class="o">(</span><span class="kt">char</span> <span class="n">c</span><span class="o">:</span> <span class="o">(</span><span class="s">""</span> <span class="o">+</span> <span class="o">(</span><span class="n">read</span> <span class="o">-</span> <span class="n">anchor</span> <span class="o">+</span> <span class="mi">1</span><span class="o">)).</span><span class="na">toCharArray</span><span class="o">())</span> <span class="o">{</span>
                        <span class="n">chars</span><span class="o">[</span><span class="n">write</span><span class="o">++]</span> <span class="o">=</span> <span class="n">c</span><span class="o">;</span>
                    <span class="o">}</span>
                <span class="o">}</span>
                <span class="n">anchor</span> <span class="o">=</span> <span class="n">read</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">write</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>chars</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>, the space used by <code>read</code>, <code>write</code>, and <code>anchor</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
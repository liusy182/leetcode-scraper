<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-with-initial-character-map-time-limit-exceeded">Approach #1: Brute Force with Initial Character Map [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-binary-search-with-naive-check-time-limit-exceeded">Approach #2: Binary Search with Naive Check [Time Limit Exceeded]</a></li>
<li><a href="#approach-3-dynamic-programming-accepted">Approach #3: Dynamic Programming [Accepted]</a></li>
<li><a href="#approach-4-binary-search-with-rolling-hash-accepted">Approach #4: Binary Search with Rolling Hash [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-with-initial-character-map-time-limit-exceeded">Approach #1: Brute Force with Initial Character Map [Time Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>In a typical brute force, for all starting indices <code>i</code> of <code>A</code> and <code>j</code> of <code>B</code>, we will check for the longest matching subarray <code>A[i:i+k] == B[j:j+k]</code> of length <code>k</code>.  This would look roughly like the following psuedocode:</p>
<div class="codehilite"><pre><span></span><span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">0</span> <span class="o">..</span> <span class="n">A</span><span class="o">.</span><span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]:</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">0</span> <span class="o">..</span> <span class="n">B</span><span class="o">.</span><span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]:</span>
        <span class="n">k</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">while</span> <span class="p">(</span><span class="n">A</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="n">k</span><span class="p">]</span> <span class="o">==</span> <span class="n">B</span><span class="p">[</span><span class="n">j</span><span class="o">+</span><span class="n">k</span><span class="p">]):</span> <span class="n">k</span> <span class="o">+=</span> <span class="mi">1</span> <span class="c1">#and i+k &lt; A.length etc.</span>
        <span class="n">ans</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">ans</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span>
</pre></div>


<p>Our insight is that in typical cases, most of the time <code>A[i] != B[j]</code>.  We could instead keep a hashmap <code>Bstarts[A[i]] = all j such that B[j] == A[i]</code>, and only loop through those in our <code>j</code> loop.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">findLength</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">A</span><span class="p">,</span> <span class="n">B</span><span class="p">):</span>
        <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">Bstarts</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">j</span><span class="p">,</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">B</span><span class="p">):</span>
            <span class="n">Bstarts</span><span class="p">[</span><span class="n">y</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">j</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">A</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">Bstarts</span><span class="p">[</span><span class="n">x</span><span class="p">]:</span>
                <span class="n">k</span> <span class="o">=</span> <span class="mi">0</span>
                <span class="k">while</span> <span class="n">i</span><span class="o">+</span><span class="n">k</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">)</span> <span class="ow">and</span> <span class="n">j</span><span class="o">+</span><span class="n">k</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">B</span><span class="p">)</span> <span class="ow">and</span> <span class="n">A</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="n">k</span><span class="p">]</span> <span class="o">==</span> <span class="n">B</span><span class="p">[</span><span class="n">j</span><span class="o">+</span><span class="n">k</span><span class="p">]:</span>
                    <span class="n">k</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">ans</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">ans</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ans</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">findLength</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">A</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">B</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;&gt;</span> <span class="n">Bstarts</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">B</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">j</span><span class="o">++)</span> <span class="o">{</span>
            <span class="n">Bstarts</span><span class="o">.</span><span class="na">computeIfAbsent</span><span class="o">(</span><span class="n">B</span><span class="o">[</span><span class="n">j</span><span class="o">],</span> <span class="n">x</span> <span class="o">-&gt;</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">()).</span><span class="na">add</span><span class="o">(</span><span class="n">j</span><span class="o">);</span>
        <span class="o">}</span>

        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">A</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="k">if</span> <span class="o">(</span><span class="n">Bstarts</span><span class="o">.</span><span class="na">containsKey</span><span class="o">(</span><span class="n">A</span><span class="o">[</span><span class="n">i</span><span class="o">]))</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span><span class="o">:</span> <span class="n">Bstarts</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">A</span><span class="o">[</span><span class="n">i</span><span class="o">]))</span> <span class="o">{</span>
                <span class="kt">int</span> <span class="n">k</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
                <span class="k">while</span> <span class="o">(</span><span class="n">i</span><span class="o">+</span><span class="n">k</span> <span class="o">&lt;</span> <span class="n">A</span><span class="o">.</span><span class="na">length</span> <span class="o">&amp;&amp;</span> <span class="n">j</span><span class="o">+</span><span class="n">k</span> <span class="o">&lt;</span> <span class="n">B</span><span class="o">.</span><span class="na">length</span> <span class="o">&amp;&amp;</span> <span class="n">A</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="n">k</span><span class="o">]</span> <span class="o">==</span> <span class="n">B</span><span class="o">[</span><span class="n">j</span><span class="o">+</span><span class="n">k</span><span class="o">])</span> <span class="o">{</span>
                    <span class="n">k</span><span class="o">++</span>
                <span class="o">}</span>
                <span class="n">ans</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">max</span><span class="o">(</span><span class="n">ans</span><span class="o">,</span> <span class="n">k</span><span class="o">);</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M*N*\min(M, N))</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>A, B</code>.  The worst case is when all the elements are equal.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>Bstarts</code>.  (Of course, we could amend our algorithm to make this <script type="math/tex; mode=display">O(\min(M, N))</script>.)</p>
</li>
</ul>
<hr>
<h4 id="approach-2-binary-search-with-naive-check-time-limit-exceeded">Approach #2: Binary Search with Naive Check [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>If there is a length <code>k</code> subarray common to <code>A</code> and <code>B</code>, then there is a length <code>j &lt;= k</code> subarray as well.  </p>
<p>Let <code>check(length)</code> be the answer to the question "Is there a subarray with <code>length</code> length, common to <code>A</code> and <code>B</code>?"  This is a function with range that must take the form <code>[True, True, ..., True, False, False, ..., False]</code> with at least one <code>True</code>.  We can binary search on this function.</p>
<p><strong>Algorithm</strong></p>
<p>Focusing on the binary search, our invariant is that <code>check(hi)</code> will always be <code>False</code>.  We'll start with <code>hi = min(len(A), len(B)) + 1</code>; clearly <code>check(hi) is False</code>.</p>
<p>Now we perform our check in the midpoint <code>mi</code> of <code>lo</code> and <code>hi</code>.  When it is possible, then <code>lo = mi + 1</code>, and when it isn't, <code>hi = mi</code>.  This maintains the invariant.  At the end of our binary search, <code>hi == lo</code> and <code>lo</code> is the lowest value such that <code>check(lo) is False</code>, so we want <code>lo - 1</code>.</p>
<p>As for the check itself, we can naively check whether any <code>A[i:i+k] == B[j:j+k]</code> using set structures.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">findLength</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">A</span><span class="p">,</span> <span class="n">B</span><span class="p">):</span>
        <span class="k">def</span> <span class="nf">check</span><span class="p">(</span><span class="n">length</span><span class="p">):</span>
            <span class="n">seen</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">A</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="n">length</span><span class="p">])</span>
                       <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">)</span> <span class="o">-</span> <span class="n">length</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
            <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">B</span><span class="p">[</span><span class="n">j</span><span class="p">:</span><span class="n">j</span><span class="o">+</span><span class="n">length</span><span class="p">])</span> <span class="ow">in</span> <span class="n">seen</span>
                       <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">B</span><span class="p">)</span> <span class="o">-</span> <span class="n">length</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>

        <span class="n">lo</span><span class="p">,</span> <span class="n">hi</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">min</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">),</span> <span class="nb">len</span><span class="p">(</span><span class="n">B</span><span class="p">))</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">while</span> <span class="n">lo</span> <span class="o">&lt;</span> <span class="n">hi</span><span class="p">:</span>
            <span class="n">mi</span> <span class="o">=</span> <span class="p">(</span><span class="n">lo</span> <span class="o">+</span> <span class="n">hi</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span>
            <span class="k">if</span> <span class="n">check</span><span class="p">(</span><span class="n">mi</span><span class="p">):</span>
                <span class="n">lo</span> <span class="o">=</span> <span class="n">mi</span> <span class="o">+</span> <span class="mi">1</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">hi</span> <span class="o">=</span> <span class="n">mi</span>
        <span class="k">return</span> <span class="n">lo</span> <span class="o">-</span> <span class="mi">1</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">check</span><span class="o">(</span><span class="kt">int</span> <span class="n">length</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">A</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">B</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Set</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">seen</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashSet</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">+</span> <span class="n">length</span> <span class="o">&lt;=</span> <span class="n">A</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">seen</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">Arrays</span><span class="o">.</span><span class="na">toString</span><span class="o">(</span><span class="n">Arrays</span><span class="o">.</span><span class="na">copyOfRange</span><span class="o">(</span><span class="n">A</span><span class="o">,</span> <span class="n">i</span><span class="o">,</span> <span class="n">i</span><span class="o">+</span><span class="n">length</span><span class="o">)));</span>
        <span class="o">}</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">j</span> <span class="o">+</span> <span class="n">length</span> <span class="o">&lt;=</span> <span class="n">B</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="o">++</span><span class="n">j</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">seen</span><span class="o">.</span><span class="na">contains</span><span class="o">(</span><span class="n">Arrays</span><span class="o">.</span><span class="na">toString</span><span class="o">(</span><span class="n">Arrays</span><span class="o">.</span><span class="na">copyOfRange</span><span class="o">(</span><span class="n">B</span><span class="o">,</span> <span class="n">j</span><span class="o">,</span> <span class="n">j</span><span class="o">+</span><span class="n">length</span><span class="o">))))</span> <span class="o">{</span>
                <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">findLength</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">A</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">B</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">lo</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">hi</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">A</span><span class="o">.</span><span class="na">length</span><span class="o">,</span> <span class="n">B</span><span class="o">.</span><span class="na">length</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">lo</span> <span class="o">&lt;</span> <span class="n">hi</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">mi</span> <span class="o">=</span> <span class="o">(</span><span class="n">lo</span> <span class="o">+</span> <span class="n">hi</span><span class="o">)</span> <span class="o">/</span> <span class="mi">2</span><span class="o">;</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">check</span><span class="o">(</span><span class="n">mi</span><span class="o">,</span> <span class="n">A</span><span class="o">,</span> <span class="n">B</span><span class="o">))</span> <span class="n">lo</span> <span class="o">=</span> <span class="n">mi</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
            <span class="k">else</span> <span class="n">hi</span> <span class="o">=</span> <span class="n">mi</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">lo</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O((M + N) * \min(M, N) * \log{(\min(M, N))})</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>A, B</code>.  The log factor comes from the binary search.  The complexity of our naive check of a given <script type="math/tex; mode=display">\text{length}</script> is <script type="math/tex; mode=display">O((M+N) * \text{length})</script>, as we will create the <code>seen</code> strings with complexity <script type="math/tex; mode=display">O(M * \text{length})</script>, then search for them with complexity <script type="math/tex; mode=display">O(N * \text{length})</script>, and our total complexity when performing our <code>check</code> is the addition of these two.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M^2)</script>, the space used by <code>seen</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming-accepted">Approach #3: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Since a common subarray of <code>A</code> and <code>B</code> must start at some <code>A[i]</code> and <code>B[j]</code>, let <code>dp[i][j]</code> be the longest common prefix of <code>A[i:]</code> and <code>B[j:]</code>.  Whenever <code>A[i] == B[j]</code>, we know <code>dp[i][j] = dp[i+1][j+1] + 1</code>.  Also, the answer is <code>max(dp[i][j])</code> over all <code>i, j</code>.</p>
<p>We can perform bottom-up dynamic programming to find the answer based on this recurrence.  Our loop invariant is that the answer is already calculated correctly and stored in <code>dp</code> for any larger <code>i, j</code>.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">findLength</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">A</span><span class="p">,</span> <span class="n">B</span><span class="p">):</span>
        <span class="n">memo</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">B</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">B</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">A</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="n">B</span><span class="p">[</span><span class="n">j</span><span class="p">]:</span>
                    <span class="n">memo</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="n">memo</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="mi">1</span>
        <span class="k">return</span> <span class="nb">max</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">row</span><span class="p">)</span> <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">memo</span><span class="p">)</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">findLength</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">A</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">B</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">ans</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="kt">int</span><span class="o">[][]</span> <span class="n">memo</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">A</span><span class="o">.</span><span class="na">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">][</span><span class="n">B</span><span class="o">.</span><span class="na">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="n">A</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="o">;</span> <span class="o">--</span><span class="n">i</span><span class="o">)</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="n">B</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span> <span class="n">j</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="o">;</span> <span class="o">--</span><span class="n">j</span><span class="o">)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">A</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">==</span> <span class="n">B</span><span class="o">[</span><span class="n">j</span><span class="o">])</span> <span class="o">{</span>
                    <span class="n">memo</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">]</span> <span class="o">=</span> <span class="n">memo</span><span class="o">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="o">][</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="o">]</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
                    <span class="k">if</span> <span class="o">(</span><span class="n">ans</span> <span class="o">&lt;</span> <span class="n">memo</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">])</span> <span class="n">ans</span> <span class="o">=</span> <span class="n">memo</span><span class="o">[</span><span class="n">i</span><span class="o">][</span><span class="n">j</span><span class="o">];</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M*N)</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>A, B</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M*N)</script>, the space used by <code>dp</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-4-binary-search-with-rolling-hash-accepted">Approach #4: Binary Search with Rolling Hash [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #2</em>, we will binary search for the answer.  However, we will use a <em>rolling hash</em> (Rabin-Karp algorithm) to store hashes in our set structure.</p>
<p><strong>Algorithm</strong></p>
<p>For some prime <script type="math/tex; mode=display">p</script>, consider the following function modulo some prime modulus <script type="math/tex; mode=display">\mathcal{M}</script>:</p>
<p>
<script type="math/tex; mode=display">\text{hash}(S) = \sum_{0 \leq i < len(S)} p^i * S[i]</script>
</p>
<p>Notably, <script type="math/tex; mode=display">\text{hash}(S[1:] + x) = \frac{(\text{hash}(S) - S[0])}{p} + p^{n-1} x</script>.  This shows we can get the hash of all <script type="math/tex; mode=display">A[i:i+\text{guess}]</script> in linear time.  We will also use the fact that <script type="math/tex; mode=display">p^{-1} = p^{\mathcal{M}-2} \mod \mathcal{M}</script>.</p>
<p>For every <code>i &gt;= length - 1</code>, we will want to record the hash of <code>A[i-length+1], A[i-length+2], ..., A[i]</code>.  After, we will truncate the first element by <code>h = (h - A[i - (length - 1)]) * Pinv % MOD</code> to get ready to add the next element.</p>
<p>To make our algorithm air tight, we also make a naive check when our work with rolling hashes says that we have found a match.</p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">findLength</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">A</span><span class="p">,</span> <span class="n">B</span><span class="p">):</span>
        <span class="n">P</span><span class="p">,</span> <span class="n">MOD</span> <span class="o">=</span> <span class="mi">113</span><span class="p">,</span> <span class="mi">10</span><span class="o">**</span><span class="mi">9</span> <span class="o">+</span> <span class="mi">7</span>
        <span class="n">Pinv</span> <span class="o">=</span> <span class="nb">pow</span><span class="p">(</span><span class="n">P</span><span class="p">,</span> <span class="n">MOD</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="n">MOD</span><span class="p">)</span>
        <span class="k">def</span> <span class="nf">check</span><span class="p">(</span><span class="n">guess</span><span class="p">):</span>
            <span class="k">def</span> <span class="nf">rolling</span><span class="p">(</span><span class="n">A</span><span class="p">,</span> <span class="n">length</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">length</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="k">yield</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span>
                    <span class="k">return</span>

                <span class="n">h</span><span class="p">,</span> <span class="n">power</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span>
                <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">A</span><span class="p">):</span>
                    <span class="n">h</span> <span class="o">=</span> <span class="p">(</span><span class="n">h</span> <span class="o">+</span> <span class="n">x</span> <span class="o">*</span> <span class="n">power</span><span class="p">)</span> <span class="o">%</span> <span class="n">MOD</span>
                    <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="p">:</span>
                        <span class="n">power</span> <span class="o">=</span> <span class="p">(</span><span class="n">power</span> <span class="o">*</span> <span class="n">P</span><span class="p">)</span> <span class="o">%</span> <span class="n">MOD</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="k">yield</span> <span class="n">h</span><span class="p">,</span> <span class="n">i</span> <span class="o">-</span> <span class="p">(</span><span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span>
                        <span class="n">h</span> <span class="o">=</span> <span class="p">(</span><span class="n">h</span> <span class="o">-</span> <span class="n">A</span><span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="p">(</span><span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)])</span> <span class="o">*</span> <span class="n">Pinv</span> <span class="o">%</span> <span class="n">MOD</span>

            <span class="n">hashes</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">ha</span><span class="p">,</span> <span class="n">start</span> <span class="ow">in</span> <span class="n">rolling</span><span class="p">(</span><span class="n">A</span><span class="p">,</span> <span class="n">guess</span><span class="p">):</span>
                <span class="n">hashes</span><span class="p">[</span><span class="n">ha</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">start</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">ha</span><span class="p">,</span> <span class="n">start</span> <span class="ow">in</span> <span class="n">rolling</span><span class="p">(</span><span class="n">B</span><span class="p">,</span> <span class="n">guess</span><span class="p">):</span>
                <span class="n">iarr</span> <span class="o">=</span> <span class="n">hashes</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">ha</span><span class="p">,</span> <span class="p">[])</span>
                <span class="k">if</span> <span class="nb">any</span><span class="p">(</span><span class="n">A</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="n">guess</span><span class="p">]</span> <span class="o">==</span> <span class="n">B</span><span class="p">[</span><span class="n">start</span><span class="p">:</span><span class="n">start</span><span class="o">+</span><span class="n">guess</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">iarr</span><span class="p">):</span>
                    <span class="k">return</span> <span class="bp">True</span>
            <span class="k">return</span> <span class="bp">False</span>

        <span class="n">lo</span><span class="p">,</span> <span class="n">hi</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">min</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">A</span><span class="p">),</span> <span class="nb">len</span><span class="p">(</span><span class="n">B</span><span class="p">))</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">while</span> <span class="n">lo</span> <span class="o">&lt;</span> <span class="n">hi</span><span class="p">:</span>
            <span class="n">mi</span> <span class="o">=</span> <span class="p">(</span><span class="n">lo</span> <span class="o">+</span> <span class="n">hi</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span>
            <span class="k">if</span> <span class="n">check</span><span class="p">(</span><span class="n">mi</span><span class="p">):</span>
                <span class="n">lo</span> <span class="o">=</span> <span class="n">mi</span> <span class="o">+</span> <span class="mi">1</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">hi</span> <span class="o">=</span> <span class="n">mi</span>
        <span class="k">return</span> <span class="n">lo</span> <span class="o">-</span> <span class="mi">1</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="nn">java.math.BigInteger</span><span class="o">;</span>

<span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kt">int</span> <span class="n">P</span> <span class="o">=</span> <span class="mi">113</span><span class="o">;</span>
    <span class="kt">int</span> <span class="n">MOD</span> <span class="o">=</span> <span class="mi">1_000_000_007</span><span class="o">;</span>
    <span class="kt">int</span> <span class="n">Pinv</span> <span class="o">=</span> <span class="n">BigInteger</span><span class="o">.</span><span class="na">valueOf</span><span class="o">(</span><span class="n">P</span><span class="o">).</span><span class="na">modInverse</span><span class="o">(</span><span class="n">BigInteger</span><span class="o">.</span><span class="na">valueOf</span><span class="o">(</span><span class="n">MOD</span><span class="o">)).</span><span class="na">intValue</span><span class="o">();</span>

    <span class="kd">private</span> <span class="kt">int</span><span class="o">[]</span> <span class="nf">rolling</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">source</span><span class="o">,</span> <span class="kt">int</span> <span class="n">length</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span><span class="o">[]</span> <span class="n">ans</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">source</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="n">length</span> <span class="o">+</span> <span class="mi">1</span><span class="o">];</span>
        <span class="kt">long</span> <span class="n">h</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">power</span> <span class="o">=</span> <span class="mi">1</span><span class="o">;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">length</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">source</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="o">++</span><span class="n">i</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">h</span> <span class="o">=</span> <span class="o">(</span><span class="n">h</span> <span class="o">+</span> <span class="n">source</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">*</span> <span class="n">power</span><span class="o">)</span> <span class="o">%</span> <span class="n">MOD</span><span class="o">;</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">i</span> <span class="o">&lt;</span> <span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">)</span> <span class="o">{</span>
                <span class="n">power</span> <span class="o">=</span> <span class="o">(</span><span class="n">power</span> <span class="o">*</span> <span class="n">P</span><span class="o">)</span> <span class="o">%</span> <span class="n">MOD</span><span class="o">;</span>
            <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
                <span class="n">ans</span><span class="o">[</span><span class="n">i</span> <span class="o">-</span> <span class="o">(</span><span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">)]</span> <span class="o">=</span> <span class="o">(</span><span class="kt">int</span><span class="o">)</span> <span class="n">h</span><span class="o">;</span>
                <span class="n">h</span> <span class="o">=</span> <span class="o">(</span><span class="n">h</span> <span class="o">-</span> <span class="n">source</span><span class="o">[</span><span class="n">i</span> <span class="o">-</span> <span class="o">(</span><span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">)])</span> <span class="o">*</span> <span class="n">Pinv</span> <span class="o">%</span> <span class="n">MOD</span><span class="o">;</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">h</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="n">h</span> <span class="o">+=</span> <span class="n">MOD</span><span class="o">;</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="kd">private</span> <span class="kt">boolean</span> <span class="nf">check</span><span class="o">(</span><span class="kt">int</span> <span class="n">guess</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">A</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">B</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">,</span> <span class="n">List</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;&gt;</span> <span class="n">hashes</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="kt">int</span> <span class="n">k</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">:</span> <span class="n">rolling</span><span class="o">(</span><span class="n">A</span><span class="o">,</span> <span class="n">guess</span><span class="o">))</span> <span class="o">{</span>
            <span class="n">hashes</span><span class="o">.</span><span class="na">computeIfAbsent</span><span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">z</span> <span class="o">-&gt;</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">()).</span><span class="na">add</span><span class="o">(</span><span class="n">k</span><span class="o">++);</span>
        <span class="o">}</span>
        <span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">x</span><span class="o">:</span> <span class="n">rolling</span><span class="o">(</span><span class="n">B</span><span class="o">,</span> <span class="n">guess</span><span class="o">))</span> <span class="o">{</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span><span class="o">:</span> <span class="n">hashes</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;()))</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">Arrays</span><span class="o">.</span><span class="na">equals</span><span class="o">(</span><span class="n">Arrays</span><span class="o">.</span><span class="na">copyOfRange</span><span class="o">(</span><span class="n">A</span><span class="o">,</span> <span class="n">i</span><span class="o">,</span> <span class="n">i</span><span class="o">+</span><span class="n">guess</span><span class="o">),</span>
                                  <span class="n">Arrays</span><span class="o">.</span><span class="na">copyOfRange</span><span class="o">(</span><span class="n">B</span><span class="o">,</span> <span class="n">j</span><span class="o">,</span> <span class="n">j</span><span class="o">+</span><span class="n">guess</span><span class="o">)))</span> <span class="o">{</span>
                    <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
                <span class="o">}</span>
            <span class="n">j</span><span class="o">++;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">findLength</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">A</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">B</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">lo</span> <span class="o">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">hi</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">A</span><span class="o">.</span><span class="na">length</span><span class="o">,</span> <span class="n">B</span><span class="o">.</span><span class="na">length</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">lo</span> <span class="o">&lt;</span> <span class="n">hi</span><span class="o">)</span> <span class="o">{</span>
            <span class="kt">int</span> <span class="n">mi</span> <span class="o">=</span> <span class="o">(</span><span class="n">lo</span> <span class="o">+</span> <span class="n">hi</span><span class="o">)</span> <span class="o">/</span> <span class="mi">2</span><span class="o">;</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">check</span><span class="o">(</span><span class="n">mi</span><span class="o">,</span> <span class="n">A</span><span class="o">,</span> <span class="n">B</span><span class="o">))</span> <span class="n">lo</span> <span class="o">=</span> <span class="n">mi</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
            <span class="k">else</span> <span class="n">hi</span> <span class="o">=</span> <span class="n">mi</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">lo</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O((M+N) * \log{(\min(M, N))})</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>A, B</code>.  The log factor is contributed by the binary search, while creating the rolling hashes is <script type="math/tex; mode=display">O(M + N)</script>.  The checks for duplicate hashes are <script type="math/tex; mode=display">O(1)</script>.  If we perform a naive check to make sure our answer is correct, it adds a factor of <script type="math/tex; mode=display">O(\min(M, N))</script> to our cost of <code>check</code>, which keeps the complexity the same.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M)</script>, the space used to store <code>hashes</code> and the subarrays in our final naive check.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Idea for Solution #2 by <a href="https://leetcode.com/stefanpochmann">@StefanPochmann</a>.</p>
          </div>
        
      </div>
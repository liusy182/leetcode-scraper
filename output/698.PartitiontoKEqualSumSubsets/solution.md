<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-search-by-constructing-subset-sums-accepted">Approach #1: Search by Constructing Subset Sums [Accepted]</a></li>
<li><a href="#approach-2-dynamic-programming-on-subsets-of-input-accepted">Approach #2: Dynamic Programming on Subsets of Input [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-search-by-constructing-subset-sums-accepted">Approach #1: Search by Constructing Subset Sums [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As even when <code>k = 2</code>, the problem is a "Subset Sum" problem which is known to be NP-hard, (and because the given input limits are low,) our solution will focus on exhaustive search.</p>
<p>A natural approach is to simulate the <code>k</code> groups (disjoint subsets of nums).  For each number in <code>nums</code>, we'll check whether putting it in the <code>i</code>-th group solves the problem.  We can check those possibilities by recursively searching.</p>
<p><strong>Algorithm</strong></p>
<p>Firstly, we know that each of the <code>k</code> group-sums must be equal to <code>target = sum(nums) / k</code>.  (If this quantity is not an integer, the task is impossible.)</p>
<p>For each number in <code>nums</code>, we could add it into one of <code>k</code> group-sums, as long as the group's sum would not exceed the <code>target</code>.  For each of these choices, we recursively search with one less number to consider in <code>nums</code>.  If we placed every number successfully, then our search was successful.</p>
<p>One important speedup is that we can ensure all the 0 values of each group occur at the end of the array <code>groups</code>, by enforcing <code>if (groups[i] == 0) break;</code>.  This greatly reduces repeated work - for example, in the first run of search, we will make only 1 recursive call, instead of <code>k</code>.  Actually, we could do better by skipping any repeated values of groups[i], but it isn't necessary.</p>
<p>Another speedup is we could sort the array <code>nums</code>, so that we try to place the largest elements first.  When the answer is true and involves subsets with a low size, this method of placing elements will consider these lower size subsets sooner.  We can also handle elements <code>nums[i] &gt;= target</code> appropriately.  These tricks are not necessary to solve the problem, but they are presented in the solutions below.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">canPartitionKSubsets</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nums</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
        <span class="n">target</span><span class="p">,</span> <span class="n">rem</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="n">nums</span><span class="p">),</span> <span class="n">k</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">rem</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>

        <span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="n">groups</span><span class="p">):</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">nums</span><span class="p">:</span> <span class="k">return</span> <span class="bp">True</span>
            <span class="n">v</span> <span class="o">=</span> <span class="n">nums</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">group</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">groups</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">group</span> <span class="o">+</span> <span class="n">v</span> <span class="o">&lt;=</span> <span class="n">target</span><span class="p">:</span>
                    <span class="n">groups</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+=</span> <span class="n">v</span>
                    <span class="k">if</span> <span class="n">search</span><span class="p">(</span><span class="n">groups</span><span class="p">):</span> <span class="k">return</span> <span class="bp">True</span>
                    <span class="n">groups</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">-=</span> <span class="n">v</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">group</span><span class="p">:</span> <span class="k">break</span>
            <span class="n">nums</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">v</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">False</span>

        <span class="n">nums</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">nums</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">target</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="k">while</span> <span class="n">nums</span> <span class="ow">and</span> <span class="n">nums</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="n">target</span><span class="p">:</span>
            <span class="n">nums</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
            <span class="n">k</span> <span class="o">-=</span> <span class="mi">1</span>

        <span class="k">return</span> <span class="n">search</span><span class="p">([</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">k</span><span class="p">)</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">search</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">groups</span><span class="o">,</span> <span class="kt">int</span> <span class="n">row</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">target</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">row</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
        <span class="kt">int</span> <span class="n">v</span> <span class="o">=</span> <span class="n">nums</span><span class="o">[</span><span class="n">row</span><span class="o">--];</span>
        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">groups</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">groups</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">+</span> <span class="n">v</span> <span class="o">&lt;=</span> <span class="n">target</span><span class="o">)</span> <span class="o">{</span>
                <span class="n">groups</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">+=</span> <span class="n">v</span><span class="o">;</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">search</span><span class="o">(</span><span class="n">groups</span><span class="o">,</span> <span class="n">row</span><span class="o">,</span> <span class="n">nums</span><span class="o">,</span> <span class="n">target</span><span class="o">))</span> <span class="k">return</span> <span class="kc">true</span><span class="o">;</span>
                <span class="n">groups</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">-=</span> <span class="n">v</span><span class="o">;</span>
            <span class="o">}</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">groups</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="k">break</span><span class="o">;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">canPartitionKSubsets</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">sum</span> <span class="o">=</span> <span class="n">Arrays</span><span class="o">.</span><span class="na">stream</span><span class="o">(</span><span class="n">nums</span><span class="o">).</span><span class="na">sum</span><span class="o">();</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">sum</span> <span class="o">%</span> <span class="n">k</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
        <span class="kt">int</span> <span class="n">target</span> <span class="o">=</span> <span class="n">sum</span> <span class="o">/</span> <span class="n">k</span><span class="o">;</span>

        <span class="n">Arrays</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">nums</span><span class="o">);</span>
        <span class="kt">int</span> <span class="n">row</span> <span class="o">=</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span> <span class="o">-</span> <span class="mi">1</span><span class="o">;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">nums</span><span class="o">[</span><span class="n">row</span><span class="o">]</span> <span class="o">&gt;</span> <span class="n">target</span><span class="o">)</span> <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">row</span> <span class="o">&gt;=</span> <span class="mi">0</span> <span class="o">&amp;&amp;</span> <span class="n">nums</span><span class="o">[</span><span class="n">row</span><span class="o">]</span> <span class="o">==</span> <span class="n">target</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">row</span><span class="o">--;</span>
            <span class="n">k</span><span class="o">--;</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">search</span><span class="o">(</span><span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="n">k</span><span class="o">],</span> <span class="n">row</span><span class="o">,</span> <span class="n">nums</span><span class="o">,</span> <span class="n">target</span><span class="o">);</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(k^{N-k} k!)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>, and <script type="math/tex; mode=display">k</script> is as given.  As we skip additional zeroes in <code>groups</code>, naively we will make <script type="math/tex; mode=display">O(k!)</script> calls to <code>search</code>, then an additional <script type="math/tex; mode=display">O(k^{N-k})</script> calls after every element of <code>groups</code> is nonzero.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by recursive calls to <code>search</code> in our call stack.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-on-subsets-of-input-accepted">Approach #2: Dynamic Programming on Subsets of Input [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in <em>Approach #1</em>, we investigate methods of exhaustive search, and find <code>target = sum(nums) / k</code> in the same way.</p>
<p>Let <code>used</code> have the <code>i</code>-th bit set if and only if <code>nums[i]</code> has already been used.  Our goal is to use <code>nums</code> in some order so that placing them into groups in that order will be valid. <code>search(used, ...)</code> will answer the question: can we partition unused elements of <code>nums[i]</code> appropriately?</p>
<p>This will depend on <code>todo</code>, the sum of the remaining unused elements, not crossing multiples of <code>target</code> within one number.  If for example our target is <code>10</code>, and our elements to be placed in order are <code>[6, 5, 5, 4]</code>, this would not work as <code>6 + 5</code> "crosses" <code>10</code> prematurely.</p>
<p>If we could choose the order, then after placing <code>5</code>, our unused elements are <code>[4, 5, 6]</code>.  Using <code>6</code> would make <code>todo</code> go from <code>15</code> to <code>9</code>, which crosses <code>10</code> - something unwanted.  However, we could use <code>5</code> since <code>todo</code> goes from <code>15</code> to <code>10</code>; then later we could use <code>4</code> and <code>6</code> as those placements do not cross.</p>
<p>It turns out the maximum value that can be chosen so as to not cross a multiple of <code>target</code>, is <code>targ = (todo - 1) % target + 1</code>.  This is essentially <code>todo % target</code>, plus <code>target</code> if that would be zero.</p>
<p>Now for each unused number that doesn't cross, we'll search on that state, and we'll return <code>true</code> if any of those searches are <code>true</code>.</p>
<p>Notice that the state <code>todo</code> depends only on the state <code>used</code>, so when memoizing our search, we only need to make lookups by <code>used</code>.</p>
<p>In the solutions below, we present both a top-down dynamic programming solution, and a bottom-up one.  The bottom-up solution uses a different notion of state.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">canPartitionKSubsets</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nums</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
        <span class="n">target</span><span class="p">,</span> <span class="n">rem</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="n">nums</span><span class="p">),</span> <span class="n">k</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">rem</span> <span class="ow">or</span> <span class="nb">max</span><span class="p">(</span><span class="n">nums</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">target</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>

        <span class="n">memo</span> <span class="o">=</span> <span class="p">[</span><span class="bp">None</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">nums</span><span class="p">))</span>
        <span class="n">memo</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="n">used</span><span class="p">,</span> <span class="n">todo</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">memo</span><span class="p">[</span><span class="n">used</span><span class="p">]</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
                <span class="n">targ</span> <span class="o">=</span> <span class="p">(</span><span class="n">todo</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="n">target</span> <span class="o">+</span> <span class="mi">1</span>
                <span class="n">memo</span><span class="p">[</span><span class="n">used</span><span class="p">]</span> <span class="o">=</span> <span class="nb">any</span><span class="p">(</span><span class="n">search</span><span class="p">(</span><span class="n">used</span> <span class="o">|</span> <span class="p">(</span><span class="mi">1</span><span class="o">&lt;&lt;</span><span class="n">i</span><span class="p">),</span> <span class="n">todo</span> <span class="o">-</span> <span class="n">num</span><span class="p">)</span>
                                 <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">num</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nums</span><span class="p">)</span>
                                 <span class="k">if</span> <span class="p">(</span><span class="n">used</span> <span class="o">&gt;&gt;</span> <span class="n">i</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mi">1</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">num</span> <span class="o">&lt;=</span> <span class="n">targ</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">memo</span><span class="p">[</span><span class="n">used</span><span class="p">]</span>

        <span class="k">return</span> <span class="n">search</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">target</span> <span class="o">*</span> <span class="n">k</span><span class="p">)</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">enum</span> <span class="n">Result</span> <span class="o">{</span> <span class="n">TRUE</span><span class="o">,</span> <span class="n">FALSE</span> <span class="o">}</span>

<span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kt">boolean</span> <span class="nf">search</span><span class="o">(</span><span class="kt">int</span> <span class="n">used</span><span class="o">,</span> <span class="kt">int</span> <span class="n">todo</span><span class="o">,</span> <span class="n">Result</span><span class="o">[]</span> <span class="n">memo</span><span class="o">,</span> <span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">target</span><span class="o">)</span> <span class="o">{</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">memo</span><span class="o">[</span><span class="n">used</span><span class="o">]</span> <span class="o">==</span> <span class="kc">null</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">memo</span><span class="o">[</span><span class="n">used</span><span class="o">]</span> <span class="o">=</span> <span class="n">Result</span><span class="o">.</span><span class="na">FALSE</span><span class="o">;</span>
            <span class="kt">int</span> <span class="n">targ</span> <span class="o">=</span> <span class="o">(</span><span class="n">todo</span> <span class="o">-</span> <span class="mi">1</span><span class="o">)</span> <span class="o">%</span> <span class="n">target</span> <span class="o">+</span> <span class="mi">1</span><span class="o">;</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
                <span class="k">if</span> <span class="o">((((</span><span class="n">used</span> <span class="o">&gt;&gt;</span> <span class="n">i</span><span class="o">)</span> <span class="o">&amp;</span> <span class="mi">1</span><span class="o">)</span> <span class="o">==</span> <span class="mi">0</span><span class="o">)</span> <span class="o">&amp;&amp;</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">&lt;=</span> <span class="n">targ</span><span class="o">)</span> <span class="o">{</span>
                    <span class="k">if</span> <span class="o">(</span><span class="n">search</span><span class="o">(</span><span class="n">used</span> <span class="o">|</span> <span class="o">(</span><span class="mi">1</span><span class="o">&lt;&lt;</span><span class="n">i</span><span class="o">),</span> <span class="n">todo</span> <span class="o">-</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">],</span> <span class="n">memo</span><span class="o">,</span> <span class="n">nums</span><span class="o">,</span> <span class="n">target</span><span class="o">))</span> <span class="o">{</span>
                        <span class="n">memo</span><span class="o">[</span><span class="n">used</span><span class="o">]</span> <span class="o">=</span> <span class="n">Result</span><span class="o">.</span><span class="na">TRUE</span><span class="o">;</span>
                        <span class="k">break</span><span class="o">;</span>
                    <span class="o">}</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">memo</span><span class="o">[</span><span class="n">used</span><span class="o">]</span> <span class="o">==</span> <span class="n">Result</span><span class="o">.</span><span class="na">TRUE</span><span class="o">;</span>
    <span class="o">}</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">canPartitionKSubsets</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">sum</span> <span class="o">=</span> <span class="n">Arrays</span><span class="o">.</span><span class="na">stream</span><span class="o">(</span><span class="n">nums</span><span class="o">).</span><span class="na">sum</span><span class="o">();</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">sum</span> <span class="o">%</span> <span class="n">k</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>

        <span class="n">Result</span><span class="o">[]</span> <span class="n">memo</span> <span class="o">=</span> <span class="k">new</span> <span class="n">Result</span><span class="o">[</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">];</span>
        <span class="n">memo</span><span class="o">[(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">)</span> <span class="o">-</span> <span class="mi">1</span><span class="o">]</span> <span class="o">=</span> <span class="n">Result</span><span class="o">.</span><span class="na">TRUE</span><span class="o">;</span>
        <span class="k">return</span> <span class="n">search</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">sum</span><span class="o">,</span> <span class="n">memo</span><span class="o">,</span> <span class="n">nums</span><span class="o">,</span> <span class="n">sum</span> <span class="o">/</span> <span class="n">k</span><span class="o">);</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><em>Bottom-Up Variation</em></p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">canPartitionKSubsets</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nums</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
        <span class="n">nums</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
        <span class="n">target</span><span class="p">,</span> <span class="n">rem</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="n">nums</span><span class="p">),</span> <span class="n">k</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">rem</span> <span class="ow">or</span> <span class="n">nums</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">target</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>

        <span class="n">dp</span> <span class="o">=</span> <span class="p">[</span><span class="bp">False</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">nums</span><span class="p">))</span>
        <span class="n">dp</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="n">total</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">nums</span><span class="p">))</span>

        <span class="k">for</span> <span class="n">state</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">nums</span><span class="p">)):</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">dp</span><span class="p">[</span><span class="n">state</span><span class="p">]:</span> <span class="k">continue</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">num</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">nums</span><span class="p">):</span>
                <span class="n">future</span> <span class="o">=</span> <span class="n">state</span> <span class="o">|</span> <span class="p">(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">i</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">state</span> <span class="o">!=</span> <span class="n">future</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">dp</span><span class="p">[</span><span class="n">future</span><span class="p">]:</span>
                    <span class="k">if</span> <span class="p">(</span><span class="n">num</span> <span class="o">&lt;=</span> <span class="n">target</span> <span class="o">-</span> <span class="p">(</span><span class="n">total</span><span class="p">[</span><span class="n">state</span><span class="p">]</span> <span class="o">%</span> <span class="n">target</span><span class="p">)):</span>
                        <span class="n">dp</span><span class="p">[</span><span class="n">future</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
                        <span class="n">total</span><span class="p">[</span><span class="n">future</span><span class="p">]</span> <span class="o">=</span> <span class="n">total</span><span class="p">[</span><span class="n">state</span><span class="p">]</span> <span class="o">+</span> <span class="n">num</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="k">break</span>
        <span class="k">return</span> <span class="n">dp</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">canPartitionKSubsets</span><span class="o">(</span><span class="kt">int</span><span class="o">[]</span> <span class="n">nums</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="kt">int</span> <span class="n">N</span> <span class="o">=</span> <span class="n">nums</span><span class="o">.</span><span class="na">length</span><span class="o">;</span>
        <span class="n">Arrays</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">nums</span><span class="o">);</span>
        <span class="kt">int</span> <span class="n">sum</span> <span class="o">=</span> <span class="n">Arrays</span><span class="o">.</span><span class="na">stream</span><span class="o">(</span><span class="n">nums</span><span class="o">).</span><span class="na">sum</span><span class="o">();</span>
        <span class="kt">int</span> <span class="n">target</span> <span class="o">=</span> <span class="n">sum</span> <span class="o">/</span> <span class="n">k</span><span class="o">;</span>
        <span class="k">if</span> <span class="o">(</span><span class="n">sum</span> <span class="o">%</span> <span class="n">k</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="o">||</span> <span class="n">nums</span><span class="o">[</span><span class="n">N</span> <span class="o">-</span> <span class="mi">1</span><span class="o">]</span> <span class="o">&gt;</span> <span class="n">target</span><span class="o">)</span> <span class="k">return</span> <span class="kc">false</span><span class="o">;</span>

        <span class="kt">boolean</span><span class="o">[]</span> <span class="n">dp</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">boolean</span><span class="o">[</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">N</span><span class="o">];</span>
        <span class="n">dp</span><span class="o">[</span><span class="mi">0</span><span class="o">]</span> <span class="o">=</span> <span class="kc">true</span><span class="o">;</span>
        <span class="kt">int</span><span class="o">[]</span> <span class="n">total</span> <span class="o">=</span> <span class="k">new</span> <span class="kt">int</span><span class="o">[</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">N</span><span class="o">];</span>

        <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">state</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">state</span> <span class="o">&lt;</span> <span class="o">(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">N</span><span class="o">);</span> <span class="n">state</span><span class="o">++)</span> <span class="o">{</span>
            <span class="k">if</span> <span class="o">(!</span><span class="n">dp</span><span class="o">[</span><span class="n">state</span><span class="o">])</span> <span class="k">continue</span><span class="o">;</span>
            <span class="k">for</span> <span class="o">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="o">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">N</span><span class="o">;</span> <span class="n">i</span><span class="o">++)</span> <span class="o">{</span>
                <span class="kt">int</span> <span class="n">future</span> <span class="o">=</span> <span class="n">state</span> <span class="o">|</span> <span class="o">(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">i</span><span class="o">);</span>
                <span class="k">if</span> <span class="o">(</span><span class="n">state</span> <span class="o">!=</span> <span class="n">future</span> <span class="o">&amp;&amp;</span> <span class="o">!</span><span class="n">dp</span><span class="o">[</span><span class="n">future</span><span class="o">])</span> <span class="o">{</span>
                    <span class="k">if</span> <span class="o">(</span><span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">]</span> <span class="o">&lt;=</span> <span class="n">target</span> <span class="o">-</span> <span class="o">(</span><span class="n">total</span><span class="o">[</span><span class="n">state</span><span class="o">]</span> <span class="o">%</span> <span class="n">target</span><span class="o">))</span> <span class="o">{</span>
                        <span class="n">dp</span><span class="o">[</span><span class="n">future</span><span class="o">]</span> <span class="o">=</span> <span class="kc">true</span><span class="o">;</span>
                        <span class="n">total</span><span class="o">[</span><span class="n">future</span><span class="o">]</span> <span class="o">=</span> <span class="n">total</span><span class="o">[</span><span class="n">state</span><span class="o">]</span> <span class="o">+</span> <span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">];</span>
                    <span class="o">}</span> <span class="k">else</span> <span class="o">{</span>
                        <span class="k">break</span><span class="o">;</span>
                    <span class="o">}</span>
                <span class="o">}</span>
            <span class="o">}</span>
        <span class="o">}</span>
        <span class="k">return</span> <span class="n">dp</span><span class="o">[(</span><span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="n">N</span><span class="o">)</span> <span class="o">-</span> <span class="mi">1</span><span class="o">];</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N * 2^N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  There are <script type="math/tex; mode=display">2^N</script> states of <code>used</code> (or <code>state</code> in our bottom-up variant), and each state performs <code>O(N)</code> work searching through <code>nums</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(2^N)</script>, the space used by <code>memo</code> (or <code>dp</code>, <code>total</code> in our bottom-up variant).</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-sorting-accepted">Approach #1: Sorting [Accepted]</a></li>
<li><a href="#approach-2-heap-accepted">Approach #2: Heap [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-sorting-accepted">Approach #1: Sorting [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Count the frequency of each word, and sort the words with a custom ordering relation that uses these frequencies.  Then take the best <code>k</code> of them.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">topKFrequent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
        <span class="n">count</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">Counter</span><span class="p">(</span><span class="n">words</span><span class="p">)</span>
        <span class="n">candidates</span> <span class="o">=</span> <span class="n">count</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
        <span class="n">candidates</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">w</span><span class="p">:</span> <span class="p">(</span><span class="o">-</span><span class="n">count</span><span class="p">[</span><span class="n">w</span><span class="p">],</span> <span class="n">w</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">candidates</span><span class="p">[:</span><span class="n">k</span><span class="p">]</span>
</pre></div>


<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="nf">topKFrequent</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">String</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">count</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">count</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">word</span><span class="o">,</span> <span class="n">count</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">word</span><span class="o">,</span> <span class="mi">0</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">candidates</span> <span class="o">=</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">(</span><span class="n">count</span><span class="o">.</span><span class="na">keySet</span><span class="o">());</span>
        <span class="n">Collections</span><span class="o">.</span><span class="na">sort</span><span class="o">(</span><span class="n">candidates</span><span class="o">,</span> <span class="o">(</span><span class="n">w1</span><span class="o">,</span> <span class="n">w2</span><span class="o">)</span> <span class="o">-&gt;</span> <span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w1</span><span class="o">).</span><span class="na">equals</span><span class="o">(</span><span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w2</span><span class="o">))</span> <span class="o">?</span>
                <span class="n">w1</span><span class="o">.</span><span class="na">compareTo</span><span class="o">(</span><span class="n">w2</span><span class="o">)</span> <span class="o">:</span> <span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w2</span><span class="o">)</span> <span class="o">-</span> <span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w1</span><span class="o">));</span>

        <span class="k">return</span> <span class="n">candidates</span><span class="o">.</span><span class="na">subList</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">k</span><span class="o">);</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N \log{N})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>words</code>.  We count the frequency of each word in <script type="math/tex; mode=display">O(N)</script> time, then we sort the given words in <script type="math/tex; mode=display">O(N \log{N})</script> time.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used to store our <code>candidates</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-heap-accepted">Approach #2: Heap [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Count the frequency of each word, then add it to heap that stores the best <code>k</code> candidates.  Here, "best" is defined with our custom ordering relation, which puts the worst candidates at the top of the heap.  At the end, we pop off the heap up to <code>k</code> times and reverse the result so that the best candidates are first.</p>
<p>In Python, we instead use <code>heapq.heapify</code>, which can turn a list into a heap in linear time, simplifying our work.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">Solution</span> <span class="o">{</span>
    <span class="kd">public</span> <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="nf">topKFrequent</span><span class="o">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">words</span><span class="o">,</span> <span class="kt">int</span> <span class="n">k</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Map</span><span class="o">&lt;</span><span class="n">String</span><span class="o">,</span> <span class="n">Integer</span><span class="o">&gt;</span> <span class="n">count</span> <span class="o">=</span> <span class="k">new</span> <span class="n">HashMap</span><span class="o">();</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">words</span><span class="o">)</span> <span class="o">{</span>
            <span class="n">count</span><span class="o">.</span><span class="na">put</span><span class="o">(</span><span class="n">word</span><span class="o">,</span> <span class="n">count</span><span class="o">.</span><span class="na">getOrDefault</span><span class="o">(</span><span class="n">word</span><span class="o">,</span> <span class="mi">0</span><span class="o">)</span> <span class="o">+</span> <span class="mi">1</span><span class="o">);</span>
        <span class="o">}</span>
        <span class="n">PriorityQueue</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">heap</span> <span class="o">=</span> <span class="k">new</span> <span class="n">PriorityQueue</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;(</span>
                <span class="o">(</span><span class="n">w1</span><span class="o">,</span> <span class="n">w2</span><span class="o">)</span> <span class="o">-&gt;</span> <span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w1</span><span class="o">).</span><span class="na">equals</span><span class="o">(</span><span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w2</span><span class="o">))</span> <span class="o">?</span>
                <span class="n">w2</span><span class="o">.</span><span class="na">compareTo</span><span class="o">(</span><span class="n">w1</span><span class="o">)</span> <span class="o">:</span> <span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w1</span><span class="o">)</span> <span class="o">-</span> <span class="n">count</span><span class="o">.</span><span class="na">get</span><span class="o">(</span><span class="n">w2</span><span class="o">)</span> <span class="o">);</span>

        <span class="k">for</span> <span class="o">(</span><span class="n">String</span> <span class="n">word</span><span class="o">:</span> <span class="n">count</span><span class="o">.</span><span class="na">keySet</span><span class="o">())</span> <span class="o">{</span>
            <span class="n">heap</span><span class="o">.</span><span class="na">offer</span><span class="o">(</span><span class="n">word</span><span class="o">);</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">heap</span><span class="o">.</span><span class="na">size</span><span class="o">()</span> <span class="o">&gt;</span> <span class="n">k</span><span class="o">)</span> <span class="n">heap</span><span class="o">.</span><span class="na">poll</span><span class="o">();</span>
        <span class="o">}</span>

        <span class="n">List</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span> <span class="n">ans</span> <span class="o">=</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">();</span>
        <span class="k">while</span> <span class="o">(!</span><span class="n">heap</span><span class="o">.</span><span class="na">isEmpty</span><span class="o">())</span> <span class="n">ans</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">heap</span><span class="o">.</span><span class="na">poll</span><span class="o">());</span>
        <span class="n">Collections</span><span class="o">.</span><span class="na">reverse</span><span class="o">(</span><span class="n">ans</span><span class="o">);</span>
        <span class="k">return</span> <span class="n">ans</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">Solution</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">topKFrequent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">words</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
        <span class="n">count</span> <span class="o">=</span> <span class="n">collections</span><span class="o">.</span><span class="n">Counter</span><span class="p">(</span><span class="n">words</span><span class="p">)</span>
        <span class="n">heap</span> <span class="o">=</span> <span class="p">[(</span><span class="o">-</span><span class="n">freq</span><span class="p">,</span> <span class="n">word</span><span class="p">)</span> <span class="k">for</span> <span class="n">word</span><span class="p">,</span> <span class="n">freq</span> <span class="ow">in</span> <span class="n">count</span><span class="o">.</span><span class="n">items</span><span class="p">()]</span>
        <span class="n">heapq</span><span class="o">.</span><span class="n">heapify</span><span class="p">(</span><span class="n">heap</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">heapq</span><span class="o">.</span><span class="n">heappop</span><span class="p">(</span><span class="n">heap</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="n">k</span><span class="p">)]</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N \log{k})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>words</code>.  We count the frequency of each word in <script type="math/tex; mode=display">O(N)</script> time, then we add <script type="math/tex; mode=display">N</script> words to the heap, each in <script type="math/tex; mode=display">O(\log {k})</script> time.  Finally, we pop from the heap up to <script type="math/tex; mode=display">k</script> times.  As <script type="math/tex; mode=display">k \leq N</script>, this is <script type="math/tex; mode=display">O(N \log{k})</script> in total.</li>
</ul>
<p>In Python, we improve this to <script type="math/tex; mode=display">O(N + k \log {N})</script>: our <code>heapq.heapify</code> operation and counting operations are <script type="math/tex; mode=display">O(N)</script>, and each of <script type="math/tex; mode=display">k</script>
<code>heapq.heappop</code> operations are <script type="math/tex; mode=display">O(\log {N})</script>.</p>
<ul>
<li>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used to store our <code>count</code>.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
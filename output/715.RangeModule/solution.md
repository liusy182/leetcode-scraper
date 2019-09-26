<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-maintain-sorted-disjoint-intervals-accepted">Approach #1: Maintain Sorted Disjoint Intervals [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-maintain-sorted-disjoint-intervals-accepted">Approach #1: Maintain Sorted Disjoint Intervals [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Because <code>left, right &lt; 10^9</code>, we need to deal with the coordinates abstractly.  Let's maintain some sorted structure of disjoint intervals.  These intervals will be closed (eg. we don't store <code>[[1, 2], [2, 3]]</code>; we would store <code>[[1, 3]]</code> instead.)</p>
<p>In this article, we will go over Python and Java versions separately, as the data structures available to us that are relevant to the problem are substantially different.</p>
<p><strong>Algorithm (Python)</strong></p>
<p>We will maintain the structure as a <em>list</em> <code>self.ranges = []</code>.  </p>
<p><em>Adding a Range</em></p>
<p>When we want to add a range, we first find the indices <code>i, j = self._bounds(left, right)</code> for which <code>self.ranges[i: j+1]</code> touches (in a closed sense - not halfopen) the given interval <code>[left, right]</code>.  We can find this in log time by making steps of size 100, 10, then 1 in our linear search from both sides.</p>
<p>Every interval touched by <code>[left, right]</code> will be replaced by the single interval <code>[min(left, self.ranges[i][0]), max(right, self.ranges[j][1])]</code>.</p>
<p><em>Removing a Range</em></p>
<p>Again, we use <code>i, j = self._bounds(...)</code> to only work in the relevant subset of <code>self.ranges</code> that is in the neighborhood of our given range <code>[left, right)</code>.  For each interval <code>[x, y)</code> from <code>self.ranges[i:j+1]</code>, we may have some subset of that interval to the left and/or right of <code>[left, right)</code>.  We replace our current interval <code>[x, y)</code> with those (up to 2) new intervals.</p>
<p><em>Querying a Range</em></p>
<p>As the intervals are sorted, we use binary search to find the single interval that could intersect <code>[left, right)</code>, then verify that it does.</p>
<p><strong>Python</strong></p>
<div class="codehilite"><pre><span></span><span class="k">class</span> <span class="nc">RangeModule</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">_bounds</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">):</span>
        <span class="n">i</span><span class="p">,</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
        <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">100</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">1</span><span class="p">):</span>
            <span class="k">while</span> <span class="n">i</span> <span class="o">+</span> <span class="n">d</span> <span class="o">-</span> <span class="mi">1</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="n">d</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">left</span><span class="p">:</span>
                <span class="n">i</span> <span class="o">+=</span> <span class="n">d</span>
            <span class="k">while</span> <span class="n">j</span> <span class="o">&gt;=</span> <span class="n">d</span> <span class="o">-</span> <span class="mi">1</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">j</span><span class="o">-</span><span class="n">d</span><span class="o">+</span><span class="mi">1</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">right</span><span class="p">:</span>
                <span class="n">j</span> <span class="o">-=</span> <span class="n">d</span>
        <span class="k">return</span> <span class="n">i</span><span class="p">,</span> <span class="n">j</span>

    <span class="k">def</span> <span class="nf">addRange</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">):</span>
        <span class="n">i</span><span class="p">,</span> <span class="n">j</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bounds</span><span class="p">(</span><span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;=</span> <span class="n">j</span><span class="p">:</span>
            <span class="n">left</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">left</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span>
            <span class="n">right</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">right</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">j</span><span class="p">][</span><span class="mi">1</span><span class="p">])</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="p">[(</span><span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">)]</span>

    <span class="k">def</span> <span class="nf">queryRange</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">):</span>
        <span class="n">i</span> <span class="o">=</span> <span class="n">bisect</span><span class="o">.</span><span class="n">bisect_left</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">,</span> <span class="p">(</span><span class="n">left</span><span class="p">,</span> <span class="nb">float</span><span class="p">(</span><span class="s1">'inf'</span><span class="p">)))</span>
        <span class="k">if</span> <span class="n">i</span><span class="p">:</span> <span class="n">i</span> <span class="o">-=</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">)</span> <span class="ow">and</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="n">left</span> <span class="ow">and</span>
                <span class="n">right</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="mi">1</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">removeRange</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">):</span>
        <span class="n">i</span><span class="p">,</span> <span class="n">j</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bounds</span><span class="p">(</span><span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">)</span>
        <span class="n">merge</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">):</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">k</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">left</span><span class="p">:</span>
                <span class="n">merge</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">k</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="n">left</span><span class="p">))</span>
            <span class="k">if</span> <span class="n">right</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">k</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
                <span class="n">merge</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">right</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">k</span><span class="p">][</span><span class="mi">1</span><span class="p">]))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">ranges</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">merge</span>
</pre></div>


<hr>
<p><strong>Algorithm (Java)</strong></p>
<p>We will maintain the structure as a <em>TreeSet</em> <code>ranges = new TreeSet&lt;Interval&gt;();</code>.  We introduce a new <em>Comparable</em> class <code>Interval</code> to represent our half-open intervals.  They compare by <em>right-most</em> coordinate as later we will see that it simplifies our work.  Also note that this ordering is consistent with equals, which is important when dealing with <em>Sets</em>.</p>
<p><em>Adding and Removing a Range</em></p>
<p>The basic structure of adding and removing a range is the same.  First, we must iterate over the relevant subset of <code>ranges</code>.  This is done using iterators so that we can <code>itr.remove</code> on the fly, and breaking when the intervals go too far to the right.</p>
<p>The critical logic of <code>addRange</code> is simply to make <code>left, right</code> the smallest and largest seen coordinates.  After, we add one giant interval representing the union of all intervals seen that touched <code>[left, right]</code>.</p>
<p>The logic of <code>removeRange</code> is to remember in <code>todo</code> the intervals we wanted to replace the removed interval with.  After, we can add them all back in.</p>
<p><em>Querying a Range</em></p>
<p>As the intervals are sorted, we search to find the single interval that could intersect <code>[left, right)</code>, then verify that it does.  As the TreeSet uses a balanced (red-black) tree, this has logarithmic complexity.</p>
<p><strong>Java</strong></p>
<div class="codehilite"><pre><span></span><span class="kd">class</span> <span class="nc">RangeModule</span> <span class="o">{</span>
    <span class="n">TreeSet</span><span class="o">&lt;</span><span class="n">Interval</span><span class="o">&gt;</span> <span class="n">ranges</span><span class="o">;</span>
    <span class="kd">public</span> <span class="nf">RangeModule</span><span class="o">()</span> <span class="o">{</span>
        <span class="n">ranges</span> <span class="o">=</span> <span class="k">new</span> <span class="n">TreeSet</span><span class="o">();</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">addRange</span><span class="o">(</span><span class="kt">int</span> <span class="n">left</span><span class="o">,</span> <span class="kt">int</span> <span class="n">right</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Iterator</span><span class="o">&lt;</span><span class="n">Interval</span><span class="o">&gt;</span> <span class="n">itr</span> <span class="o">=</span> <span class="n">ranges</span><span class="o">.</span><span class="na">tailSet</span><span class="o">(</span><span class="k">new</span> <span class="n">Interval</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">left</span> <span class="o">-</span> <span class="mi">1</span><span class="o">)).</span><span class="na">iterator</span><span class="o">();</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">itr</span><span class="o">.</span><span class="na">hasNext</span><span class="o">())</span> <span class="o">{</span>
            <span class="n">Interval</span> <span class="n">iv</span> <span class="o">=</span> <span class="n">itr</span><span class="o">.</span><span class="na">next</span><span class="o">();</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">right</span> <span class="o">&lt;</span> <span class="n">iv</span><span class="o">.</span><span class="na">left</span><span class="o">)</span> <span class="k">break</span><span class="o">;</span>
            <span class="n">left</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">min</span><span class="o">(</span><span class="n">left</span><span class="o">,</span> <span class="n">iv</span><span class="o">.</span><span class="na">left</span><span class="o">);</span>
            <span class="n">right</span> <span class="o">=</span> <span class="n">Math</span><span class="o">.</span><span class="na">max</span><span class="o">(</span><span class="n">right</span><span class="o">,</span> <span class="n">iv</span><span class="o">.</span><span class="na">right</span><span class="o">);</span>
            <span class="n">itr</span><span class="o">.</span><span class="na">remove</span><span class="o">();</span>
        <span class="o">}</span>
        <span class="n">ranges</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="k">new</span> <span class="n">Interval</span><span class="o">(</span><span class="n">left</span><span class="o">,</span> <span class="n">right</span><span class="o">));</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">boolean</span> <span class="nf">queryRange</span><span class="o">(</span><span class="kt">int</span> <span class="n">left</span><span class="o">,</span> <span class="kt">int</span> <span class="n">right</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Interval</span> <span class="n">iv</span> <span class="o">=</span> <span class="n">ranges</span><span class="o">.</span><span class="na">higher</span><span class="o">(</span><span class="k">new</span> <span class="n">Interval</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">left</span><span class="o">));</span>
        <span class="k">return</span> <span class="o">(</span><span class="n">iv</span> <span class="o">!=</span> <span class="kc">null</span> <span class="o">&amp;&amp;</span> <span class="n">iv</span><span class="o">.</span><span class="na">left</span> <span class="o">&lt;=</span> <span class="n">left</span> <span class="o">&amp;&amp;</span> <span class="n">right</span> <span class="o">&lt;=</span> <span class="n">iv</span><span class="o">.</span><span class="na">right</span><span class="o">);</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">removeRange</span><span class="o">(</span><span class="kt">int</span> <span class="n">left</span><span class="o">,</span> <span class="kt">int</span> <span class="n">right</span><span class="o">)</span> <span class="o">{</span>
        <span class="n">Iterator</span><span class="o">&lt;</span><span class="n">Interval</span><span class="o">&gt;</span> <span class="n">itr</span> <span class="o">=</span> <span class="n">ranges</span><span class="o">.</span><span class="na">tailSet</span><span class="o">(</span><span class="k">new</span> <span class="n">Interval</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">left</span><span class="o">)).</span><span class="na">iterator</span><span class="o">();</span>
        <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">Interval</span><span class="o">&gt;</span> <span class="n">todo</span> <span class="o">=</span> <span class="k">new</span> <span class="n">ArrayList</span><span class="o">();</span>
        <span class="k">while</span> <span class="o">(</span><span class="n">itr</span><span class="o">.</span><span class="na">hasNext</span><span class="o">())</span> <span class="o">{</span>
            <span class="n">Interval</span> <span class="n">iv</span> <span class="o">=</span> <span class="n">itr</span><span class="o">.</span><span class="na">next</span><span class="o">();</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">right</span> <span class="o">&lt;</span> <span class="n">iv</span><span class="o">.</span><span class="na">left</span><span class="o">)</span> <span class="k">break</span><span class="o">;</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">iv</span><span class="o">.</span><span class="na">left</span> <span class="o">&lt;</span> <span class="n">left</span><span class="o">)</span> <span class="n">todo</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="k">new</span> <span class="n">Interval</span><span class="o">(</span><span class="n">iv</span><span class="o">.</span><span class="na">left</span><span class="o">,</span> <span class="n">left</span><span class="o">));</span>
            <span class="k">if</span> <span class="o">(</span><span class="n">right</span> <span class="o">&lt;</span> <span class="n">iv</span><span class="o">.</span><span class="na">right</span><span class="o">)</span> <span class="n">todo</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="k">new</span> <span class="n">Interval</span><span class="o">(</span><span class="n">right</span><span class="o">,</span> <span class="n">iv</span><span class="o">.</span><span class="na">right</span><span class="o">));</span>
            <span class="n">itr</span><span class="o">.</span><span class="na">remove</span><span class="o">();</span>
        <span class="o">}</span>
        <span class="k">for</span> <span class="o">(</span><span class="n">Interval</span> <span class="n">iv</span><span class="o">:</span> <span class="n">todo</span><span class="o">)</span> <span class="n">ranges</span><span class="o">.</span><span class="na">add</span><span class="o">(</span><span class="n">iv</span><span class="o">);</span>
    <span class="o">}</span>
<span class="o">}</span>

<span class="kd">class</span> <span class="nc">Interval</span> <span class="kd">implements</span> <span class="n">Comparable</span><span class="o">&lt;</span><span class="n">Interval</span><span class="o">&gt;{</span>
    <span class="kt">int</span> <span class="n">left</span><span class="o">;</span>
    <span class="kt">int</span> <span class="n">right</span><span class="o">;</span>

    <span class="kd">public</span> <span class="nf">Interval</span><span class="o">(</span><span class="kt">int</span> <span class="n">left</span><span class="o">,</span> <span class="kt">int</span> <span class="n">right</span><span class="o">){</span>
        <span class="k">this</span><span class="o">.</span><span class="na">left</span> <span class="o">=</span> <span class="n">left</span><span class="o">;</span>
        <span class="k">this</span><span class="o">.</span><span class="na">right</span> <span class="o">=</span> <span class="n">right</span><span class="o">;</span>
    <span class="o">}</span>

    <span class="kd">public</span> <span class="kt">int</span> <span class="nf">compareTo</span><span class="o">(</span><span class="n">Interval</span> <span class="n">that</span><span class="o">){</span>
        <span class="k">if</span> <span class="o">(</span><span class="k">this</span><span class="o">.</span><span class="na">right</span> <span class="o">==</span> <span class="n">that</span><span class="o">.</span><span class="na">right</span><span class="o">)</span> <span class="k">return</span> <span class="k">this</span><span class="o">.</span><span class="na">left</span> <span class="o">-</span> <span class="n">that</span><span class="o">.</span><span class="na">left</span><span class="o">;</span>
        <span class="k">return</span> <span class="k">this</span><span class="o">.</span><span class="na">right</span> <span class="o">-</span> <span class="n">that</span><span class="o">.</span><span class="na">right</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span>
</pre></div>


<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: Let <script type="math/tex; mode=display">K</script> be the number of elements in <code>ranges</code>.  <code>addRange</code> and <code>removeRange</code> operations have <script type="math/tex; mode=display">O(K)</script> complexity.  <code>queryRange</code> has <script type="math/tex; mode=display">O(\log K)</script> complexity.  Because <code>addRange, removeRange</code> adds at most 1 interval at a time, you can bound these further.  For example, if there are <script type="math/tex; mode=display">A</script>
<code>addRange</code>, <script type="math/tex; mode=display">R</script>
<code>removeRange</code>, and <script type="math/tex; mode=display">Q</script>
<code>queryRange</code> number of operations respectively, we can express our complexity as <script type="math/tex; mode=display">O((A+R)^2 Q \log(A+R))</script>. </p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(A+R)</script>, the space used by <code>ranges</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
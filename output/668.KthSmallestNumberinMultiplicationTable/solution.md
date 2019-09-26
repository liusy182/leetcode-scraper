<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-memory-limit-exceeded">Approach #1: Brute Force [Memory Limit Exceeded]</a></li>
<li><a href="#approach-2-next-heap-time-limit-exceeded">Approach #2: Next Heap [Time Limit Exceeded]</a></li>
<li><a href="#approach-3-binary-search-accepted">Approach #3: Binary Search [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-memory-limit-exceeded">Approach #1: Brute Force [Memory Limit Exceeded]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Create the multiplication table and sort it, then take the <script type="math/tex; mode=display">k^{th}</script> element.</p>
<iframe src="https://leetcode.com/playground/JNTnTCLa/shared" frameborder="0" name="JNTnTCLa" width="100%" height="258"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(m*n)</script> to create the table, and <script type="math/tex; mode=display">O(m*n\log(m*n))</script> to sort it.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(m*n)</script> to store the table.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-next-heap-time-limit-exceeded">Approach #2: Next Heap [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>Maintain a heap of the smallest unused element of each row.  Then, finding the next element is a pop operation on the heap.</p>
<p><strong>Algorithm</strong></p>
<p>Our <code>heap</code> is going to consist of elements <script type="math/tex; mode=display">\text{(val, root)}</script>, where <script type="math/tex; mode=display">\text{val}</script> is the next unused value of that row, and <script type="math/tex; mode=display">\text{root}</script> was the starting value of that row.</p>
<p>We will repeatedly find the next lowest element in the table.  To do this, we pop from the heap.  Then, if there's a next lowest element in that row, we'll put that element back on the heap.</p>
<iframe src="https://leetcode.com/playground/Evrh9ssK/shared" frameborder="0" name="Evrh9ssK" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(k * m \log m) = O(m^2 n \log m)</script>.  Our initial heapify operation is <script type="math/tex; mode=display">O(m)</script>.  Afterwards, each pop and push is <script type="math/tex; mode=display">O(m \log m)</script>, and our outer loop is <script type="math/tex; mode=display">O(k) = O(m*n)</script>
</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(m)</script>.  Our heap is implemented as an array with <script type="math/tex; mode=display">m</script> elements.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-binary-search-accepted">Approach #3: Binary Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As <script type="math/tex; mode=display">\text{k}</script> and <script type="math/tex; mode=display">\text{m*n}</script> are up to <script type="math/tex; mode=display">9 * 10^8</script>, linear solutions will not work.  This motivates solutions with <script type="math/tex; mode=display">\log</script> complexity, such as binary search.</p>
<p><strong>Algorithm</strong></p>
<p>Let's do the binary search for the answer <script type="math/tex; mode=display">\text{A}</script>.</p>
<p>Say <code>enough(x)</code> is true if and only if there are <script type="math/tex; mode=display">\text{k}</script> or more values in the multiplication table that are less than or equal to <script type="math/tex; mode=display">\text{x}</script>.  Colloquially, <code>enough</code> describes whether <script type="math/tex; mode=display">\text{x}</script> is large enough to be the <script type="math/tex; mode=display">k^{th}</script> value in the multiplication table.</p>
<p>Then (for our answer <script type="math/tex; mode=display">\text{A}</script>), whenever <script type="math/tex; mode=display">\text{x &geq; A}</script>, <code>enough(x)</code> is <code>True</code>; and whenever <script type="math/tex; mode=display">\text{x < A}</script>, <code>enough(x)</code> is <code>False</code>.</p>
<p>In our binary search, our loop invariant is <code>enough(hi) = True</code>.  At the beginning, <code>enough(m*n) = True</code>, and whenever <code>hi</code> is set, it is set to a value that is "enough" (<code>enough(mi) = True</code>).  That means <code>hi</code> will be the lowest such value at the end of our binary search.</p>
<p>This leaves us with the task of counting how many values are less than or equal to <script type="math/tex; mode=display">\text{x}</script>.  For each of <script type="math/tex; mode=display">\text{m}</script> rows, the <script type="math/tex; mode=display">i^{th}</script> row looks like <script type="math/tex; mode=display">\text{[i, 2*i, 3*i, ..., n*i]}</script>.  The largest possible <script type="math/tex; mode=display">\text{k*i &leq; x}</script> that could appear is <script type="math/tex; mode=display">\text{k = x // i}</script>. However, if <script type="math/tex; mode=display">\text{x}</script> is really big, then perhaps <script type="math/tex; mode=display">\text{k > n}</script>, so in total there are <script type="math/tex; mode=display">\text{min(k, n) = min(x // i, n)}</script> values in that row that are less than or equal to <script type="math/tex; mode=display">\text{x}</script>.</p>
<p>After we have the count of how many values in the table are less than or equal to <script type="math/tex; mode=display">\text{x}</script>, by the definition of <code>enough(x)</code>, we want to know if that count is greater than or equal to <script type="math/tex; mode=display">\text{k}</script>.</p>
<iframe src="https://leetcode.com/playground/4ankdsg9/shared" frameborder="0" name="4ankdsg9" width="100%" height="377"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(m * \log (m*n))</script>.  Our binary search divides the interval <script type="math/tex; mode=display">\text{[lo, hi]}</script> into half at each step.  At each step, we call <code>enough</code> which requires <script type="math/tex; mode=display">O(m)</script> time.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.  We only keep integers in memory during our intermediate calculations.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>
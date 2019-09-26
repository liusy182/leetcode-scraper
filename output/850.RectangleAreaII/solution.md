<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-principle-of-inclusion-exclusion">Approach #1: Principle of Inclusion-Exclusion</a></li>
<li><a href="#approach-2-coordinate-compression">Approach #2: Coordinate Compression</a></li>
<li><a href="#approach-3-line-sweep">Approach #3: Line Sweep</a></li>
<li><a href="#approach-4-segment-tree">Approach #4: Segment Tree</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-principle-of-inclusion-exclusion">Approach #1: Principle of Inclusion-Exclusion</h4>
<p><strong>Intuition</strong></p>
<p>Say we have two rectangles, <script type="math/tex; mode=display">A</script> and <script type="math/tex; mode=display">B</script>.  The area of their union is:</p>
<p>
<script type="math/tex; mode=display">
|A \cup B| = |A| + |B| - |A \cap B|
</script>
</p>
<p>Say we have three rectangles, <script type="math/tex; mode=display">A, B, C</script>.  The area of their union is:</p>
<p>
<script type="math/tex; mode=display">
|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|
</script>
</p>
<p>This can be seen by drawing a Venn diagram.</p>
<p>Say we have four rectangles, <script type="math/tex; mode=display">A, B, C, D</script>.  The area of their union is:</p>
<p>
<script type="math/tex; mode=display">
\begin{align}
|A \cup B \cup C \cup D| =\,&\left( |A| + |B| + |C| + |D| \right) - \\
\,&\left(|A \cap B| + |A \cap C| + |A \cap D| + |B \cap C| + |B \cap D| + |C \cap D|\right) +\\
\,&\left(|A \cap B \cap C| + |A \cap B \cap D| + |A \cap C \cap D| + |B \cap C \cap D|\right) -\\
\,&\left(|A \cap B \cap C \cap D|\right)
\end{align}
</script>
</p>
<p>In general, the area of the union of <script type="math/tex; mode=display">n</script> rectangles <script type="math/tex; mode=display">A_1, A_2, \cdots , A_n</script> will be:</p>
<p>
<script type="math/tex; mode=display">
\bigg|\bigcup_{i=1}^n A_i\bigg| = \sum_{\emptyset \neq S \subseteq [n]} (-1)^{|S| + 1} \bigg| \bigcap_{i \in S} A_i \bigg|
</script>
</p>
<p><strong>Algorithm</strong></p>
<p>If we do not know the above fact, we can prove it by considering any point in <script type="math/tex; mode=display">\bigg|\bigcup_{i=1}^n A_i\bigg|</script>.  Say this point occurs in all <script type="math/tex; mode=display">A_i (i \in S)</script>, and let <script type="math/tex; mode=display">|S| = n</script>.  Then on the right side, it is counted <script type="math/tex; mode=display">\binom{n}{1} - \binom{n}{2} + \binom{n}{3} - \cdots \pm \binom{n}{n}</script> times.  By considering the binomial expansion of <script type="math/tex; mode=display">(1 - 1)^n</script>, this is in fact equal to <script type="math/tex; mode=display">1</script>.</p>
<p>From <em>Rectangle Area I</em>, we know that the intersection of two axis-aligned rectangles is another axis-aligned rectangle (or nothing).  So in particular, the intersection <script type="math/tex; mode=display">\bigcap_{i \in S} A_i</script> is always a rectangle (or nothing).</p>
<p>Now our algorithm proceeds as follows:  for every subset <script type="math/tex; mode=display">S</script> of <script type="math/tex; mode=display">\{1, 2, 3, \cdots, N\}</script> (where <script type="math/tex; mode=display">N</script> is the number of rectangles), we'll calculate the intersection of the rectangles in that subset <script type="math/tex; mode=display">\bigcap_{i \in S} A_i</script>, and then the area of that rectangle.  This allows us to calculate algorithmically the right-hand side of the general equation we wrote earlier.</p>
<iframe src="https://leetcode.com/playground/LVWa7ckv/shared" frameborder="0" width="100%" height="500" name="LVWa7ckv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N * 2^N)</script>, where <script type="math/tex; mode=display">N</script> is the number of rectangles.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-coordinate-compression">Approach #2: Coordinate Compression</h4>
<p><strong>Intuition</strong></p>
<p></p><center>
    <img src="../Figures/850/example.png" alt="Image from problem description" style="height: 200px;">
</center>
<p>Suppose instead of <code>rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]</code>, we had <code>[[0,0,200,200],[100,0,200,300],[100,0,300,100]]</code>.  The answer would just be 100 times bigger.</p>
<p>What about if <code>rectangles = [[0,0,2,2],[1,0,2,3],[1,0,30002,1]]</code> ?  Only the blue region would have area <code>30000</code> instead of <code>1</code>.</p>
<p>Our idea is this: we'll take all the <code>x</code> and <code>y</code> coordinates, and re-map them to <code>0, 1, 2, ...</code> etc.  For example, if <code>rectangles  = [[0,0,200,200],[100,0,200,300],[100,0,300,100]]</code>, we could re-map it to <code>[[0,0,2,2],[1,0,2,3],[1,0,3,1]]</code>.  Then, we can solve the problem with brute force.  However, each region may actually represent some larger area, so we'll need to adjust for that at the end.</p>
<p><strong>Algorithm</strong></p>
<p>Re-map each <code>x</code> coordinate to <code>0, 1, 2, ...</code>.  Independently, re-map all <code>y</code> coordinates too.</p>
<p>We then have a problem that can be solved by brute force: for each rectangle with re-mapped coordinates <code>(rx1, ry1, rx2, ry2)</code>, we can fill the grid <code>grid[x][y] = True</code> for <code>rx1 &lt;= x &lt; rx2</code> and <code>ry1 &lt;= y &lt; ry2</code>.</p>
<p>Afterwards, each <code>grid[rx][ry]</code> represents the area <code>(imapx(rx+1) - imapx(rx)) * (imapy(ry+1) - imapy(ry))</code>, where if <code>x</code> got remapped to <code>rx</code>, then <code>imapx(rx) = x</code> ("inverse-map-x of remapped-x equals x"), and similarly for <code>imapy</code>.</p>
<iframe src="https://leetcode.com/playground/hp6mu9MY/shared" frameborder="0" width="100%" height="500" name="hp6mu9MY"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the number of rectangles.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N^2)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-line-sweep">Approach #3: Line Sweep</h4>
<p><strong>Intuition</strong></p>
<p>Imagine we pass a horizontal line from bottom to top over the shape.  We have some active intervals on this horizontal line, which gets updated twice for each rectangle.  In total, there are <script type="math/tex; mode=display">2 * N</script> events, and we can update our (up to <script type="math/tex; mode=display">N</script>) active horizontal intervals for each update.</p>
<p><strong>Algorithm</strong></p>
<p>For a rectangle like <code>rec = [1,0,3,1]</code>, the first update is to add <code>[1, 3]</code> to the active set at <code>y = 0</code>, and the second update is to remove <code>[1, 3]</code> at <code>y = 1</code>.  Note that adding and removing respects multiplicity - if we also added <code>[0, 2]</code> at <code>y = 0</code>, then removing <code>[1, 3]</code> at <code>y = 1</code> will still leave us with <code>[0, 2]</code> active.</p>
<p>This gives us a plan: create these two events for each rectangle, then process all the events in sorted order of <code>y</code>.  The issue now is deciding how to process the events <code>add(x1, x2)</code> and <code>remove(x1, x2)</code> such that we are able to <code>query()</code> the total horizontal length of our active intervals.</p>
<p>We can use the fact that our <code>remove(...)</code> operation will always be on an interval that was previously added.  Let's store all the <code>(x1, x2)</code> intervals in sorted order.  Then, we can <code>query()</code> in linear time using a technique similar to a classic LeetCode problem, <a href="https://leetcode.com/problems/merge-intervals/">Merge Intervals</a>.</p>
<iframe src="https://leetcode.com/playground/vyrMx2Y9/shared" frameborder="0" width="100%" height="500" name="vyrMx2Y9"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2 \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of rectangles.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-segment-tree">Approach #4: Segment Tree</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in <em>Approach #3</em>, we want to support <code>add(x1, x2)</code>, <code>remove(x1, x2)</code>, and <code>query()</code>.  While outside the scope of a typical interview, this is the perfect setting for using a <em>segment tree</em>.  For completeness, we include the following implementation.</p>
<p>You can learn more about Segment Trees by visiting the articles of these problems: <a href="https://leetcode.com/problems/falling-squares/">Falling Squares</a>, <a href="https://leetcode.com/problems/number-of-longest-increasing-subsequence/">Number of Longest Increasing Subsequence</a>.</p>
<iframe src="https://leetcode.com/playground/MmabC4t6/shared" frameborder="0" width="100%" height="500" name="MmabC4t6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of rectangles.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Idea for Solution #4 by <a href="https://leetcode.com/lee215">@lee215</a>.</p>
          </div>
        
      </div>
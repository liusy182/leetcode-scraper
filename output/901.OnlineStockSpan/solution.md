<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-stack">Approach 1: Stack</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-stack">Approach 1: Stack</h4>
<p><strong>Intuition</strong></p>
<p>Clearly, we need to focus on how to make each query faster than a linear scan.  In a typical case, we get a new element like <code>7</code>, and there are some previous elements like <code>11, 3, 9, 5, 6, 4</code>.  Let's try to create some relationship between this query and the next query.</p>
<p>If (after getting <code>7</code>) we get an element like <code>2</code>, then the answer is <code>1</code>.  So in general, whenever we get a smaller element, the answer is 1.</p>
<p>If we get an element like <code>8</code>, the answer is 1 plus the previous answer (for <code>7</code>), as the <code>8</code> "stops" on the same value that <code>7</code> does (namely, <code>9</code>).</p>
<p>If we get an element like <code>10</code>, the answer is 1 plus the previous answer, plus the answer for <code>9</code>.</p>
<p>Notice throughout this evaluation, we only care about elements that occur in increasing order - we "shortcut" to them.  That is, from adding an element like <code>10</code>, we cut to <code>7</code> [with "weight" 4], then to <code>9</code> [with weight 2], then cut to <code>11</code> [with weight 1].</p>
<p>A stack is the ideal data structure to maintain what we care about efficiently.</p>
<p><strong>Algorithm</strong></p>
<p>Let's maintain a weighted stack of decreasing elements.  The size of the weight will be the total number of elements skipped.  For example, <code>11, 3, 9, 5, 6, 4, 7</code> will be <code>(11, weight=1), (9, weight=2), (7, weight=4)</code>.</p>
<p>When we get a new element like <code>10</code>, this helps us count the previous values faster by popping weighted elements off the stack.  The new stack at the end will look like <code>(11, weight=1), (10, weight=7)</code>.</p>
<iframe src="https://leetcode.com/playground/5aJytT6D/shared" frameborder="0" width="100%" height="395" name="5aJytT6D"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(Q)</script>, where <script type="math/tex; mode=display">Q</script> is the number of calls to <code>StockSpanner.next</code>.  In total, there are <script type="math/tex; mode=display">Q</script> pushes to the stack, and at most <script type="math/tex; mode=display">Q</script> pops.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(Q)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
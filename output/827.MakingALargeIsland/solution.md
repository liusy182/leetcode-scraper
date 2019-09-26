<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-naive-depth-first-search-time-limit-exceeded">Approach #1: (Naive) Depth First Search [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-component-sizes-accepted">Approach #2: Component Sizes [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-naive-depth-first-search-time-limit-exceeded">Approach #1: (Naive) Depth First Search [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>For each <code>0</code> in the grid, let's temporarily change it to a <code>1</code>, then count the size of the group from that square.</p>
<p><strong>Algorithm</strong></p>
<p>For each <code>0</code>, change it to a <code>1</code>, then do a depth first search to find the size of that component.  The answer is the maximum size component found.</p>
<p>Of course, if there is no <code>0</code> in the grid, then the answer is the size of the whole grid.</p>
<iframe src="https://leetcode.com/playground/T2PdhCGT/shared" frameborder="0" width="100%" height="500" name="T2PdhCGT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^4)</script>, where <script type="math/tex; mode=display">N</script> is the length and width of the <code>grid</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the additional space used in the depth first search by <code>stack</code> and <code>seen</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-component-sizes-accepted">Approach #2: Component Sizes [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>As in the previous solution, we check every <code>0</code>.  However, we also store the size of each group, so that we do not have to use depth-first search to repeatedly calculate the same size.</p>
<p>However, this idea fails when the <code>0</code> touches the same group.  For example, consider <code>grid = [[0,1],[1,1]]</code>.  The answer is <code>4</code>, not <code>1 + 3 + 3</code>, since the right neighbor and the bottom neighbor of the <code>0</code> belong to the same group.</p>
<p>We can remedy this problem by keeping track of a group id (or index), that is unique for each group.  Then, we'll only add areas of neighboring groups with different ids.</p>
<p><strong>Algorithm</strong></p>
<p>For each group, fill it with value <code>index</code> and remember it's size as <code>area[index] = dfs(...)</code>.</p>
<p>Then for each <code>0</code>, look at the neighboring group ids <code>seen</code> and add the area of those groups, plus 1 for the <code>0</code> we are toggling.  This gives us a candidate answer, and we take the maximum.</p>
<p>To solve the issue of having potentially no <code>0</code>, we take the maximum of the previously calculated areas.</p>
<iframe src="https://leetcode.com/playground/ZBn4MTj4/shared" frameborder="0" width="100%" height="500" name="ZBn4MTj4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length and width of the <code>grid</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the additional space used in the depth first search by <code>area</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Idea for Solution #2 by <a href="https://leetcode.com/lee215">@lee215</a>.</p>
          </div>
        
      </div>
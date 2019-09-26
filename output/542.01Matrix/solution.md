<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-using-bfs-accepted">Approach #2 Using BFS [Accepted]</a></li>
<li><a href="#approach-3-dp-approach-accepted">Approach #3 DP Approach [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>Do what the question says.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize <code>dist[i][j]=INT_MAX</code> for all <code>{i,j}</code> cells.</li>
<li>Iterate over the matrix.</li>
<li>If cell is <code>0</code>, <code>dist[i][j]=0</code>,</li>
<li>Else, for each <code>1</code> cell,<ul>
<li>Iterate over the entire matrix</li>
<li>If the cell is <code>0</code>, calculate its distance from current cell as <code>abs(k-i)+abs(l-j)</code>.</li>
<li>If the distance is smaller than the current distance, update it.</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/WrxDXrW3/shared" frameborder="0" name="WrxDXrW3" width="100%" height="445"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O((r \cdot c)^2)</script>.
Iterating over the entire matrix for each <code>1</code> in the matrix.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(r \cdot c)</script>.
No extra space required than the <code>vector&lt;vector&lt;int&gt; &gt; dist</code></p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-bfs-accepted">Approach #2 Using BFS [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p><em>A better brute force</em>:
Looking over the entire matrix appears wasteful and hence, we can use Breadth First Search(BFS) to limit the search to the nearest <code>0</code> found for each <code>1</code>. As soon as a <code>0</code> appears during the BFS, we know that the <code>0</code> is nearest, and hence, we move to the next <code>1</code>.</p>
<p><em>Think again</em>:
But, in this approach, we will only be able to update the distance of one <code>1</code> using one BFS, which could in fact, result in slightly higher complexity than the Approach #1 brute force.
But hey,this could be optimised if we start the BFS from <code>0</code>s and thereby, updating the distances of all the <code>1</code>s in the path.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>For our BFS routine, we keep a queue, <code>q</code> to maintain the queue of cells to be examined next.</li>
<li>We start by adding all the cells with <code>0</code>s to <code>q</code>.</li>
<li>Intially, distance for each <code>0</code> cell is <code>0</code> and distance for each <code>1</code> is <code>INT_MAX</code>, which is updated during the BFS.</li>
<li>Pop the cell from queue, and examine its neighbours. If the new calculated distance for neighbour <code>{i,j}</code> is smaller, we add <code>{i,j}</code> to <code>q</code> and update <code>dist[i][j]</code>.</li>
</ul>
<iframe src="https://leetcode.com/playground/abTJGHUf/shared" frameborder="0" name="abTJGHUf" width="100%" height="515"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(r \cdot c)</script>.</li>
<li>
<p>Since, the new cells are added to the queue only if their current distance is greater than the calculated distance, cells are not likely to be added multiple times.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(r \cdot c)</script>. Additional <script type="math/tex; mode=display">O(r \cdot c)</script> for queue than in Approach #1</p>
</li>
</ul>
<hr>
<h4 id="approach-3-dp-approach-accepted">Approach #3 DP Approach [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The distance of a cell from <code>0</code> can be calculated if we know the nearest distance for all the neighbours, in which case the distance is minimum distance of any neightbour + 1. And, instantly, the word come to mind DP!!<br>
For each <code>1</code>, the minimum path to <code>0</code> can be in any direction. So, we need to check all the 4 direction. In one iteration from top to bottom, we can check left and top directions, and we need another iteration from bottom to top to check for right and bottom direction.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Iterate the matrix from top to bottom-left to right:</li>
<li>Update
  <script type="math/tex; mode=display">\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j-1],\text{dist}[i-1][j])+1)</script>
  i.e., minimum of the current dist and distance from top or left neighbour +1, that would have been already calculated previously in the current iteration.</li>
<li>Now, we need to do the back iteration in the similar manner: from bottom to top-right to left:</li>
<li>Update
  <script type="math/tex; mode=display">\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j+1],\text{dist}[i+1][j])+1)</script>
  i.e. minimum of current dist and distances calculated from bottom and right neighbours, that would be already available in current iteration.</li>
</ul>
<iframe src="https://leetcode.com/playground/ZLQD7VF7/shared" frameborder="0" name="ZLQD7VF7" width="100%" height="515"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(r \cdot c)</script>. 2 passes of <script type="math/tex; mode=display">r \cdot c</script> each</li>
<li>Space complexity: <script type="math/tex; mode=display">O(r \cdot c)</script>. No additional space required than <code>dist vector&lt;vector&lt;int&gt; &gt;</code></li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/abhinavbansal0">@abhinavbansal0</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-dynamic-programming-accepted">Approach #1: Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>First, we can simplify all the numbers by dividing by 25.  More specifically, each unit is 25ml, and partial quantities of 25ml are rounded up to a full quantity.</p>
<p>When <code>N</code> is small, this is a relatively straightforward dynamic programming problem: we have quantities of soup represented by the state <code>(x, y)</code>, and we can either go to <code>(x-4, y-0)</code>, <code>(x-3, y-1)</code>, <code>(x-2, y-2)</code>, or <code>(x-1, y-3)</code> each with equal probability.  </p>
<p>When <code>N</code> is very large, this approach fails, so we need a different idea.</p>
<p>Instead of serving in batches of <code>(4, 0), (3, 1), (2, 2), (1, 3)</code>, pretend we serve <code>(1, 0)</code> on the side first, and then serve from the fair distribution <code>(3, 0), (2, 1), (1, 2), (0, 3)</code>.  If the pots of soup initially start at <code>(N, N)</code>, then after roughly less than <code>N/2</code> servings, one pot will still have soup.  Because of the <code>(1, 0)</code> servings on the side, this means that roughly speaking, pot <code>A</code> is used first if we serve <code>N/2</code> fairly from the first pot before <code>N</code> from the second pot.</p>
<p>When <code>N</code> is very large, this almost always happens (better than 99.9999%, so we can output 1), and we can check this either experimentally or mathematically.</p>
<p><strong>Algorithm</strong></p>
<p>We convert all units by dividing by 25 and rounding up.  If <code>N &gt;= 500</code> (in new units), then by the above argument the answer is <code>1</code>.</p>
<p>Otherwise, we will perform a dynamic programming algorithm to find the answer.  Our Java implementation showcases a "bottom-up" approach, that fills <code>memo</code> diagonally from top left to bottom right, where <code>s = i + j</code> is the sum of the indices.  Our Python implemtation showcases a "top-down" approach that uses memoization.</p>
<iframe src="https://leetcode.com/playground/aS5JpTPa/shared" frameborder="0" width="100%" height="497" name="aS5JpTPa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(1)</script>.  (There exists a constant <code>C</code> such that the algorithm never performs more than <code>C</code> steps.)</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.  (There exists a constant <code>C</code> such that the algorithm never uses more than <code>C</code> space.)</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
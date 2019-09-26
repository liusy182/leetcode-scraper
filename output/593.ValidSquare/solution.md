<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</a></li>
<li><a href="#approach-2-using-sorting-accepted">Approach #2 Using Sorting [Accepted]</a></li>
<li><a href="#approach-3-checking-every-case-accepted">Approach #3 Checking every case [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</h4>
<p>The idea behind determining whether 4 given set of points constitute a valid square or not is really simple. Firstly, we need to determine if the sides of the qaudrilateral formed by these 4 points are equal. But checking only this won't suffice. Since, this condition will be satisfied even in the case of a rhombus, where all the four sides are equal but the adjacent sides aren't perpendicular to each other. Thus, we also need to check if the lengths of the diagonals formed between the corners of the quadrilateral are equal. If both the conditions are satisfied, then only the given set of points can be deemed appropriate for constituting a square.</p>
<p>Now, the problem arises in determining which pairs of points act as the adjacent points on the square boundary. So, the simplest method is to consider every possible case. For the given 4 points, <script type="math/tex; mode=display">[p_0, p_1, p_2, p_3]</script>, there are a total of 4! ways in which these points can be arranged to be considered as the square's boundaries. We can generate every possible permutation and check if any permutation leads to the valid square arrangement of points.</p>
<iframe src="https://leetcode.com/playground/kR62YSDY/shared" frameborder="0" name="kR62YSDY" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>. Constant number of permutations(<script type="math/tex; mode=display">4!</script>) are generated.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is required.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-sorting-accepted">Approach #2 Using Sorting [Accepted]</h4>
<p>Instead of considering all the permutations of arrangements possible, we can make use of maths to simplify this problem a bit. If we sort the given set of points based on their x-coordinate values, and in the case of a tie, based on their y-coordinate value, we can obtain an arrangement, which directly reflects the arrangement of points on a valid square boundary possible.</p>
<p>Consider the only possible cases as shown in the figure below:</p>
<p><img alt="Valid_Square" src="../Figures/593_Valid_Square_1.PNG"></p>
<p>In each case, after sorting, we obtain the following conclusion regarding the connections of the points:</p>
<ol>
<li>
<p>
<script type="math/tex; mode=display">p_0p_1</script>, <script type="math/tex; mode=display">p_1p_3</script>, <script type="math/tex; mode=display">p_3p_2</script> and <script type="math/tex; mode=display">p_2p_0</script> form the four sides of any valid square.</p>
</li>
<li>
<p>
<script type="math/tex; mode=display">p_0p_3</script> and <script type="math/tex; mode=display">p_1p_2</script> form the diagonals of the square.</p>
</li>
</ol>
<p>Thus, once the sorting of the points is done, based on the above knowledge, we can directly compare <script type="math/tex; mode=display">p_0p_1</script>, <script type="math/tex; mode=display">p_1p_3</script>, <script type="math/tex; mode=display">p_3p_2</script> and <script type="math/tex; mode=display">p_2p_0</script> for equality of lengths(corresponding to the sides); and <script type="math/tex; mode=display">p_0p_3</script> and <script type="math/tex; mode=display">p_1p_2</script> for equality of lengths(corresponding to the diagonals).</p>
<iframe src="https://leetcode.com/playground/xp6gv2NM/shared" frameborder="0" name="xp6gv2NM" width="100%" height="241"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>. Sorting 4 points takes constant time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is required.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-checking-every-case-accepted">Approach #3 Checking every case [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>If we consider all the permutations descripting the arrangement of points as in the brute force approach, we can come up with the following set of 24 arrangements:</p>
<p><img alt="Valid_Square" src="../Figures/593_Valid_Square_2.PNG"></p>
<p>In this figure, the rows with the same shaded color indicate that the corresponding arrangements lead to the same set of edges and diagonals. Thus, we can see that only three unique cases exist. Thus, instead of generating all the 24 permutations, we check for the equality of edges and diagonals for only the three distinct cases.</p>
<iframe src="https://leetcode.com/playground/7wt6ZUJR/shared" frameborder="0" name="7wt6ZUJR" width="100%" height="258"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>. A fixed number of comparisons are done.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No extra space required.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
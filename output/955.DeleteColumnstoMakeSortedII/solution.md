<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-greedy">Approach 1: Greedy</a></li>
<li><a href="#approach-2-greedy-with-optimizations">Approach 2: Greedy with Optimizations</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-greedy">Approach 1: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>Instead of thinking about column deletions, let's think about which columns we will keep in the final answer.</p>
<p>If the first column isn't lexicographically sorted, we have to delete it.</p>
<p>Otherwise, we will argue that we can keep this first column without consequence.  There are two cases:</p>
<ul>
<li>
<p>If we don't keep the first column, then the final rows of the answer all have to be sorted.</p>
</li>
<li>
<p>If we do keep the first column, then the final rows of the answer (minus the first column) only have to be sorted if they share the same first letter (coming from the first column).</p>
</li>
</ul>
<p>The above statement is hard to digest, so let's use an example:</p>
<p>Say we have <code>A = ["axx","ayy","baa","bbb","bcc"]</code>.  When we keep the first column, the final rows are <code>R = ["xx","yy","aa","bb","cc"]</code>, and instead of the requirement that these all have to be sorted (ie. <code>R[0] &lt;= R[1] &lt;= R[2] &lt;= R[3] &lt;= R[4]</code>), we have a weaker requirement that they only have to be sorted if they share the same first letter of the first column, (ie. <code>R[0] &lt;= R[1] and R[2] &lt;= R[3] &lt;= R[4]</code>).</p>
<p>Now, we applied this argument only for the first column, but it actually works for every column we could consider taking.  If we can't take a column, we have to delete it.  Otherwise, we take it because it can only make adding subsequent columns easier.</p>
<p><strong>Algorithm</strong></p>
<p>All our effort has led us to a simple algorithmic idea.</p>
<p>Start with no columns kept.  For each column, if we could keep it and have a valid answer, keep it - otherwise delete it.</p>
<iframe src="https://leetcode.com/playground/VebVmQZ4/shared" frameborder="0" width="100%" height="500" name="VebVmQZ4"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NW^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">W</script> is the length of <code>A[i]</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(NW)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy-with-optimizations">Approach 2: Greedy with Optimizations</h4>
<p><strong>Explanation</strong></p>
<p>It is also possible to implement the solution in <em>Approach 1</em> without using as much time and space.</p>
<p>The key idea is that we will record the "cuts" that each column makes.  In our first example from <em>Approach 1</em> with <code>A = ["axx","ayy","baa","bbb","bcc"]</code> (and <code>R</code> defined as in Approach 1), the first column cuts our condition from <code>R[0] &lt;= R[1] &lt;= R[2] &lt;= R[3] &lt;= R[4]</code> to <code>R[0] &lt;= R[1]</code> and <code>R[2] &lt;= R[3] &lt;= R[4]</code>.  That is, the boundary <code>"a" == column[1] != column[2] == "b"</code> has 'cut' one of the conditions for <code>R</code> out.</p>
<p>At a high level, our algorithm depends on evaluating whether adding a new column will keep all the rows sorted.  By maintaining information about these cuts, we only need to compare characters in the newest column.</p>
<iframe src="https://leetcode.com/playground/bbGofp6M/shared" frameborder="0" width="100%" height="500" name="bbGofp6M"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(NW)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">W</script> is the length of <code>A[i]</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script> in additional space complexity.  (In Python, <code>zip(*A)</code> uses <script type="math/tex; mode=display">O(NW)</script> space.)
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
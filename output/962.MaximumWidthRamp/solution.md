<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sort">Approach 1: Sort</a></li>
<li><a href="#approach-2-binary-search-candidates">Approach 2: Binary Search Candidates</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sort">Approach 1: Sort</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For all elements like <code>A[i] = v</code>, let's write the indices <code>i</code> in sorted order of their values <code>v</code>.  For example with <code>A[0] = 7, A[1] = 2, A[2] = 5, A[3] = 4</code>, we can write the order of indices <code>i=1, i=3, i=2, i=0</code>.</p>
<p>Then, whenever we write an index <code>i</code>, we know there was a ramp of width <code>i - min(indexes_previously_written)</code> (if this quantity is positive).  We can keep track of the minimum of all indexes previously written as <code>m</code>.</p>
<iframe src="https://leetcode.com/playground/cTgKu5cw/shared" frameborder="0" width="100%" height="378" name="cTgKu5cw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, depending on the implementation of the sorting function.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-binary-search-candidates">Approach 2: Binary Search Candidates</h4>
<p><strong>Intuition</strong></p>
<p>Consider <code>i</code> in decreasing order.  We want to find the largest <code>j</code> with <code>A[j] &gt;= A[i]</code> if it exists.</p>
<p>Thus, the candidates for <code>j</code> are decreasing: if there is <code>j1 &lt; j2</code> and <code>A[j1] &lt;= A[j2]</code> then we strictly prefer <code>j2</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's keep a list of these candidates <code>j</code>.  For example, with <code>A = [0,8,2,7,5]</code>, the candidates for <code>i = 0</code> would be <code>candidates = [(v=5, i=4), (v=7, i=3), (v=8, i=1)]</code>.  We keep the list of <code>candidates</code> in decreasing order of <code>i</code> and increasing order of <code>v</code>.</p>
<p>Now we can binary search to find the largest <code>j</code> with <code>A[j] &gt;= A[i]</code>: it's the first one in this list of candidates with <code>v &gt;= A[i]</code>.</p>
<iframe src="https://leetcode.com/playground/jtYswxPE/shared" frameborder="0" width="100%" height="500" name="jtYswxPE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
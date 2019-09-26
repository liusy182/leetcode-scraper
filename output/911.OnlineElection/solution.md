<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-list-of-lists-binary-search">Approach 1: List of Lists + Binary Search</a></li>
<li><a href="#approach-2-precomputed-answer-binary-search">Approach 2: Precomputed Answer + Binary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-list-of-lists-binary-search">Approach 1: List of Lists + Binary Search</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can store the votes in a list <code>A</code> of lists of votes.  Each vote has a person and a timestamp, and <code>A[count]</code> is a list of the <code>count</code>-th votes received for that person.</p>
<p>Then, <code>A[i][0]</code> and <code>A[i]</code> are monotone increasing, so we can binary search on them to find the most recent vote by time.</p>
<iframe src="https://leetcode.com/playground/vXWSxDmZ/shared" frameborder="0" width="100%" height="500" name="vXWSxDmZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + Q \log^2 N)</script>, where <script type="math/tex; mode=display">N</script> is the number of votes, and <script type="math/tex; mode=display">Q</script> is the number of queries.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-precomputed-answer-binary-search">Approach 2: Precomputed Answer + Binary Search</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As the votes come in, we can remember every event <code>(winner, time)</code> when the winner changes.  After, we have a sorted list of these events that we can binary search for the answer.</p>
<iframe src="https://leetcode.com/playground/fWa6yR8V/shared" frameborder="0" width="100%" height="500" name="fWa6yR8V"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + Q \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of votes, and <script type="math/tex; mode=display">Q</script> is the number of queries.</p>
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
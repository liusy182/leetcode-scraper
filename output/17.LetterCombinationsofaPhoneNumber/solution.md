<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-backtracking">Approach 1: Backtracking</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-backtracking">Approach 1: Backtracking</h4>
<p><a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a> 
is an algorithm for finding all
solutions by exploring all potential candidates.
If the solution candidate turns to be <em>not</em> a solution 
(or at least not the <em>last</em> one), 
backtracking algorithm discards it by making some changes 
on the previous step, <em>i.e.</em> <em>backtracks</em> and then try again.</p>
<p>Here is a backtrack function <code>backtrack(combination, next_digits)</code>
which takes as arguments an ongoing letter combination 
and the next digits to check.</p>
<ul>
<li>If there is no more digits to check
that means that the current combination is done.</li>
<li>If there are still digits to check :<ul>
<li>Iterate over the letters mapping the next available digit.<ul>
<li>Append the current letter to the current combination 
<code>combination = combination + letter</code>.</li>
<li>Proceed to check next digits : 
<code>backtrack(combination + letter, next_digits[1:])</code>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>!?!../Documents/17_LIS.json:1000,592!?!</p>
<iframe src="https://leetcode.com/playground/26oBRSTE/shared" frameborder="0" width="100%" height="500" name="26oBRSTE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(3^N \times 4^M)</script>
where <code>N</code> is the number of digits in the input that maps to  3 letters 
(<em>e.g.</em> <code>2, 3, 4, 5, 6, 8</code>) and <code>M</code> is the number of digits in the input
that maps to 4 letters (<em>e.g.</em> <code>7, 9</code>),
and <code>N+M</code> is the total number digits in the input.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(3^N \times 4^M)</script> since one has to keep
<script type="math/tex; mode=display">3^N \times 4^M</script> solutions.</p>
</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>
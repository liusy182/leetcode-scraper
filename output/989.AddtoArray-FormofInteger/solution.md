<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-schoolbook-addition">Approach 1: Schoolbook Addition</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-schoolbook-addition">Approach 1: Schoolbook Addition</h4>
<p><strong>Intuition</strong></p>
<p>Let's add numbers in a schoolbook way, column by column.  For example, to add 123 and 912, we add 3+2, then 2+1, then 1+9.  Whenever our addition result is more than 10, we carry the 1 into the next column.  The result is 1035.</p>
<p><strong>Algorithm</strong></p>
<p>We can do a variant of the above idea that is easier to implement - we put the entire addend in the first column from the right.</p>
<p>Continuing the example of 123 + 912, we start with [1, 2, 3+912].  Then we perform the addition 3+912, leaving 915.  The 5 stays as the digit, while we 'carry' 910 into the next column which becomes 91.</p>
<p>We repeat this process with [1, 2+91, 5].  We have 93, where 3 stays and 90 is carried over as 9.  Again, we have [1+9, 3, 5] which transforms into [1, 0, 3, 5].</p>
<iframe src="https://leetcode.com/playground/sf5gg5Sj/shared" frameborder="0" width="100%" height="361" name="sf5gg5Sj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\max(N, \log K))</script> where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\max(N, \log K))</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
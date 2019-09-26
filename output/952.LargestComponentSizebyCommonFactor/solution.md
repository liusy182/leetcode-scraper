<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-union-find">Approach 1: Union-Find</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-union-find">Approach 1: Union-Find</h4>
<p>We will skip the explanation of how a DSU structure is implemented.  Please refer to <a href="https://leetcode.com/problems/redundant-connection/solution/">https://leetcode.com/problems/redundant-connection/solution/</a> for a tutorial on DSU.</p>
<p><strong>Intuition</strong></p>
<p>Let <script type="math/tex; mode=display">W = \max(A[i])</script>, and <script type="math/tex; mode=display">R = \sqrt{W}</script>.  For each value <script type="math/tex; mode=display">A[i]</script>, there is at most one prime factor <script type="math/tex; mode=display">p \geq R</script> dividing <script type="math/tex; mode=display">A[i]</script>.  Let's call <script type="math/tex; mode=display">A[i]</script>'s "big prime" this <script type="math/tex; mode=display">p</script>, if it exists.</p>
<p>This means that there are at most <script type="math/tex; mode=display">R + A\text{.length}</script> unique prime divisors of elements in <script type="math/tex; mode=display">A</script>:  the big primes correspond to a maximum of <script type="math/tex; mode=display">A\text{.length}</script> values, and the small primes are all less than <script type="math/tex; mode=display">R</script>, so there's at most <script type="math/tex; mode=display">R</script> of them too.</p>
<p><strong>Algorithm</strong></p>
<p>Factor each <script type="math/tex; mode=display">A[i]</script> into prime factors, and index every occurrence of these primes.  (To save time, we can use a sieve.  Please see this article's comments for more details.)</p>
<p>Then, use a union-find structure to union together any prime factors that came from the same <script type="math/tex; mode=display">A[i]</script>.</p>
<p>Finally, we can count the size of each component, by inspecting and counting the id of the component each <script type="math/tex; mode=display">A[i]</script> belongs to.</p>
<iframe src="https://leetcode.com/playground/MAiR5RjS/shared" frameborder="0" width="100%" height="500" name="MAiR5RjS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N\sqrt{W})</script> where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">W = \max(A[i])</script>.</p>
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
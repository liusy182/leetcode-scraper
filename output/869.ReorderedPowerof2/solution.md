<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-permutations">Approach 1: Permutations</a></li>
<li><a href="#approach-2-counting">Approach 2: Counting</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-permutations">Approach 1: Permutations</h4>
<p><strong>Intuition</strong></p>
<p>For each permutation of the digits of <code>N</code>, let's check if that permutation is a power of 2.</p>
<p><strong>Algorithm</strong></p>
<p>This approach has two steps: how will we generate the permutations of the digits, and how will we check that the permutation represents a power of 2?</p>
<p>To generate permutations of the digits, we place any digit into the first position (<code>start = 0</code>), then any of the remaining digits into the second position (<code>start = 1</code>), and so on.  In Python, we can use the builtin function <code>itertools.permutations</code>.</p>
<p>To check whether a permutation represents a power of 2, we check that there is no leading zero, and divide out all factors of 2.  If the result is <code>1</code> (that is, it contained no other factors besides <code>2</code>), then it was a power of 2.  In Python, we can use the check <code>bin(N).count('1') == 1</code>.</p>
<iframe src="https://leetcode.com/playground/jfG2dxr5/shared" frameborder="0" width="100%" height="500" name="jfG2dxr5"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O((\log N)! * \log N)</script>.  Note that <script type="math/tex; mode=display">\log N</script> is the number of digits in the binary representation of <script type="math/tex; mode=display">N</script>.  For each of <script type="math/tex; mode=display">(\log N)!</script> permutations of the digits of <script type="math/tex; mode=display">N</script>, we need to check that it is a power of 2 in <script type="math/tex; mode=display">O(\log N)</script> time.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, the space used by <code>A</code> (or <code>cand</code> in Python).
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-counting">Approach 2: Counting</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can check whether two numbers have the same digits by comparing the <em>count</em> of their digits.  For example, 338 and 833 have the same digits because they both have exactly two 3's and one 8.</p>
<p>Since <script type="math/tex; mode=display">N</script> could only be a power of 2 with 9 digits or less (namely, <script type="math/tex; mode=display">2^0, 2^1, \cdots, 2^29</script>), we can just check whether <script type="math/tex; mode=display">N</script> has the same digits as any of these possibilities.</p>
<iframe src="https://leetcode.com/playground/ZV2nPKdj/shared" frameborder="0" width="100%" height="395" name="ZV2nPKdj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log^2 N)</script>.  There are <script type="math/tex; mode=display">\log N</script> different candidate powers of 2, and each comparison has <script type="math/tex; mode=display">O(\log N)</script> time complexity.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>Let's create every possible string - then we can compare them and choose the best one.</p>
<p><strong>Algorithm</strong></p>
<p>In our depth first search, we will maintain <code>sb</code> (or <code>A</code> in Python), the contents of a path from the root to this node.</p>
<p>When we reach a leaf, we will reverse this path to create a candidate answer.  If it is better than our current answer, we'll update our answer.</p>
<iframe src="https://leetcode.com/playground/ZpZvkz97/shared" frameborder="0" width="100%" height="480" name="ZpZvkz97"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  We use <script type="math/tex; mode=display">O(N)</script> to traverse the array and maintain <code>A</code> [Python] or <code>sb</code>.  Then, our reversal and comparison with the previous answer is <script type="math/tex; mode=display">O(L)</script>, where <script type="math/tex; mode=display">L</script> is the size of the string we have when at the leaf.  For example, for a perfectly balanced tree, <script type="math/tex; mode=display">L = \log N</script> and the time complexity would be <script type="math/tex; mode=display">O(N \log N)</script>.</p>
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
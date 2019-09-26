<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-recursion">Approach 1: Using Recursion</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-recursion">Approach 1: Using Recursion</h4>
<p><strong>Algorithm</strong></p>
<p>From the problem statement, it is clear that we need to find the tilt value at every node of the given tree and add up all the tilt values to obtain the final result. To find the tilt value at any node, we need to subtract the sum of all the nodes in its left subtree and the sum of all the nodes in its right subtree. </p>
<p>Thus, to find the solution, we make use of a recursive function <code>traverse</code> which when called from any node, returns the sum of the nodes below the current node including itself. With the help of such sum values for the right and left subchild of any node, we can directly obtain the tilt value corresponding to that node.</p>
<p>The below animation depicts how the value passing and tilt calculation:</p>
<p>!?!../Documents/563_Binary.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/kegZTTSb/shared" frameborder="0" width="100%" height="480" name="kegZTTSb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n)</script>. where <script type="math/tex; mode=display">n</script> is the number of nodes. Each node is visited once.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script>. In worst case when the tree is skewed depth of tree will be <script type="math/tex; mode=display">n</script>. In average case depth will be <script type="math/tex; mode=display">\log n</script>.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
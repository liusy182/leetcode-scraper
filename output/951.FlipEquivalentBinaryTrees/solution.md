<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-canonical-traversal">Approach 2: Canonical Traversal</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>If <code>root1</code> and <code>root2</code> have the same root value, then we only need to check if their children are equal (up to ordering.)</p>
<p><strong>Algorithm</strong></p>
<p>There are 3 cases:</p>
<ul>
<li>
<p>If <code>root1</code> or <code>root2</code> is <code>null</code>, then they are equivalent if and only if they are both <code>null</code>.</p>
</li>
<li>
<p>Else, if <code>root1</code> and <code>root2</code> have different values, they aren't equivalent.</p>
</li>
<li>
<p>Else, let's check whether the children of <code>root1</code> are equivalent to the children of <code>root2</code>.  There are two different ways to pair these children.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/wjoLqdDo/shared" frameborder="0" width="100%" height="242" name="wjoLqdDo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(min(N_1, N_2))</script>, where <script type="math/tex; mode=display">N_1, N_2</script> are the lengths of <code>root1</code> and <code>root2</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(min(H_1, H_2))</script>, where <script type="math/tex; mode=display">H_1, H_2</script> are the heights of the trees of <code>root1</code> and <code>root2</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-canonical-traversal">Approach 2: Canonical Traversal</h4>
<p><strong>Intuition</strong></p>
<p>Flip each node so that the left child is smaller than the right, and call this the <em>canonical representation</em>.  All equivalent trees have exactly one canonical representation.</p>
<p><strong>Algorithm</strong></p>
<p>We can use a depth-first search to compare the canonical representation of each tree.  If the traversals are the same, the representations are equal.</p>
<p>When traversing, we should be careful to encode both when we enter or leave a node.</p>
<iframe src="https://leetcode.com/playground/PZJH2Hcn/shared" frameborder="0" width="100%" height="500" name="PZJH2Hcn"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N_1 + N_2)</script>, where <script type="math/tex; mode=display">N_1, N_2</script> are the lengths of <code>root1</code> and <code>root2</code>.  (In Python, this is <script type="math/tex; mode=display">\min(N_1, N_2)</script>.)</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N_1 + N_2)</script>.  (In Python, this is <script type="math/tex; mode=display">\min(H_1, H_2)</script>, where <script type="math/tex; mode=display">H_1, H_2</script> are the heights of the trees of <code>root1</code> and <code>root2</code>.)
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-in-order-traversal">Approach 1: In-Order Traversal</a></li>
<li><a href="#approach-2-traversal-with-relinking">Approach 2: Traversal with Relinking</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-in-order-traversal">Approach 1: In-Order Traversal</h4>
<p><strong>Intuition</strong></p>
<p>The definition of a binary search tree is that for every node, all the values of the left branch are less than the value at the root, and all the values of the right branch are greater than the value at the root.</p>
<p>Because of this, an <em>in-order traversal</em> of the nodes will yield all the values in increasing order.</p>
<p><strong>Algorithm</strong></p>
<p>Once we have traversed all the nodes in increasing order, we can construct new nodes using those values to form the answer.</p>
<iframe src="https://leetcode.com/playground/RonWhYrN/shared" frameborder="0" width="100%" height="378" name="RonWhYrN"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the size of the answer.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-traversal-with-relinking">Approach 2: Traversal with Relinking</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can perform the same in-order traversal as in <em>Approach 1</em>.  During the traversal, we'll construct the answer on the fly, reusing the nodes of the given tree by cutting their left child and adjoining them to the answer.</p>
<iframe src="https://leetcode.com/playground/5M7CYgmK/shared" frameborder="0" width="100%" height="361" name="5M7CYgmK"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(H)</script> in <em>additional</em> space complexity, where <script type="math/tex; mode=display">H</script> is the height of the given tree, and the size of the implicit call stack in our in-order traversal.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
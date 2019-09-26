<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth-First Search</a></li>
<li><a href="#approach-2-recursion">Approach 2: Recursion</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth-First Search</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's output all the values of the array.  After, we can check that they are all equal.</p>
<p>To output all the values of the array, we perform a depth-first search.</p>
<iframe src="https://leetcode.com/playground/dL2Yo8pb/shared" frameborder="0" width="100%" height="378" name="dL2Yo8pb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursion">Approach 2: Recursion</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>A tree is univalued if both its children are univalued, plus the root node has the same value as the child nodes.</p>
<p>We can write our function recursively.  <code>left_correct</code> will represent that the left child is correct: ie., that it is univalued, and the root value is equal to the left child's value.  <code>right_correct</code> will represent the same thing for the right child.  We need both of these properties to be true.</p>
<iframe src="https://leetcode.com/playground/xLY6bNWX/shared" frameborder="0" width="100%" height="208" name="xLY6bNWX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given tree.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(H)</script>, where <script type="math/tex; mode=display">H</script> is the height of the given tree.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
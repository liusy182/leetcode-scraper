<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth First Search</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's find the leaf value sequence for both given trees.  Afterwards, we can compare them to see if they are equal or not.</p>
<p>To find the leaf value sequence of a tree, we use a depth first search.  Our <code>dfs</code> function writes the node's value if it is a leaf, and then recursively explores each child.  This is guaranteed to visit each leaf in left-to-right order, as left-children are fully explored before right-children.</p>
<iframe src="https://leetcode.com/playground/2esZiYkH/shared" frameborder="0" width="100%" height="378" name="2esZiYkH"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(T_1 + T_2)</script>, where <script type="math/tex; mode=display">T_1, T_2</script> are the lengths of the given trees.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(T_1 + T_2)</script>, the space used in storing the leaf values.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth-First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth-First Search</h4>
<p><strong>Intuition</strong></p>
<p>As we do a pre-order traversal, we will flip nodes on the fly to try to match our voyage with the given one.</p>
<p>If we are expecting the next integer in our voyage to be <code>voyage[i]</code>, then there is only at most one choice for path to take, as all nodes have different values.</p>
<p><strong>Algorithm</strong></p>
<p>Do a depth first search.  If at any node, the node's value doesn't match the voyage, the answer is <code>[-1]</code>.</p>
<p>Otherwise, we know when to flip: the next number we are expecting in the voyage <code>voyage[i]</code> is different from the next child.</p>
<iframe src="https://leetcode.com/playground/TSMMADqh/shared" frameborder="0" width="100%" height="500" name="TSMMADqh"></iframe>

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
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
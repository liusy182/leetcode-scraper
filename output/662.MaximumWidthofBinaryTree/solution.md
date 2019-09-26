<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-framework">Approach Framework</a></li>
<li><a href="#approach-1-breadth-first-search-accepted">Approach #1: Breadth-First Search [Accepted]</a></li>
<li><a href="#approach-2-depth-first-search-accepted">Approach #2: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-framework">Approach Framework</h4>
<p><strong>Explanation</strong></p>
<p>As we need to reach every node in the given tree, we will have to traverse the tree, either with a depth-first search, or with a breadth-first search.</p>
<p>The main idea in this question is to give each node a <code>position</code> value. If we go down the left neighbor, then <code>position -&gt; position * 2</code>; and if we go down the right neighbor, then <code>position -&gt; position * 2 + 1</code>. This makes it so that when we look at the position values <code>L</code> and <code>R</code> of two nodes with the same depth, the width will be <code>R - L + 1</code>.</p>
<hr>
<h4 id="approach-1-breadth-first-search-accepted">Approach #1: Breadth-First Search [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Traverse each node in breadth-first order, keeping track of that node's position.  For each depth, the first node reached is the left-most, while the last node reached is the right-most.</p>
<iframe src="https://leetcode.com/playground/GsZid6zn/shared" frameborder="0" width="100%" height="500" name="GsZid6zn"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the number of nodes in the input tree.  We traverse every node.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of our <code>queue</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-depth-first-search-accepted">Approach #2: Depth-First Search [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Traverse each node in depth-first order, keeping track of that node's position.  For each depth, the position of the first node reached of that depth will be kept in <code>left[depth]</code>.</p>
<p>Then, for each node, a candidate width is <code>pos - left[depth] + 1</code>.  We take the maximum of the candidate answers.</p>
<iframe src="https://leetcode.com/playground/A9iKAcsQ/shared" frameborder="0" width="100%" height="344" name="A9iKAcsQ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the number of nodes in the input tree.  We traverse every node.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of the implicit call stack in our DFS.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
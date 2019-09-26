<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursive-solutionaccepted">Approach #1 Recursive Solution[Accepted]</a></li>
<li><a href="#approach-2-using-queuebfsaccepted">Approach #2 Using queue(BFS)[Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursive-solutionaccepted">Approach #1 Recursive Solution[Accepted]</h4>
<p>We start by initializing a <script type="math/tex; mode=display">res</script> array with the dimensions being <script type="math/tex; mode=display">height</script>x<script type="math/tex; mode=display">2^{height}-1</script>. Here, <script type="math/tex; mode=display">height</script> refers to the number of levels in the given tree. In order to fill this <script type="math/tex; mode=display">res</script> array with the required elements, initially, we fill the complete array with <code>""</code> .  After this we make use of a recursive function <code>fill(res, root, i, l, r)</code> which fills the <script type="math/tex; mode=display">res</script> array such that the current element has to be filled in <script type="math/tex; mode=display">i^{th}</script> row, and the column being the middle of the indices <script type="math/tex; mode=display">l</script> and <script type="math/tex; mode=display">r</script>, where <script type="math/tex; mode=display">l</script> and <script type="math/tex; mode=display">r</script> refer to the left and the right boundaries of the columns in which the current element can be filled.</p>
<p>In every recursive call, we do as follows:</p>
<ol>
<li>
<p>If we've reached the end of the tree, i.e. if root==null, return.</p>
</li>
<li>
<p>Determine the column in which the current element(<script type="math/tex; mode=display">root</script>) needs to be filled, which is the middle of <script type="math/tex; mode=display">l</script> and <script type="math/tex; mode=display">r</script>, given by say, <script type="math/tex; mode=display">j</script>. The row number is same as <script type="math/tex; mode=display">i</script>. Put the current element at <script type="math/tex; mode=display">res[i][j]</script>.</p>
</li>
<li>
<p>Make the recursive call for the left child of the <script type="math/tex; mode=display">root</script> using <code>fill(res, root.left, i + 1, l, (l + r) / 2)</code>.</p>
</li>
<li>
<p>Make the recursive call for the right child of the <script type="math/tex; mode=display">root</script> using <code>fill(res, root.right, i + 1, (l + r + 1) / 2, r)</code>.</p>
</li>
</ol>
<p>Note, that in the last two recursive calls, we update the row number(level of the tree). This ensures that the child nodes fit into the correct row. We also update the column boundaries appropriately based on the <script type="math/tex; mode=display">l</script> and <script type="math/tex; mode=display">r</script> values.</p>
<p>Further, to determine the <script type="math/tex; mode=display">height</script> also, we make use of recursive funtion <code>getHeight(root)</code>, which returns the height of the tree starting from the <script type="math/tex; mode=display">root</script> node. We traverse into all the branches possible in the tree recursively and find the depth of the longest branch.</p>
<p>At the end, we convert the <script type="math/tex; mode=display">res</script> array into the required list format, before returning the results.</p>
<iframe src="https://leetcode.com/playground/ncTFx4nd/shared" frameborder="0" name="ncTFx4nd" width="100%" height="479"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(h*2^h)</script>. We need to fill the <script type="math/tex; mode=display">res</script> array of size <script type="math/tex; mode=display">h</script>x<script type="math/tex; mode=display">2^h - 1</script>. Here, <script type="math/tex; mode=display">h</script> refers to the height of the given tree.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(h*2^h)</script>.  <script type="math/tex; mode=display">res</script> array of size <script type="math/tex; mode=display">h</script>x<script type="math/tex; mode=display">2^h - 1</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-queuebfsaccepted">Approach #2 Using queue(BFS)[Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>We can also solve the problem by making use of Breadth First Search's idea. For this, we make use of a class <script type="math/tex; mode=display">Params</script> which stores the parameters of a <script type="math/tex; mode=display">node</script> of  the tree, including its value, its level in the tree(<script type="math/tex; mode=display">i</script>), and the left(<script type="math/tex; mode=display">l</script>) and right(<script type="math/tex; mode=display">r</script>) boundaries of the columns in which this element can be filled in the result to be returned.</p>
<p>We start by initializing a <script type="math/tex; mode=display">res</script> array as in the previous approach. After this, we add the parametrized <script type="math/tex; mode=display">root</script> of the tree into a <script type="math/tex; mode=display">queue</script>. After this, we do the following at every step.</p>
<ol>
<li>
<p>Remove an element, $$p$,  from the front of the <script type="math/tex; mode=display">queue</script>. </p>
</li>
<li>
<p>Add this element at its correct position in the <script type="math/tex; mode=display">res</script> array given by <script type="math/tex; mode=display">res[p.i][(p.l + p.r) / 2]</script>. Here, the values <script type="math/tex; mode=display">i</script>, <script type="math/tex; mode=display">l</script> and <script type="math/tex; mode=display">r</script> refer to the column/level number, and the left and right boundaries permissible for putting the current node into <script type="math/tex; mode=display">res</script>. These are obtained from the node's parameters, which have been associated with it before putting it into the <script type="math/tex; mode=display">queue</script>.</p>
</li>
<li>
<p>If the left child of <script type="math/tex; mode=display">p</script> exists, put it at the back of the <script type="math/tex; mode=display">queue</script>, in a parametized form, by appropriately updating the level as the next level and the boundaries permissible as well.</p>
</li>
<li>
<p>If the right child of <script type="math/tex; mode=display">p</script> exists, put it at the back of the <script type="math/tex; mode=display">queue</script>, in a parametized form, by appropriately updating the level as the next level and the boundaries permissible as well.</p>
</li>
<li>
<p>Continue steps 1. to 4. till the <script type="math/tex; mode=display">queue</script> becomes empty. </p>
</li>
</ol>
<p>At the end, we again convert the <script type="math/tex; mode=display">res</script> array into the required list format, before returning the results.</p>
<iframe src="https://leetcode.com/playground/jb3EALV4/shared" frameborder="0" name="jb3EALV4" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(h*2^h)</script>. We need to fill the <script type="math/tex; mode=display">res</script> array of size <script type="math/tex; mode=display">h</script>x<script type="math/tex; mode=display">2^h - 1</script>. Here, <script type="math/tex; mode=display">h</script> refers to the height of the given tree.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(h*2^h)</script>.  <script type="math/tex; mode=display">res</script> array of size <script type="math/tex; mode=display">h</script>x<script type="math/tex; mode=display">2^h - 1</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
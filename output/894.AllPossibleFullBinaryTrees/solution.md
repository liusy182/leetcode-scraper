<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let <script type="math/tex; mode=display">\text{FBT}(N)</script> be the list of all possible full binary trees with <script type="math/tex; mode=display">N</script> nodes.</p>
<p>Every full binary tree <script type="math/tex; mode=display">T</script> with 3 or more nodes, has 2 children at its root.  Each of those children <code>left</code> and <code>right</code> are themselves full binary trees.</p>
<p>Thus, for <script type="math/tex; mode=display">N \geq 3</script>, we can formulate the recursion: <script type="math/tex; mode=display">\text{FBT}(N) =</script> [All trees with left child from <script type="math/tex; mode=display">\text{FBT}(x)</script> and right child from <script type="math/tex; mode=display">\text{FBT}(N-1-x)</script>, for all <script type="math/tex; mode=display">x</script>].</p>
<p>Also, by a simple counting argument, there are no full binary trees with a positive, even number of nodes.</p>
<p>Finally, we should cache previous results of the function <script type="math/tex; mode=display">\text{FBT}</script> so that we don't have to recalculate them in our recursion.</p>
<iframe src="https://leetcode.com/playground/MNvnRoUP/shared" frameborder="0" width="100%" height="497" name="MNvnRoUP"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^N)</script>.  For odd <script type="math/tex; mode=display">N</script>, let <script type="math/tex; mode=display">N = 2k + 1</script>.  Then, <script type="math/tex; mode=display">\Big| \text{FBT}(N) \Big| = C_k</script>, the <script type="math/tex; mode=display">k</script>-th catalan number; and <script type="math/tex; mode=display">\sum\limits_{k < \frac{N}{2}} C_k</script> (the complexity involved in computing intermediate results required) is bounded by <script type="math/tex; mode=display">O(2^N)</script>.  However, the proof is beyond the scope of this article.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(2^N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
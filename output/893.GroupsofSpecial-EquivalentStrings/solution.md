<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-counting">Approach 1: Counting</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-counting">Approach 1: Counting</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's try to characterize a special-equivalent string <script type="math/tex; mode=display">S</script>, by finding a function <script type="math/tex; mode=display">\mathcal{C}</script> so that <script type="math/tex; mode=display">S \equiv T \iff \mathcal{C}(S) = \mathcal{C}(T)</script>.</p>
<p>Through swapping, we can permute the even indexed letters, and the odd indexed letters.  What characterizes these permutations is the count of the letters: all such permutations have the same count, and different counts have different permutations.</p>
<p>Thus, the function <script type="math/tex; mode=display">\mathcal{C}(S) =</script> (the count of the even indexed letters in S, followed by the count of the odd indexed letters in S) successfully characterizes the equivalence relation.</p>
<p>Afterwards, we count the number of unique <script type="math/tex; mode=display">\mathcal{C}(S)</script> for <script type="math/tex; mode=display">S \in A</script>.</p>
<iframe src="https://leetcode.com/playground/VUyxHYTk/shared" frameborder="0" width="100%" height="259" name="VUyxHYTk"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\sum\limits_{i} (A_i)\text{.length})</script>
</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
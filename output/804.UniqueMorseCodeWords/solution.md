<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-hash-set-accepted">Approach #1: Hash Set [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-hash-set-accepted">Approach #1: Hash Set [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We can transform each <code>word</code> into it's Morse Code representation.</p>
<p>After, we put all transformations into a set <code>seen</code>, and return the size of the set.</p>
<iframe src="https://leetcode.com/playground/f4mHEzpq/shared" frameborder="0" width="100%" height="361" name="f4mHEzpq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(S)</script>, where <script type="math/tex; mode=display">S</script> is the sum of the lengths of words in <code>words</code>.  We iterate through each character of each word in <code>words</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(S)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
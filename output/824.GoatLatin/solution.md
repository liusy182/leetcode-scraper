<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-string-accepted">Approach #1: String [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-string-accepted">Approach #1: String [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We apply the steps given in the problem in a straightforward manner.  The difficulty lies in the implementation.</p>
<p><strong>Algorithm</strong></p>
<p>For each <code>word</code> in the sentence split, if it is a vowel we consider the word, otherwise we consider the rotation of the word (either <code>word[1:] + word[:1]</code> in Python, otherwise <code>word.substring(1) + word.substring(0, 1)</code> in Java).</p>
<p>Afterwards, we add <code>"ma"</code>, the desired number of <code>"a"</code>'s, and a space character.</p>
<iframe src="https://leetcode.com/playground/oPStDbDq/shared" frameborder="0" width="100%" height="500" name="oPStDbDq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>.  This represents the complexity of rotating the word and adding extra <code>"a"</code> characters.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>, the space added to the answer by adding extra <code>"a"</code> characters.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
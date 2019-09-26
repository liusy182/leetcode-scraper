<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-run-length-encoding-accepted">Approach #1: Run Length Encoding [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-run-length-encoding-accepted">Approach #1: Run Length Encoding [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>For some word, write the head character of every group, and the count of that group.  For example, for <code>"abbcccddddaaaaa"</code>, we'll write the "key" of <code>"abcda"</code>, and the "count" <code>[1,2,3,4,5]</code>.</p>
<p>Let's see if a <code>word</code> is stretchy.  Evidently, it needs to have the same key as <code>S</code>.</p>
<p>Now, let's say we have individual counts <code>c1 = S.count[i]</code> and <code>c2 = word.count[i]</code>.</p>
<ul>
<li>
<p>If <code>c1 &lt; c2</code>, then we can't make the <code>i</code>th group of <code>word</code> equal to the <code>i</code>th word of <code>S</code> by adding characters.</p>
</li>
<li>
<p>If <code>c1 &gt;= 3</code>, then we can add letters to the <code>i</code>th group of <code>word</code> to match the <code>i</code>th group of <code>S</code>, as the latter is <em>extended</em>.</p>
</li>
<li>
<p>Else, if <code>c1 &lt; 3</code>, then we must have <code>c2 == c1</code> for the <code>i</code>th groups of <code>word</code> and <code>S</code> to match.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/CtqN5Fqo/shared" frameborder="0" width="100%" height="500" name="CtqN5Fqo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(QK)</script>, where <script type="math/tex; mode=display">Q</script> is the length of <code>words</code> (at least 1), and <script type="math/tex; mode=display">K</script> is the maximum length of a word.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(K)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
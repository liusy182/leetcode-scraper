<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-group-into-blocks">Approach 1: Group into Blocks</a></li>
<li><a href="#approach-2-two-pointer">Approach 2: Two Pointer</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-group-into-blocks">Approach 1: Group into Blocks</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For a string like <code>S = 'aabbbbccc'</code>, we can group it into blocks <code>groupify(S) = [('a', 2), ('b', 4), ('c', 3)]</code>, that consist of a <em>key</em> <code>'abc'</code> and a <em>count</em> <code>[2, 4, 3]</code>.</p>
<p>Then, the necessary and sufficient condition for <code>typed</code> to be a long-pressed version of <code>name</code> is that the keys are the same, and each entry of the count of <code>typed</code> is at least the entry for the count of <code>name</code>.</p>
<p>For example, <code>'aaleex'</code> is a long-pressed version of <code>'alex'</code>: because when considering the groups <code>[('a', 2), ('l', 1), ('e', 2), ('x', 1)]</code> and <code>[('a', 1), ('l', 1), ('e', 1), ('x', 1)]</code>, they both have the key <code>'alex'</code>, and the count <code>[2,1,2,1]</code> is at least <code>[1,1,1,1]</code> when making an element-by-element comparison <code>(2 &gt;= 1, 1 &gt;= 1, 2 &gt;= 1, 1 &gt;= 1)</code>.</p>
<iframe src="https://leetcode.com/playground/TfwwqxiQ/shared" frameborder="0" width="100%" height="500" name="TfwwqxiQ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N+T)</script>, where <script type="math/tex; mode=display">N, T</script> are the lengths of <code>name</code> and <code>typed</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N+T)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pointer">Approach 2: Two Pointer</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach 1</em>, we want to check the key and the count.  We can do this on the fly.</p>
<p>Suppose we read through the characters <code>name</code>, and eventually it doesn't match <code>typed</code>.</p>
<p>There are some cases for when we are allowed to skip characters of <code>typed</code>. Let's use a tuple to denote the case (<code>name</code>, <code>typed</code>):</p>
<ul>
<li>
<p>In a case like <code>('aab', 'aaaaab')</code>, we can skip the 3rd, 4th, and 5th <code>'a'</code> in <code>typed</code> because we have already processed an <code>'a'</code> in this block.</p>
</li>
<li>
<p>In a case like <code>('a', 'b')</code>, we can't skip the 1st <code>'b'</code> in <code>typed</code> because we haven't processed anything in the current block yet.</p>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>This leads to the following algorithm:</p>
<ul>
<li>For each character in <code>name</code>, if there's a mismatch with the next character in <code>typed</code>:<ul>
<li>If it's the first character of the block in <code>typed</code>, the answer is <code>False</code>.</li>
<li>Else, discard all similar characers of <code>typed</code> coming up.  The next (different) character coming must match.</li>
</ul>
</li>
</ul>
<p>Also, we'll keep track on the side of whether we are at the first character of the block.</p>
<iframe src="https://leetcode.com/playground/Wv6ufLEV/shared" frameborder="0" width="100%" height="500" name="Wv6ufLEV"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N+T)</script>, where <script type="math/tex; mode=display">N, T</script> are the lengths of <code>name</code> and <code>typed</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script> in additional space complexity.  (In Java, <code>.toCharArray</code> makes this <script type="math/tex; mode=display">O(N)</script>, but this can be easily remedied.)
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
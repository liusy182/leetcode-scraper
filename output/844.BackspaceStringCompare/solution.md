<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-build-string-accepted">Approach #1: Build String [Accepted]</a></li>
<li><a href="#approach-2-two-pointer-accepted">Approach #2: Two Pointer [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-build-string-accepted">Approach #1: Build String [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's individually build the result of each string (<code>build(S)</code> and <code>build(T)</code>), then compare if they are equal.</p>
<p><strong>Algorithm</strong></p>
<p>To build the result of a string <code>build(S)</code>, we'll use a stack based approach, simulating the result of each keystroke.</p>
<iframe src="https://leetcode.com/playground/oeguUYg8/shared" frameborder="0" width="100%" height="327" name="oeguUYg8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(M + N)</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>S</code> and <code>T</code> respectively.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(M + N)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pointer-accepted">Approach #2: Two Pointer [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes occur in the future.</p>
<p>If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, and therefore whether the result includes our character.</p>
<p><strong>Algorithm</strong></p>
<p>Iterate through the string in reverse.  If we see a backspace character, the next non-backspace character is skipped.  If a character isn't skipped, it is part of the final answer.</p>
<p>See the comments in the code for more details.</p>
<iframe src="https://leetcode.com/playground/sqdQBEmS/shared" frameborder="0" width="100%" height="500" name="sqdQBEmS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(M + N)</script>, where <script type="math/tex; mode=display">M, N</script> are the lengths of <code>S</code> and <code>T</code> respectively.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-mathematical-accepted">Approach #1: Mathematical [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-mathematical-accepted">Approach #1: Mathematical [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The crux of the problem is to put <code>+</code> and <code>-</code> signs on the numbers <code>1, 2, 3, ..., k</code> so that the sum is <code>target</code>.</p>
<p>When <code>target &lt; 0</code> and we made a sum of <code>target</code>, we could switch the signs of all the numbers so that it equals <code>Math.abs(target)</code>.  Thus, the answer for <code>target</code> is the same as <code>Math.abs(target)</code>, and so without loss of generality, we can consider only <code>target &gt; 0</code>.</p>
<p>Now let's say <code>k</code> is the smallest number with <code>S = 1 + 2 + ... + k &gt;= target</code>.  If <code>S == target</code>, the answer is clearly <code>k</code>.</p>
<p>If <code>S &gt; target</code>, we need to change some number signs.  If <code>delta = S - target</code> is even, then we can always find a subset of <code>{1, 2, ..., k}</code> equal to <code>delta / 2</code> and switch the signs, so the answer is <code>k</code>.  (This depends on <code>T = delta / 2</code> being at most <code>S</code>.)  [The proof is simple: either <code>T &lt;= k</code> and we choose it, or we choose <code>k</code> in our subset and try to solve the same instance of the problem for <code>T -= k</code> and the set <code>{1, 2, ..., k-1}</code>.]</p>
<p>Otherwise, if <code>delta</code> is odd, we can't do it, as every sign change from positive to negative changes the sum by an even number.  So let's consider a candidate answer of <code>k+1</code>, which changes <code>delta</code> by <code>k+1</code>.  If this is odd, then <code>delta</code> will be even and we can have an answer of <code>k+1</code>.  Otherwise, <code>delta</code> will be odd, and we will have an answer of <code>k+2</code>.</p>
<p>For concrete examples of the above four cases, consider the following:</p>
<ul>
<li>If <code>target = 3</code>, then <code>k = 2, delta = 0</code> and the answer is <code>k = 2</code>.</li>
<li>If <code>target = 4</code>, then <code>k = 3, delta = 2</code>, delta is even and the answer is <code>k = 3</code>.</li>
<li>If <code>target = 7</code>, then <code>k = 4, delta = 3</code>, delta is odd and adding <code>k+1</code> makes delta even.  The answer is <code>k+1 = 5</code>.</li>
<li>If <code>target = 5</code>, then <code>k = 3, delta = 1</code>, delta is odd and adding <code>k+1</code> keeps delta odd.  The answer is <code>k+2 = 5</code>.</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>Subtract <code>++k</code> from <code>target</code> until it goes non-positive.  Then <code>k</code> will be as described, and <code>target</code> will be <code>delta</code> as described.  We can output the four cases above: if <code>delta</code> is even then the answer is <code>k</code>, if <code>delta</code> is odd then the answer is <code>k+1</code> or <code>k+2</code> depending on the parity of <code>k</code>.</p>
<iframe src="https://leetcode.com/playground/VZd5DozE/shared" frameborder="0" width="100%" height="208" name="VZd5DozE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(\sqrt{\text{target}})</script>.  Our while loop needs this many steps, as <script type="math/tex; mode=display">1 + 2 + \dots + k = \frac{k(k+1)}{2}</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
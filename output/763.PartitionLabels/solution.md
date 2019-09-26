<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-greedy-accepted">Approach #1: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to repeatedly choose the smallest left-justified partition.
Consider the first label, say it's <code>'a'</code>.  The first partition must include it, and also the last occurrence of <code>'a'</code>.
However, between those two occurrences of <code>'a'</code>, there could be other labels that make the minimum size of this partition bigger.  For example, in <code>"abccaddbeffe"</code>, the minimum first partition is <code>"abccaddb"</code>. 
This gives us the idea for the algorithm:  For each letter encountered, process the last occurrence of that letter, extending the current partition <code>[anchor, j]</code> appropriately.</p>
<p><strong>Algorithm</strong></p>
<p>We need an array <code>last[char] -&gt; index of S where char occurs last</code>.
Then, let <code>anchor</code> and <code>j</code> be the start and end of the current partition.
If we are at a label that occurs last at some index after <code>j</code>, we'll extend the partition <code>j = last[c]</code>.  If we are at the end of the partition (<code>i == j</code>) then we'll append a partition size to our answer, and set the start of our new partition to <code>i+1</code>.</p>
<iframe src="https://leetcode.com/playground/sSLPrXHh/shared" frameborder="0" width="100%" height="361" name="sSLPrXHh"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <script type="math/tex; mode=display">S</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
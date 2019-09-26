<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-store-indexes">Approach 1: Store Indexes</a></li>
<li><a href="#approach-2-one-pass">Approach 2: One Pass</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-store-indexes">Approach 1: Store Indexes</h4>
<p><strong>Intuition</strong></p>
<p>Since we wanted to inspect the distance between consecutive 1s in the binary representation of <code>N</code>, let's write down the index of each <code>1</code> in that binary representation.  For example, if <code>N = 22 = 0b10110</code>, then we'll write <code>A = [1, 2, 4]</code>.  This makes it easier to proceed, as now we have a problem about adjacent values in an array.</p>
<p><strong>Algorithm</strong></p>
<p>Let's make a list <code>A</code> of indices <code>i</code> such that <code>N</code> has the <code>i</code>th bit set.</p>
<p>With this array <code>A</code>, finding the maximum distance between consecutive <code>1</code>s is much easier: it's the maximum distance between adjacent values of this array.</p>
<iframe src="https://leetcode.com/playground/vjdm4iZG/shared" frameborder="0" width="100%" height="293" name="vjdm4iZG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log N)</script>.  Note that <script type="math/tex; mode=display">\log N</script> is the number of digits in the binary representation of <script type="math/tex; mode=display">N</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, the space used by <code>A</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-one-pass">Approach 2: One Pass</h4>
<p><strong>Intuition</strong></p>
<p>In <em>Approach 1</em>, we created an array <code>A</code> of indices <code>i</code> for which <code>N</code> had the <code>i</code>th bit set.</p>
<p>Since we only care about consecutive values of this array <code>A</code>, we don't need to store the whole array.  We only need to remember the last value seen.</p>
<p><strong>Algorithm</strong></p>
<p>We'll store <code>last</code>, the last value added to the <em>virtual</em> array <code>A</code>.  If <code>N</code> has the <code>i</code>th bit set, a candidate answer is <code>i - last</code>, and then the new last value added to <code>A</code> would be <code>last = i</code>.</p>
<iframe src="https://leetcode.com/playground/Pae8eWML/shared" frameborder="0" width="100%" height="276" name="Pae8eWML"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log N)</script>.  Note that <script type="math/tex; mode=display">\log N</script> is the number of digits in the binary representation of <script type="math/tex; mode=display">N</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
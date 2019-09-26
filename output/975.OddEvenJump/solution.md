<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-monotonic-stack">Approach 1: Monotonic Stack</a></li>
<li><a href="#approach-2-tree-map">Approach 2: Tree Map</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-monotonic-stack">Approach 1: Monotonic Stack</h4>
<p><strong>Intuition</strong></p>
<p>First, we notice that where you jump to is determined only by the state of your current index and the jump number parity.</p>
<p>For each state, there is exactly one state you could jump to (or you can't jump.)  If we somehow knew these jumps, we could solve the problem by a simple traversal.</p>
<p>So the problem reduces to solving this question: for some index <code>i</code> during an odd numbered jump, what index do we jump to (if any)?  The question for even-numbered jumps is similar.</p>
<p><strong>Algorithm</strong></p>
<p>Let's figure out where index <code>i</code> jumps to, assuming this is an odd-numbered jump.</p>
<p>Let's consider each value of <code>A</code> in order from smallest to largest.  When we consider a value <code>A[j] = v</code>, we search the values we have already processed (which are <code>&lt;= v</code>) from largest to smallest.  If we find that we have already processed some value <code>v0 = A[i]</code> with <code>i &lt; j</code>, then we know <code>i</code> jumps to <code>j</code>.</p>
<p>Naively this is a little slow, but we can speed this up with a common trick for harder problems: a monotonic stack.  (For another example of this technique, please see the solution to this problem: <a href="https://leetcode.com/articles/sum-of-subarray-minimums/">(Article - Sum of Subarray Minimums)</a>)</p>
<p>Let's store the indices <code>i</code> of the processed values <code>v0 = A[i]</code> in a stack, and maintain the invariant that this is monotone decreasing.  When we add a new index <code>j</code>, we pop all the smaller indices <code>i &lt; j</code> from the stack, which all jump to <code>j</code>.</p>
<p>Afterwards, we know <code>oddnext[i]</code>, the index where <code>i</code> jumps to if this is an odd numbered jump.  Similarly, we know <code>evennext[i]</code>.  We can use this information to quickly build out all reachable states using dynamic programming.</p>
<iframe src="https://leetcode.com/playground/fYvxEXx8/shared" frameborder="0" width="100%" height="500" name="fYvxEXx8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-tree-map">Approach 2: Tree Map</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach 1</em>, the problem reduces to solving this question: for some index <code>i</code> during an odd numbered jump, what index do we jump to (if any)?</p>
<p><strong>Algorithm</strong></p>
<p>We can use a <code>TreeMap</code>, which is an excellent structure for maintaining sorted data.  Our map <code>vals</code> will map values <code>v = A[i]</code> to indices <code>i</code>.</p>
<p>Iterating from <code>i = N-2</code> to <code>i = 0</code>, we have some value <code>v = A[i]</code> and we want to know what the next largest or next smallest value is.  The <code>TreeMap.lowerKey</code> and <code>TreeMap.higherKey</code> functions do this for us.</p>
<p>With this in mind, the rest of the solution is straightforward: we use dynamic programming to maintain <code>odd[i]</code> and <code>even[i]</code>: whether the state of being at index <code>i</code> on an odd or even numbered jump is possible to reach.</p>
<iframe src="https://leetcode.com/playground/RtJL4zUR/shared" frameborder="0" width="100%" height="500" name="RtJL4zUR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-next-array-accepted">Approach #1: Next Array [Accepted]</a></li>
<li><a href="#approach-2-stack-accepted">Approach #2: Stack [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-next-array-accepted">Approach #1: Next Array [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>The problem statement asks us to find the next occurrence of a warmer temperature.  Because temperatures can only be in <code>[30, 100]</code>, if the temperature right now is say, <code>T[i] = 50</code>, we only need to check for the next occurrence of <code>51</code>, <code>52</code>, ..., <code>100</code> and take the one that occurs soonest.</p>
<p><strong>Algorithm</strong></p>
<p>Let's process each <code>i</code> in reverse (decreasing order).  At each <code>T[i]</code>, to know when the next occurrence of say, temperature <code>100</code> is, we should just remember the last one we've seen, <code>next[100]</code>.</p>
<p>Then, the first occurrence of a warmer value occurs at <code>warmer_index</code>, the minimum of <code>next[T[i]+1], next[T[i]+2], ..., next[100]</code>.</p>
<iframe src="https://leetcode.com/playground/zXoveQ5r/shared" frameborder="0" width="100%" height="361" name="zXoveQ5r"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(NW)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>T</code> and <script type="math/tex; mode=display">W</script> is the number of allowed values for <code>T[i]</code>.  Since <script type="math/tex; mode=display">W = 71</script>, we can consider this complexity <script type="math/tex; mode=display">O(N)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N + W)</script>, the size of the answer and the next array.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-stack-accepted">Approach #2: Stack [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Consider trying to find the next warmer occurrence at <code>T[i]</code>.  What information (about <code>T[j]</code> for <code>j &gt; i</code>) must we remember?</p>
<p>Say we are trying to find <code>T[0]</code>.  If we remembered <code>T[10] = 50</code>, knowing <code>T[20] = 50</code> wouldn't help us, as any <code>T[i]</code> that has its next warmer ocurrence at <code>T[20]</code> would have it at <code>T[10]</code> instead.  However, <code>T[20] = 100</code> would help us, since if <code>T[0]</code> were <code>80</code>, then <code>T[20]</code> might be its next warmest occurrence, while <code>T[10]</code> couldn't.</p>
<p>Thus, we should remember a list of indices representing a strictly increasing list of temperatures.  For example, <code>[10, 20, 30]</code> corresponding to temperatures <code>[50, 80, 100]</code>.  When we get a new temperature like <code>T[i] = 90</code>, we will have <code>[5, 30]</code> as our list of indices (corresponding to temperatures <code>[90, 100]</code>).  The most basic structure that will satisfy our requirements is a <em>stack</em>, where the top of the stack is the first value in the list, and so on.</p>
<p><strong>Algorithm</strong></p>
<p>As in <em>Approach #1</em>, process indices <code>i</code> in descending order.  We'll keep a <code>stack</code> of indices such that <code>T[stack[-1]] &lt; T[stack[-2]] &lt; ...</code>, where <code>stack[-1]</code> is the top of the stack, <code>stack[-2]</code> is second from the top, and so on; and where <code>stack[-1] &gt; stack[-2] &gt; ...</code>; and we will maintain this invariant as we process each temperature.</p>
<p>After, it is easy to know the next occurrence of a warmer temperature: it's simply the top index in the stack.</p>
<p>Here is a worked example of the contents of the <code>stack</code> as we work through <code>T = [73, 74, 75, 71, 69, 72, 76, 73]</code> in reverse order, at the end of the loop (after we add <code>T[i]</code>).  For clarity, <code>stack</code> only contains indices <code>i</code>, but we will write the value of <code>T[i]</code> beside it in brackets, such as <code>0 (73)</code>.</p>
<ul>
<li>When <code>i = 7</code>, <code>stack = [7 (73)]</code>.  <code>ans[i] = 0</code>.</li>
<li>When <code>i = 6</code>, <code>stack = [6 (76)]</code>.  <code>ans[i] = 0</code>.</li>
<li>When <code>i = 5</code>, <code>stack = [5 (72), 6 (76)]</code>.  <code>ans[i] = 1</code>.</li>
<li>When <code>i = 4</code>, <code>stack = [4 (69), 5 (72), 6 (76)]</code>.  <code>ans[i] = 1</code>.</li>
<li>When <code>i = 3</code>, <code>stack = [3 (71), 5 (72), 6 (76)]</code>.  <code>ans[i] = 2</code>.</li>
<li>When <code>i = 2</code>, <code>stack = [2 (75), 6 (76)]</code>.  <code>ans[i] = 4</code>.</li>
<li>When <code>i = 1</code>, <code>stack = [1 (74), 2 (75), 6 (76)]</code>.  <code>ans[i] = 1</code>.</li>
<li>When <code>i = 0</code>, <code>stack = [0 (73), 1 (74), 2 (75), 6 (76)]</code>.  <code>ans[i] = 1</code>.</li>
</ul>
<iframe src="https://leetcode.com/playground/GrKNCrcf/shared" frameborder="0" width="100%" height="259" name="GrKNCrcf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>T</code> and <script type="math/tex; mode=display">W</script> is the number of allowed values for <code>T[i]</code>.  Each index gets pushed and popped at most once from the stack.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(W)</script>.  The size of the stack is bounded as it represents strictly increasing temperatures.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
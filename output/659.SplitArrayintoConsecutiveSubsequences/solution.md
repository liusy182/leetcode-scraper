<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-opening-and-closing-events-accepted">Approach #1: Opening and Closing Events [Accepted]</a></li>
<li><a href="#approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-opening-and-closing-events-accepted">Approach #1: Opening and Closing Events [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We can think of the problem as drawing intervals on a number line.  This gives us the idea of opening and closing events.</p>
<p>To illustrate this concept, say we have <code>nums = [10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13]</code>, with no <code>9</code>s and no <code>14</code>s.  We must have two sequences start at 10, two sequences start at 11, and 3 sequences end at 12.</p>
<p>In general, when considering a chain of consecutive integers <code>x</code>, we must have <code>C = count[x+1] - count[x]</code> sequences start at <code>x+1</code> when <code>C &gt; 0</code>, and <code>-C</code> sequences end at <code>x</code> if <code>C &lt; 0</code>.  Even if there are more endpoints on the intervals we draw, there must be at least this many endpoints.</p>
<p>With the above example, <code>count[11] - count[10] = 2</code> and <code>count[13] - count[12] = -3</code> show that two sequences start at <code>11</code>, and three sequences end at <code>12</code>.</p>
<p>Also, if for example we know some sequences must start at time <code>1</code> and <code>4</code> and some sequences end at <code>5</code> and <code>7</code>, to maximize the smallest length sequence, we should pair the events together in the order they occur: ie., <code>1</code> with <code>5</code> and <code>4</code> with <code>7</code>.</p>
<p><strong>Algorithm</strong></p>
<p>For each group of numbers, say the number is <code>x</code> and there are <code>count</code> of them.  Furthermore, say <code>prev, prev_count</code> is the previous integer encountered and it's count.</p>
<p>Then, in general there are <code>abs(count - prev_count)</code> events that will happen: if <code>count &gt; prev_count</code> then we will add this many <code>t</code>'s to <code>starts</code>; and if <code>count &lt; prev_count</code> then we will attempt to pair <code>starts.popleft()</code> with <code>t-1</code>.</p>
<p>More specifically, when we have finished a consecutive group, we will have <code>prev_count</code> endings; and when we are in a consecutive group, we may have <code>count - prev_count</code> starts or <code>prev_count - count</code> endings.</p>
<p>For example, when <code>nums = [1,2,3,3,4,5]</code>, then the starts are at <code>[1, 3]</code> and the endings are at <code>[3, 5]</code>.  As our algorithm progresses:</p>
<ul>
<li>When <code>t = 1, count = 1</code>: <code>starts = [1]</code></li>
<li>When <code>t = 2, count = 1</code>: <code>starts = [1]</code></li>
<li>When <code>t = 3, count = 2</code>: <code>starts = [1, 3]</code></li>
<li>When <code>t = 4, count = 1</code>: <code>starts = [3]</code>, since <code>prev_count - count = 1</code> we process one closing event, which is accepted as <code>t-1 &gt;= starts.popleft() + 2</code>.</li>
<li>When <code>t = 5, count = 1</code>: <code>starts = [3]</code></li>
</ul>
<p>And at the end, we process <code>prev_count</code> more closing events <code>nums[-1]</code>.</p>
<iframe src="https://leetcode.com/playground/aPKnzzAo/shared" frameborder="0" width="100%" height="500" name="aPKnzzAo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  We iterate over the array and every event is added or popped to <code>starts</code> at most once.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>starts</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-greedy-accepted">Approach #2: Greedy [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Call a <em>chain</em> a sequence of 3 or more consecutive numbers.</p>
<p>Considering numbers <code>x</code> from left to right, if <code>x</code> can be added to a current chain, it's at least as good to add <code>x</code> to that chain first, rather than to start a new chain.</p>
<p>Why?  If we started with numbers <code>x</code> and greater from the beginning, the shorter chains starting from <code>x</code> could be concatenated with the chains ending before <code>x</code>, possibly helping us if there was a "chain" from <code>x</code> that was only length 1 or 2.</p>
<p><strong>Algorithm</strong></p>
<p>Say we have a count of each number, and let <code>tails[x]</code> be the number of chains ending right before <code>x</code>.</p>
<p>Now let's process each number.  If there's a chain ending before <code>x</code>, then add it to that chain.  Otherwise, if we can start a new chain, do so.</p>
<p>It's worth noting that our solution can be amended to take only <script type="math/tex; mode=display">O(1)</script> additional space, since we could do our counts similar to <em>Approach #1</em>, and we only need to know the last 3 counts at a time.</p>
<iframe src="https://leetcode.com/playground/RErfKTGx/shared" frameborder="0" width="100%" height="500" name="RErfKTGx"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  We iterate over the array.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of <code>count</code> and <code>tails</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approach #2 inspired by <a href="https://discuss.leetcode.com/topic/99187/java-o-n-time-o-n-space">@compton_scatter</a>.</p>
          </div>
        
      </div>
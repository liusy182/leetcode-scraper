<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
<li><a href="#approach-2-balanced-tree-accepted">Approach #2: Balanced Tree [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>When booking a new event <code>[start, end)</code>, check if every current event conflicts with the new event.  If none of them do, we can book the event.</p>
<p><strong>Algorithm</strong></p>
<p>We will maintain a list of interval <em>events</em> (not necessarily sorted).  Evidently, two events <code>[s1, e1)</code> and <code>[s2, e2)</code> do <em>not</em> conflict if and only if one of them starts after the other one ends: either <code>e1 &lt;= s2</code> OR <code>e2 &lt;= s1</code>.  By De Morgan's laws, this means the events conflict when <code>s1 &lt; e2</code> AND <code>s2 &lt; e1</code>.</p>
<iframe src="https://leetcode.com/playground/RbxQb2Zj/shared" frameborder="0" width="100%" height="310" name="RbxQb2Zj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the number of events booked.  For each new event, we process every previous event to decide whether the new event can be booked.  This leads to <script type="math/tex; mode=display">\sum_k^N O(k) = O(N^2)</script> complexity.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of the <code>calendar</code>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-balanced-tree-accepted">Approach #2: Balanced Tree [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>If we maintained our events in <em>sorted</em> order, we could check whether an event could be booked in <script type="math/tex; mode=display">O(\log N)</script> time (where <script type="math/tex; mode=display">N</script> is the number of events already booked) by binary searching for where the event should be placed.  We would also have to insert the event in our sorted structure.</p>
<p><strong>Algorithm</strong></p>
<p>We need a data structure that keeps elements sorted and supports fast insertion.  In Java, a <code>TreeMap</code> is the perfect candidate.  In Python, we can build our own binary tree structure.</p>
<p>For Java, we will have a <code>TreeMap</code> where the keys are the start of each interval, and the values are the ends of those intervals.  When inserting the interval <code>[start, end)</code>, we check if there is a conflict on each side with neighboring intervals: we would like <code>calendar.get(prev)) &lt;= start &lt;= end &lt;= next</code> for the booking to be valid (or for <code>prev</code> or <code>next</code> to be null respectively.)</p>
<p>For Python, we will create a binary tree.  Each node represents some interval <code>[self.start, self.end)</code> while <code>self.left, self.right</code> represents nodes that are smaller or larger than the current node.</p>
<iframe src="https://leetcode.com/playground/huRxLsMu/shared" frameborder="0" width="100%" height="500" name="huRxLsMu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity (Java): <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of events booked.  For each new event, we search that the event is legal in <script type="math/tex; mode=display">O(\log N)</script> time, then insert it in <script type="math/tex; mode=display">O(1)</script> time.</p>
</li>
<li>
<p>Time Complexity (Python): <script type="math/tex; mode=display">O(N^2)</script> worst case, with <script type="math/tex; mode=display">O(N \log N)</script> on random data.  For each new event, we insert the event into our binary tree.  As this tree may not be balanced, it may take a linear number of steps to add each event.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of the data structures used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Solutions in Approach #2 inspired by <a href="https://discuss.leetcode.com/topic/111205/java-8-liner-treemap">@shawngao</a> and  <a href="https://discuss.leetcode.com/topic/111203/binary-search-tree-python">@persianPanda</a>.</p>
          </div>
        
      </div>
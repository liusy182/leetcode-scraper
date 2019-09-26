<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
<li><a href="#approach-2-segment-tree">Approach 2: Segment Tree</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Suppose for sequences ending at <code>nums[i]</code>, we knew the length <code>length[i]</code> of the longest sequence, and the number <code>count[i]</code> of such sequences with that length.</p>
<p>For every <code>i &lt; j</code> with <code>A[i] &lt; A[j]</code>, we might append <code>A[j]</code> to a longest subsequence ending at <code>A[i]</code>.  It means that we have demonstrated <code>count[i]</code> subsequences of length <code>length[i] + 1</code>.  </p>
<p>Now, if those sequences are longer than <code>length[j]</code>, then we know we have <code>count[i]</code> sequences of this length.  If these sequences are equal in length to <code>length[j]</code>, then we know that there are now <code>count[i]</code> additional sequences to be counted of that length (ie. <code>count[j] += count[i]</code>).</p>
<iframe src="https://leetcode.com/playground/NY6NUMPF/shared" frameborder="0" width="100%" height="500" name="NY6NUMPF"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script> where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  There are two for-loops and the work inside is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by <code>lengths</code> and <code>counts</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-segment-tree">Approach 2: Segment Tree</h4>
<p><strong>Intuition</strong></p>
<p>Suppose we knew for each length <code>L</code>, the number of sequences with length <code>L</code> ending in <code>x</code>.  Then when considering the next element of <code>nums</code>, updating our knowledge hinges on knowing the number of sequences with length <code>L-1</code> ending in <code>y &lt; x</code>.  This type of query over an interval is a natural fit for using some sort of tree.</p>
<p>We could try using Fenwick trees, but we would have to store <script type="math/tex; mode=display">N</script> of them, which naively might be <script type="math/tex; mode=display">O(N^2)</script> space.  Here, we focus on an implementation of a Segment Tree.</p>
<p><strong>Algorithm</strong></p>
<p>Implementing Segment Trees is discussed in more detail <a href="https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/">here</a>.  In this approach, we will attempt a variant of segment tree that doesn't use lazy propagation.</p>
<p>First, let us call the "value" of an interval, the longest length of an increasing subsequence, and the number of such subsequences in that interval.</p>
<p>Each node knows about the interval of <code>nums</code> values it is considering <code>[node.range_left, node.range_right]</code>, and it knows about <code>node.val</code>, which contains information on the value of interval.  Nodes also have <code>node.left</code> and <code>node.right</code> children that represents the left and right half of the interval <code>node</code> considers.  These child nodes are created on demand as appropriate.</p>
<p>Now, <code>query(node, key)</code> will tell us the value of the interval specified by <code>node</code>, except we'll exclude anything above <code>key</code>.  When key is outside the interval specified by <code>node</code>, we return the answer.  Otherwise, we'll divide the interval into two and query both intervals, then <code>merge</code> the result.</p>
<p>What does <code>merge(v1, v2)</code> do?  Suppose two nodes specify adjacent intervals, and have corresponding values <code>v1 = node1.val, v2 = node2.val</code>.  What should the aggregate value, <code>v = merge(v1, v2)</code> be?  If there are longer subsequences in one node, then <code>v</code> will just be that.  If both nodes have longest subsequences of equal length, then we should count subsequences in both nodes.  Note that we did not have to consider cases where larger subsequences were made, since these were handled by <code>insert</code>.</p>
<p>What does <code>insert(node, key, val)</code> do?  We repeatedly insert the <code>key</code> into the correct half of the interval that <code>node</code> specifies (possibly a point), and after such insertion this node's value could change, so we merge the values together again.</p>
<p>Finally, in our main algorithm, for each <code>num in nums</code> we <code>query</code> for the value <code>length, count</code> of the interval below <code>num</code>, and we know it will lead to <code>count</code> additional sequences of length <code>length + 1</code>.  We then update our tree with that knowledge.</p>
<iframe src="https://leetcode.com/playground/JqcEDf3A/shared" frameborder="0" width="100%" height="500" name="JqcEDf3A"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N\log {N})</script> where <script type="math/tex; mode=display">N</script> is the length of <code>nums</code>.  In our main for loop, we do <script type="math/tex; mode=display">O(\log{N})</script> work to <code>query</code> and <code>insert</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by the segment tree.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approach 2 inspired by <a href="https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/107307/python-dp-segment_tree-onlogn">@dut200901102</a>.</p>
          </div>
        
      </div>
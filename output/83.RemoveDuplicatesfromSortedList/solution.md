<div class="article-body">
        
          <div class="block-markdown">
            <h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-straight-forward-approach">Approach 1: Straight-Forward Approach</h4>
<p><strong>Algorithm</strong></p>
<p>This is a simple problem that merely tests your ability to manipulate list node pointers. Because the input list is sorted, we can determine if a node is a duplicate by comparing its value to the node <em>after</em> it in the list. If it is a duplicate, we change the <code>next</code> pointer of the current node so that it skips the next node and points directly to the one after the next node.</p>
<iframe src="https://leetcode.com/playground/KHvbA6CF/shared" frameborder="0" width="100%" height="242" name="KHvbA6CF"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n</script> is the number of nodes in the list.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. No additional space is used.</p>
</li>
</ul>
<p><strong>Correctness</strong></p>
<p>We can prove the correctness of this code by defining a <em>loop invariant</em>. A loop invariant is condition that is true before and after every iteration of the loop. In this case, a loop invariant that helps us prove correctness is this:</p>
<blockquote>
<p>All nodes in the list up to the pointer <code>current</code> do not contain duplicate elements.</p>
</blockquote>
<p>We can prove that this condition is indeed a loop invariant by induction. Before going into the loop, <code>current</code> points to the head of the list. Therefore, the part of the list up to <code>current</code> contains only the head. And so it can not contain any duplicate elements. Now suppose <code>current</code> is now pointing to some node in the list (but not the last element), and the part of the list up to <code>current</code> contains no duplicate elements. After another loop iteration, one of two things happen.</p>
<ol>
<li>
<p><code>current.next</code> was a duplicate of <code>current</code>. In this case, the duplicate node at <code>current.next</code> is deleted, and <code>current</code> stays pointing to the same node as before. Therefore, the condition still holds; there are still no duplicates up to <code>current</code>.</p>
</li>
<li>
<p><code>current.next</code> was not a duplicate of <code>current</code> (and, because the list is sorted, <code>current.next</code> is also not a duplicate of any other element appearing <em>before</em> <code>current</code>). In this case, <code>current</code> moves forward one step to point to <code>current.next</code>. Therefore, the condition still holds; there are no duplicates up to <code>current</code>.</p>
</li>
</ol>
<p>At the last iteration of the loop, <code>current</code> must point to the last element, because afterwards, <code>current.next = null</code>. Therefore, after the loop ends, all elements up to the last element do not contain duplicates.</p>
          </div>
        
      </div>
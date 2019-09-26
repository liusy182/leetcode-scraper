<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-hash-table">Approach 1: Hash Table</a></li>
<li><a href="#approach-2-two-pointers">Approach 2: Two Pointers</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for beginners. It introduces the following ideas: Linked List, Hash Table and Two Pointers.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-hash-table">Approach 1: Hash Table</h4>
<p><strong>Intuition</strong></p>
<p>To detect if a list is cyclic, we can check whether a node had been visited before. A natural way is to use a hash table.</p>
<p><strong>Algorithm</strong></p>
<p>We go through each node one by one and record each node's reference (or memory address) in a hash table. If the current node is <code>null</code>, we have reached the end of the list and it must not be cyclic. If current node’s reference is in the hash table, then return true.</p>
<iframe src="https://leetcode.com/playground/3tqYc6gz/shared" frameborder="0" width="100%" height="259" name="3tqYc6gz"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
We visit each of the <script type="math/tex; mode=display">n</script> elements in the list at most once. Adding a node to the hash table costs only <script type="math/tex; mode=display">O(1)</script> time.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script>.
The space depends on the number of elements added to the hash table, which contains at most <script type="math/tex; mode=display">n</script> elements.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pointers">Approach 2: Two Pointers</h4>
<p><strong>Intuition</strong></p>
<p>Imagine two runners running on a track at different speed. What happens when the track is actually a circle?</p>
<p><strong>Algorithm</strong></p>
<p>The space complexity can be reduced to <script type="math/tex; mode=display">O(1)</script> by considering two pointers at <strong>different speed</strong> - a slow pointer and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two steps at a time.</p>
<p>If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.</p>
<p>Now consider a cyclic list and imagine the slow and fast pointers are two runners racing around a circle track. The fast runner will eventually meet the slow runner. Why? Consider this case (we name it case A) - The fast runner is just one step behind the slow runner. In the next iteration, they both increment one and two steps respectively and meet each other.</p>
<p>How about other cases? For example, we have not considered cases where the fast runner is two or three steps behind the slow runner yet. This is simple, because in the next or next's next iteration, this case will be reduced to case A mentioned above.</p>
<iframe src="https://leetcode.com/playground/B6ffJ2Xk/shared" frameborder="0" width="100%" height="310" name="B6ffJ2Xk"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
Let us denote <script type="math/tex; mode=display">n</script> as the total number of nodes in the linked list. To analyze its time complexity, we consider the following two cases separately.</p>
<ul>
<li>
<p><strong><em>List has no cycle:</em></strong><br>
The fast pointer reaches the end first and the run time depends on the list's length, which is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p><strong><em>List has a cycle:</em></strong><br>
We break down the movement of the slow pointer into two steps, the non-cyclic part and the cyclic part:</p>
<ol>
<li>
<p>The slow pointer takes "non-cyclic length" steps to enter the cycle. At this point, the fast pointer has already reached the cycle. <script type="math/tex; mode=display">\text{Number of iterations} = \text{non-cyclic length} = N</script>
</p>
</li>
<li>
<p>Both pointers are now in the cycle. Consider two runners running in a cycle - the fast runner moves 2 steps while the slow runner moves 1 steps at a time. Since the speed difference is 1, it takes <script type="math/tex; mode=display">\dfrac{\text{distance between the 2 runners}}{\text{difference of speed}}</script> loops for the fast runner to catch up with the slow runner. As the distance is at most "<script type="math/tex; mode=display">\text{cyclic length K}</script>" and the speed difference is 1, we conclude that    <br>
<script type="math/tex; mode=display">\text{Number of iterations} = \text{almost}</script> "<script type="math/tex; mode=display">\text{cyclic length K}</script>".</p>
</li>
</ol>
</li>
</ul>
<p>Therefore, the worst case time complexity is <script type="math/tex; mode=display">O(N+K)</script>, which is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
We only use two nodes (slow and fast) so the space complexity is <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-two-pass-algorithm">Approach 1: Two pass algorithm</a></li>
<li><a href="#approach-2-one-pass-algorithm">Approach 2: One pass algorithm</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for beginners. It introduces the following idea:
Linked List traversal and removal of nth element from the end.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-two-pass-algorithm">Approach 1: Two pass algorithm</h4>
<p><strong>Intuition</strong></p>
<p>We notice that the problem could be simply reduced to another one : Remove the <script type="math/tex; mode=display">(L - n + 1)</script> th node from the beginning in the list , where <script type="math/tex; mode=display">L</script> is the list length. This problem is easy to solve once we found list length <script type="math/tex; mode=display">L</script>.</p>
<p><strong>Algorithm</strong></p>
<p>First we will add an auxiliary "dummy" node, which points to the list head. The "dummy" node is used to simplify some corner cases such as a list with only one node, or removing the head of the list. On the first pass, we find the list length <script type="math/tex; mode=display">L</script>. Then we set a pointer to the dummy node and start to move it through the list till it comes to the <script type="math/tex; mode=display">(L - n)</script> th node. We relink <code>next</code> pointer of the <script type="math/tex; mode=display">(L - n)</script> th node to the <script type="math/tex; mode=display">(L - n + 2)</script> th node and we are done.</p>
<p align="center"><img alt="Remove the nth element from a list" src="https://leetcode.com/media/original_images/19_Remove_nth_node_from_end_of_listA.png"></p>
<p align="center"><em>Figure 1. Remove the L - n + 1 th element from a list.</em></p>
<iframe src="https://leetcode.com/playground/mjMSbADc/shared" frameborder="0" width="100%" height="361" name="mjMSbADc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(L)</script>.</p>
<p>The algorithm makes two traversal of the list, first to calculate list length <script type="math/tex; mode=display">L</script> and second to find the <script type="math/tex; mode=display">(L - n)</script> th node. There are <script type="math/tex; mode=display">2L-n</script> operations and time complexity is <script type="math/tex; mode=display">O(L)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>We only used constant extra space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-one-pass-algorithm">Approach 2: One pass algorithm</h4>
<p><strong>Algorithm</strong></p>
<p>The above algorithm could be optimized to one pass. Instead of one pointer, we could use two pointers. The first pointer advances the list by <script type="math/tex; mode=display">n+1</script> steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by <script type="math/tex; mode=display">n</script> nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. The second pointer will be pointing at the <script type="math/tex; mode=display">n</script>th node counting from the last.
We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.</p>
<p align="center"><img alt="Remove the nth element from a list" src="https://leetcode.com/media/original_images/19_Remove_nth_node_from_end_of_listB.png"></p>
<p align="center"><em>Figure 2. Remove the nth element from end of a list.</em></p>
<iframe src="https://leetcode.com/playground/BPxLi8Wz/shared" frameborder="0" width="100%" height="344" name="BPxLi8Wz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(L)</script>.</p>
<p>The algorithm makes one traversal of the list of <script type="math/tex; mode=display">L</script> nodes. Therefore time complexity is <script type="math/tex; mode=display">O(L)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
<p>We only used constant extra space.</p>
</li>
</ul>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursive">Approach 1: Recursive</h4>
<p>A tree is symmetric if the left subtree is a mirror reflection of the right subtree.</p>
<p align="center"><img alt="Push an element in stack" src="https://leetcode.com/media/original_images/101_Symmetric.png" width="200px"></p>
<p>Therefore, the question is: when are two trees a mirror reflection of each other?</p>
<p>Two trees are a mirror reflection of each other if:</p>
<ol>
<li>Their two roots have the same value.</li>
<li>The right subtree of each tree is a mirror reflection of the left subtree of the other tree.</li>
</ol>
<p align="center"><img alt="Push an element in stack" src="https://leetcode.com/media/original_images/101_Symmetric_Mirror.png" width="400px"></p>
<p>This is like a person looking at a mirror. The reflection in the mirror has the same head, but the reflection's right arm corresponds to the actual person's left arm, and vice versa.</p>
<p>The explanation above translates naturally to a recursive function as follows.</p>
<iframe src="https://leetcode.com/playground/bQ9ZjXvv/shared" frameborder="0" width="100%" height="242" name="bQ9ZjXvv"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Because we traverse the entire input tree once, the total run time is <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n</script> is the total number of nodes in the tree.</p>
</li>
<li>
<p>Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in <script type="math/tex; mode=display">O(n)</script>. Therefore, space complexity due to recursive calls on the stack is <script type="math/tex; mode=display">O(n)</script> in the worst case.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-iterative">Approach 2: Iterative</h4>
<p>Instead of recursion, we can also use iteration with the aid of a queue. Each two consecutive nodes in the queue should be equal, and their subtrees a mirror of each other. Initially, the queue contains <code>root</code> and <code>root</code>. Then the algorithm works similarly to BFS, with some key differences. Each time, two nodes are extracted and their values compared. Then, the right and left children of the two nodes are inserted in the queue in opposite order. The algorithm is done when either the queue is empty, or we detect that the tree is not symmetric (i.e. we pull out two consecutive nodes from the queue that are unequal).</p>
<iframe src="https://leetcode.com/playground/n5mXkUjQ/shared" frameborder="0" width="100%" height="344" name="n5mXkUjQ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Because we traverse the entire input tree once, the total run time is <script type="math/tex; mode=display">O(n)</script>, where <script type="math/tex; mode=display">n</script> is the total number of nodes in the tree.</p>
</li>
<li>
<p>Space complexity : There is additional space required for the search queue. In the worst case, we have to insert <script type="math/tex; mode=display">O(n)</script> nodes in the queue. Therefore, space complexity is <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
</ul>
          </div>
        
      </div>
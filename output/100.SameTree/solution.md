<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-iteration">Approach 2: Iteration</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>The simplest strategy here is to use recursion. 
Check if <code>p</code> and <code>q</code> nodes are not <code>None</code>, and their values are equal.
If all checks are OK, do the same for the child nodes
recursively.</p>
<p><strong>Implementation</strong></p>
<p>!?!../Documents/100_LIS.json:1000,373!?!</p>
<iframe src="https://leetcode.com/playground/CtxuC6Za/shared" frameborder="0" width="100%" height="395" name="CtxuC6Za"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script>, 
where N is a number of nodes in the tree, since one visits
each node exactly once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(\log(N))</script> in the best case of completely 
balanced tree and <script type="math/tex; mode=display">\mathcal{O}(N)</script> in the worst case
of completely unbalanced tree, to keep a recursion stack.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-iteration">Approach 2: Iteration</h4>
<p><strong>Intuition</strong></p>
<p>Start from the root and then at each iteration 
pop the current node out of the deque. Then do the same checks as in
 the approach 1 :</p>
<ul>
<li>
<p><code>p</code> and <code>p</code> are not <code>None</code>, </p>
</li>
<li>
<p><code>p.val</code> is equal to <code>q.val</code>,</p>
</li>
</ul>
<p>and if checks are OK, push the child nodes. </p>
<p><strong>Implementation</strong></p>
<iframe src="https://leetcode.com/playground/e9Z7Jfqf/shared" frameborder="0" width="100%" height="500" name="e9Z7Jfqf"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(N)</script> since each node is visited
exactly once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(\log(N))</script> in the best case of completely 
balanced tree and <script type="math/tex; mode=display">\mathcal{O}(N)</script> in the worst case
of completely unbalanced tree, to keep a deque.</p>
</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>
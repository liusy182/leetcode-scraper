<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-greedy">Approach 1: Greedy</a></li>
<li><a href="#approach-2-heap">Approach 2: Heap</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-greedy">Approach 1: Greedy</h4>
<p><strong>Intuition</strong></p>
<p>At least one worker will be paid their minimum wage expectation.  If not, we could scale all payments down by some factor and still keep everyone earning more than their wage expectation.</p>
<p><strong>Algorithm</strong></p>
<p>For each <code>captain</code> worker that will be paid their minimum wage expectation, let's calculate the cost of hiring K workers where each point of quality is worth <code>wage[captain] / quality[captain]</code> dollars.  With this approach, the remaining implementation is straightforward.</p>
<p>Note that this algorithm would not be efficient enough to pass larger test cases.</p>
<iframe src="https://leetcode.com/playground/6wfBasLL/shared" frameborder="0" width="100%" height="500" name="6wfBasLL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2 \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of workers.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-heap">Approach 2: Heap</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, at least one worker is paid their minimum wage expectation.</p>
<p>Additionally, every worker has some minimum <code>ratio</code> of dollars to quality that they demand.  For example, if <code>wage[0] = 100</code> and <code>quality[0] = 20</code>, then the <code>ratio</code> for worker 0 is <code>5.0</code>.</p>
<p>The key insight is to iterate over the ratio.  Let's say we hire workers with a ratio <code>R</code> or lower.  Then, we would want to know the <code>K</code> workers with the lowest quality, and the sum of that quality.  We can use a heap to maintain these variables.</p>
<p><strong>Algorithm</strong></p>
<p>Maintain a max heap of quality.  (We're using a minheap, with negative values.)  We'll also maintain <code>sumq</code>, the sum of this heap.</p>
<p>For each worker in order of ratio, we know all currently considered workers have lower ratio.  (This worker will be the 'captain', as described in <em>Approach #1</em>.)  We calculate the candidate answer as this ratio times the sum of the smallest K workers in quality.</p>
<iframe src="https://leetcode.com/playground/KRXJr8dq/shared" frameborder="0" width="100%" height="500" name="KRXJr8dq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of workers.</p>
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
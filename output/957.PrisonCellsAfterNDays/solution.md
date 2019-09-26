<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-simulation">Approach 1: Simulation</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-simulation">Approach 1: Simulation</h4>
<p><strong>Intuition</strong></p>
<p>We simulate each day of the prison.</p>
<p>Because there are at most 256 possible states for the prison, eventually the states repeat into a cycle rather quickly.  We can keep track of when the states repeat to find the period <code>t</code> of this cycle, and skip days in multiples of <code>t</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's do a naive simulation, iterating one day at a time.  For each day, we will decrement <code>N</code>, the number of days remaining, and transform the state of the prison forward (<code>state -&gt; nextDay(state)</code>).</p>
<p>If we reach a state we have seen before, we know how many days ago it occurred, say <code>t</code>.  Then, because of this cycle, we can do <code>N %= t</code>.  This ensures that our algorithm only needs <script type="math/tex; mode=display">O(2**{\text{cells.length}})</script> steps.</p>
<iframe src="https://leetcode.com/playground/HKcoATQ8/shared" frameborder="0" width="100%" height="500" name="HKcoATQ8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^N)</script>, where <script type="math/tex; mode=display">N</script> is the number of cells in the prison.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(2^N * N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
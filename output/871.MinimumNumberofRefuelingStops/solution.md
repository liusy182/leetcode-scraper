<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming">Approach 1: Dynamic Programming</a></li>
<li><a href="#approach-2-heap">Approach 2: Heap</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming">Approach 1: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>Let's determine <code>dp[i]</code>, the farthest location we can get to using <code>i</code> refueling stops.  This is motivated by the fact that we want the smallest <code>i</code> for which <code>dp[i] &gt;= target</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Let's update <code>dp</code> as we consider each station in order.  With no stations, clearly we can get a maximum distance of <code>startFuel</code> with <code>0</code> refueling stops.</p>
<p>Now let's look at the update step.  When adding a station <code>station[i] = (location, capacity)</code>, any time we could reach this station with <code>t</code> refueling stops, we can now reach <code>capacity</code> further with <code>t+1</code> refueling stops.</p>
<p>For example, if we could reach a distance of 15 with 1 refueling stop, and now we added a station at location 10 with 30 liters of fuel, then we could potentially reach a distance of 45 with 2 refueling stops.</p>
<iframe src="https://leetcode.com/playground/CrpMSMbm/shared" frameborder="0" width="100%" height="310" name="CrpMSMbm"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>stations</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by <code>dp</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-heap">Approach 2: Heap</h4>
<p><strong>Intuition</strong></p>
<p>When driving past a gas station, let's remember the amount of fuel it contained.  We don't need to decide yet whether to fuel up here or not - for example, there could be a bigger gas station up ahead that we would rather refuel at.</p>
<p>When we run out of fuel before reaching the next station, we'll retroactively fuel up: greedily choosing the largest gas stations first.</p>
<p>This is guaranteed to succeed because we drive the largest distance possible before each refueling stop, and therefore have the largest choice of gas stations to (retroactively) stop at.</p>
<p><strong>Algorithm</strong></p>
<p><code>pq</code> ("priority queue") will be a max-heap of the capacity of each gas station we've driven by.  We'll also keep track of <code>tank</code>, our current fuel.</p>
<p>When we reach a station but have negative fuel (ie. we needed to have refueled at some point in the past), we will add the capacities of the largest gas stations we've driven by until the fuel is non-negative.</p>
<p>If at any point this process fails (that is, no more gas stations), then the task is impossible.</p>
<iframe src="https://leetcode.com/playground/k5wvzRam/shared" frameborder="0" width="100%" height="500" name="k5wvzRam"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>stations</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by <code>pq</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approach 1 inspired by @lee215.</p>
          </div>
        
      </div>
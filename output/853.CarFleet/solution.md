<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-sort">Approach 1: Sort</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-sort">Approach 1: Sort</h4>
<p><strong>Intuition</strong></p>
<p>Call the "lead fleet" the fleet furthest in position.</p>
<p>If the car <code>S</code> (Second) behind the lead car <code>F</code> (First) would arrive earlier, then <code>S</code> forms a fleet with the lead car <code>F</code>.  Otherwise, fleet <code>F</code> is final as no car can catch up to it - cars behind <code>S</code> would form fleets with <code>S</code>, never <code>F</code>.</p>
<p><strong>Algorithm</strong></p>
<p>A car is a <code>(position, speed)</code> which implies some arrival time <code>(target - position) / speed</code>.  Sort the cars by position.</p>
<p>Now apply the above reasoning - if the lead fleet drives away, then count it and continue.  Otherwise, merge the fleets and continue.</p>
<iframe src="https://leetcode.com/playground/L7RDfW2A/shared" frameborder="0" width="100%" height="497" name="L7RDfW2A"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log N)</script>, where <script type="math/tex; mode=display">N</script> is the number of cars.  The complexity is dominated by the sorting operation.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used to store information about the cars.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
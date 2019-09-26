<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-simulation-accepted">Approach #1: Simulation [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-simulation-accepted">Approach #1: Simulation [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>A senator performing a ban doesn't need to use it on another senator immediately.  We can wait to see when another team's senator will vote, then use that ban retroactively.</p>
<p><strong>Algorithm</strong></p>
<p>Put the senators in an integer queue: <code>1</code> for <code>'Radiant'</code> and <code>0</code> for <code>'Dire'</code>.</p>
<p>Now process the queue: if there is a floating ban for that senator, exercise it and continue.  Otherwise, add a floating ban against the other team, and enqueue this senator again.</p>
<iframe src="https://leetcode.com/playground/zdvGbwLN/shared" frameborder="0" width="100%" height="497" name="zdvGbwLN"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script> where <script type="math/tex; mode=display">N</script> is the size of the senate.  Every vote removes one senator from the other team.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space used by our queue.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
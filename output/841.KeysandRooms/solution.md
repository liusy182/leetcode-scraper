<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>When visiting a room for the first time, look at all the keys in that room.  For any key that hasn't been used yet, add it to the todo list (<code>stack</code>) for it to be used.</p>
<p>See the comments of the code for more details.</p>
<iframe src="https://leetcode.com/playground/DStbTdKq/shared" frameborder="0" width="100%" height="446" name="DStbTdKq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + E)</script>, where <script type="math/tex; mode=display">N</script> is the number of rooms, and <script type="math/tex; mode=display">E</script> is the total number of keys.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script> in additional space complexity, to store <code>stack</code> and <code>seen</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
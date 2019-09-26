<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-depth-first-search">Approach 1: Depth-First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-depth-first-search">Approach 1: Depth-First Search</h4>
<p><strong>Intuition</strong></p>
<p>It's natural to try to assign everyone to a group.  Let's say people in the first group are red, and people in the second group are blue.</p>
<p>If the first person is red, anyone disliked by this person must be blue.  Then, anyone disliked by a blue person is red, then anyone disliked by a red person is blue, and so on.</p>
<p>If at any point there is a conflict, the task is impossible, as every step logically follows from the first step.  If there isn't a conflict, then the coloring was valid, so the answer would be <code>true</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Consider the graph on <code>N</code> people formed by the given "dislike" edges.  We want to check that each connected component of this graph is bipartite.</p>
<p>For each connected component, we can check whether it is bipartite by just trying to coloring it with two colors.  How to do this is as follows: color any node red, then all of it's neighbors blue, then all of those neighbors red, and so on.  If we ever color a red node blue (or a blue node red), then we've reached a conflict.</p>
<iframe src="https://leetcode.com/playground/aD5rzLRZ/shared" frameborder="0" width="100%" height="500" name="aD5rzLRZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + E)</script>, where <script type="math/tex; mode=display">E</script> is the length of <code>dislikes</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N + E)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
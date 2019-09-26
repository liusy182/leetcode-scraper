<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-grouping-accepted">Approach #1: Grouping [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-grouping-accepted">Approach #1: Grouping [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>Instead of thinking about connected components in <code>G</code>, think about them in the linked list.  Connected components in <code>G</code> must occur consecutively in the linked list.</p>
<p><strong>Algorithm</strong></p>
<p>Scanning through the list, if <code>node.val</code> is in <code>G</code> and <code>node.next.val</code> isn't (including if <code>node.next</code> is <code>null</code>), then this must be the end of a connected component.</p>
<p>For example, if the list is <code>0 -&gt; 1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6 -&gt; 7</code>, and <code>G = [0, 2, 3, 5, 7]</code>, then when scanning through the list, we fulfill the above condition at <code>0, 3, 5, 7</code>, for a total answer of <code>4</code>.</p>
<iframe src="https://leetcode.com/playground/V3u2LbFe/shared" frameborder="0" width="100%" height="361" name="V3u2LbFe"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N + G\text{.length})</script>, where <script type="math/tex; mode=display">N</script> is the length of the linked list with root node <code>head</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(G\text{.length})</script>, to store <code>Gset</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
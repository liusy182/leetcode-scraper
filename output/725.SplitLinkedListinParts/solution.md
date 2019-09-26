<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-create-new-lists-accepted">Approach #1: Create New Lists [Accepted]</a></li>
<li><a href="#approach-2-split-input-list-accepted">Approach #2: Split Input List [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-create-new-lists-accepted">Approach #1: Create New Lists [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>If there are <script type="math/tex; mode=display">N</script> nodes in the linked list <code>root</code>, then there are <script type="math/tex; mode=display">N / k</script> items in each part, plus the first <script type="math/tex; mode=display">N \% k</script> parts have an extra item.  We can count <script type="math/tex; mode=display">N</script> with a simple loop.</p>
<p>Now for each part, we have calculated how many nodes that part will have: <code>width + (i &lt; remainder ? 1 : 0)</code>.  We create a new list and write the part to that list.</p>
<p>Our solution showcases constructs of the form <code>a = b = c</code>.  Note that this syntax behaves differently for different languages.</p>
<iframe src="https://leetcode.com/playground/mPv7qf7R/shared" frameborder="0" width="100%" height="463" name="mPv7qf7R"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N + k)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given list.  If <script type="math/tex; mode=display">k</script> is large, it could still require creating many new empty lists.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(max(N, k))</script>, the space used in writing the answer.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-split-input-list-accepted">Approach #2: Split Input List [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>As in <em>Approach #1</em>, we know the size of each part.  Instead of creating new lists, we will split the input list directly and return a list of pointers to nodes in the original list as appropriate.</p>
<p>Our solution proceeds similarly.  For a part of size <code>L = width + (i &lt; remainder ? 1 : 0)</code>, instead of stepping <code>L</code> times, we will step <code>L-1</code> times, and our final time will also sever the link between the last node from the previous part and the first node from the next part.</p>
<iframe src="https://leetcode.com/playground/RmD7xooU/shared" frameborder="0" width="100%" height="500" name="RmD7xooU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N + k)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given list.  If <script type="math/tex; mode=display">k</script> is large, it could still require creating many new empty lists.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(k)</script>, the additional space used in writing the answer.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
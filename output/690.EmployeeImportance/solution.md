<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-depth-first-search-accepted">Approach #1: Depth-First Search [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Let's use a hashmap <code>emap = {employee.id -&gt; employee}</code> to query employees quickly.</p>
<p>Now to find the total importance of an employee, it will be the importance of that employee, plus the total importance of each of that employee's subordinates.  This is a straightforward depth-first search.</p>
<iframe src="https://leetcode.com/playground/NX7sm9qW/shared" frameborder="0" width="100%" height="310" name="NX7sm9qW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of employees.  We might query each employee in <code>dfs</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the size of the implicit call stack when evaluating <code>dfs</code>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
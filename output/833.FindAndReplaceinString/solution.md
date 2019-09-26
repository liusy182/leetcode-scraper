<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-direct-accepted">Approach #1: Direct [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-direct-accepted">Approach #1: Direct [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We showcase two different approaches.  In both approaches, we build some answer string <code>ans</code>, that starts as <code>S</code>.  Our main motivation in these approaches is to be able to identify and handle when a given replacement operation does nothing.</p>
<p>In <em>Java</em>, the idea is to build an array <code>match</code> that tells us <code>match[ix] = j</code> whenever <code>S[ix]</code> is the head of a successful replacement operation <code>j</code>: that is, whenever <code>S[ix:].startswith(sources[j])</code>.</p>
<p>After, we build the answer using this match array.  For each index <code>ix</code> in <code>S</code>, we can use <code>match</code> to check whether <code>S[ix]</code> is being replaced or not.  We repeatedly either write the next character <code>S[ix]</code>, or groups of characters <code>targets[match[ix]]</code>, depending on the value of <code>match[ix]</code>.</p>
<p>In <em>Python</em>, we sort our replacement jobs <code>(i, x, y)</code> in reverse order.  If <code>S[i:].startswith(x)</code>, then we can replace that section <code>S[i:i+len(x)]</code> with the target <code>y</code>.  We used a reverse order so that edits to <code>S</code> do not interfere with the rest of the queries.</p>
<iframe src="https://leetcode.com/playground/2qLJpytD/shared" frameborder="0" width="100%" height="480" name="2qLJpytD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(NQ)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>S</code>, and we have <script type="math/tex; mode=display">Q</script> replacement operations.  (Our complexity could be faster with a more accurate implementation, but it isn't necessary.)</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, if we consider <code>targets[i].length &lt;= 100</code> as a constant bound.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-output-to-array">Approach 1: Output to Array</a></li>
<li><a href="#approach-2-fast-and-slow-pointer">Approach 2: Fast and Slow Pointer</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-output-to-array">Approach 1: Output to Array</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Put every node into an array <code>A</code> in order.  Then the middle node is just <code>A[A.length // 2]</code>, since we can retrieve each node by index.</p>
<iframe src="https://leetcode.com/playground/fsou5N8T/shared" frameborder="0" width="100%" height="242" name="fsou5N8T"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given list.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>, the space used by <code>A</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-fast-and-slow-pointer">Approach 2: Fast and Slow Pointer</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>When traversing the list with a pointer <code>slow</code>, make another pointer <code>fast</code> that traverses twice as fast.  When <code>fast</code> reaches the end of the list, <code>slow</code> must be in the middle.</p>
<iframe src="https://leetcode.com/playground/brPhWpn3/shared" frameborder="0" width="100%" height="259" name="brPhWpn3"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the number of nodes in the given list.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(1)</script>, the space used by <code>slow</code> and <code>fast</code>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
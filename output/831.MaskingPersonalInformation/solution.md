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
<p>We perform the algorithm as described.</p>
<p>First, to check if information is an email, we check whether it contains a <code>'@'</code>.  (There are many different tests: we could check for letters versus digits, for example.)</p>
<p>If we have an email, we should replace the first name with the first letter of that name, followed by 5 asterisks, followed by the last letter of that name.</p>
<p>If we have a phone number, we should collect all the digits and then format it according to the description.</p>
<iframe src="https://leetcode.com/playground/9iWWL6yp/shared" frameborder="0" width="100%" height="327" name="9iWWL6yp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(1)</script>, if we consider the length of <code>S</code> as bounded by a constant.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
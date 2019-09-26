<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-cartesian-product-accepted">Approach #1: Cartesian Product [Accepted]</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-cartesian-product-accepted">Approach #1: Cartesian Product [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each place to put the comma, we separate the string into two fragments.  For example, with a string like <code>"1234"</code>, we could separate it into fragments <code>"1" and "234"</code>, <code>"12" and "34"</code>, or <code>"123"</code> and <code>"4"</code>.</p>
<p>Then, for each fragment, we have a choice of where to put the period, to create a list <code>make(...)</code> of choices.  For example, <code>"123"</code> could be made into <code>"1.23"</code>, <code>"12.3"</code>, or <code>"123"</code>.</p>
<p>Because of extranneous zeroes, we should ignore possibilities where the part of the fragment to the <code>left</code> of the decimal starts with <code>"0"</code> (unless it is exactly <code>"0"</code>), and ignore possibilities where the part of the fragment to the <code>right</code> of the decimal ends with <code>"0"</code>, as these are not allowed.</p>
<p>Note that this process could result in an empty answer, such as for the case <code>S = "(000)"</code>.</p>
<iframe src="https://leetcode.com/playground/Gdyt4CNE/shared" frameborder="0" width="100%" height="463" name="Gdyt4CNE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N^3)</script>, where <script type="math/tex; mode=display">N</script> is the length <code>S</code>.  We evaluate the sum <script type="math/tex; mode=display">O(\sum_k k(N-k))</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^3)</script>, to store the answer.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
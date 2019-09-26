<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-mathematical">Approach 1: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-mathematical">Approach 1: Mathematical</h4>
<p><strong>Intuition</strong></p>
<p>Say <script type="math/tex; mode=display">P = R^2</script> is a superpalindrome.</p>
<p>Because <script type="math/tex; mode=display">R</script> is a palindrome, the first half of the digits in <script type="math/tex; mode=display">R</script> determine <script type="math/tex; mode=display">R</script> up to two possibilities.  We can iterate through these digits: let <script type="math/tex; mode=display">k</script> be the first half of the digits in <script type="math/tex; mode=display">R</script>.  For example, if <script type="math/tex; mode=display">k = 1234</script>, then <script type="math/tex; mode=display">R = 1234321</script> or <script type="math/tex; mode=display">R = 12344321</script>.  Each possibility has either an odd or an even number of digits in <script type="math/tex; mode=display">R</script>.</p>
<p>Notice because <script type="math/tex; mode=display">P < 10^{18}</script>, <script type="math/tex; mode=display">R < (10^{18})^{\frac{1}{2}} = 10^9</script>, and <script type="math/tex; mode=display">R = k \| k'</script> (concatenation), where <script type="math/tex; mode=display">k'</script> is <script type="math/tex; mode=display">k</script> reversed (and also possibly truncated by one digit); so that <script type="math/tex; mode=display">k < 10^5 = \small\text{MAGIC}</script>, our magic constant.</p>
<p><strong>Algorithm</strong></p>
<p>For each <script type="math/tex; mode=display">1 \leq k < \small\text{MAGIC}</script>, let's create the associated palindrome <script type="math/tex; mode=display">R</script>, and check whether <script type="math/tex; mode=display">R^2</script> is a palindrome.</p>
<p>We should handle the odd and even possibilities separately, as we would like to break early so as not to do extra work.</p>
<p>To check whether an integer is a palindrome, we could check whether it is equal to its reverse.  To create the reverse of an integer, we can do it digit by digit.</p>
<iframe src="https://leetcode.com/playground/ZRTHqoUW/shared" frameborder="0" width="100%" height="500" name="ZRTHqoUW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(W^{\frac{1}{4}} * \log W)</script>, where <script type="math/tex; mode=display">W = 10^{18}</script> is our upper limit for <script type="math/tex; mode=display">R</script>.  The <script type="math/tex; mode=display">\log W</script> term comes from checking whether each candidate is the root of a palindrome.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log W)</script>, the space used to create the candidate palindrome.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-accepted">Approach #1: Brute Force [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>For each number in the given range, we will directly test if that number is self-dividing.</p>
<p>By definition, we want to test each whether each digit is non-zero and divides the number.  For example, with <code>128</code>, we want to test <code>d != 0 &amp;&amp; 128 % d == 0</code> for <code>d = 1, 2, 8</code>.  To do that, we need to iterate over each digit of the number.</p>
<p>A straightforward approach to that problem would be to convert the number into a character array (string in Python), and then convert back to integer to perform the modulo operation when checking <code>n % d == 0</code>.</p>
<p>We could also continually divide the number by 10 and peek at the last digit.  That is shown as a variation in a comment.</p>
<iframe src="https://leetcode.com/playground/6GUVmusj/shared" frameborder="0" width="100%" height="500" name="6GUVmusj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(D)</script>, where <script type="math/tex; mode=display">D</script> is the number of integers in the range <script type="math/tex; mode=display">[L, R]</script>, and assuming <script type="math/tex; mode=display">\log(R)</script> is bounded.  (In general, the complexity would be <script type="math/tex; mode=display">O(D\log R)</script>.)</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(D)</script>, the length of the answer.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
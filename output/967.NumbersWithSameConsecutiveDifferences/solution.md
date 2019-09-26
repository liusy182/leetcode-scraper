<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to write some number in the answer digit by digit.</p>
<p>For each digit except the first, there are at most 2 choices for that digit.  This means that there are at most <script type="math/tex; mode=display">9 * 2^8</script> possible 9 digit numbers, for example.  This is small enough to brute force.</p>
<p><strong>Algorithm</strong></p>
<p>An <script type="math/tex; mode=display">N</script> digit number is just an <script type="math/tex; mode=display">N-1</script> digit number with a final digit added.  If the <script type="math/tex; mode=display">N-1</script> digit number ends in a digit <script type="math/tex; mode=display">d</script>, then the <script type="math/tex; mode=display">N</script> digit number will end in <script type="math/tex; mode=display">d-K</script> or <script type="math/tex; mode=display">d+K</script> (provided these are digits in the range <script type="math/tex; mode=display">[0,9]</script>).  We store these numbers in a <code>Set</code> structure to avoid duplicates.</p>
<p>Also, we should be careful about leading zeroes -- only 1 digit numbers will start with <code>0</code>.</p>
<iframe src="https://leetcode.com/playground/QMVwzekW/shared" frameborder="0" width="100%" height="500" name="QMVwzekW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(2^N)</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(2^N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
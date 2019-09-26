<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-dynamic-programming-counting">Approach 1: Dynamic Programming + Counting</a></li>
<li><a href="#approach-2-mathematical">Approach 2: Mathematical</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-dynamic-programming-counting">Approach 1: Dynamic Programming + Counting</h4>
<p><strong>Intuition</strong></p>
<p>First, call a positive integer <code>X</code> <em>valid</em> if <code>X &lt;= N</code> and <code>X</code> only consists of digits from <code>D</code>.  Our goal is to find the number of valid integers.</p>
<p>Say <code>N</code> has <code>K</code> digits.  If we write a valid number with <code>k</code> digits (<code>k &lt; K</code>), then there are <script type="math/tex; mode=display">(D\text{.length})^k</script> possible numbers we could write, since all of them will definitely be less than <code>N</code>.</p>
<p>Now, say we are to write a valid <code>K</code> digit number from left to right.  For example, <code>N = 2345</code>, <code>K = 4</code>, and <code>D = '1', '2', ..., '9'</code>.  Let's consider what happens when we write the first digit.</p>
<ul>
<li>
<p>If the first digit we write is less than the first digit of <code>N</code>, then we could write any numbers after, for a total of <script type="math/tex; mode=display">(D\text{.length})^{K-1}</script> valid numbers from this one-digit prefix.  In our example, if we start with <code>1</code>, we could write any of the numbers <code>1111</code> to <code>1999</code> from this prefix.</p>
</li>
<li>
<p>If the first digit we write is the same, then we require that the next digit we write is equal to or lower than the next digit in <code>N</code>.  In our example (with <code>N = 2345</code>), if we start with <code>2</code>, the next digit we write must be <code>3</code> or less.</p>
</li>
<li>
<p>We can't write a larger digit, because if we started with eg. <code>3</code>, then even a number of <code>3000</code> is definitely larger than <code>N</code>.</p>
</li>
</ul>
<p><strong>Algorithm</strong></p>
<p>Let <code>dp[i]</code> be the number of ways to write a valid number if <code>N</code> became <code>N[i], N[i+1], ...</code>.  For example, if <code>N = 2345</code>, then <code>dp[0]</code> would be the number of valid numbers at most <code>2345</code>, <code>dp[1]</code> would be the ones at most <code>345</code>, <code>dp[2]</code> would be the ones at most <code>45</code>, and <code>dp[3]</code> would be the ones at most <code>5</code>.</p>
<p>Then, by our reasoning above, <code>dp[i] = (number of d in D with d &lt; S[i]) * ((D.length) ** (K-i-1))</code>, plus <code>dp[i+1]</code> if <code>S[i]</code> is in <code>D</code>.</p>
<iframe src="https://leetcode.com/playground/en4D5WXi/shared" frameborder="0" width="100%" height="446" name="en4D5WXi"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, and assuming <script type="math/tex; mode=display">D\text{.length}</script> is constant.  (We could make this better by pre-calculating the number of <code>d &lt; S[i]</code> for all possible digits <code>S[i]</code>, but this isn't necessary.)</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, the space used by <code>S</code> and <code>dp</code>.  (Actually, we could store only the last 2 entries of <code>dp</code>, but this isn't necessary.)
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-mathematical">Approach 2: Mathematical</h4>
<p><strong>Intuition</strong></p>
<p>As in <em>Approach #1</em>, call a positive integer <code>X</code> <em>valid</em> if <code>X &lt;= N</code> and <code>X</code> only consists of digits from <code>D</code>.</p>
<p>Now let <code>B = D.length</code>.  There is a bijection between valid integers and so called "bijective-base-<code>B</code>" numbers.  For example, if <code>D = ['1', '3', '5', '7']</code>, then we could write the numbers <code>'1', '3', '5', '7', '11', '13', '15', '17', '31', ...</code> as (bijective-base-<code>B</code>) numbers <code>'1', '2', '3', '4', '11', '12', '13', '14', '21', ...</code>.</p>
<p>It is clear that both of these sequences are increasing, which means that the first sequence is a contiguous block of valid numbers, followed by invalid numbers.</p>
<p>Our approach is to find the largest valid integer, and convert it into bijective-base-<code>B</code> from which it is easy to find its rank (position in the sequence.)  Because of the bijection, the rank of this element must be the number of valid integers.</p>
<p>Continuing our example, if <code>N = 64</code>, then the valid numbers are <code>'1', '3', ..., '55', '57'</code>, which can be written as bijective-base-4 numbers <code>'1', '2', ..., '33', '34'</code>.  Converting this last entry <code>'34'</code> to decimal, the answer is <code>16</code> (3 * 4 + 4).</p>
<p><strong>Algorithm</strong></p>
<p>Let's convert <code>N</code> into the largest possible valid integer <code>X</code>, convert <code>X</code> to bijective-base-B, then convert that result to a decimal answer.  The last two conversions are relatively straightforward, so let's focus on the first part of the task.</p>
<p>Let's try to write <code>X</code> one digit at a time.  Let's walk through an example where <code>D = ['2', '4', '6', '8']</code>.  There are some cases:</p>
<ul>
<li>
<p>If the first digit of <code>N</code> is in <code>D</code>, we write that digit and continue.  For example, if <code>N = 25123</code>, then we will write <code>2</code> and continue.</p>
</li>
<li>
<p>If the first digit of <code>N</code> is larger than <code>min(D)</code>, then we write the largest possible number from <code>D</code> less than that digit, and the rest of the numbers will be big.  For example, if <code>N = 5123</code>, then we will write <code>4888</code> (<code>4</code> then <code>888</code>).</p>
</li>
<li>
<p>If the first digit of <code>N</code> is smaller than <code>min(D)</code>, then we must "subtract 1" (in terms of <code>X</code>'s bijective-base-B representation), and the rest of the numbers will be big.</p>
<p>For example, if  <code>N = 123</code>, we will write <code>88</code>.  If <code>N = 4123</code>, we will write <code>2888</code>.  And if <code>N = 22123</code>, we will write <code>8888</code>.  This is because "subtracting 1" from <code>'', '4', '22'</code> yields <code>'', '2', '8'</code> (can't go below 0).</p>
</li>
</ul>
<p>Actually, in our solution, it is easier to write in bijective-base-B, so instead of writing digits of <code>D</code>, we'll write the index of those digits (1-indexed).  For example, <code>X = 24888</code> will be <code>A = [1, 2, 4, 4, 4]</code>.  Afterwards, we convert this to decimal.</p>
<iframe src="https://leetcode.com/playground/bVuoAcr9/shared" frameborder="0" width="100%" height="500" name="bVuoAcr9"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, and assuming <script type="math/tex; mode=display">D\text{.length}</script> is constant.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(\log N)</script>, the space used by <code>A</code>.
<br>
<br></p>
</li>
</ul>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
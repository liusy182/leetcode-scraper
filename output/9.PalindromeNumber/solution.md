<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-revert-half-of-the-number">Approach 1: Revert half of the number</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-revert-half-of-the-number">Approach 1: Revert half of the number</h4>
<p><strong>Intuition</strong></p>
<p>The first idea that comes to mind is to convert the number into string, and check if the string is a palindrome, but
this would require extra non-constant space for creating the string which is not allowed by the problem description.</p>
<p>Second idea would be reverting the number itself, and then compare the number with original number,
if they are the same, then the number is a palindrome. However, if the reversed number is larger than <script type="math/tex; mode=display">\text{int.MAX}</script>,
we will hit integer overflow problem.</p>
<p>Following the thoughts based on the second idea, to avoid the overflow issue of the reverted number, what if we only
revert half of the <script type="math/tex; mode=display">\text{int}</script> number? After all, the reverse of the last half of the palindrome should be the same as the
first half of the number, if the number is a palindrome.</p>
<p>For example, if the input is <code>1221</code>, if we can revert the last part of the number "12<strong>21</strong>" from "<strong>21</strong>" to "<strong>12</strong>",
and compare it with the first half of the number "12", since 12 is the same as 12, we know that the number is a palindrome.</p>
<p>Let's see how we could translate this idea into an algorithm.</p>
<p><strong>Algorithm</strong></p>
<p>First of all we should take care of some edge cases. All negative numbers are not palindrome, for example: -123 is
not a palindrome since the '-' does not equal to '3'. So we can return false for all negative numbers.</p>
<p>Now let's think about how to revert the last half of the number. For number <code>1221</code>, if we do <code>1221 % 10</code>, we get the
last digit <code>1</code>, to get the second to the last digit, we need to remove the last digit from <code>1221</code>, we could do so by
dividing it by 10, <code>1221 / 10 = 122</code>. Then we can get the last digit again by doing a modulus by 10, <code>122 % 10 = 2</code>, and if we multiply the last digit by 10 and add the second last digit, <code>1 * 10 + 2 = 12</code>, it gives us the reverted number we want. Continuing this process would give us the reverted number with more digits.</p>
<p>Now the question is, how do we know that we've reached the half of the number?</p>
<p>Since we divided the number by 10, and multiplied the reversed number by 10, when the original number is less than the
reversed number, it means we've processed half of the number digits.</p>
<iframe src="https://leetcode.com/playground/A2cW8TnM/shared" frameborder="0" width="100%" height="446" name="A2cW8TnM"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log_{10}(n))</script>.
We divided the input by 10 for every iteration, so the time complexity is <script type="math/tex; mode=display">O(\log_{10}(n))</script>
</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.</p>
</li>
</ul>
          </div>
        
      </div>
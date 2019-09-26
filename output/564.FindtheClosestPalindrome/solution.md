<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-forcetime-limit-exceeded">Approach #1 Brute Force[Time Limit Exceeded]</a></li>
<li><a href="#approach-2-using-mathaccepted">Approach #2 Using Math[Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-forcetime-limit-exceeded">Approach #1 Brute Force[Time Limit Exceeded]</h4>
<p>The simplest solution is to consider every possible number smaller than the given number <script type="math/tex; mode=display">n</script>, starting by decrementing 1 from the given number and go on in descending order. Similarly, we can consider every possible number greater than <script type="math/tex; mode=display">n</script> starting by incrementing 1 from the given number and going in ascending order. We can continue doing so in an alternate manner till we find a number which is a palindrome.</p>
<iframe src="https://leetcode.com/playground/DvreVK8V/shared" frameborder="0" name="DvreVK8V" width="100%" height="377"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\sqrt{n})</script>. Upto <script type="math/tex; mode=display">2*\sqrt{n}</script> numbers could be generated in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-mathaccepted">Approach #2 Using Math[Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>To understand this method, let's start with a simple illustration. Assume that the number given to us is "abcxy". One way to convert this number into a palindrome is to replicate one half of the string to the other half. If we try replicating the second half to the first half, the new palindrome obtained will be "yxcxy" which lies at an absolute of <script type="math/tex; mode=display">\left|10000(a-y) + 1000(b-x)\right|</script> from the original number. But, if we replicate the first half to the second half of the string, we obtain "abcba", which lies at an absolute difference of <script type="math/tex; mode=display">\left|10(x-b) + (y-a)\right|</script>. Trying to change <script type="math/tex; mode=display">c</script> additionaly in either case would incur an additional value of atleast 100 in the absolute difference.</p>
<p>From the above illustration, we can conclude that if replication is used to generate the palindromic number, we should always replicate the first half to the second half. In this implementation, we've stored such a number in <script type="math/tex; mode=display">a</script> at a difference of <script type="math/tex; mode=display">diff1</script> from <script type="math/tex; mode=display">n</script>.</p>
<p>But, there exists another case as well, where the digit at the middle index is incremented or decremented. In such cases, it could be profitable to make changes to the central digit only since such changes could lead to a palindrome formation nearer to the original digit. e.g. 10987. Using the above criteria, the palindrome obtained will be 10901 which is at a more difference from 10987 than 11011. A similar situation occurs if a 0 occurs at the middle digit. But, again as discussed previously, we need to consider only the first half digits to obtain the new palindrome. This special effect occurs with 0 or 9 at the middle digit since, only decrementing 0 and incrementing 9 at that digit place can lead to the change in the rest of the digits towards their left. In any other case, the situation boils down to the one discussed in the first paragraph.</p>
<p>Now, whenever we find a 0 near the middle index, in order to consider the palindromes which are lesser than <script type="math/tex; mode=display">n</script>, we subtract a 1 from the first half of the number to obtain a new palindromic half e.g. If the given number <script type="math/tex; mode=display">n</script> is 20001, we subtract a 1 from 200 creating a number of the form 199xx. To obtain the new palindrome, we replicate the first half to obtain 19991. Taking another example of  10000, (with a 1 at the MSB), we subtract a 1 from 100 creating 099xx as the new number transforming to a 9999 as the new palindrome. This number is stored in <script type="math/tex; mode=display">b</script> having a difference of <script type="math/tex; mode=display">diff2</script> from <script type="math/tex; mode=display">n</script>
</p>
<p>Similar treatment needs to be done with a 9 at the middle digit, except that this time we need to consider the numbers larger than the current number. For this, we add a 1 to the first half. e.g. Taking the number 10987, we add a 1 to 109 creating a number of the form 110xx(11011 is the new palindrome). This palindrome is stored in <script type="math/tex; mode=display">c</script> having a difference of <script type="math/tex; mode=display">diff3</script> from <script type="math/tex; mode=display">n</script>.</p>
<p>Out of these three palindromes, we can choose the one with a minimum difference from <script type="math/tex; mode=display">n</script>. Further, in case of a tie, we need to return the smallest palindrome obtained. For resolving this tie's conflict, we can observe that a tie is possible only if one number is larger than <script type="math/tex; mode=display">n</script> and another is lesser than <script type="math/tex; mode=display">n</script>. Further, we know that the number <script type="math/tex; mode=display">b</script> is obtained by decreasing <script type="math/tex; mode=display">n</script>. Thus, in case of conflict between <script type="math/tex; mode=display">b</script> and any other number, we need to choose <script type="math/tex; mode=display">b</script>. Similarly, <script type="math/tex; mode=display">c</script> is obtained by increasing <script type="math/tex; mode=display">n</script>. Thus, in case of a tie between <script type="math/tex; mode=display">c</script> and any other number, we need to choose the number other than <script type="math/tex; mode=display">c</script>.</p>
<iframe src="https://leetcode.com/playground/Y6G9NDDf/shared" frameborder="0" name="Y6G9NDDf" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(l)</script>. Scanning, insertion, deletion,, mirroring takes <script type="math/tex; mode=display">O(l)</script>, where <script type="math/tex; mode=display">l</script> is the length of the string.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(l)</script>. Temporary variables are used to store the strings.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
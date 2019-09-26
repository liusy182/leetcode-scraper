<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-longest-common-substring">Approach 1: Longest Common Substring</a></li>
<li><a href="#approach-2-brute-force">Approach 2: Brute Force</a></li>
<li><a href="#approach-3-dynamic-programming">Approach 3: Dynamic Programming</a></li>
<li><a href="#approach-4-expand-around-center">Approach 4: Expand Around Center</a></li>
<li><a href="#approach-5-manachers-algorithm">Approach 5: Manacher's Algorithm</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>This article is for intermediate readers. It introduces the following ideas:
Palindrome, Dynamic Programming and String Manipulation. Make sure you understand what a palindrome means. A palindrome is a string which reads the same in both directions. For example, <script type="math/tex; mode=display">S</script> = "aba" is a palindrome, <script type="math/tex; mode=display">S</script> = "abc" is not.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-longest-common-substring">Approach 1: Longest Common Substring</h4>
<p><strong>Common mistake</strong></p>
<p>Some people will be tempted to come up with a quick solution, which is unfortunately flawed (however can be corrected easily):</p>
<blockquote>
<p>Reverse <script type="math/tex; mode=display">S</script> and become <script type="math/tex; mode=display">S'</script>. Find the longest common substring between <script type="math/tex; mode=display">S</script> and <script type="math/tex; mode=display">S'</script>, which must also be the longest palindromic substring.</p>
</blockquote>
<p>This seemed to work, let’s see some examples below.</p>
<p>For example, <script type="math/tex; mode=display">S</script> = "caba", <script type="math/tex; mode=display">S'</script> = "abac".</p>
<p>The longest common substring between <script type="math/tex; mode=display">S</script> and <script type="math/tex; mode=display">S'</script> is "aba", which is the answer.</p>
<p>Let’s try another example: <script type="math/tex; mode=display">S</script> = "abacdfgdcaba", <script type="math/tex; mode=display">S'</script> = "abacdgfdcaba".</p>
<p>The longest common substring between <script type="math/tex; mode=display">S</script> and <script type="math/tex; mode=display">S'</script> is "abacd". Clearly, this is not a valid palindrome.</p>
<p><strong>Algorithm</strong></p>
<p>We could see that the longest common substring method fails when there exists a reversed copy of a non-palindromic substring in some other part of <script type="math/tex; mode=display">S</script>. To rectify this, each time we find a longest common substring candidate, we check if the substring’s indices are the same as the reversed substring’s original indices. If it is, then we attempt to update the longest palindrome found so far; if not, we skip this and find the next candidate.</p>
<p>This gives us an <script type="math/tex; mode=display">O(n^2)</script> Dynamic Programming solution which uses <script type="math/tex; mode=display">O(n^2)</script> space (could be improved to use <script type="math/tex; mode=display">O(n)</script> space). Please read more about Longest Common Substring <a href="https://en.wikipedia.org/wiki/Longest_common_substring">here</a>.
<br>
<br></p>
<hr>
<h4 id="approach-2-brute-force">Approach 2: Brute Force</h4>
<p>The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>.
Assume that <script type="math/tex; mode=display">n</script> is the length of the input string, there are a total of <script type="math/tex; mode=display">\binom{n}{2} = \frac{n(n-1)}{2}</script> such substrings (excluding the trivial solution where a character itself is a palindrome). Since verifying each substring takes <script type="math/tex; mode=display">O(n)</script> time, the run time complexity is <script type="math/tex; mode=display">O(n^3)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming">Approach 3: Dynamic Programming</h4>
<p>To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.</p>
<p>We define <script type="math/tex; mode=display">P(i,j)</script> as following:</p>
<p>
<script type="math/tex; mode=display">
P(i,j) =
     \begin{cases}
       \text{true,} &\quad\text{if the substring } S_i \dots S_j \text{ is a palindrome}\\
       \text{false,} &\quad\text{otherwise.} \
     \end{cases}
</script>
</p>
<p>Therefore,</p>
<p>
<script type="math/tex; mode=display">
P(i, j) = ( P(i+1, j-1) \text{ and } S_i == S_j )
</script>
</p>
<p>The base cases are:</p>
<p>
<script type="math/tex; mode=display">
P(i, i) = true
</script>
</p>
<p>
<script type="math/tex; mode=display">
P(i, i+1) = ( S_i == S_{i+1} )
</script>
</p>
<p>This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>.
This gives us a runtime complexity of <script type="math/tex; mode=display">O(n^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^2)</script>.
It uses <script type="math/tex; mode=display">O(n^2)</script> space to store the table.</p>
</li>
</ul>
<p><strong>Additional Exercise</strong></p>
<p>Could you improve the above space complexity further and how?
<br>
<br></p>
<hr>
<h4 id="approach-4-expand-around-center">Approach 4: Expand Around Center</h4>
<p>In fact, we could solve it in <script type="math/tex; mode=display">O(n^2)</script> time using only constant space.</p>
<p>We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only <script type="math/tex; mode=display">2n - 1</script> such centers.</p>
<p>You might be asking why there are <script type="math/tex; mode=display">2n - 1</script> but not <script type="math/tex; mode=display">n</script> centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.</p>
<iframe src="https://leetcode.com/playground/5w5ZZtTd/shared" frameborder="0" width="100%" height="446" name="5w5ZZtTd"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>.
Since expanding a palindrome around its center could take <script type="math/tex; mode=display">O(n)</script> time, the overall complexity is <script type="math/tex; mode=display">O(n^2)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-manachers-algorithm">Approach 5: Manacher's Algorithm</h4>
<p>There is even an <script type="math/tex; mode=display">O(n)</script> algorithm called Manacher's algorithm, explained <a href="https://articles.leetcode.com/longest-palindromic-substring-part-ii/">here in detail</a>. However, it is a non-trivial algorithm, and no one expects you to come up with this algorithm in a 45 minutes coding session. But, please go ahead and understand it, I promise it will be a lot of fun.</p>
          </div>
        
      </div>
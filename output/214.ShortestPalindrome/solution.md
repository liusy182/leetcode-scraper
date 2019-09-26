<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1 Brute force [Accepted]</a></li>
<li><a href="#approach-2-two-pointers-and-recursion-accepted">Approach #2 Two pointers and recursion [Accepted]</a></li>
<li><a href="#approach-3-kmp-accepted">Approach #3 KMP [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1 Brute force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>According to the question, we are allowed to insert the characters only at the beginning of the string. Hence, we can find the largest segment from the beginning that is a palindrome, and we can then easily reverse the remaining segment and append to the beginning. This must be the required answer as no shorter palindrome could be found than this by just appending at the beginning.</p>
<p>For example: Take the string <script type="math/tex; mode=display">\text{"abcbabcab"}</script>. Here, the largest palindrome segment from beginning is <script type="math/tex; mode=display">\text{"abcba"}</script>, and the remaining segment is <script type="math/tex; mode=display">\text{"bcab"}</script>. Hence the required string is reverse of <script type="math/tex; mode=display">\text{"bcab"}</script>( = <script type="math/tex; mode=display">\text{"bacb"}</script>) + original string( = <script type="math/tex; mode=display">\text{"abcbabcab"}</script>) = <script type="math/tex; mode=display">\text{"bacbabcbabcab"}</script>.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Create the reverse of the original string <script type="math/tex; mode=display">s</script>, say <script type="math/tex; mode=display">\text{rev}</script>. This is used for comparison to find the largest palindrome segment from the front.</li>
<li>Iterate over the variable <script type="math/tex; mode=display">i</script> from 0 to the <script type="math/tex; mode=display">\text{size(s)}-1</script>:<ul>
<li>If <script type="math/tex; mode=display">s[0:n-i] == rev[i:]</script> (i.e. substring of <script type="math/tex; mode=display">s</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">n-i</script> is equal to the substring of <script type="math/tex; mode=display">\text{rev}</script> from <script type="math/tex; mode=display">i</script> to the end of string). This essentially means that that substring from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">n-i</script> is a palindrome, as <script type="math/tex; mode=display">\text{rev}</script> is the reverse of <script type="math/tex; mode=display">s</script>.</li>
<li>Since, we find the larger palindromes first, we can return reverse of largest palindrome + <script type="math/tex; mode=display">s</script> as soon as we get it.</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/ofq6FrQW/shared" frameborder="0" name="ofq6FrQW" width="100%" height="258"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n^2)</script>.</p>
<ul>
<li>We iterate over the entire length of string <script type="math/tex; mode=display">s</script>.</li>
<li>In each iteration, we compare the substrings which is linear in size of substrings to be compared.</li>
<li>Hence, the total time complexity is <script type="math/tex; mode=display">O(n*n) = O(n^2)</script>.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script> extra space for the reverse string <script type="math/tex; mode=display">\text{rev}</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-two-pointers-and-recursion-accepted">Approach #2 Two pointers and recursion [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>In Approach #1, we found the largest palindrome substring from the string using substring matching which is <script type="math/tex; mode=display">O(n)</script> in length of substring. We could make the process more efficient if we could reduce the size of string to search for the substring without checking the complete substring each time.</p>
<p>Lets take a string <script type="math/tex; mode=display">\text{"abcbabcaba"}</script>. Let us consider 2 pointers <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script>.
Initialize <script type="math/tex; mode=display">i = 0</script>. Iterate over <script type="math/tex; mode=display">j</script> from <script type="math/tex; mode=display">n-1</script> to <script type="math/tex; mode=display">0</script>, incrementing <script type="math/tex; mode=display">i</script> each time <script type="math/tex; mode=display">\text{s[i]==s[j]}</script>. Now, we just need to search in range <script type="math/tex; mode=display">\text[0,i)</script>. This way, we have reduced the size of string to search for the largest palindrome substring from the beginning. The range <script type="math/tex; mode=display">\text{[0,i)}</script> must always contain the largest palindrome substring. The proof of correction is that: Say the string was a perfect palindrome, <script type="math/tex; mode=display">i</script> would be incremented <script type="math/tex; mode=display">n</script> times. Had there been other characters at the end, <script type="math/tex; mode=display">i</script> would still be incremented by the size of the palindrome. Hence, even though there is a chance that the range <script type="math/tex; mode=display">\text{[0,i)}</script> is not always tight, it is ensured that it will always contain the longest palindrome from the beginning.  </p>
<p>The best case for the algorithm is when the entire string is palindrome and the worst case is string like <script type="math/tex; mode=display">\text{"aababababababa"}</script>, wherein <script type="math/tex; mode=display">i</script> first becomes <script type="math/tex; mode=display">12</script>(check by doing on paper), and we need to recheck in [0,12) corresponding to string <script type="math/tex; mode=display">\text{"aabababababa"}</script>. Again continuing in the same way, we get <script type="math/tex; mode=display">{i=10}</script>.  In such a case, the string is reduced only by as few as 2 elements at each step. Hence, the number of steps in such cases is linear(<script type="math/tex; mode=display">n/2</script>).</p>
<p>This reduction of length could be easily done with the help of a recursive routine, as shown in the algorithm section.</p>
<p><strong>Algorithm</strong></p>
<p>The routine <script type="math/tex; mode=display">\text{shortestPalindrome}</script> is recursive and takes string <script type="math/tex; mode=display">s</script> as parameter:</p>
<ul>
<li>Initialize <script type="math/tex; mode=display">i=0</script>
</li>
<li>Iterate over <script type="math/tex; mode=display">j</script> from <script type="math/tex; mode=display">n-1</script> to <script type="math/tex; mode=display">0</script>:<ul>
<li>If <script type="math/tex; mode=display">\text{s[i]==s[j]}</script>, increase <script type="math/tex; mode=display">i</script> by <script type="math/tex; mode=display">1</script>
</li>
</ul>
</li>
<li>If <script type="math/tex; mode=display">i</script> equals the size of <script type="math/tex; mode=display">s</script>, the entire string is palindrome, and hence return the entire string <script type="math/tex; mode=display">s</script>.</li>
<li>Else:<ul>
<li>Return reverse of remaining substring after <script type="math/tex; mode=display">i</script> to the end of string + <script type="math/tex; mode=display">\text{shortestPalindrome}</script> routine on substring from start to index <script type="math/tex; mode=display">i-1</script> + remaining substring after <script type="math/tex; mode=display">i</script> to the end of string.</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/zeLz2M4w/shared" frameborder="0" name="zeLz2M4w" width="100%" height="292"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n^2)</script>.<ul>
<li>Each iteration of <script type="math/tex; mode=display">\text{shortestPalindrome}</script> is linear in size of substring and the maximum number of recursive calls can be <script type="math/tex; mode=display">n/2</script> times as shown in the Intuition section.</li>
<li>Let the time complexity of the algorithm be T(n). Since, at the each step for the worst case, the string can be divide into 2 parts and we require only one part for further computation. Hence, the time complexity for the worst case can be represented as : <script type="math/tex; mode=display">T(n)=T(n-2)+O(n)</script>. So, <script type="math/tex; mode=display">T(n) = O(n) + O(n-2) + O(n-4) + ... + O(1)</script> which is  <script type="math/tex; mode=display">O(n^2)</script>.</li>
</ul>
</li>
</ul>
<p>Thanks @CONOVER for the time complexity analysis.</p>
<ul>
<li>Space complexity: <script type="math/tex; mode=display">O(n)</script> extra space for <script type="math/tex; mode=display">\text{remain_rev}</script> string.</li>
</ul>
<hr>
<h4 id="approach-3-kmp-accepted">Approach #3 KMP [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We have seen that the question boils down to  finding the largest palindrome substring from the beginning.</p>
<p>The people familiar with KMP(Knuth–Morris–Pratt) algorithm may wonder that the task at hand can be easily be compared with the concept of the lookup table in KMP.</p>
<p><em>KMP Overview:</em></p>
<p>KMP is a string matching algorithm that runs in <script type="math/tex; mode=display">O(n+m)</script> times, where <script type="math/tex; mode=display">n</script> and <script type="math/tex; mode=display">m</script> are sizes of the text and string to be searched respectively. The key component of KMP is the failure function lookup table,say <script type="math/tex; mode=display">f(s)</script>. The purpose of the lookup table is to store the length of the proper prefix of the string <script type="math/tex; mode=display">b_{1}b_{2}...b_{s}</script> that is also a suffix of <script type="math/tex; mode=display">b_{1}b_{2}...b_{s}</script>. This table is important because if we are trying to match a text string for <script type="math/tex; mode=display">b_{1}b_{2}...b_{n}</script>, and we have matched the first <script type="math/tex; mode=display">s</script> positions, but when we fail, then the value of lookup table for <script type="math/tex; mode=display">s</script> is the longest prefix of <script type="math/tex; mode=display">b_{1}b_{2}...b_{n}</script> that could possibly match the text string upto the point we are at. Thus, we don't need to start all over again, and can resume searching from the matching prefix.</p>
<p>The algorithm to generate the lookup table is easy and inutitive, as given below:</p>
<div class="codehilite"><pre><span></span>f(0) = 0
for(i = 1; i &lt; n; i++)
{
    t = f(i-1)
    while(t &gt; 0 &amp;&amp; b[i] != b[t])
        t = f(t-1)
    if(b[i] == b[t]){
        ++t
    f(i) = t
}
</pre></div>


<ul>
<li>Here, we first set f(0)=0 since, no proper prefix is available.</li>
<li>Next, iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">1</script> to <script type="math/tex; mode=display">n-1</script>:<ul>
<li>Set <script type="math/tex; mode=display">t=f(i-1)</script>
</li>
<li>While t&gt;0 and char at <script type="math/tex; mode=display">i</script> doesn't match the char at <script type="math/tex; mode=display">t</script> position, set <script type="math/tex; mode=display">t=f(t)</script>, which essentially means that we have problem matching and must consider a shorter prefix, which will be <script type="math/tex; mode=display">b_{f(t-1)}</script>, until we find a match or t becomes 0.</li>
<li>If <script type="math/tex; mode=display">b_{i}==b_{t}</script>, add 1 to t</li>
<li>Set <script type="math/tex; mode=display">f(i)=t</script>
</li>
</ul>
</li>
</ul>
<p>The lookup table generation is as illustrated below:</p>
<p align="center"><img alt="KMP" src="../Figures/214/shortest_palindrome.png" width="600px"></p>
<p><em>Wait! I get it!!</em></p>
<p>In Approach #1, we reserved the original string <script type="math/tex; mode=display">s</script> and stored it as <script type="math/tex; mode=display">\text{rev}</script>. We iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">n-1</script> and check for <script type="math/tex; mode=display">s[0:n-i] == rev[i:]</script>.
Pondering over this statement, had the <script type="math/tex; mode=display">\text{rev}</script> been concatenated to <script type="math/tex; mode=display">s</script>, this statement is just finding the longest prefix that is equal to the suffix. Voila!</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>We use the KMP lookup table generation</li>
<li>Create <script type="math/tex; mode=display">\text{new_s}</script> as <script type="math/tex; mode=display">s + \text{"#"} + \text{reverse(s)}</script> and use the string in the lookup-generation algorithm<ul>
<li>The "#" in the middle is required, since without the #, the  2 strings could mix with each ther, producing wrong answer. For example, take the string <script type="math/tex; mode=display">\text{"aaaa"}</script>. Had we not inserted "#" in the middle, the new string would be <script type="math/tex; mode=display">\text{"aaaaaaaa"}</script> and the largest prefix size would be 7 corresponding to "aaaaaaa" which would be obviously wrong. Hence, a delimiter is required at the middle.</li>
</ul>
</li>
<li>Return reversed string after the largest palindrome from beginning length(given by <script type="math/tex; mode=display">n-\text{f[n_new-1]}</script>) + original string <script type="math/tex; mode=display">s</script>
</li>
</ul>
<iframe src="https://leetcode.com/playground/Uu5sN23P/shared" frameborder="0" name="Uu5sN23P" width="100%" height="360"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n)</script>.</p>
<ul>
<li>In every iteration of the inner while loop, <script type="math/tex; mode=display">t</script> decreases until it reaches 0 or until it matches. After that, it is incremented by one. Therefore, in the worst case, <script type="math/tex; mode=display">t</script> can only be decreased up to <script type="math/tex; mode=display">n</script> times and increased up to <script type="math/tex; mode=display">n</script> times.</li>
<li>Hence, the algorithm is linear with maximum <script type="math/tex; mode=display">(2 * n) * 2</script> iterations.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script>. Additional space for the reverse string and the concatenated string.</p>
</li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/abhinavbansal0">@abhinavbansal0</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-sliding-window">Approach 1: Sliding Window</a></li>
<li><a href="#approach-2-optimized-sliding-window">Approach 2: Optimized Sliding Window</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-sliding-window">Approach 1: Sliding Window</h4>
<p><strong>Intuition</strong></p>
<p>The question asks us to return the minimum window from the string <script type="math/tex; mode=display">S</script> which has all the characters of the string <script type="math/tex; mode=display">T</script>. Let us call a window <code>desirable</code> if it has all the characters from <script type="math/tex; mode=display">T</script>.</p>
<p>We can use a simple sliding window approach to solve this problem.</p>
<p>In any sliding window based problem we have two pointers. One <script type="math/tex; mode=display">right</script> pointer whose job is to expand the current window and then we have the <script type="math/tex; mode=display">left</script> pointer whose job is to contract a given window. At any point in time only one of these pointers move and the other one remains fixed.</p>
<p>The solution is pretty intuitive. We keep expanding the window by moving the right pointer. When the window has all the desired characters, we contract (if possible) and save the smallest window till now.</p>
<p>The answer is the smallest desirable window.</p>
<p>For eg. <code>S = "ABAACBAB" T = "ABC"</code>. Then our answer window is <code>"ACB"</code> and shown below is one of the possible desirable windows.
</p><center>
<img src="../Figures/76/76_Minimum_Window_Substring_1.png" width="500">
</center>
<br>
<p><strong>Algorithm</strong></p>
<ol>
<li>
<p>We start with two pointers, <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> initially pointing to the first element of the string <script type="math/tex; mode=display">S</script>.</p>
</li>
<li>
<p>We use the <script type="math/tex; mode=display">right</script> pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of <script type="math/tex; mode=display">T</script>.</p>
</li>
<li>
<p>Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.</p>
</li>
<li>
<p>If the window is not desirable any more, we repeat <script type="math/tex; mode=display">step \; 2</script> onwards.</p>
</li>
</ol>
<p></p><center>
<img src="../Figures/76/76_Minimum_Window_Substring_2.png" width="500">
</center>
<p>The above steps are repeated until we have looked at all the windows. The smallest window is returned.</p>
<p></p><center>
<img src="../Figures/76/76_Minimum_Window_Substring_3.png" width="500">
</center>
<br>
<iframe src="https://leetcode.com/playground/e5nQuXma/shared" frameborder="0" width="100%" height="500" name="e5nQuXma"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(|S| + |T|)</script> where |S| and |T| represent the lengths of strings <script type="math/tex; mode=display">S</script> and <script type="math/tex; mode=display">T</script>.
In the worst case we might end up visiting every element of string <script type="math/tex; mode=display">S</script> twice, once by left pointer and once by right pointer. <script type="math/tex; mode=display">|T|</script> represents the length of string <script type="math/tex; mode=display">T</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(|S| + |T|)</script>. <script type="math/tex; mode=display">|S|</script> when the window size is equal to the entire string <script type="math/tex; mode=display">S</script>. <script type="math/tex; mode=display">|T|</script> when <script type="math/tex; mode=display">T</script> has all unique characters.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-optimized-sliding-window">Approach 2: Optimized Sliding Window</h4>
<p><strong>Intuition</strong></p>
<p>A small improvement to the above approach can reduce the time complexity of the algorithm to <script type="math/tex; mode=display">O(2*|filtered\_S| + |S| + |T|)</script>, where <script type="math/tex; mode=display">filtered\_S</script> is the string formed from S by removing all the elements not present in <script type="math/tex; mode=display">T</script>.</p>
<p>This complexity reduction is evident when <script type="math/tex; mode=display">|filtered\_S| <<< |S|</script>.</p>
<p>This kind of scenario might happen when length of string <script type="math/tex; mode=display">T</script> is way too small than the length of string <script type="math/tex; mode=display">S</script> and string <script type="math/tex; mode=display">S</script> consists of numerous characters which are not present in <script type="math/tex; mode=display">T</script>.</p>
<p><strong>Algorithm</strong></p>
<p>We create a list called <script type="math/tex; mode=display">filtered\_S</script> which has all the characters from string <script type="math/tex; mode=display">S</script> along with their indices in <script type="math/tex; mode=display">S</script>, but these characters should be present in <script type="math/tex; mode=display">T</script>.</p>
<pre>
  S = "ABCDDDDDDEEAFFBC" T = "ABC"
  filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
  Here (0, 'A') means in string S character A is at index 0.
</pre>

<p>We can now follow our sliding window approach on the smaller string <script type="math/tex; mode=display">filtered\_S</script>.</p>
<iframe src="https://leetcode.com/playground/PGDBbStw/shared" frameborder="0" width="100%" height="500" name="PGDBbStw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity : <script type="math/tex; mode=display">O(|S| + |T|)</script> where |S| and |T| represent the lengths of strings <script type="math/tex; mode=display">S</script> and <script type="math/tex; mode=display">T</script>. The complexity is same as the previous approach. But in certain cases where <script type="math/tex; mode=display">|filtered\_S|</script> &lt;&lt;&lt; <script type="math/tex; mode=display">|S|</script>, the complexity would reduce because the number of iterations would be <script type="math/tex; mode=display">2*|filtered\_S| + |S| + |T|</script>.</li>
<li>Space Complexity : <script type="math/tex; mode=display">O(|S| + |T|)</script>.
<br><br></li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>
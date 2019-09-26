<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-sliding-window">Approach 2: Sliding Window</a></li>
<li><a href="#approach-3-sliding-window-optimized">Approach 3: Sliding Window Optimized</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>Check all the substring one by one to see if it has no duplicate character.</p>
<p><strong>Algorithm</strong></p>
<p>Suppose we have a function <code>boolean allUnique(String substring)</code> which will return true if the characters in the substring are all unique, otherwise false. We can iterate through all the possible substrings of the given string <code>s</code> and call the function <code>allUnique</code>. If it turns out to be true, then we update our answer of the maximum length of substring without duplicate characters.</p>
<p>Now let's fill the missing parts:</p>
<ol>
<li>
<p>To enumerate all substrings of a given string, we enumerate the start and end indices of them. Suppose the start and end indices are <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script>, respectively. Then we have <script type="math/tex; mode=display">0 \leq i \lt j \leq n</script> (here end index <script type="math/tex; mode=display">j</script> is exclusive by convention). Thus, using two nested loops with <script type="math/tex; mode=display">i</script> from 0 to <script type="math/tex; mode=display">n - 1</script> and <script type="math/tex; mode=display">j</script> from <script type="math/tex; mode=display">i+1</script> to <script type="math/tex; mode=display">n</script>, we can enumerate all the substrings of <code>s</code>.</p>
</li>
<li>
<p>To check if one string has duplicate characters, we can use a set. We iterate through all the characters in the string and put them into the <code>set</code> one by one. Before putting one character, we check if the set already contains it. If so, we return <code>false</code>. After the loop, we return <code>true</code>.</p>
</li>
</ol>
<iframe src="https://leetcode.com/playground/dDeYomT6/shared" frameborder="0" width="100%" height="395" name="dDeYomT6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>.</p>
<p>To verify if characters within index range <script type="math/tex; mode=display">[i, j)</script> are all unique, we need to scan all of them. Thus, it costs <script type="math/tex; mode=display">O(j - i)</script> time.</p>
<p>For a given <code>i</code>, the sum of time costed by each <script type="math/tex; mode=display">j \in [i+1, n]</script> is</p>
<p>
<script type="math/tex; mode=display">
\sum_{i+1}^{n}O(j - i)
</script>
</p>
<p>Thus, the sum of all the time consumption is:</p>
<p>
<script type="math/tex; mode=display">
O\left(\sum_{i = 0}^{n - 1}\left(\sum_{j = i + 1}^{n}(j - i)\right)\right) =
O\left(\sum_{i = 0}^{n - 1}\frac{(1 + n - i)(n - i)}{2}\right) =
O(n^3)
</script>
</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(min(n, m))</script>. We need <script type="math/tex; mode=display">O(k)</script> space for checking a substring has no duplicate characters, where <script type="math/tex; mode=display">k</script> is the size of the <code>Set</code>. The size of the Set is upper bounded by the size of the string <script type="math/tex; mode=display">n</script> and the size of the charset/alphabet <script type="math/tex; mode=display">m</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-sliding-window">Approach 2: Sliding Window</h4>
<p><strong>Algorithm</strong></p>
<p>The naive approach is very straightforward. But it is too slow. So how can we optimize it?</p>
<p>In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary. If a substring <script type="math/tex; mode=display">s_{ij}</script> from index <script type="math/tex; mode=display">i</script> to <script type="math/tex; mode=display">j - 1</script> is already checked to have no duplicate characters. We only need to check if <script type="math/tex; mode=display">s[j]</script> is already in the substring <script type="math/tex; mode=display">s_{ij}</script>.</p>
<p>To check if a character is already in the substring, we can scan the substring, which leads to an <script type="math/tex; mode=display">O(n^2)</script> algorithm. But we can do better.</p>
<p>By using HashSet as a sliding window, checking if a character in the current can be done in <script type="math/tex; mode=display">O(1)</script>.</p>
<p>A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. <script type="math/tex; mode=display">[i, j)</script> (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide <script type="math/tex; mode=display">[i, j)</script> to the right by <script type="math/tex; mode=display">1</script> element, then it becomes <script type="math/tex; mode=display">[i+1, j+1)</script> (left-closed, right-open).</p>
<p>Back to our problem. We use HashSet to store the characters in current window <script type="math/tex; mode=display">[i, j)</script> (<script type="math/tex; mode=display">j = i</script> initially). Then we slide the index <script type="math/tex; mode=display">j</script> to the right. If it is not in the HashSet, we slide <script type="math/tex; mode=display">j</script> further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index <script type="math/tex; mode=display">i</script>. If we do this for all <script type="math/tex; mode=display">i</script>, we get our answer.</p>
<iframe src="https://leetcode.com/playground/gajHJS2a/shared" frameborder="0" width="100%" height="361" name="gajHJS2a"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2n) = O(n)</script>. In the worst case each character will be visited twice by <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(min(m, n))</script>. Same as the previous approach. We need <script type="math/tex; mode=display">O(k)</script> space for the sliding window, where <script type="math/tex; mode=display">k</script> is the size of the <code>Set</code>. The size of the Set is upper bounded by the size of the string <script type="math/tex; mode=display">n</script> and the size of the charset/alphabet <script type="math/tex; mode=display">m</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-sliding-window-optimized">Approach 3: Sliding Window Optimized</h4>
<p>The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.</p>
<p>The reason is that if <script type="math/tex; mode=display">s[j]</script> have a duplicate in the range <script type="math/tex; mode=display">[i, j)</script> with index <script type="math/tex; mode=display">j'</script>, we don't need to increase <script type="math/tex; mode=display">i</script> little by little. We can skip all the elements in the range <script type="math/tex; mode=display">[i, j']</script> and let <script type="math/tex; mode=display">i</script> to be <script type="math/tex; mode=display">j' + 1</script> directly.</p>
<p><strong>Java (Using HashMap)</strong></p>
<iframe src="https://leetcode.com/playground/ers9VnKH/shared" frameborder="0" width="100%" height="310" name="ers9VnKH"></iframe>

<p><strong>Java (Assuming ASCII 128)</strong></p>
<p>The previous implements all have no assumption on the charset of the string <code>s</code>.</p>
<p>If we know that the charset is rather small, we can replace the <code>Map</code> with an integer array as direct access table.</p>
<p>Commonly used tables are:</p>
<ul>
<li><code>int[26]</code> for Letters 'a' - 'z' or 'A' - 'Z'</li>
<li><code>int[128]</code> for ASCII</li>
<li><code>int[256]</code> for Extended ASCII</li>
</ul>
<iframe src="https://leetcode.com/playground/KgRWfFiE/shared" frameborder="0" width="100%" height="276" name="KgRWfFiE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Index <script type="math/tex; mode=display">j</script> will iterate <script type="math/tex; mode=display">n</script> times.</p>
</li>
<li>
<p>Space complexity (HashMap) : <script type="math/tex; mode=display">O(min(m, n))</script>. Same as the previous approach.</p>
</li>
<li>
<p>Space complexity (Table): <script type="math/tex; mode=display">O(m)</script>. <script type="math/tex; mode=display">m</script> is the size of the charset.</p>
</li>
</ul>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-dynamic-programming-accepted">Approach #2 Dynamic Programming [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>Enumerate all possible subsequences to see if they are arithmetic sequences.</p>
<p><strong>Algorithm</strong></p>
<p>We can use depth-first search to generate all subsequences. We can check a Subsequence is arithmetic or not by its definition.</p>
<iframe src="https://leetcode.com/playground/yNoZjyFt/shared" frameborder="0" width="100%" height="500" name="yNoZjyFt"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^n)</script>. For each element in the array, it can be in or outside the subsequence. So the time complexity is <script type="math/tex; mode=display">O(2^n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. We only need the space to store the array.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-accepted">Approach #2 Dynamic Programming [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>To determine an arithmetic sequence, we need at least two parameters: the first (or last) element of the sequence, and the common difference.</p>
<p><strong>Algorithm</strong></p>
<p>Starting from this point, we can easily figure out that one state representation that may work:</p>
<blockquote>
<p><code>f[i][d]</code> denotes the number of arithmetic subsequences that ends with <code>A[i]</code> and its common difference is <code>d</code>.</p>
</blockquote>
<p>Let's try to find the state transitions based on the representation above. Assume we want to append a new element <code>A[i]</code> to existing arithmetic subsequences to form new subsequences. We can append <code>A[i]</code> to an existing arithmetic subsequence, only if the difference between the sequence's last element and <code>A[i]</code> is equal to the sequence's common difference.</p>
<p>Thus, we can define the state transitions for the element <code>A[i]</code> intuitively :</p>
<blockquote>
<p>for all <code>j &lt; i</code>, f[i][A[i] - A[j]] += f[j][A[i] - A[j]].</p>
</blockquote>
<p>This demonstrates the appending process above to form new arithmetic subsequences.</p>
<p>But here comes the problem. Initially all <code>f[i][d]</code> are set to be <code>0</code>, but how can we form a new arithmetic subsequence if there are no existing subsequences before?</p>
<p>In the original definition of arithmetic subsequences, the length of the subsequence must be at least <code>3</code>. This makes it hard to form new subsequences if only two indices <code>i</code> and <code>j</code> are given. How about taking the subsequences of length <code>2</code> into account?</p>
<p>We can define <code>weak arithmetic subsequences</code> as follows:</p>
<blockquote>
<p><strong>Weak arithmetic subsequences</strong> are subsequences that  consist of at least two elements and if the difference between any two consecutive elements is the same.</p>
</blockquote>
<p>There are two properties of weak arithmetic subsequences that are very useful:</p>
<ul>
<li>
<p>For any pair <code>i, j (i != j)</code>, <code>A[i]</code> and <code>A[j]</code> can always form a weak arithmetic subsequence.</p>
</li>
<li>
<p>If we can append a new element to a weak arithmetic subsequence and keep it arithmetic, then the new subsequence must be an arithmetic subsequence.</p>
</li>
</ul>
<p>The second property is quite trival, because the only difference between arithmetic subsequences and weak arithmetic subsequences is their length.</p>
<p>Thus we can change the state representations accordingly:</p>
<blockquote>
<p><code>f[i][d]</code> denotes the number of weak arithmetic subsequences that ends with <code>A[i]</code> and its common difference is <code>d</code>.</p>
</blockquote>
<p>Now the state transitions are quite straightforward:</p>
<blockquote>
<p>for all <code>j &lt; i</code>, f[i][A[i] - A[j]] += (f[j][A[i] - A[j]] + 1).</p>
</blockquote>
<p>The <code>1</code> appears here because of the property one, we can form a new weak arithmetic subsequence for the pair <code>(i, j)</code>.</p>
<p>Now the number of all weak arithmetic subsequences is the sum of all <code>f[i][d]</code>. But how can we get the number of arithmetic subsequences that are not <code>weak</code>?</p>
<p>There are two ways:</p>
<ul>
<li>
<p>First, we can count the number of <code>pure weak</code> arithmetic subsequences directly. The <code>pure weak</code> arithmetic subsequences are the arithmetic subsequences of length <code>2</code>, so the number of <code>pure weak</code> arithmetic subsequences should be equal to the number of pairs <code>(i, j)</code>, which is <script type="math/tex; mode=display">\binom{n}{2} = \frac{n * (n - 1)}{2}.</script>
</p>
</li>
<li>
<p>Second, for the summation <code>f[i][A[i] - A[j]] += (f[j][A[i] - A[j]] + 1)</code>, <code>f[j][A[i] - A[j]]</code> is the number of existing weak arithmetic subsequences, while <code>1</code> is the new subsequence built with <code>A[i]</code> and <code>A[j]</code>. Based on property two, when we are appending new elements to existing weak arithmetic subsequences, we are forming arithmetic subsequences. So the first part, <code>f[j][A[i] - A[j]]</code> is the number of new formed arithmetic subsequences, and can be added to the answer.</p>
</li>
</ul>
<p>We can use the following example to illustrate the process:</p>
<blockquote>
<p>[1, 1, 2, 3, 4, 5]</p>
</blockquote>
<p>We need to count the answer for the above sequence.</p>
<ul>
<li>
<p>For the first element <code>1</code>, there is no element in front of it, the answer remains <code>0</code>.</p>
</li>
<li>
<p>For the second element <code>1</code>, the element itself with the previous <code>1</code> can form a pure weak arithmetic subsequence with common difference <code>0</code> : <code>[1, 1]</code>.</p>
</li>
<li>
<p>For the third element <code>2</code>, it cannot be appended to the only weak arithmetic subsequence <code>[1, 1]</code>, so the answer remains <code>0</code>. Similar to the second element, it can form new weak arithmetic subsequences <code>[1, 2]</code> and <code>[1, 2]</code>.</p>
</li>
<li>
<p>For the forth element <code>3</code>, if we append it to some arithmetic subsequences ending with <code>2</code>, these subsequences must have a common difference of <code>3 - 2 = 1</code>. Indeed there are two: <code>[1, 2]</code> and <code>[1, 2]</code>. So we can append <code>3</code> to the end of these subsequences, and the answer is added by <code>2</code>. Similar to above, it can form new weak arithmetic subsequences <code>[1, 3], [1, 3]</code> and <code>[2, 3]</code>.</p>
</li>
<li>
<p>The other elements are the same, we can view the process in the figure below. The red bracket indicates the weak arithmetic subsequence of length <code>2</code>, and the black bracket indicates the arithmetic subsequence. The answer should be the total number of black brackets.</p>
</li>
</ul>
<p><img src="../Figures/446_Arithmetic_Slices_II_Subsequence.png" width="80%" height="80%"></p>
<iframe src="https://leetcode.com/playground/MVagoidb/shared" frameborder="0" width="100%" height="446" name="MVagoidb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n ^ 2)</script>. We can use double loop to enumerate all possible states.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n ^ 2)</script>. For each <code>i</code>, we need to store at most <code>n</code> distinct common differences, so the total space complexity is <script type="math/tex; mode=display">O(n ^ 2)</script>.</p>
</li>
</ul>
          </div>
        
      </div>
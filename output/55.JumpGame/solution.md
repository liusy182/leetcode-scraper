<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#naming">Naming</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-backtracking">Approach 1: Backtracking</a></li>
<li><a href="#approach-2-dynamic-programming-top-down">Approach 2: Dynamic Programming Top-down</a></li>
<li><a href="#approach-3-dynamic-programming-bottom-up">Approach 3: Dynamic Programming Bottom-up</a></li>
<li><a href="#approach-4-greedy">Approach 4: Greedy</a></li>
</ul>
</li>
<li><a href="#conclusion">Conclusion</a></li>
<li><a href="#appendix-a-complexity-analysis-for-approach-1">Appendix A - Complexity Analysis for Approach 1</a></li>
<li><a href="#references">References</a></li>
</ul>
</div>
<h2 id="naming">Naming</h2>
<hr>
<ul>
<li>We call a position in the array a <strong>"good index"</strong> if starting at that position, we can reach the last index. Otherwise, that index is called a <strong>"bad index"</strong>. The problem then reduces to whether or not index 0 is a "good index".</li>
</ul>
<h2 id="solution">Solution</h2>
<hr>
<p>This is a dynamic programming<sup id="fnref:1"><a class="footnote-ref" href="#fn:1" rel="footnote">1</a></sup> question. Usually, solving and fully understanding a dynamic programming problem is a 4 step process:</p>
<ol>
<li>Start with the recursive backtracking solution</li>
<li>Optimize by using a memoization table (top-down<sup id="fnref:3"><a class="footnote-ref" href="#fn:3" rel="footnote">3</a></sup> dynamic programming)</li>
<li>Remove the need for recursion (bottom-up dynamic programming)</li>
<li>Apply final tricks to reduce the time / memory complexity</li>
</ol>
<p>All solutions presented below produce the correct result, but they differ in run time and memory requirements.<br><br></p>
<hr>
<h4 id="approach-1-backtracking">Approach 1: Backtracking</h4>
<p>This is the inefficient solution where we try every single jump pattern that takes us from the first position to the last. We start from the first position and jump to every index that is reachable. We repeat the process until last index is reached. When stuck, backtrack.</p>
<iframe src="https://leetcode.com/playground/S9aCUfCG/shared" frameborder="0" width="100%" height="395" name="S9aCUfCG"></iframe>

<p>One quick optimization we can do for the code above is to check the <code>nextPosition</code> from right to left. The theoretical worst case performance is the same, but in practice, for silly examples, the code might run faster. Intuitively, this means we always try to make the biggest jump such that we reach the end as soon as possible</p>
<p>The change required is:</p>
<iframe src="https://leetcode.com/playground/Eak7LXyr/shared" frameborder="0" width="100%" height="123" name="Eak7LXyr"></iframe>

<p>For instance, in the example below, if we start from index <strong>0</strong>, jump as far as possible and reach <strong>1</strong>, jump as far as possible and reach <strong>6</strong>. By doing so, we determine that <strong>0</strong> is a <em>GOOD</em> index in 3 steps.</p>
<table>
<thead>
<tr>
<th align="center">Index</th>
<th align="center">0</th>
<th align="center">1</th>
<th align="center">2</th>
<th align="center">3</th>
<th align="center">4</th>
<th align="center">5</th>
<th align="center">6</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">nums</td>
<td align="center">1</td>
<td align="center">5</td>
<td align="center">2</td>
<td align="center">1</td>
<td align="center">0</td>
<td align="center">2</td>
<td align="center">0</td>
</tr>
</tbody>
</table>
<p>To illustrate the worst case, where this optimization has no effect, take the example below. Index <strong>6</strong> cannot be reached from any position, but all combinations will be tried.</p>
<table>
<thead>
<tr>
<th align="center">Index</th>
<th align="center">0</th>
<th align="center">1</th>
<th align="center">2</th>
<th align="center">3</th>
<th align="center">4</th>
<th align="center">5</th>
<th align="center">6</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">nums</td>
<td align="center">5</td>
<td align="center">4</td>
<td align="center">3</td>
<td align="center">2</td>
<td align="center">1</td>
<td align="center">0</td>
<td align="center">0</td>
</tr>
</tbody>
</table>
<p>The first few steps of the backtracking algorithm for the example above are: 0 -&gt; 4 -&gt; 5 -&gt; 4 -&gt; 0 -&gt; 3 -&gt; 5 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; etc.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^n)</script>. There are <script type="math/tex; mode=display">2^n</script> (upper bound) ways of jumping from the first position to the last, where <script type="math/tex; mode=display">n</script> is the length of array <code>nums</code>. For a complete proof, please refer to Appendix A.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Recursion requires additional memory for the stack frames.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming-top-down">Approach 2: Dynamic Programming Top-down</h4>
<p>Top-down Dynamic Programming can be thought of as optimized backtracking. It relies on the observation that once we determine that a certain index is good / bad, this result will never change. This means that we can store the result and not need to recompute it every time.</p>
<p>Therefore, for each position in the array, we remember whether the index is good or bad. Let's call this array <code>memo</code> and let its values be either one of: GOOD, BAD, UNKNOWN. This technique is called memoization<sup id="fnref:2"><a class="footnote-ref" href="#fn:2" rel="footnote">2</a></sup>.</p>
<p>An example of a memoization table for input array <code>nums = [2, 4, 2, 1, 0, 2, 0]</code> can be seen in the diagram below. We write <strong>G</strong> for a <em>GOOD</em> position and <strong>B</strong> for a <em>BAD</em> one. We can see that we cannot start from indices 2, 3 or 4 and eventually reach last index (6), but we can do that from indices 0, 1, 5 and (trivially) 6.</p>
<table>
<thead>
<tr>
<th align="center">Index</th>
<th align="center">0</th>
<th align="center">1</th>
<th align="center">2</th>
<th align="center">3</th>
<th align="center">4</th>
<th align="center">5</th>
<th align="center">6</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">nums</td>
<td align="center">2</td>
<td align="center">4</td>
<td align="center">2</td>
<td align="center">1</td>
<td align="center">0</td>
<td align="center">2</td>
<td align="center">0</td>
</tr>
<tr>
<td align="center">memo</td>
<td align="center">G</td>
<td align="center">G</td>
<td align="center">B</td>
<td align="center">B</td>
<td align="center">B</td>
<td align="center">G</td>
<td align="center">G</td>
</tr>
</tbody>
</table>
<p><strong>Steps</strong></p>
<ol>
<li>Initially, all elements of the <code>memo</code> table are <em>UNKNOWN</em>, except for the last one, which is (trivially) <em>GOOD</em> (it can reach itself)</li>
<li>Modify the backtracking algorithm such that the recursive step first checks if the index is known (<em>GOOD</em> / <em>BAD</em>)<ol>
<li>If it is known then return <em>True</em> / <em>False</em></li>
<li>Otherwise perform the backtracking steps as before</li>
</ol>
</li>
<li>Once we determine the value of the current index, we store it in the <code>memo</code> table</li>
</ol>
<iframe src="https://leetcode.com/playground/cAV9h4Nb/shared" frameborder="0" width="100%" height="500" name="cAV9h4Nb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>.
For every element in the array, say <code>i</code>, we are looking at the next <code>nums[i]</code> elements to its right aiming to find a <em>GOOD</em> index. <code>nums[i]</code> can be at most <script type="math/tex; mode=display">n</script>, where <script type="math/tex; mode=display">n</script> is the length of array <code>nums</code>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(2n) = O(n)</script>.
First n originates from recursion. Second n comes from the usage of the memo table.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming-bottom-up">Approach 3: Dynamic Programming Bottom-up</h4>
<p>Top-down to bottom-up conversion is done by eliminating recursion. In practice, this achieves better performance as we no longer have the method stack overhead and might even benefit from some caching. More importantly, this step opens up possibilities for future optimization. The recursion is usually eliminated by trying to reverse the order of the steps from the top-down approach.</p>
<p>The observation to make here is that we only ever jump to the right. This means that if we start from the right of the array, every time we will query a position to our right, that position has already be determined as being <em>GOOD</em> or <em>BAD</em>. This means we don't need to recurse anymore, as we will always hit the <code>memo</code> table.</p>
<iframe src="https://leetcode.com/playground/V8VSofDS/shared" frameborder="0" width="100%" height="480" name="V8VSofDS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>.
For every element in the array, say <code>i</code>, we are looking at the next <code>nums[i]</code> elements to its right aiming to find a <em>GOOD</em> index. <code>nums[i]</code> can be at most <script type="math/tex; mode=display">n</script>, where <script type="math/tex; mode=display">n</script> is the length of array <code>nums</code>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>.
This comes from the usage of the memo table.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-greedy">Approach 4: Greedy</h4>
<p>Once we have our code in the bottom-up state, we can make one final, important observation. From a given position, when we try to see if we can jump to a <em>GOOD</em> position, we only ever use one - the first one (see the break statement). In other words, the left-most one. If we keep track of this left-most <em>GOOD</em> position as a separate variable, we can avoid searching for it in the array. Not only that, but we can stop using the array altogether.</p>
<p>Iterating right-to-left, for each position we check if there is a potential jump that reaches a <em>GOOD</em> index (<code>currPosition + nums[currPosition] &gt;= leftmostGoodIndex</code>). If we can reach a <em>GOOD</em> index, then our position is itself <em>GOOD</em>. Also, this new <em>GOOD</em> position will be the new leftmost <em>GOOD</em> index. Iteration continues until the beginning of the array. If first position is a <em>GOOD</em> index then we can reach the last index from the first position.</p>
<p>To illustrate this scenario, we will use the diagram below, for input array <code>nums = [9, 4, 2, 1, 0, 2, 0]</code>. We write <strong>G</strong> for <em>GOOD</em>, <strong>B</strong> for <em>BAD</em> and <strong>U</strong> for <em>UNKNOWN</em>. Let's assume we have iterated all the way to position 0 and we need to decide if index 0 is <em>GOOD</em>. Since index 1 was determined to be <em>GOOD</em>, it is enough to jump there and then be sure we can eventually reach index 6. It does not matter that <code>nums[0]</code> is big enough to jump all the way to the last index. All we need is <strong>one</strong> way.</p>
<table>
<thead>
<tr>
<th align="center">Index</th>
<th align="center">0</th>
<th align="center">1</th>
<th align="center">2</th>
<th align="center">3</th>
<th align="center">4</th>
<th align="center">5</th>
<th align="center">6</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">nums</td>
<td align="center">9</td>
<td align="center">4</td>
<td align="center">2</td>
<td align="center">1</td>
<td align="center">0</td>
<td align="center">2</td>
<td align="center">0</td>
</tr>
<tr>
<td align="center">memo</td>
<td align="center">U</td>
<td align="center">G</td>
<td align="center">B</td>
<td align="center">B</td>
<td align="center">B</td>
<td align="center">G</td>
<td align="center">G</td>
</tr>
</tbody>
</table>
<iframe src="https://leetcode.com/playground/9y9y7Lry/shared" frameborder="0" width="100%" height="242" name="9y9y7Lry"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>.
We are doing a single pass through the <code>nums</code> array, hence <script type="math/tex; mode=display">n</script> steps, where <script type="math/tex; mode=display">n</script> is the length of array <code>nums</code>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>.
We are not using any extra memory.</p>
</li>
</ul>
<h2 id="conclusion">Conclusion</h2>
<p>The question left unanswered is how should one approach such a question in an interview scenario. I would say "it depends". The perfect solution is cleaner and shorter than all the other versions, but it might not be so straightforward to figure out.</p>
<p>The (recursive) backtracking is the easiest to figure out, so it is worth mentioning it verbally while warming up for the tougher challenge. It might be that your interviewer actually wants to see that solution, but if not, mention that there might be a dynamic programming solution and try to think how could you use a memoization table. If you figure it out and the interviewer wants you to go for the top-down approach, it will not generally be time to think of the bottom-up version, but I would always mention the advantages of this technique as a final thought in the interview.</p>
<p>Most people are stuck when converting from top-down Dynamic Programming (expressed naturally in recursion) to bottom-up. Practicing similar problems will help bridge this gap.</p>
<h2 id="appendix-a-complexity-analysis-for-approach-1">Appendix A - Complexity Analysis for <a href="#approach-1-backtracking">Approach 1</a></h2>
<p>There are <script type="math/tex; mode=display">2^n</script> (upper bound) ways of jumping from the first position to the last, where <script type="math/tex; mode=display">n</script> is the length of array <code>nums</code>. We get this recursively. Let <script type="math/tex; mode=display">T(x)</script> be the number of possible ways of jumping from position <strong>x</strong> to position <strong>n</strong>. <script type="math/tex; mode=display">T(n) = 1</script> trivially. <script type="math/tex; mode=display">T(x) = \sum_{i = x + 1}^{n} T(i)</script> because from position <strong>x</strong> we can potentially jump to all following positions <strong>i</strong> and then from there there are <script type="math/tex; mode=display">T(i)</script> ways of continuing. Notice this is an upper bound.</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
T(x) &= \sum_{i = x + 1}^{n} T(i) \\
&= T(x + 1) + \sum_{i = x + 2}^{n} T(i) \\
&= T(x + 1) + T(x + 1) \\
&= 2 \cdot T(x + 1)
\end{aligned}
</script>
</p>
<p>Now by induction, assume <script type="math/tex; mode=display">T(x) = 2^{n - x - 1}</script> and prove <script type="math/tex; mode=display">T(x - 1) = 2^{n - (x - 1) - 1}</script>
</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
T(x - 1) &= 2 \cdot T(x) \\
&= 2 \cdot 2^{n - x - 1} \\
&= 2^{n - x - 1 + 1} \\
&= 2^{n - (x - 1) - 1}
\end{aligned}
</script>
</p>
<p>Therefore, since we start from position 1, <script type="math/tex; mode=display">T(1) = 2^{n - 2}</script>. Final complexity <script type="math/tex; mode=display">O(2^{n - 2})</script> = <script type="math/tex; mode=display">O(2^n)</script>.</p>
<h2 id="references">References</h2>
<div class="footnote">
<hr>
<ol>
<li id="fn:1">
<p><a href="https://en.wikipedia.org/wiki/Dynamic_programming">https://en.wikipedia.org/wiki/Dynamic_programming</a> <a class="footnote-backref" href="#fnref:1" rev="footnote" title="Jump back to footnote 1 in the text">↩</a></p>
</li>
<li id="fn:2">
<p><a href="https://en.wikipedia.org/wiki/Memoization">https://en.wikipedia.org/wiki/Memoization</a> <a class="footnote-backref" href="#fnref:2" rev="footnote" title="Jump back to footnote 2 in the text">↩</a></p>
</li>
<li id="fn:3">
<p><a href="https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design">https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design</a> <a class="footnote-backref" href="#fnref:3" rev="footnote" title="Jump back to footnote 3 in the text">↩</a></p>
</li>
</ol>
</div>
          </div>
        
      </div>
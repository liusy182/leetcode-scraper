<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</a></li>
<li><a href="#approach-2-using-memorization-accepted">Approach #2 Using Memorization [Accepted]</a></li>
<li><a href="#approach-3-using-some-math-accepted">Approach #3 Using some Math [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-accepted">Approach #1 Brute Force [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Brute force of this problem is to divide the list into two parts <script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> and call function for these two parts. We will iterate <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">start</script> to <script type="math/tex; mode=display">end</script> so that <script type="math/tex; mode=display">left=(start,i)</script> and <script type="math/tex; mode=display">right=(i+1,end)</script>.</p>
<p>
<script type="math/tex; mode=display">left</script> and <script type="math/tex; mode=display">right</script> parts return their maximum and minimum value and corresponding strings.</p>
<p>Minimum value can be found by dividing minimum of left by maximum of right i.e. <script type="math/tex; mode=display">minVal=left.min/right.max</script>.</p>
<p>Similarly,Maximum value can be found by dividing maximum of left value by minimum of right value. i.e. <script type="math/tex; mode=display">maxVal=left.max/right.min</script>.</p>
<p>Now, how to add parenthesis? As associativity of division operator is from left to right i.e. by default left most divide should be done first, we need not have to add paranthesis to the left part, but we must add parenthesis to the right part.</p>
<p>eg- "2/(3/4)" will be formed as leftPart+"/"+"("+rightPart+")", assuming leftPart is "2" and rightPart is"3/4".</p>
<p>One more point, we also don't require parenthesis to right part when it contains single digit.</p>
<p>eg- "2/3", here left part is "2" and right part is "3" (contains single digit) . 2/(3) is not valid.</p>
<iframe src="https://leetcode.com/playground/CAbJyzm4/shared" frameborder="0" name="CAbJyzm4" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n!)</script>. Number of permutations of expression after applying brackets will be in <script type="math/tex; mode=display">O(n!)</script> where <script type="math/tex; mode=display">n</script> is the number of items in the list.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n^2)</script>. Depth of recursion tree will be <script type="math/tex; mode=display">O(n)</script> and each node contains string of maximum length <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-memorization-accepted">Approach #2 Using Memorization [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the above approach we called optimal function recursively for ever <script type="math/tex; mode=display">start</script> and <script type="math/tex; mode=display">end</script>. We can notice that there are many redundant calls in the above approach, we can reduce these calls by using memorization to store the result of different function calls. Here, <script type="math/tex; mode=display">memo</script> array is used for this purpose.</p>
<iframe src="https://leetcode.com/playground/xFgr7Cpd/shared" frameborder="0" name="xFgr7Cpd" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n^2</script> is filled and filling of each cell of the <script type="math/tex; mode=display">memo</script> array takes <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^3)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n^2</script> where each cell of array contains string of length <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-some-math-accepted">Approach #3 Using some Math [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Using some simple math we can find the easy solution of this problem. Consider the input in the form of [a,b,c,d], now we have to set priority of
operations to maximize a/b/c/d. We know that to maximize fraction <script type="math/tex; mode=display">p/q</script>, <script type="math/tex; mode=display">q</script>(denominator) should be minimized. So, to maximize <script type="math/tex; mode=display">a/b/c/d</script>  we have to first minimize b/c/d. Now our objective turns to minimize the expression b/c/d.</p>
<p>There are two possible combinations of this expression, b/(c/d) and (b/c)/d.</p>
<div class="codehilite"><pre><span></span>b/(c/d)        (b/c)/d = b/c/d
(b*d)/c        b/(d*c)
d/c            1/(d*c)
</pre></div>


<p>Obviously, <script type="math/tex; mode=display">d/c > 1/(d*c)</script> for <script type="math/tex; mode=display">d>1</script>.</p>
<p>You can see that second combination will always be less than first one for numbers greater than <script type="math/tex; mode=display">1</script>. So, the answer will be a/(b/c/d).
Similarly for expression like a/b/c/d/e/f... answer will be a/(b/c/d/e/f...).</p>
<iframe src="https://leetcode.com/playground/wUbJEUre/shared" frameborder="0" name="wUbJEUre" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single loop to traverse <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">res</script> variable is used to store the result.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
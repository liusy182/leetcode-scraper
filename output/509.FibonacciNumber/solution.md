<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-recursion">Approach 1: Recursion</a></li>
<li><a href="#approach-2-bottom-up-approach-using-memoization">Approach 2: Bottom-Up Approach using Memoization</a></li>
<li><a href="#approach-3-top-down-approach-using-memoization">Approach 3: Top-Down Approach using Memoization</a></li>
<li><a href="#approach-4-iterative-top-down-approach">Approach 4: Iterative Top-Down Approach</a></li>
<li><a href="#approach-5-matrix-exponentiation">Approach 5: Matrix Exponentiation</a></li>
<li><a href="#approach-6-math">Approach 6: Math</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-recursion">Approach 1: Recursion</h4>
<p><strong>Intuition</strong></p>
<p>Use recursion to compute the Fibonacci number of a given integer.</p>
<p align="center"><img alt="fib(5) Recursion diagram" src="../Figures/509/fibonacciRecursion5.png" width="539px"></p>
<p align="center"><em>Figure 1. An example tree representing what <code>fib(5)</code> would look like</em></p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Check if the provided input value, N, is less than or equal to 1. If true, return N.</li>
<li>
<p>Otherwise, the function <code>fib(int N)</code> calls itself, with the result of the 2 previous numbers being added to each other, passed in as the argument.
This is derived directly from the <code>recurrence relation</code>:
<script type="math/tex; mode=display">F_{n} = F_{n-1} + F_{n-2}</script>
</p>
</li>
<li>
<p>Do this until all numbers have been computed, then return the resulting answer.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/LkwrRUoJ/shared" frameborder="0" width="100%" height="191" name="LkwrRUoJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^N)</script>. This is the slowest way to solve the <code>Fibonacci Sequence</code> because it takes exponential time. The amount of operations needed, for each level of recursion, grows exponentially as the depth approaches <code>N</code>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(N)</script>. We need space proportionate to <code>N</code> to account for the max size of the stack, in memory. This stack keeps track of the function calls to <code>fib(N)</code>. This has the potential to be bad in cases that there isn't enough physical memory to handle the increasingly growing stack, leading to a <code>StackOverflowError</code>. The <a href="https://docs.oracle.com/javase/7/docs/api/java/lang/StackOverflowError.html">Java docs</a> have a good explanation of this, describing it as an error that occurs because an application recurses too deeply.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-2-bottom-up-approach-using-memoization">Approach 2: Bottom-Up Approach using Memoization</h4>
<p><strong>Intuition</strong></p>
<p>Improve upon the recursive option by using iteration, still solving for all of the sub-problems and returning the answer for N, using already computed Fibonacci values. In using a bottom-up approach, we can iteratively compute and store the values, only returning once we reach the result.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>If <code>N</code> is less than or equal to 1, return <code>N</code></li>
<li>Otherwise, iterate through <code>N</code>, storing each computed answer in an array along the way.</li>
<li>Use this array as a reference to the 2 previous numbers to calculate the current Fibonacci number.</li>
<li>Once we've reached the last number, return it's Fibonacci number.</li>
</ul>
<iframe src="https://leetcode.com/playground/D7nAMtfU/shared" frameborder="0" width="100%" height="361" name="D7nAMtfU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(N)</script>. Each number, starting at 2 up to and including <code>N</code>, is visited, computed and then stored for <script type="math/tex; mode=display">O(1)</script> access later on.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(N)</script>. The size of the data structure is proportionate to <code>N</code>.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-3-top-down-approach-using-memoization">Approach 3: Top-Down Approach using Memoization</h4>
<p><strong>Intuition</strong></p>
<p>Solve for all of the sub-problems, use memoization to store the pre-computed answers, then return the answer for N. We will leverage recursion, but in a smarter way by not repeating the work to calculate existing values.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Check if <code>N &lt;= 1</code>. If it is, return <code>N</code>.</li>
<li>Call and return <code>memoize(N)</code></li>
<li>If <code>N</code> exists in the map, return the cached value for <code>N</code></li>
<li>Otherwise set the value of <code>N</code>, in our mapping, to the value of <code>memoize(N-1) + memoize(N-2)</code></li>
</ul>
<iframe src="https://leetcode.com/playground/GNj9PYYG/shared" frameborder="0" width="100%" height="395" name="GNj9PYYG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(N)</script>. Each number, starting at 2 up to and including <code>N</code>, is visited, computed and then stored for <script type="math/tex; mode=display">O(1)</script> access later on.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(N)</script>. The size of the stack in memory is proportionate to <code>N</code>.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-4-iterative-top-down-approach">Approach 4: Iterative Top-Down Approach</h4>
<p><strong>Intuition</strong></p>
<p>Let's get rid of the need to use all of that space and instead use the minimum amount of space required. We can achieve <script type="math/tex; mode=display">O(1)</script> space complexity by only storing the value of the two previous numbers and updating them as we iterate to <code>N</code>.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Check if <code>N &lt;= 1</code>, if it is then we should return <code>N</code>.</li>
<li>Check if <code>N == 2</code>, if it is then we should return <code>1</code> since <code>N</code> is 2 and <code>fib(2-1) + fib(2-2)</code> equals <code>1 + 0 = 1</code>.</li>
<li>To use an iterative approach, we need at least 3 variables to store each state <code>fib(N)</code>, <code>fib(N-1)</code> and <code>fib(N-2)</code>.</li>
<li>Preset the initial values:</li>
<li>Initialize <code>current</code> with 0.</li>
<li>Initialize <code>prev1</code> with 1, since this will represent <code>fib(N-1)</code> when computing the current value.</li>
<li>Initialize <code>prev2</code> with 1, since this will represent <code>fib(N-2)</code> when computing the current value.</li>
<li>Iterate, incrementally by 1, all the way up to and including <code>N</code>. Starting at 3, since <code>0</code>, <code>1</code> and <code>2</code> are pre-computed.</li>
<li>Set the <code>current</code> value to <code>fib(N-1) + fib(N-2)</code> because that is the value we are currently computing.</li>
<li>Set the <code>prev2</code> value to <code>fib(N-1)</code>.</li>
<li>Set the <code>prev1</code> value to <code>current_value</code>.</li>
<li>When we reach <code>N+1</code>, we will exit the loop and return the previously set <code>current</code> value.</li>
</ul>
<iframe src="https://leetcode.com/playground/SEzLkERR/shared" frameborder="0" width="100%" height="412" name="SEzLkERR"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(N)</script>. Each value from <code>2 to N</code> will be visited at least once. The time it takes to do this is directly proportionate to <code>N</code> where <code>N</code> is the <code>Fibonacci Number</code> we are looking to compute.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. This requires 1 unit of Space for the integer <code>N</code> and 3 units of Space to store the computed values (<code>curr</code>, <code>prev1</code> and <code>prev2</code>) for every loop iteration. The amount of Space doesn't change so this is constant Space complexity.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-5-matrix-exponentiation">Approach 5: Matrix Exponentiation</h4>
<p><strong>Intuition</strong></p>
<p>Use Matrix Exponentiation to get the Fibonacci number from the element at (0, 0) in the resultant matrix.</p>
<p>In order to do this we can rely on the matrix equation for the Fibonacci sequence, to find the <code>Nth</code> Fibonacci number:
<script type="math/tex; mode=display">
\begin{pmatrix}
 1\,\,1 \\
 1\,\,0
\end{pmatrix}^{n}=\begin{pmatrix}
 \: F_{(n+1)}\;\;\:F_{(n)}\\
 \: F_{(n)}\;\;\:F_{(n-1)}
\end{pmatrix}
</script>
</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Check if <code>N</code> is less than or equal to 1. If it is, return <code>N</code>.</li>
<li>Use a recursive function, <code>matrixPower</code>, to calculate the power of a given matrix <code>A</code>. The power will be <code>N-1</code>, where <code>N</code> is the <code>Nth Fibonacci number</code>.</li>
<li>The <code>matrixPower</code> function will be performed for <code>N/2</code> of the Fibonacci numbers.</li>
<li>Within <code>matrixPower</code>, call the <code>multiply</code> function to multiply 2 matrices.</li>
<li>Once we finish doing the calculations, return <code>A[0][0]</code> to get the <code>Nth</code> Fibonacci number.</li>
</ul>
<iframe src="https://leetcode.com/playground/NCxGpFr2/shared" frameborder="0" width="100%" height="500" name="NCxGpFr2"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log N)</script>. By halving the <code>N</code> value in every <code>matrixPower</code>'s call to itself, we are halving the work needed to be done.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\log N)</script>. The size of the stack in memory is proportionate to the function calls to <code>matrixPower</code> plus the memory used to account for the matrices which takes up constant space.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-6-math">Approach 6: Math</h4>
<p><strong>Intuition</strong>
Using the <code>golden ratio</code>, a.k.a <code>Binet's forumula</code>: <script type="math/tex; mode=display"> \varphi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887.... </script>
</p>
<p>Here's a <a href="http://demonstrations.wolfram.com/GeneralizedFibonacciSequenceAndTheGoldenRatio/">link</a> to find out more about how the Fibonacci sequence and the golden ratio work.</p>
<p>We can derive the most efficient solution to this problem using only constant time and constant space!</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Use the <code>golden ratio</code> formula to calculate the <code>Nth</code> Fibonacci number.</li>
</ul>
<iframe src="https://leetcode.com/playground/F8NT7g5D/shared" frameborder="0" width="100%" height="157" name="F8NT7g5D"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(1)</script>. Constant time complexity since we are using no loops or recursion and the time is based on the result of performing the calculation using <code>Binet's formula</code>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. The space used is the space needed to create the variable to store the <code>golden ratio</code> formula.</p>
</li>
</ul>
          </div>
        
      </div>
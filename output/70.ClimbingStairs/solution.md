<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</a></li>
<li><a href="#approach-3-dynamic-programming">Approach 3: Dynamic Programming</a></li>
<li><a href="#approach-4-fibonacci-number">Approach 4: Fibonacci Number</a></li>
<li><a href="#approach-5-binets-method">Approach 5: Binets Method</a></li>
<li><a href="#approach-6-fibonacci-formula">Approach 6: Fibonacci Formula</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>You are climbing a stair case. It takes n steps to reach to the top.</p>
<p>Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>In this brute force approach we take all possible step combinations i.e. 1 and 2, at every step. At every step we are calling the function <script type="math/tex; mode=display">climbStairs</script> for step <script type="math/tex; mode=display">1</script> and <script type="math/tex; mode=display">2</script>, and return the sum of returned values of both functions.</p>
<p>
<script type="math/tex; mode=display">
climbStairs(i,n)=(i + 1, n) + climbStairs(i + 2, n)
</script>
</p>
<p>where <script type="math/tex; mode=display">i</script> defines the current step and <script type="math/tex; mode=display">n</script> defines the destination step.</p>
<iframe src="https://leetcode.com/playground/vSGtWB6q/shared" frameborder="0" width="100%" height="293" name="vSGtWB6q"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(2^n)</script>. Size of recursion tree will be <script type="math/tex; mode=display">2^n</script>.</p>
<p>Recursion tree for n=5 would be like this:</p>
<p><img alt="Climbing_Stairs" src="../Figures/70_Climbing_Stairs_rt.jpg"></p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of the recursion tree can go upto <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</h4>
<p><strong>Algorithm</strong></p>
<p>In the previous approach we are redundantly calculating the result for every step. Instead, we can store the result at each step in <script type="math/tex; mode=display">memo</script> array and directly returning the result from the memo array whenever that function is called again.</p>
<p>In this way we are pruning recursion tree with the help of <script type="math/tex; mode=display">memo</script> array and reducing the size of recursion tree upto <script type="math/tex; mode=display">n</script>.</p>
<iframe src="https://leetcode.com/playground/5fLezqKW/shared" frameborder="0" width="100%" height="378" name="5fLezqKW"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Size of recursion tree can go upto <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The depth of recursion tree can go upto <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-dynamic-programming">Approach 3: Dynamic Programming</h4>
<p><strong>Algorithm</strong></p>
<p>As we can see this problem can be broken into subproblems, and it contains the optimal substructure property i.e. its optimal solution can be constructed efficiently from optimal solutions of its subproblems, we can use dynamic programming to solve this problem.</p>
<p>One can reach <script type="math/tex; mode=display">i^{th}</script> step in one of the two ways:</p>
<ol>
<li>
<p>Taking a single step from <script type="math/tex; mode=display">(i-1)^{th}</script> step.</p>
</li>
<li>
<p>Taking a step of <script type="math/tex; mode=display">2</script> from <script type="math/tex; mode=display">(i-2)^{th}</script> step.</p>
</li>
</ol>
<p>So, the total number of ways to reach <script type="math/tex; mode=display">i^{th}</script> is equal to sum of ways of reaching <script type="math/tex; mode=display">(i-1)^{th}</script> step and ways of reaching <script type="math/tex; mode=display">(i-2)^{th}</script> step.</p>
<p>Let <script type="math/tex; mode=display">dp[i]</script> denotes the number of ways to reach on <script type="math/tex; mode=display">i^{th}</script> step:</p>
<p>
<script type="math/tex; mode=display">
dp[i]=dp[i-1]+dp[i-2]
</script>
</p>
<p>Example:</p>
<!--![Climbing_Stairs](../Figures/70_Climbing_Stairs.gif)-->

<p>!?!../Documents/70_Climbing_Stairs.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/bJT3YiVD/shared" frameborder="0" width="100%" height="293" name="bJT3YiVD"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single loop upto <script type="math/tex; mode=display">n</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">dp</script> array of size <script type="math/tex; mode=display">n</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-fibonacci-number">Approach 4: Fibonacci Number</h4>
<p><strong>Algorithm</strong></p>
<p>In the above approach we have used <script type="math/tex; mode=display">dp</script> array where <script type="math/tex; mode=display">dp[i]=dp[i-1]+dp[i-2]</script>. It can be easily analysed that <script type="math/tex; mode=display">dp[i]</script> is nothing but <script type="math/tex; mode=display">i^{th}</script> fibonacci number.</p>
<p>
<script type="math/tex; mode=display">
Fib(n)=Fib(n-1)+Fib(n-2)
</script>
</p>
<p>Now we just have to find <script type="math/tex; mode=display">n^{th}</script> number of the fibonacci series having <script type="math/tex; mode=display">1</script> and <script type="math/tex; mode=display">2</script> their first and second term respectively, i.e. <script type="math/tex; mode=display">Fib(1)=1</script> and <script type="math/tex; mode=display">Fib(2)=2</script>.</p>
<iframe src="https://leetcode.com/playground/jXMy3r3P/shared" frameborder="0" width="100%" height="310" name="jXMy3r3P"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single loop upto <script type="math/tex; mode=display">n</script> is required to calculate <script type="math/tex; mode=display">n^{th}</script> fibonacci number.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-binets-method">Approach 5: Binets Method</h4>
<p><strong>Algorithm</strong></p>
<p>This is an interesting solution which uses matrix multiplication to obtain the <script type="math/tex; mode=display">n^{th}</script> Fibonacci Number. The matrix takes the following form:</p>
<p>
<script type="math/tex; mode=display">
\left[ {\begin{array}{cc} F_{n+1} & F_n \\  F_n & F_{n-1}     \end{array} } \right] = \left[ {\begin{array}{cc} 1 & 1 \\  1 & 0     \end{array} } \right]
</script>
</p>
<p>Let's say <script type="math/tex; mode=display">Q=\left[ {\begin{array}{cc} F_{n+1} & F_n \\  F_n & F_{n-1}     \end{array} } \right]</script>. As per the method, the <script type="math/tex; mode=display">n^{th}</script> Fibonacci Number is given by <script type="math/tex; mode=display">Q^{n-1}[0,0]</script>.</p>
<p>Let's look at the proof of this method.</p>
<p>We can prove this method using Mathematical Induction. We know, this matrix gives the correct result for the <script type="math/tex; mode=display">3^{rd}</script> term(base case). Since <script type="math/tex; mode=display">Q^2 = \left[ {\begin{array}{cc} 2 & 1 \\  1 & 1     \end{array} } \right]</script>. This proves that the base case holds.</p>
<p>Assume that this method holds for finding the <script type="math/tex; mode=display">n^{th}</script> Fibonacci Number, i.e. <script type="math/tex; mode=display">F_n=Q^{n-1}[0,0]</script>, where
<script type="math/tex; mode=display">
Q^{n-1}=\left[ {\begin{array}{cc} F_{n} & F_{n-1} \\  F_{n-1} & F_{n-2}     \end{array} } \right]
</script>
</p>
<p>Now, we need to prove that with the above two conditions holding true, the method is valid for finding the <script type="math/tex; mode=display">(n+1)^{th}</script> Fibonacci Number, i.e. <script type="math/tex; mode=display">F_{n+1}=Q^{n}[0,0]</script>.</p>
<p>Proof: <script type="math/tex; mode=display">Q^{n} = \left[ {\begin{array}{cc} F_{n} & F_{n-1} \\  F_{n-1} & F_{n-2}     \end{array} } \right]\left[ {\begin{array}{cc} 1 & 1 \\  1 & 0     \end{array} } \right]</script>.
 <script type="math/tex; mode=display">Q^{n} = \left[ {\begin{array}{cc} F_{n}+F_{n-1} & F_n \\  F_{n-1}+F_{n-2} & F_{n-1}    \end{array} } \right]</script>
<script type="math/tex; mode=display">Q^{n} = \left[ {\begin{array}{cc} F_{n+1} & F_n \\  F_n & F_{n-1}     \end{array} } \right]</script>
</p>
<p>Thus, <script type="math/tex; mode=display">F_{n+1}=Q^{n}[0,0]</script>. This completes the proof of this method.</p>
<p>The only variation we need to do for our problem is that we need to modify the initial terms to 2 and 1 instead of 1 and 0 in the Fibonacci series. Or, another way is to use the same initial <script type="math/tex; mode=display">Q</script> matrix and use <script type="math/tex; mode=display">result = Q^{n}[0,0]</script> to get the final result. This happens because the initial terms we have to use are the 2nd and 3rd terms of the otherwise normal Fibonacci Series.</p>
<p><iframe src="https://leetcode.com/playground/DTs7qYKy/shared" frameborder="0" width="100%" height="500" name="DTs7qYKy"></iframe></p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log n)</script>. Traversing on <script type="math/tex; mode=display">\log n</script> bits.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
<p>Proof of Time Complexity:</p>
<p>Let's say there is a  matrix <script type="math/tex; mode=display">M</script> to be raised to  power <script type="math/tex; mode=display">n</script>. Suppose, <script type="math/tex; mode=display">n</script> is the power of 2. Thus, <script type="math/tex; mode=display">n = 2^i</script>, <script type="math/tex; mode=display">i\in\mathbb{N}</script>, where <script type="math/tex; mode=display">\mathbb{N}</script> represents the set of natural numbers(including 0). We can represent  in the form of a tree:</p>
<p align="center"><img alt="Climbing Stairs" src="../Figures/70_Climbing_Stairs.PNG"></p>
<p>Meaning that: <script type="math/tex; mode=display">M^n = M^{n/2}.M^{n/2} = .... = \prod_{1}^{n} M^{1}</script>
</p>
<p>So, to calculate  <script type="math/tex; mode=display">M^{n}</script> matrix, we should calculate <script type="math/tex; mode=display">M^{n/2}</script>  matrix and multiply it by itself. To calculate <script type="math/tex; mode=display">M^{n/2}</script> we would have to do the same with <script type="math/tex; mode=display">M^{n/4}</script> and so on.</p>
<p>Obviously, the tree height is <script type="math/tex; mode=display">\log_{2} n</script>.</p>
<p>Let’s estimate <script type="math/tex; mode=display">M^{n}</script> calculation time. <script type="math/tex; mode=display">M</script> matrix is of the same size in any power . Therefore, we can perform the multiplication of two matrices in any power in <script type="math/tex; mode=display">O(1)</script>. We should perform <script type="math/tex; mode=display">\log_2 n</script> of such multiplications. So, <script type="math/tex; mode=display">M^{n}</script> calculation complexity is <script type="math/tex; mode=display">O(\log_{2} n)</script>.</p>
<p>In case, the number <script type="math/tex; mode=display">n</script> is not a power of two, we can break it in terms of powers of 2 using its binary representation:</p>
<p>
<script type="math/tex; mode=display">
n= \sum_{p\in P} 2^{p}, \text{where }P\subset\mathbb{N}
</script>
</p>
<p>Thus, we can obtain the final result using:</p>
<p>
<script type="math/tex; mode=display">
M^{n} = \prod_{p\in P} M^{2^{p}}
</script>
</p>
<p>This is the method we've used in our implementation. Again, the complexity remains <script type="math/tex; mode=display">O(\log_{2} n)</script> as we have limited the number of multiplications to <script type="math/tex; mode=display">O(\log_{2} n)</script>.<br><br></p>
<hr>
<h4 id="approach-6-fibonacci-formula">Approach 6: Fibonacci Formula</h4>
<p><strong>Algorithm</strong></p>
<p>We can find <script type="math/tex; mode=display">n^{th}</script> fibonacci number using this formula:</p>
<p>
<script type="math/tex; mode=display">
F_n = 1/\sqrt{5}\left[ \left(\frac{1+\sqrt{5}}{2}\right)^{n} - \left(\frac{1-\sqrt{5}}{2}\right)^{n} \right]
</script>
</p>
<p>For the given problem, the Fibonacci sequence is defined by <script type="math/tex; mode=display">F_0 = 1</script>, <script type="math/tex; mode=display">F_1= 1</script>,  <script type="math/tex; mode=display">F_1= 2</script>, <script type="math/tex; mode=display">F_{n+2}= F_{n+1} + F_n</script>. A standard method of trying to solve such recursion formulas is assume <script type="math/tex; mode=display">F_n</script> of the form <script type="math/tex; mode=display">F_n= a^n</script>. Then, of course, <script type="math/tex; mode=display">F_{n+1} = a^{n+1}</script> and <script type="math/tex; mode=display">F_{n+2}= a^{n+2}</script> so the equation becomes <script type="math/tex; mode=display">a^{n+2}= a^{n+1}+ a^n</script>. If we divide the entire equation by an we arrive at <script type="math/tex; mode=display">a^2= a + 1</script> or the quadratic equation <script type="math/tex; mode=display">a^2 - a- 1= 0</script>.</p>
<p>Solving this by the quadratic formula, we get:</p>
<p>
<script type="math/tex; mode=display">
a=1/\sqrt{5}\left(\left(\frac{1\pm \sqrt{5}}{2}\right)\right)
</script>
</p>
<p>The general solution, thus takes the form:</p>
<p>
<script type="math/tex; mode=display">
F_n = A\left(\frac{1+\sqrt{5}}{2}\right)^{n} + B\left(\frac{1-\sqrt{5}}{2}\right)^{n}
</script>
</p>
<p>For <script type="math/tex; mode=display">n=0</script>, we get <script type="math/tex; mode=display">A + B = 1</script>
</p>
<p>For <script type="math/tex; mode=display">n=1</script>, we get <script type="math/tex; mode=display">A\left(\frac{1+\sqrt{5}}{2}\right) + B\left(\frac{1-\sqrt{5}}{2}\right) = 1</script>
</p>
<p>Solving the above equations, we get:</p>
<p>
<script type="math/tex; mode=display">
A = \left(\frac{1+\sqrt{5}}{2\sqrt{5}}\right), B = \left(\frac{1-\sqrt{5}}{2\sqrt{5}}\right)
</script>
</p>
<p>Putting these values of <script type="math/tex; mode=display">A</script> and <script type="math/tex; mode=display">B</script> in the above general solution equation, we get:</p>
<p>
<script type="math/tex; mode=display">
F_n = 1/\sqrt{5}\left( \left(\frac{1+\sqrt{5}}{2}\right)^{n+1} - \left(\frac{1-\sqrt{5}}{2}\right)^{n+1} \right)
</script>
</p>
<iframe src="https://leetcode.com/playground/nGLhVjXP/shared" frameborder="0" width="100%" height="174" name="nGLhVjXP"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\log n)</script>. <script type="math/tex; mode=display">pow</script> method takes <script type="math/tex; mode=display">\log n</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space is used.</p>
</li>
</ul>
          </div>
        
      </div>
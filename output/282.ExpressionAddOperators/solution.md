<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-backtracking">Approach 1: Backtracking</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-backtracking">Approach 1: Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>Let us first look at what the question asks us to do before getting at the approach to solve it. So, we are given a string of numbers and 3 different operators:</p>
<ul>
<li><code>+</code> Addition,</li>
<li><code>-</code> Subtraction or</li>
<li><code>*</code> Multiplication</li>
</ul>
<p>We have to find all possible combinations of binary operators between the digits so that the overall value of the resulting expression becomes equal to a given target value. Let us look at a few possibilities of what it means exactly to <em>place the operators between digits</em> so that the question becomes clearer.</p>
<p>Let's say we are given the following set of digits <code>"123456789"</code> and the target value given to us is <code>45</code>. Let us see some of the possible resulting expressions that we can get by placing the operators in different locations.</p>
<pre>
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
1 + 2 - 3 + 4 - 5 + 6 - 7 + 8 - 9 = -3
1 + 2 * 3 - 4 + 5 + 6 - 7 * 8 - 9 = -51
1 + 2 + 3 + 4 + 5 - 6 * 7 + 8 * 9 = 45
</pre>

<p>These are just 4 of the many resulting expressions that are possible by using the given string of digits and the three operators.</p>
<p>By looking at the above examples we can't really figure out any specific pattern among the resulting expressions that tells us which of them will give us the resulting target.</p>
<p>Since the question explicitly states that we are given binary operators, this means that each of the operator would require two operands.</p>
<blockquote>
<p>We can consider each of our digits as an operand.</p>
</blockquote>
<p>This means that between every pair of digits we can have any of the three operators i.e. <script type="math/tex; mode=display">+</script>, <script type="math/tex; mode=display">-</script> or <script type="math/tex; mode=display">\times</script>.</p>
<p>If you've looked at the question's statement and the examples that are given in the question, you would realize that there is an example where the digits are <code>"105"</code> and the target value is <code>5</code>. For this particular example, there are two expressions given to us and they are <code>1*0+5</code> and <code>10-5</code>.</p>
<p>The second expression is something that you need to look out for before getting to solve this question because this complicates things a bit.</p>
<p>It would have been an easier question to solve if we just had to consider those expressions that simply had <em>digits as operands</em>.</p>
<p>But, in this question, we can have all sorts of digits getting together and forming a bigger number that becomes a part of the expression. Let us look at some example expressions for the digits <code>"123456"</code> and target <code>30</code>.</p>
<pre>
1 * 23 - 4 + 5 + 6 = 30
12 - 3 * 4 + 5 * 6 = 30
1 - 23 - 4 + 56 = 30
</pre>

<p>So this means that although the number of operators are defined for us i.e. 3 different binary operators, but the number of operands are <strong>not really well defined for us</strong>.</p>
<p>This is a big portion of the original problem that we need to address in our solution.</p>
<p>Since we are asked to find out all of the valid expressions whose value equals the given target and we don't really know what specific operator between two operands would eventually give us a valid expression,</p>
<blockquote>
<p>We try out all of the options.</p>
</blockquote>
<p>This means once we have defined what the operands are for our given expression, we would have three possible choices of operators between each consecutive pair of operands.</p>
<p>From an implementation perspective, what would an operand imply with respect to our original string?</p>
<blockquote>
<p>An operand would be an integer formed from a substring of our original string.</p>
</blockquote>
<p>Let's look at two different array partitions for the given string <code>"123456789"</code></p>
<p></p><center>
<img src="../Figures/282/282_Expression_Add_Operators_Diag_1.png" height="300"></center>
<p>Since we are required to return all of the valid expressions that evaluate to a given target value, we have to try all possible partitions of the given array thereby considering all of the possible operands that can be formed from the digits.</p>
<p>There is a very simple way of incorporating this into our algorithm. Right now, at every point in the algorithm, we have three different choices corresponding to the three different operators.</p>
<blockquote>
<p>The way we incorporate these partitions is by considering a 4th operator as well which simply moves one step forward and extends the current operand by one digit. Essentially, going from 12 --&gt; 123 is a NO OP operand in our implementation. (12 * 10) + 3.</p>
</blockquote>
<p>Now we have 4 different recursion paths in our algorithm and we have to try out all of them to see which ones lead to a potential solution.</p>
<p>This <code>try out everything</code> hints at a backtracking solution and that is exactly what we are going to look at here.</p>
<p><strong>Algorithm</strong></p>
<p>Let's quickly look at the steps involved in our backtracking algorithm before looking at the pseudo-code.</p>
<ol>
<li>As discussed above, we have multiple choices of what operators to use and what the operands can be and hence, we have to look at all the possibilities to find <strong><em>all</em></strong> valid expressions.</li>
<li>Our recursive call will have an <code>index</code> which represents the current digit we're looking at in the original <code>nums</code> string and also the expression string built till now.</li>
<li>At every step, we have exactly 4 different recursive calls. The <code>NO OP</code> call simply extends the <code>current_operand</code> by the current digit and moves ahead. Rest of the recursive calls correspond to <code>+</code>, <code>-</code>, and <code>*</code>.</li>
<li>We keep on building our expression like this and eventually, the entire <code>nums</code> string would be processed. At that time we check if the expression we built till now is a valid expression or not and we record it if it is a valid one.</li>
</ol>
<pre>
1. procedure recurse(digits, index, expression):
2.     if we have reached the end of the string:
3.         if the expression evaluates to the target:
4.             Valid Expression found!
5.     else:
6.         try out operator 'NO OP' and recurse
7.         try out operator * and recurse
8.         try out operator + and recurse
9.         try out operator - and recurse
</pre>

<p>The algorithm now looks pretty straightforward. However, the implementation is something that needs more thought and there are some things that we need to address before actually looking at the implementation.</p>
<p>When we are done building an expression out of all of the digits in our original string i.e. the base case, then we check if the expression is a valid expression or not. Right ?</p>
<blockquote>
<p>How do we actually check if an expression is a valid one or not if all we have is a string representing the expression and not the integer value for the same?</p>
</blockquote>
<p>Well, one way to go about this is to write a custom <code>eval</code> function that takes in a string and returns the value of that expression. If you do that (Python people can use the inbuilt function <code>eval</code> for this), you will get a TLE i.e. time limit exceeded error.</p>
<p><br></p>
<p><strong>Can't we keep track of the expression's value on the fly?</strong></p>
<p>Well yes. That's the idea we will go with. Instead of just keeping track of what the expression string is, we will also keep track of it's value along the way so that when the recursion hits the base case, we can check in <script type="math/tex; mode=display">O(1)</script> time if the expression's value equals the target value or not.</p>
<p>The implementation would have been straightforward had it just been <code>+</code> and <code>-</code> operators involved. This is because both these operators have an equal precedence. That means that we can continue to evaluate the expression on the fly without any problems. Have a look at the following example.</p>
<p></p><center>
<img src="../Figures/282/282_Expression_Add_Operators_Diag_2.png" width="550"></center>
<p>So far so good. Now let us add the <code>*</code> operator as well and see how building the expression on the fly like this breaks.</p>
<p></p><center>
<img src="../Figures/282/282_Expression_Add_Operators_Diag_3.png" width="550"></center>
<p>What we mean by building the expression on the fly is that we keep track of the expression's value till now and we simply consider that value as one of the two operands for our operators. As we can see from the two examples above, this would have worked had it just been <code>+</code> and <code>-</code> operators.</p>
<p>But, this approach is bound to fail because the <code>*</code> operator takes precedence over <code>+</code> and <code>-</code>. The <code>*</code> operator would require the <strong><em>actual</em></strong> previous operand in our expression rather than the current value of the expression. i.e. In the above example, the <code>*</code> operator needed <code>2</code> rather than <code>12</code> to get us the correct value of <code>18</code>.</p>
<p><br></p>
<p><strong>How to handle this?</strong></p>
<p>The idea on how to handle this problem springs from the discussion above. We simply need to keep track of the last operand in our expression and how it modified the expression's value overall so that when we consider the <code>*</code> operator, we can <strong>reverse</strong> the effects of the previous operand and consider it for multiplication. Let's take a look at the example that was breaking before.</p>
<p></p><center>
<img src="../Figures/282/282_Expression_Add_Operators_Diag_4.png" width="550"></center>
<p>Now we can look at the actual implementation of this algorithm.</p>
<iframe src="https://leetcode.com/playground/BFyUVxwz/shared" frameborder="0" width="100%" height="500" name="BFyUVxwz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:</p>
<ul>
<li>At every step along the way, we consider exactly 4 different choices or 4 different recursive paths. The base case is when the value of <code>index</code> reaches <script type="math/tex; mode=display">N</script> i.e. the length of the <code>nums</code> array. Hence, our complexity would be <script type="math/tex; mode=display">O(4^N)</script>.</li>
<li>For the base case we use a <code>StringBuilder::toString</code> operation in Java and <code>.join()</code> operation in Python and that takes <script type="math/tex; mode=display">O(N)</script> time. Here <script type="math/tex; mode=display">N</script> represents the length of our expression. In the worst case, each digit would be an operand and we would have <script type="math/tex; mode=display">N</script> digits and <script type="math/tex; mode=display">N - 1</script> operators. So <script type="math/tex; mode=display">O(N)</script>. This is for one expression. In the worst case, we can have <script type="math/tex; mode=display">O(4^N)</script> valid expressions.</li>
<li>Overall time complexity = <script type="math/tex; mode=display">O(N \times 4^N)</script>.</li>
</ul>
</li>
<li>
<p>Space Complexity:</p>
<ul>
<li>For both Python and Java implementations we have a list data structure that we update on the fly and only for valid expressions do we create a new string and add to our <code>answers</code> array. So, the space occupied by the intermediate list would be <script type="math/tex; mode=display">O(N)</script> since in the worst case the expression would be built out of all the digits as operands.</li>
<li>Additionally, the space used up by the recursion stack would also be <script type="math/tex; mode=display">O(N)</script> since the size of recursion stack is determined by the value of <code>index</code> and it goes from <script type="math/tex; mode=display">0</script> all the way to <script type="math/tex; mode=display">N</script>.</li>
<li>We don't consider the space occupied by the <code>answers</code> array since that is a part of the question's requirement and we can't reduce that in any way</li>
</ul>
</li>
</ul>
<p><strong>EDIT:</strong>
The previous implementation of the algorithm, although correct, lead me to write an incorrect complexity analysis section. I've re-written the algorithm from scratch and corrected the complexity analysis as well. Sorry for the inconvenience to all the readers. The core idea of the algorithm is still the same. That hasn't changed.</p>
<p>Special thanks to <a href="https://leetcode.com/ufarooqi/">@ufarooqi</a>, <a href="https://leetcode.com/vortexwolf">@vortexwolf</a> for providing correct complexity analysis in the discussion forum leading to corrections in the article. Pardon me if I've missed out on any other names :)</p>
<p><br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>
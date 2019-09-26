<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-stack-and-string-reversal">Approach 1: Stack and String Reversal</a></li>
<li><a href="#approach-2-stack-and-no-string-reversal">Approach 2: Stack and No String Reversal</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>This problem is all about understanding the following:</p>
<ul>
<li>Input always contains valid strings</li>
<li>The rules of addition and subtraction</li>
<li>Implication of precedence by parenthesis</li>
<li>Spaces do not affect the evaluation of the input expression</li>
</ul>
<p></p><center>
<img src="../Figures/224/Basic_Calculator_0.png" width="600">
</center>
<h4 id="approach-1-stack-and-string-reversal">Approach 1: Stack and String Reversal</h4>
<p><strong>Intuition</strong></p>
<p>This question qualifies really well for a stack question. Since the expression might have parenthesis, we can use a stack to find the value for each sub-expression within a parenthesis. Essentially, we need to <em>delay</em> processing the main expression until we are done evaluating the interim sub-expressions within parenthesis and to introduce this delay, we use a stack.</p>
<p>We push the elements of the expression one by one onto the stack until we get a closing bracket <code>)</code>. Then we pop the elements from the stack one by one and evaluate the expression on-the-go. This is done till we find the corresponding <code>(</code> opening bracket. This kind of evaluation is very common when using the stack data structure. However, if you notice the way we calculate the final answer, you will realize that we actually process the values from right to left whereas it should be the other way around.</p>
<p></p><center>
<img src="../Figures/224/Basic_Calculator_1.png" width="600">
</center>
<p>From the above example we realize that following the simple stack push and pop methodology will not help us here. We need to understand how <code>+</code> and <code>-</code> work. <code>+</code> follows the associative property. For the expression <script type="math/tex; mode=display">A+B+C</script>,  we have <script type="math/tex; mode=display">(A+B)+C = A+(B+C)</script>. However,  <code>-</code> does not follow this rule which is the root cause of all the problems in this approach.</p>
<p>If we use a stack and read the elements of the expression from left to right, we end up evaluating the expression from right-to-left. This means we are expecting <script type="math/tex; mode=display">(A-B)-C</script> to be equal to <script type="math/tex; mode=display">(C-B)-A</script> which is not correct. Subtraction is neither associative nor commutative.</p>
<p>This problem could be solved very easily by reversing the string and then using basic drill using a stack. Reversing a string helps since we now put the elements of the expression into the stack from right to left and evaluation for the expression is done correctly from left to right.</p>
<p></p><center>
<img src="../Figures/224/Basic_Calculator_2.png" width="600">
</center>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate the expression string in reverse order one character at a time. Since we are reading the expression character by character, we need to be careful when we are reading digits and non-digits.</li>
<li>The operands could be formed by multiple characters. A string "123" would mean a numeric 123, which could be formed as: <code>123</code> &gt;&gt; <code>120 + 3</code> &gt;&gt; <code>100 + 20 + 3</code>. Thus, if the character read is a digit we need to form the operand by multiplying a power of <code>10</code> to the current digit and adding it to the overall operand. We do this since we are processing the string in the reverse order.</li>
<li>The operands could be formed by multiple characters. We need to keep track of an on-going operand. This part is a bit tricky since in this case the string is reversed. Once we encounter a character which is not a digit, we push the operand onto the stack.</li>
<li>
<p>When we encounter an opening parenthesis <code>(</code>, this means an expression just ended. Recall we have reversed the expression. So an opening bracket would signify the end of the an expression. This calls for evaluation of the expression by popping operands and operators off the stack till we pop corresponding closing parenthesis. The final result of the expression is pushed back onto the stack.</p>
<blockquote>
<p>Note: We are evaluating all the sub-expressions within the main expression. The sub-expressions on the right get evaluated first but the main expression itself is evaluated from left to right when all its components are resolved, which is very important for correct results.</p>
</blockquote>
<p>For eg. For expression <script type="math/tex; mode=display">A - (B+C) + (D+E-F)</script>, <script type="math/tex; mode=display">D+E-F</script> is evaluated before <script type="math/tex; mode=display">B+C</script>. While evaluating <script type="math/tex; mode=display">D+E-F</script> the order is from left to right. Similarly for the parent expression, all the child components are evaluated and stored on the stack so that final evaluation is left to right.</p>
</li>
<li>
<p>Push the other non-digits onto to the stack.</p>
</li>
<li>
<p>Do this until we get the final result. It's possible that we don't have any more characters left to process but the stack is still non-empty. This would happen when the main expression is not enclosed by parenthesis. So, once we are done evaluating the entire expression, we check if the stack is non-empty. If it is, we treat the elements in it as one final expression and evaluate it the same way we would if we had encountered an opening bracket.</p>
<p>We can also cover the original expression with a set of parenthesis to avoid this extra call.</p>
</li>
</ol>
<iframe src="https://leetcode.com/playground/QJQ2NUUT/shared" frameborder="0" width="100%" height="500" name="QJQ2NUUT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where N is the length of the string.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, where N is the length of the string.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-stack-and-no-string-reversal">Approach 2: Stack and No String Reversal</h4>
<p><strong>Intuition</strong></p>
<p>A very easy way to solve the problem of associativity for <code>-</code> we tackled in the previous approach, is to use <code>-</code> operator as the magnitude for the operand to the right of the operator. Once we start using <code>-</code> as a magnitude for the operands, we just have one operator left which is addition and <code>+</code> is associative.</p>
<p>for e.g. <script type="math/tex; mode=display">A - B - C</script> could be re-written as <script type="math/tex; mode=display">A + (-B) + (-C)</script>.</p>
<blockquote>
<p>The re-written expression would follow associativity rule. Thus evaluating the expression from right or left, won't change the result.</p>
</blockquote>
<p>What we need to keep in mind is that the expressions given would be complicated, i.e. there would be expressions nested within other expressions. Even if we have something like <code>(A - (B - C))</code> we need to associate the <code>negative sign</code> outside of <code>B-C</code> with the result of <code>B-C</code> instead of just with <code>B</code>.</p>
<p>We can solve this problem by following the basic drill before and associating the sign with the expression to the right of it. However, the approach that we will instead take has a small twist to it in that we will be evaluating most of the expression on-the-go. This reduces the number of push and pop operations.</p>
<p></p><center>
<img src="../Figures/224/Basic_Calculator_3.png" width="600">
</center>
<p>Follow the below steps closely. This algorithm is inspired from <a href="https://leetcode.com/problems/basic-calculator/discuss/62361/southpenguin">discussion post</a> by <a href="https://leetcode.com/southpenguin/">southpenguin</a>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate the expression string one character at a time. Since we are reading the expression character by character, we need to be careful when we are reading digits and non-digits.</li>
<li>The operands could be formed by multiple characters. A string "123" would mean a numeric 123, which could be formed as: <code>123</code> &gt;&gt; <code>120 + 3</code> &gt;&gt; <code>100 + 20 + 3</code>. Thus, if the character read is a digit we need to form the operand by multiplying <code>10</code> to the previously formed continuing operand and adding the digit to it.</li>
<li>Whenever we encounter an operator such as <code>+</code> or <code>-</code> we first evaluate the expression to the left and then save this <code>sign</code> for the next evaluation.
    <center>
    <img src="../Figures/224/Basic_Calculator_4.png" width="600">
    </center></li>
<li>If the character is an opening parenthesis <code>(</code>, we just push the result calculated so far and the <code>sign</code> on to the stack (the sign and the magnitude) and start a fresh as if we are calculating a new expression.</li>
<li>If the character is a closing parenthesis <code>)</code>, we first calculate the expression to the left. The result from this would be the result of the expression within the set of parenthesis that just concluded. This result is then multiplied with the sign, if there is any on top of the stack.
Remember we saved the <code>sign</code> on top of the stack when we had encountered an open parenthesis? This sign is associated with the parenthesis that started then, thus when the expression ends or concludes, we pop the <code>sign</code> and multiply it with result of the expression. It is then just added to the next element on top of the stack.</li>
</ol>
<iframe src="https://leetcode.com/playground/phpuMfKr/shared" frameborder="0" width="100%" height="500" name="phpuMfKr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N)</script>, where N is the length of the string. The difference in time complexity between this approach and the previous one is that every character in this approach will get processed exactly once. However, in the previous approach, each character can potentially get processed twice, once when it's pushed onto the stack and once when it's popped for processing of the final result (or a subexpression). That's why this approach is faster.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, where N is the length of the string.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>
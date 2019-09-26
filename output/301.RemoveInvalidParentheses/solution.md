<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-backtracking">Approach 1: Backtracking</a></li>
<li><a href="#approach-2-limited-backtracking">Approach 2: Limited Backtracking!</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-backtracking">Approach 1: Backtracking</h4>
<p><strong>Intuition</strong></p>
<p>For this question, we are given an expression consisting of parentheses and there can be some misplaced or extra brackets in the expression that cause it to be invalid. An expression consisting of parentheses is considered valid only when every closing bracket has a corresponding opening bracket and vice versa.</p>
<p>This means if we start looking at each of the bracket from left to right, as soon as we encounter a closing bracket, there should be an unmatched opening bracket available to match it. Otherwise the expression would become invalid. The expression can also become invalid if the number of opening parentheses i.e. <code>(</code> are more than the number of closing parentheses i.e. <code>)</code>.</p>
<p>Let us look at an invalid expression and all the possible valid expressions that can be formed from it by removing some of the brackets. There is no restriction on which parentheses we can remove. We simply have to make the expression valid.</p>
<blockquote>
<p>The only condition is that we should be removing the minimum number of brackets to make an invalid expression, valid. If this condition was not present, we could potentially remove most of the brackets and come down to say 2 brackets in the end which form <code>()</code> and that would be a valid expression.</p>
</blockquote>
<p></p><center>
<img src="../Figures/301/Diag_1.png" width="800"></center>
<p>An important thing to observe in the above diagram is that there are multiple ways of reaching the same solution i.e. say the optimal number of parentheses to be removed to make the original expression valid is K. We can remove multiple different sets of K brackets that will eventually give us the same final expression. But, each valid expression should be recorded only once. We have to take care of this in our solution. Note that there are other possible ways of reaching one of the two valid expressions shown above. We have simply shown 3 ways each for the two valid expressions.</p>
<p>Coming back to our problem, the question that now arises is, how to decide which of the parentheses to remove?</p>
<blockquote>
<p>Since we don't know which of the brackets can possibly be removed, we try out all the options!</p>
</blockquote>
<p>For every bracket we have two choices:</p>
<ul>
<li>Either it can be considered a part of the final expression OR</li>
<li>It can be ignored i.e. we can delete it from our final expression.</li>
</ul>
<p>Such kind of problems where we have multiple options and we have no strategy or metric of deciding greedily which option to take, we try out all of the options and see which ones lead to an answer. These type of problems are perfect candidates for the programming paradigm, <code>Recursion</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize an array that will store all of our valid expressions finally.</li>
<li>Start with the leftmost bracket in the given sequence and proceed right in the recursion.</li>
<li>The state of recursion is defined by the index which we are currently processing in the original expression. Let this index be represented by the character <code>i</code>. Also, we have two different variables <code>left_count</code> and <code>right_count</code> that represent the number of left and right parentheses we have added to our expression till now. These are the parentheses that were considered.</li>
<li>If the current character i.e. <code>S[i]</code> (considering S is the expression string) is neither a closing or an opening parenthesis, then we simply add this character to our final solution string for the current recursion.</li>
<li>However, if the current character is either of the two brackets i.e. <code>S[i] == '(' or S[i] == ')'</code>, then we have two options. We can either discard this character by marking it an invalid character or we can consider this bracket to be a part of the final expression.</li>
<li>When all of the parentheses in the original expression have been processed, we simply check if the expression represented by <code>expr</code> i.e. the expression formed till now is valid one or not. The way we check if the final expression is valid or not is by looking at the values in <code>left_count</code> and <code>right_count</code>. For an expression to be valid <code>left_count == right_count</code>. If it is indeed valid, then it could be one of our possible solutions.<ul>
<li>Even though we have a valid expression, we also need to keep track of the number of removals we did to get this expression. This is done by another variable passed in recursion called <code>rem_count</code>.</li>
<li>Once recursion finishes we check if the current value of <code>rem_count</code> is &lt; the least number of steps we took to form a valid expression till now i.e. the global minima. If this is not the case, we don't record the new expression, else we record it.</li>
</ul>
</li>
</ol>
<p>One small optimization that we can do from an implementation perspective is introducing some sort of pruning in our algorithm. Right now we simply go till the very end i.e. process all of the parentheses and when we are done processing all of them, we check if the expression we have can be considered or not.</p>
<p>We have to wait till the very end to decide if the expression formed in recursion is a valid expression or not. Is there a way for us to cutoff from some of the recursion paths early on because they wouldn't lead to a solution? The answer to this is Yes! The optimization is based on the following idea.</p>
<p>For a left bracket encountered during recursion, if we decide to consider it, then it may or may not lead to an invalid final expression. It may lead to an invalid expression eventually if there are no matching closing bracket available afterwards. But, we don't know for sure if this will happen or not.</p>
<blockquote>
<p>However, for a closing bracket, if we decide to keep it as a part of our final expression (remember for every bracket we have two options, either to keep it or to remove it and recurse further) and there is no corresponding opening bracket to match it in the expression till now, then it will definitely lead to an invalid expression no matter what we do afterwards.</p>
</blockquote>
<p>e.g.</p>
<pre>
( (  ) ) )
</pre>

<p>In this case the third closing bracket will make the expression invalid. No matter what comes afterwards, this will give us an invalid expression and if such a thing happens, we shouldn't recurse further and simply prune the recursion tree.</p>
<p>That is why, in addition to having the index in the original string/expression which we are currently processing and the expression string formed till now, we also keep track of the number of left and right parentheses. Whenever we keep a left parenthesis in the expression, we increment its counter. For a right parenthesis, we check if <code>right_count &lt; left_count</code>. If this is the case then only we consider that right parenthesis and recurse further. Otherwise we don't as we know it will make the expression invalid. This simple optimization saves a lot of runtime.</p>
<p>Now, let us look at the implementation for this algorithm.</p>
<iframe src="https://leetcode.com/playground/CqP9Vt73/shared" frameborder="0" width="100%" height="500" name="CqP9Vt73"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time Complexity : <script type="math/tex; mode=display">O(2^N)</script> since in the worst case we will have only left parentheses in the expression and for every bracket we will have two options i.e. whether to remove it or consider it. Considering that the expression has <script type="math/tex; mode=display">N</script> parentheses, the time complexity will be <script type="math/tex; mode=display">O(2^N)</script>.</li>
<li>Space Complexity : <script type="math/tex; mode=display">O(N)</script> because we are resorting to a recursive solution and for a recursive solution there is always stack space used as internal function states are saved onto a stack during recursion. The maximum depth of recursion decides the stack space used. Since we process one character at a time and the base case for the recursion is when we have processed all of the characters of the expression string, the size of the stack would be <script type="math/tex; mode=display">O(N)</script>. Note that we are not considering the space required to store the valid expressions. We only count the intermediate space here.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-limited-backtracking">Approach 2: Limited Backtracking!</h4>
<p>Although the previous solution does get accepted on the platform, it is a very inefficient solution because we try removing each and every possible parentheses from the expression and in the end we check two things:</p>
<ol>
<li>if the expression is valid or not</li>
<li>if the total number of removed parentheses removed in the current recursion is less than the global minimum till now or not.</li>
</ol>
<p>We cannot determine which of the parentheses are misplaced because, as the problem statement puts across, we can remove multiple combinations of parentheses and end up with a valid expression. This means there can be multiple valid expressions from a single invalid expression and we have to find all of them.</p>
<blockquote>
<p>The one thing all these valid expressions have in common is that they will all be of the same length i.e. as compared to the original expression, all of these expressions will have the same number of characters removed.</p>
</blockquote>
<p>What if we could determine this count?</p>
<p>What if in addition to determining this count of characters to be removed, we could also determine the number of left parentheses and number of right parentheses to be removed from the original expression to get <strong>any</strong> valid expression?</p>
<p>This would cut down the computations immensely and the runtime would plummet as a result. The reason for this is, if we knew how many left and right parentheses are to be removed from the original expression to get a valid expression, we would cut down on so many unwanted recursive calls.</p>
<p>Imagine the original expression to be 1000 characters with only 3 misplaced <code>(</code> parentheses and 2 misplaced <code>)</code> parentheses. In our previous solution we would end up trying to remove each one of left and right parentheses and try to reach a valid expression in the end whereas we should only be trying out removing 3 <code>(</code> brackets and 2 <code>)</code> brackets.</p>
<blockquote>
<p>This is the exact number of <code>(</code> and <code>)</code> that have to be removed to get a valid expression. No more, no less.</p>
</blockquote>
<p>Let us look at how we can find out the number of misplaced left and right parentheses in a given expression first and then we will slightly modify our original algorithm to incorporate these counts as well.</p>
<ol>
<li>We process the expression one bracket at a time starting from the left.</li>
<li>Suppose we encounter an opening bracket i.e. <code>(</code>, it may or may not lead to an invalid expression because there can be a matching ending bracket somewhere in the remaining part of the expression. Here, we simply increment the counter keeping track of left parentheses till now. <code>left += 1</code></li>
<li>If we encounter a closing bracket, this has two meanings:<ul>
<li>Either there was no matching opening bracket for this closing bracket and in that case we have an invalid expression. This is the case when <code>left == 0</code> i.e. when there are no unmatched left brackets available. In such a case we increment another counter say <code>right += 1</code> to represent misplaced right parentheses.</li>
<li>Or, we had some unmatched opening bracket available to match this closing bracket. This is the case when <code>left &gt; 0</code>. In this case we simply decrement the left counter we had i.e. <code>left -= 1</code></li>
</ul>
</li>
<li>Continue processing the string until all parentheses have been processed.</li>
<li>In the end the values of <code>left</code> and <code>right</code> would tell us the number of unmatched <code>(</code> and <code>)</code> parentheses respectively.</li>
</ol>
<p>Now that we have these two values available that tell us the total number of left i.e. <code>(</code> and right i.e. <code>)</code> parentheses that have to be removed to make the invalid expression valid, we will modify our original algorithm discussed in the previous session to avoid unwanted recursions.</p>
<p><strong>Algorithm</strong></p>
<p>The overall algorithm remains exactly the same as before. The changes that we will incorporate are listed below:</p>
<ul>
<li>The state of the recursion is now defined by five different variables:<ol>
<li><code>index</code> which represents the current character that we have to process in the original string.</li>
<li><code>left_count</code> which represents the number of left parentheses that have been added to the expression we are building.</li>
<li><code>right_count</code> which represents the number of right parentheses that have been added to the expression we are building.</li>
<li><code>left_rem</code> is the number of left parentheses that remain to be removed.</li>
<li><code>right_rem</code> represents the number of right parentheses that remain to be removed. Overall, for the final expression to be valid, <code>left_rem == 0</code> and <code>right_rem == 0</code>.</li>
</ol>
</li>
<li>When we decide to not consider a parenthesis i.e. delete a parenthesis, be it a left or a right parentheses, we have to consider their corresponding remaining counts as well. This means that we can only discard a left parentheses if <code>left_rem &gt; 0</code> and similarly for the right one we will check for <code>right_rem &gt; 0</code>.</li>
<li>There are no changes to checks for <strong>considering</strong> a parenthesis. Only the conditions change for <strong>discarding</strong> a parenthesis.</li>
<li>Condition for an expression being valid in the base case would now become <code>left_rem == 0 and right_rem == 0</code>. Note that we don't have to check if <code>left_count == right_count</code> anymore because in the case of a valid expression, we would have removed all the misplaced or invalid parenthesis by the time the recursion ends. So, the only check we need if <code>left_rem == 0 and right_rem == 0</code>.</li>
</ul>
<blockquote>
<p>The most important thing here is that we have completely gotten rid of checking if the number of parentheses removed is lesser than the current minimum or not. The reason for this is we always remove the same number of parentheses as defined by <code>left_rem + right_rem</code> at the start of recursion.</p>
</blockquote>
<p>Now let us look at the implementation for this modified version of algorithm.</p>
<iframe src="https://leetcode.com/playground/YQCnqBTg/shared" frameborder="0" width="100%" height="500" name="YQCnqBTg"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time Complexity : The optimization that we have performed is simply a better form of pruning. Pruning here is something that will vary from one test case to another. In the worst case, we can have something like <code>(((((((((</code> and the <code>left_rem = len(S)</code> and in such a case we can discard all of the characters because all are misplaced. So, in the worst case we <strong>still</strong> have 2 options per parenthesis and that gives us a complexity of <script type="math/tex; mode=display">O(2^N)</script>.</li>
<li>Space Complexity : The space complexity remains the same i.e. <script type="math/tex; mode=display">O(N)</script> as previous solution. We have to go to a maximum recursion depth of <script type="math/tex; mode=display">N</script> before hitting the base case. Note that we are not considering the space required to store the valid expressions. We only count the intermediate space here.</li>
</ul>
<p><br>
<br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>
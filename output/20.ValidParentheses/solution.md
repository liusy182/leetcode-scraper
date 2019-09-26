<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-stacks">Approach 1: Stacks</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<p><br></p>
<p><strong>Intuition</strong></p>
<p>Imagine you are writing a small compiler for your college project and one of the tasks (or say sub-tasks) for the compiler would be to detect if the parenthesis are in place or not.</p>
<p>The algorithm we will look at in this article can be then used to process all the parenthesis in the program your compiler is compiling and checking if all the parenthesis are in place. This makes checking if a given string of parenthesis is valid or not, an important programming problem.</p>
<p>The expressions that we will deal with in this problem can consist of three different type of parenthesis:</p>
<ul>
<li><code>()</code>,</li>
<li><code>{}</code> and</li>
<li><code>[]</code></li>
</ul>
<p>Before looking at how we can check if a given expression consisting of these parenthesis is valid or not, let us look at a simpler version of the problem that consists of just one type of parenthesis. So, the expressions we can encounter in this simplified version of the problem are e.g.</p>
<pre>
(((((()))))) -- VALID

()()()()     -- VALID

(((((((()    -- INVALID

((()(())))   -- VALID
</pre>

<p>Let's look at a simple algorithm to deal with this problem.</p>
<ol>
<li>We process the expression one bracket at a time starting from the left.</li>
<li>Suppose we encounter an opening bracket i.e. <code>(</code>, it may or may not be an invalid expression because there can be a matching ending bracket somewhere in the remaining part of the expression. Here, we simply increment the counter keeping track of left parenthesis till now. <code>left += 1</code></li>
<li>
<p>If we encounter a closing bracket, this has two meanings:</p>
<ol>
<li>One, there was no matching opening bracket for this closing bracket and in that case we have an invalid expression. This is the case when <code>left == 0</code> i.e. when there are no unmatched left brackets available.</li>
<li>We had <code>some unmatched</code> opening bracket available to match this closing bracket. This is the case when <code>left &gt; 0</code> i.e. we have unmatched left brackets available.</li>
</ol>
</li>
<li>
<p>If we encounter a closing bracket i.e. <code>)</code> when <code>left == 0</code>, then we have an invalid expression on our hands. Else, we decrement <code>left</code> thus reducing the number of unmatched left parenthesis available.</p>
</li>
<li>Continue processing the string until all parenthesis have been processed.</li>
<li>If in the end we still have unmatched left parenthesis available, this implies an invalid expression.</li>
</ol>
<p>The reason we discussed this particular algorithm here is because the approach for the original problem derives its inspiration from this very solution. Have a look at the following dry run of the algorithm we discussed to have a better understanding.</p>
<p>!?!../Documents/20_Simple.json:1000,400!?!</p>
<p>If we try and follow the same approach for our original problem, then it simply won't work. The reason a simple counter based approach works above is because all the parenthesis are of the same type. So when we encounter a closing bracket, we simply assume a corresponding opening matching bracket to be available i.e. if <code>left &gt; 0</code>.</p>
<p>But, in our problem, if we encounter say <code>]</code>, we don't really know if there is a corresponding opening <code>[</code> available or not. You could say:</p>
<blockquote>
<p>Why not maintain a separate counter for the different types of parenthesis?</p>
</blockquote>
<p>This doesn't work because the relative placement of the parenthesis also matters here. e.g.:</p>
<pre>
[{]
</pre>

<p>If we simply keep counters here, then as soon as we encounter the closing square bracket, we would know there is an unmatched opening square bracket available as well. But, the <strong>closest unmatched opening bracket available is a curly bracket and not a square bracket</strong> and hence the counting approach breaks here.
<br>
<br></p>
<hr>
<h4 id="approach-1-stacks">Approach 1: Stacks</h4>
<p>An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression. (Not every sub-expression) e.g.</p>
<p></p><center>
<img src="../Figures/20/20-Valid-Parentheses-Recursive-Property.png" width="700"></center>
<p>Also, if you look at the above structure carefully, the color coded cells mark the opening and closing pairs of parenthesis. The entire expression is valid, but sub portions of it are also valid in themselves. This lends a sort of a recursive structure to the problem. For e.g. Consider the expression enclosed within the two green parenthesis in the diagram above. The opening bracket at index <code>1</code> and the corresponding closing bracket at index <code>6</code>.</p>
<blockquote>
<p>What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression?</p>
</blockquote>
<p>Let's have a look at this idea below where remove the smaller expressions one at a time from the overall expression and since this is a valid expression, we would be left with an empty string in the end.</p>
<p>!?!../Documents/20_Recursive.json:1000,400!?!</p>
<blockquote>
<p>The stack data structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an idea about the overall structure. But, the stack can help us process this recursively i.e. from outside to inwards.</p>
</blockquote>
<p>Let us have a look at the algorithm for this problem using stacks as the intermediate data structure.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize a stack S.</li>
<li>Process each bracket of the expression one at a time.</li>
<li>If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later, let us simply move onto the <strong>sub-expression</strong> ahead.</li>
<li>If we encounter a closing bracket, then we check the element on top of the stack. If the element at the top of the stack is an opening bracket <code>of the same type</code>, then we pop it off the stack and continue processing. Else, this implies an invalid expression.</li>
<li>In the end, if we are left with a stack still having elements, then this implies an invalid expression.</li>
</ol>
<p>We'll have a look a dry run for the algorithm and then move onto the implementation.</p>
<p>!?!../Documents/20_Stack.json:1000,560!?!</p>
<p>Let us now have a look at the implementation for this algorithm.</p>
<iframe src="https://leetcode.com/playground/UfER2d7C/shared" frameborder="0" width="100%" height="500" name="UfER2d7C"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity : <script type="math/tex; mode=display">O(n)</script> because we simply traverse the given string one character at a time and push and pop operations on a stack take <script type="math/tex; mode=display">O(1)</script> time.</li>
<li>Space complexity : <script type="math/tex; mode=display">O(n)</script> as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. <code>((((((((((</code>.</li>
</ul>
<p><br>
<br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>
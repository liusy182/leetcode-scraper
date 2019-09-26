<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-recursive-parsing-accepted">Approach #1: Recursive Parsing [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-recursive-parsing-accepted">Approach #1: Recursive Parsing [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>This question is relatively straightforward in terms of the idea of the solution, but presents substantial difficulties in the implementation.</p>
<p>Expressions may involve the evaluation of other expressions, which motivates a recursive approach.</p>
<p>One difficulty is managing the correct scope of the variables.  We can use a stack of hashmaps.  As we enter an inner scope defined by parentheses, we need to add that scope to our stack, and when we exit, we need to pop that scope off.</p>
<p>Our main <code>evaluate</code> function will go through each case of what form the <code>expression</code> could take.</p>
<ul>
<li>
<p>If the expression starts with a digit or '-', it's an integer: return it.</p>
</li>
<li>
<p>If the expression starts with a letter, it's a variable.  Recall it by checking the current scope in reverse order.</p>
</li>
<li>
<p>Otherwise, group the tokens (variables or expressions) within this expression by counting the "balance" <code>bal</code> of the occurrences of <code>'('</code> minus the number of occurrences of <code>')'</code>.  When the balance is zero, we have ended a token.  For example, <code>(add 1 (add 2 3))</code> should have tokens <code>'1'</code> and <code>'(add 2 3)'</code>.</p>
</li>
<li>
<p>For add and mult expressions, evaluate each token and return the addition or multiplication of them.</p>
</li>
<li>
<p>For let expressions, evaluate each expression sequentially and assign it to the variable in the current scope, then return the evaluation of the final expression.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/NPtxmW53/shared" frameborder="0" width="100%" height="500" name="NPtxmW53"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>expression</code>.  Each expression is evaluated once, but within that evaluation we may search the entire scope.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script>.  We may pass <script type="math/tex; mode=display">O(N)</script> new strings to our <code>evaluate</code> function when making intermediate evaluations, each of length <script type="math/tex; mode=display">O(N)</script>.  With effort, we could reduce the total space complexity to <script type="math/tex; mode=display">O(N)</script> with interning or passing pointers.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
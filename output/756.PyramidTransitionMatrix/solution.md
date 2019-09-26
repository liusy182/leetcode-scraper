<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-state-to-state-transition-wrong-answer">Approach #1: State to State Transition [Wrong Answer]</a></li>
<li><a href="#approach-2-depth-first-search-accepted">Approach #2: Depth-First Search [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-state-to-state-transition-wrong-answer">Approach #1: State to State Transition [Wrong Answer]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>We model the states that blocks can be in.  Each state is a binary number where the <code>k</code>th bit is set if the <code>k</code>th type of block is a possibility.  Then, we create a transition map <code>T[state1][state2] -&gt; state</code> that takes a left state and a right state and outputs all possible parent states.</p>
<p>At the end, applying these transitions is straightforward.  However, this approach is not correct, because the transitions are not independent.  If for example we have states in a row <code>A, {B or C}, A</code>, and allowed triples <code>(A, B, D)</code>, <code>(C, A, D)</code>, then regardless of the choice of <code>{B or C}</code> we cannot create the next row of the pyramid.</p>
<iframe src="https://leetcode.com/playground/FoBNczLu/shared" frameborder="0" width="100%" height="429" name="FoBNczLu"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(2^{2\mathcal{A}}A + N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>bottom</code>, <script type="math/tex; mode=display">A</script> is the length of <code>allowed</code>, and <script type="math/tex; mode=display">\mathcal{A}</script> is the size of the alphabet.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(2^{2\mathcal{A}})</script> in additional space complexity.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-depth-first-search-accepted">Approach #2: Depth-First Search [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>We exhaustively try every combination of blocks.</p>
<p><strong>Algorithm</strong></p>
<p>We can work in either strings or integers, but we need to create a transition map <code>T</code> from the list of allowed triples.  This map <code>T[x][y] = {set of z}</code> will be all possible parent blocks for a left child of <code>x</code> and a right child of <code>y</code>.  When we work in strings, we use <code>Set</code>, and when we work in integers, we will use the set bits of the result integer.</p>
<p>Afterwards, to <code>solve</code> a row, we generate every possible combination of the next row and solve them.  If any of those new rows are solvable, we return <code>True</code>, otherwise <code>False</code>.</p>
<p>We can also cache intermediate results, saving us time.  This is illustrated in the comments for Python.  For Java, all caching is done with lines of code that mention the integer <code>R</code>.</p>
<iframe src="https://leetcode.com/playground/W723Lgci/shared" frameborder="0" width="100%" height="500" name="W723Lgci"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(\mathcal{A}^{N})</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>bottom</code>, and <script type="math/tex; mode=display">\mathcal{A}</script> is the size of the alphabet, and assuming we cache intermediate results.  We might try every sequence of letters for each row.  [The total complexity is because <script type="math/tex; mode=display">O(\sum_{k}^n \mathcal{A}^{k})</script> is a geometric series equal to <script type="math/tex; mode=display">O(\frac{\mathcal{A^{n+1}}-1}{\mathcal{A}-1})</script>.]  Without intermediate caching, this would be <script type="math/tex; mode=display">O(\mathcal{A}^{N^2})</script>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N^2)</script> additional space complexity.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
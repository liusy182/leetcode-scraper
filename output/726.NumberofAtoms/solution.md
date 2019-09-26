<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</a></li>
<li><a href="#approach-2-stack-accepted">Approach #2: Stack [Accepted]</a></li>
<li><a href="#approach-3-regular-expressions-accepted">Approach #3: Regular Expressions [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-recursion-accepted">Approach #1: Recursion [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Write a function <code>parse</code> that parses the formula from index <code>i</code>, returning a map <code>count</code> from names to multiplicities (the number of times that name is recorded).</p>
<p>We will put <code>i</code> in global state: our <code>parse</code> function increments <code>i</code> throughout any future calls to <code>parse</code>.</p>
<ul>
<li>
<p>When we see a <code>'('</code>, we will parse whatever is inside the brackets (up to the closing ending bracket) and add it to our count.</p>
</li>
<li>
<p>Otherwise, we should see an uppercase character: we will parse the rest of the letters to get the name, and add that (plus the multiplicity if there is one.)</p>
</li>
<li>
<p>At the end, if there is a final multiplicity (representing the multiplicity of a bracketed sequence), we'll multiply our answer by this.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/pdZAZ5dG/shared" frameborder="0" width="100%" height="500" name="pdZAZ5dG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of the formula.  It is <script type="math/tex; mode=display">O(N)</script> to parse through the formula, but each of <script type="math/tex; mode=display">O(N)</script> multiplicities after a bracket may increment the count of each name in the formula (inside those brackets), leading to an <script type="math/tex; mode=display">O(N^2)</script> complexity.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(N)</script>.  We aren't recording more intermediate information than what is contained in the formula.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-stack-accepted">Approach #2: Stack [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Instead of recursion, we can simulate the call stack by using a stack of <code>count</code>s directly.</p>
<iframe src="https://leetcode.com/playground/KLEWBfKw/shared" frameborder="0" width="100%" height="500" name="KLEWBfKw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity <script type="math/tex; mode=display">O(N^2)</script>, and Space Complexity <script type="math/tex; mode=display">O(N)</script>.  The analysis is the same as <em>Approach #1</em>.</li>
</ul>
<hr>
<h4 id="approach-3-regular-expressions-accepted">Approach #3: Regular Expressions [Accepted]</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Whenever parsing is involved, we can use <em>regular expressions</em>, a language for defining patterns in text.</p>
<p>Our regular expression will be <code>"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)"</code>.  Breaking this down by <em>capture group</em>, this is:</p>
<ul>
<li><code>([A-Z][a-z]*)</code> Match an uppercase character followed by any number of lowercase characters, then (<code>(\d*)</code>) match any number of digits.</li>
<li>OR, <code>(\()</code> match a left bracket or <code>(\))</code> right bracket, then <code>(\d*)</code> match any number of digits.</li>
</ul>
<p>Now we can proceed as in <em>Approach #2</em>.</p>
<ul>
<li>
<p>If we parsed a name and multiplicity <code>([A-Z][a-z]*)(\d*)</code>, we will add it to our current count.</p>
</li>
<li>
<p>If we parsed a left bracket, we will append a new <code>count</code> to our stack, representing the nested depth of parentheses.</p>
</li>
<li>
<p>If we parsed a right bracket (and possibly another multiplicity), we will multiply our deepest level <code>count</code>, <code>top = stack.pop()</code>, and add those entries to our current count.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/rnaR7xpb/shared" frameborder="0" width="100%" height="500" name="rnaR7xpb"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity <script type="math/tex; mode=display">O(N^2)</script>, and Space Complexity <script type="math/tex; mode=display">O(N)</script>.  The analysis is the same as <em>Approach #1</em>, as this regular expression did not look backwards when parsing.</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.  Approaches #1 and #2 inspired by <a href="https://leetcode.com/zestypanda/">@zestypanda</a>.  Java solution for #3 by <a href="https://discuss.leetcode.com/user/jianchao-li-fighter">@jianchao.li.fighter</a>.</p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-backtracking">Approach 2: Backtracking</a></li>
<li><a href="#approach-3-closure-number">Approach 3: Closure Number</a></li>
</ul>
</div>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Intuition</strong></p>
<p>We can generate all <script type="math/tex; mode=display">2^{2n}</script> sequences of <code>'('</code> and <code>')'</code> characters.  Then, we will check if each one is valid.</p>
<p><strong>Algorithm</strong></p>
<p>To generate all sequences, we use a recursion.  All sequences of length <code>n</code> is just <code>'('</code> plus all sequences of length <code>n-1</code>, and then <code>')'</code> plus all sequences of length <code>n-1</code>.</p>
<p>To check whether a sequence is valid, we keep track of <code>balance</code>, the net number of opening brackets minus closing brackets.  If it falls below zero at any time, or doesn't end in zero, the sequence is invalid - otherwise it is valid.</p>
<iframe src="https://leetcode.com/playground/eDRvbWjL/shared" frameborder="0" width="100%" height="500" name="eDRvbWjL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity : <script type="math/tex; mode=display">O(2^{2n}n)</script>.  For each of <script type="math/tex; mode=display">2^{2n}</script> sequences, we need to create and validate the sequence, which takes <script type="math/tex; mode=display">O(n)</script> work.</p>
</li>
<li>
<p>Space Complexity : <script type="math/tex; mode=display">O(2^{2n}n)</script>.  Naively, every sequence could be valid.  See <a href="#approach-3-closure-number">Approach 3</a> for development of a tighter asymptotic bound.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-backtracking">Approach 2: Backtracking</h4>
<p><strong>Intuition and Algorithm</strong></p>
<p>Instead of adding <code>'('</code> or <code>')'</code> every time as in <a href="#approach-1-brute-force">Approach 1</a>, let's only add them when we know it will remain a valid sequence.  We can do this by keeping track of the number of opening and closing brackets we have placed so far.</p>
<p>We can start an opening bracket if we still have one (of <code>n</code>) left to place.  And we can start a closing bracket if it would not exceed the number of opening brackets.</p>
<iframe src="https://leetcode.com/playground/npPa38Mh/shared" frameborder="0" width="100%" height="378" name="npPa38Mh"></iframe>

<p><strong>Complexity Analysis</strong></p>
<p>Our complexity analysis rests on understanding how many elements there are in <code>generateParenthesis(n)</code>.  This analysis is outside the scope of this article, but it turns out this is the <code>n</code>-th Catalan number <script type="math/tex; mode=display">\dfrac{1}{n+1}\binom{2n}{n}</script>, which is bounded asymptotically by <script type="math/tex; mode=display">\dfrac{4^n}{n\sqrt{n}}</script>.</p>
<ul>
<li>
<p>Time Complexity : <script type="math/tex; mode=display">O(\dfrac{4^n}{\sqrt{n}})</script>.  Each valid sequence has at most <code>n</code> steps during the backtracking procedure.</p>
</li>
<li>
<p>Space Complexity : <script type="math/tex; mode=display">O(\dfrac{4^n}{\sqrt{n}})</script>, as described above, and using <script type="math/tex; mode=display">O(n)</script> space to store the sequence.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-closure-number">Approach 3: Closure Number</h4>
<p><strong>Intuition</strong></p>
<p>To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.</p>
<p>Consider the <em>closure number</em> of a valid parentheses sequence <code>S</code>: the least <code>index &gt;= 0</code> so that <code>S[0], S[1], ..., S[2*index+1]</code> is valid.  Clearly, every parentheses sequence has a unique <em>closure number</em>.  We can try to enumerate them individually.</p>
<p><strong>Algorithm</strong></p>
<p>For each closure number <code>c</code>, we know the starting and ending brackets must be at index <code>0</code> and <code>2*c + 1</code>. Then, the <code>2*c</code> elements between must be a valid sequence, plus the rest of the elements must be a valid sequence.</p>
<iframe src="https://leetcode.com/playground/Z3ZYfRAo/shared" frameborder="0" width="100%" height="293" name="Z3ZYfRAo"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time and Space Complexity : <script type="math/tex; mode=display">O(\dfrac{4^n}{\sqrt{n}})</script>.  The analysis is similar to <a href="#approach-2-backtracking">Approach 2</a>.</li>
</ul>
          </div>
        
      </div>
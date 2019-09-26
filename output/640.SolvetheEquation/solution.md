<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-partioning-coefficients-accepted">Approach #1 Partioning Coefficients [Accepted]</a></li>
<li><a href="#approach-2-using-regex-for-spliting-accepted">Approach #2 Using regex for spliting [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-partioning-coefficients-accepted">Approach #1 Partioning Coefficients [Accepted]</h4>
<p>In the current approach, we start by splitting the given <script type="math/tex; mode=display">equation</script> based on <code>=</code> sign. This way, we've separated the left and right hand side of this equation. Once this is done, we need to extract the individual elements(i.e. <code>x</code>'s and the numbers) from both sides of the equation. To do so, we make use of <code>breakIt</code> function, in which we traverse over the given equation(either left hand side or right hand side), and put the separated parts into an array. </p>
<p>Now, the idea is as follows. We treat the given equation as if we're bringing all the <code>x</code>'s on the left hand side and all the rest of the numbers on the right hand side as done below for an example.</p>
<p><code>x+5-3+x=6+x-2</code></p>
<p><code>x+x-x=6-2-5+3</code></p>
<p>Thus, every <code>x</code> in the left hand side of the given equation is treated as positive, while that on the right hand side is treated as negative, in the current implementation. </p>
<p>Likewise, every number on the left hand side is treated as negative, while that on the right hand side is treated as positive. Thus, by doing so, we obtain all the <code>x</code>'s in the new <script type="math/tex; mode=display">lhs</script> and all the numbers in the new <script type="math/tex; mode=display">rhs</script> of the original equation. </p>
<p>Further, in case of an <code>x</code>, we also need to find its corresponding coefficients in order to evaluate the final effective coefficient of <code>x</code> on the left hand side. We also evaluate the final effective number on the right hand side as well.</p>
<p>Now, in case of a unique solution, the ratio of the effective <script type="math/tex; mode=display">rhs</script> and <script type="math/tex; mode=display">lhs</script> gives the required result. In case of infinite solutions, both the effective <script type="math/tex; mode=display">lhs</script> and <script type="math/tex; mode=display">rhs</script> turns out to be zero e.g. <code>x+1=x+1</code>. In case of no solution, the coefficient of <code>x</code>(<script type="math/tex; mode=display">lhs</script>) turns out to be zero, but the effective number on the <script type="math/tex; mode=display">rhs</script> is non-zero.</p>
<iframe src="https://leetcode.com/playground/5qsPscf9/shared" frameborder="0" name="5qsPscf9" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Generating coefficients and findinn <script type="math/tex; mode=display">lhs</script> and <script type="math/tex; mode=display">rhs</script> will take <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. ArrayList <script type="math/tex; mode=display">res</script> size can grow upto <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-regex-for-spliting-accepted">Approach #2 Using regex for spliting [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we made use of a new function <code>breakIt</code> to obtain the individual components of either the left hand side or the right hand side. Instead of doing so, we can also make use of splitting based on <code>+</code> or <code>-</code> sign, to obtain the individual elements. The rest of the process remains the same as in the last approach. </p>
<p>In order to do the splitting, we make use of an expression derived from regular expressions(regex). Simply speaking, regex is a functionality used to match a target string based on some given criteria. The ?=n quantifier, in regex, matches any string that is followed by a specific string <script type="math/tex; mode=display">n</script>. What it's saying is that the captured match must be followed by <script type="math/tex; mode=display">n</script> but the <script type="math/tex; mode=display">n</script> itself isn't captured.</p>
<p>By making use of this kind of expression in the <code>split</code> functionality, we make sure that the partitions are obtained such that the <code>+</code> or <code>-</code> sign remains along with the parts(numbers or coefficients) even after the splitting.</p>
<iframe src="https://leetcode.com/playground/9JbHjYgz/shared" frameborder="0" name="9JbHjYgz" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Generating coefficients and finding <script type="math/tex; mode=display">lhs</script> and <script type="math/tex; mode=display">rhs</script> will take <script type="math/tex; mode=display">O(n)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. ArrayList <script type="math/tex; mode=display">res</script> size can grow upto <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-counting">Approach 1: Counting</a></li>
<li><a href="#approach-2-maintain-duplicate-info">Approach 2: Maintain Duplicate Info</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-counting">Approach 1: Counting</h4>
<p><strong>Intuition</strong></p>
<p>Let's count the quantity of each element.  Clearly, we want to increment duplicated values.</p>
<p>For each duplicate value, we could do a "brute force" solution of incrementing it repeatedly until it is not unique.  However, we might do a lot of work - consider the work done by an array of all ones.  We should think of how to amend our solution to solve this case as well.</p>
<p>What we can do instead is lazily evaluate our increments.  If for example we have <code>[1, 1, 1, 1, 3, 5]</code>, we don't need to process all the increments of duplicated <code>1</code>s.  We could take three ones (<code>taken = [1, 1, 1]</code>) and continue processing.  When we find an empty place like <code>2</code>, <code>4</code>, or <code>6</code>, we can then recover that our increment will be <code>2-1</code>, <code>4-1</code>, and <code>6-1</code>.</p>
<p><strong>Algorithm</strong></p>
<p>Count the values.  For each possible value <code>x</code>:</p>
<ul>
<li>If there are 2 or more values <code>x</code> in <code>A</code>, save the extra duplicated values to increment later.</li>
<li>If there are 0 values <code>x</code> in <code>A</code>, then a saved value <code>v</code> gets incremented to <code>x</code>.</li>
</ul>
<p>In Java, the code is less verbose with a slight optimization:  we record only the number of saved values, and we subtract from the answer in advance.  In the <code>[1, 1, 1, 1, 3, 5]</code> example, we do <code>taken = 3</code> and <code>ans -= 3</code> in advance, and later we do <code>ans += 2; ans += 4; ans += 6</code>.  This optimization is also used in <em>Approach 2</em>.</p>
<iframe src="https://leetcode.com/playground/hDLTpYAB/shared" frameborder="0" width="100%" height="412" name="hDLTpYAB"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-maintain-duplicate-info">Approach 2: Maintain Duplicate Info</h4>
<p><strong>Intuition</strong></p>
<p>Let's imagine the array is sorted and we are moving from left to right.  As in Approach 1, we want to take duplicate values to release later.</p>
<p><strong>Algorithm</strong></p>
<p>There are two cases.</p>
<ul>
<li>
<p>If <code>A[i-1] == A[i]</code>, we have a duplicate to take.</p>
</li>
<li>
<p>If <code>A[i-1] &lt; A[i]</code>, we might be able to place our taken values into those free positions.  Specifically, we have <code>give = min(taken, A[i] - A[i-1] - 1)</code> possible values to release, and they will have final values <code>A[i-1] + 1, A[i-1] + 2, ..., A[i-1] + give</code>.  This has a sum of <script type="math/tex; mode=display">A[i-1] * \text{give} + (\sum_{k=1}^{give})</script>.</p>
</li>
</ul>
<iframe src="https://leetcode.com/playground/P7fCXnrT/shared" frameborder="0" width="100%" height="429" name="P7fCXnrT"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N\log N)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N)</script> in additional space complexity, depending on the specific implementation of the built in sort.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
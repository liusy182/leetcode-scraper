<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-frontier-set">Approach 1: Frontier Set</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-frontier-set">Approach 1: Frontier Set</h4>
<p><strong>Intuition</strong></p>
<p>Let's try to speed up a brute force answer.  Evidently, the brute force approach is to calculate every result <code>result(i, j) = A[i] | A[i+1] | ... | A[j]</code>.  We can speed this up by taking note of the fact that <code>result(i, j+1) = result(i, j) | A[j+1]</code>.  Naively, this approach has time complexity <script type="math/tex; mode=display">O(N^2)</script>, where <script type="math/tex; mode=display">N</script> is the length of the array.</p>
<p>Actually, this approach can be better than that.  At the <code>k</code>th step, say we have all the <code>result(i, k)</code> in some set <code>cur</code>.  Then we can find the next <code>cur</code> set (for <code>k -&gt; k+1</code>) by using <code>result(i, k+1) = result(i, k) | A[k+1]</code>.</p>
<p>However, the number of unique values in this set <code>cur</code> is at most 32, since the list <code>result(k, k), result(k-1, k), result(k-2, k), ...</code> is monotone increasing, and any subsequent values that are different must have more 1s in it's binary representation (to a maximum of 32 ones).</p>
<p><strong>Algorithm</strong></p>
<p>In the <code>k</code>th step, we'll maintain <code>cur</code>: the set of results <code>A[i] | ... | A[k]</code> for all <code>i</code>.  These results will be included in our final answer set.</p>
<iframe src="https://leetcode.com/playground/rDNmUE84/shared" frameborder="0" width="100%" height="344" name="rDNmUE84"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  <script type="math/tex; mode=display">O(N \log W)</script>, where <script type="math/tex; mode=display">N</script> is the length of <code>A</code>, and <script type="math/tex; mode=display">W</script> is the maximum size of elements in <code>A</code>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(N \log W)</script>, the size of the answer.
<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
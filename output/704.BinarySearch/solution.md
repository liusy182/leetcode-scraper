<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-binary-search">Approach 1: Binary Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-binary-search">Approach 1: Binary Search</h4>
<p><strong>Intuition</strong></p>
<p><a href="https://en.wikipedia.org/wiki/Binary_search_algorithm">Binary search</a>
is a textbook algorithm based on the idea to 
compare the target value to the middle element of the array.</p>
<p>If the target value is equal to the middle element - we're done.</p>
<p>If the target value is smaller - continue to search on the left.</p>
<p>If the target value is larger - continue to search on the right.</p>
<p><img alt="postorder" src="../Figures/704/search.png"></p>
<p><strong>Algorithm</strong></p>
<ul>
<li>
<p>Initialise left and right pointers : <code>left = 0</code>, <code>right = n - 1</code>.</p>
</li>
<li>
<p>While <code>left &lt;= right</code> :</p>
<ul>
<li>
<p>Compare middle element of the array <code>nums[pivot]</code> to the target
value <code>target</code>.</p>
<ul>
<li>
<p>If the middle element <em>is</em> the target <code>target = nums[pivot]</code> : return <code>pivot</code>. </p>
</li>
<li>
<p>If the target is not yet found : </p>
<ul>
<li>
<p>If <code>target &lt; nums[pivot]</code>, continue the search on the left 
<code>right = pivot - 1</code>.</p>
</li>
<li>
<p>Else continue the search on the right 
<code>left = pivot + 1</code>.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><strong>Implementation</strong></p>
<p>!?!../Documents/704_LIS.json:1000,401!?!</p>
<iframe src="https://leetcode.com/playground/87ynKoMa/shared" frameborder="0" width="100%" height="276" name="87ynKoMa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(\log N)</script>. </p>
<p>Let's compute time complexity with the help of 
<a href="https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)">master theorem</a> 
<script type="math/tex; mode=display">T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)</script>.
The equation represents dividing the problem 
up into <script type="math/tex; mode=display">a</script> subproblems of size <script type="math/tex; mode=display">\frac{N}{b}</script> in <script type="math/tex; mode=display">\Theta(N^d)</script> time. 
Here at step there is only one subproblem <code>a = 1</code>, its size 
is a half of the initial problem <code>b = 2</code>, 
and all this happens in a constant time <code>d = 0</code>.
That means that <script type="math/tex; mode=display">\log_b{a} = d</script> and hence we're dealing with 
<a href="https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Case_2_example">case 2</a>
that results in <script type="math/tex; mode=display">\mathcal{O}(n^{\log_b{a}} \log^{d + 1} N)</script>
= <script type="math/tex; mode=display">\mathcal{O}(\log N)</script> time complexity.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(1)</script> since it's a constant space
solution.</p>
</li>
</ul>
<p>Analysis written by @<a href="https://leetcode.com/liaison/">liaison</a>
and @<a href="https://leetcode.com/andvary/">andvary</a></p>
          </div>
        
      </div>
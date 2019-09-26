<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-one-pass">Approach 2: One Pass</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).</p>
<p>In formal terms, we need to find <script type="math/tex; mode=display">\max(prices[j] - prices[i])</script>, for every <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> such that <script type="math/tex; mode=display">j > i</script>.</p>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<iframe src="https://leetcode.com/playground/enjmphvG/shared" frameborder="0" width="100%" height="276" name="enjmphvG"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Loop runs <script type="math/tex; mode=display">\dfrac{n (n-1)}{2}</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Only two variables - <script type="math/tex; mode=display">\text{maxprofit}</script> and <script type="math/tex; mode=display">\text{profit}</script> are used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-one-pass">Approach 2: One Pass</h4>
<p><strong>Algorithm</strong></p>
<p>Say the given array is:</p>
<p>[7, 1, 5, 3, 6, 4]</p>
<p>If we plot the numbers of the given array on a graph, we get:</p>
<p><img alt="Profit Graph" src="https://leetcode.com/media/original_images/121_profit_graph.png"></p>
<p>The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley.
We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.</p>
<iframe src="https://leetcode.com/playground/G8wkXsyB/shared" frameborder="0" width="100%" height="276" name="G8wkXsyB"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Only a single pass is needed.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Only two variables are used.</p>
</li>
</ul>
          </div>
        
      </div>
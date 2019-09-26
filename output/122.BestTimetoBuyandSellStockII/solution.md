<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-peak-valley-approach">Approach 2: Peak Valley Approach</a></li>
<li><a href="#approach-3-simple-one-pass">Approach 3: Simple One Pass</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<p>We have to determine the maximum profit that can be obtained by making the transactions (no limit on the number of transactions done). For this we need to find out those sets of buying and selling prices which together lead to the maximization of profit.</p>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>In this case, we simply calculate the profit corresponding to all the possible sets of transactions and find out the maximum profit out of them.</p>
<iframe src="https://leetcode.com/playground/DQfAGPiL/shared" frameborder="0" width="100%" height="463" name="DQfAGPiL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^n)</script>. Recursive function is called <script type="math/tex; mode=display">n^n</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Depth of recursion is <script type="math/tex; mode=display">n</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-peak-valley-approach">Approach 2: Peak Valley Approach</h4>
<p><strong>Algorithm</strong></p>
<p>Say the given array is:</p>
<p>[7, 1, 5, 3, 6, 4].</p>
<p>If we plot the numbers of the given array on a graph, we get:</p>
<p align="center"><img alt="Profit Graph" src="https://leetcode.com/media/original_images/122_maxprofit_1.PNG" width="539px"></p>
<p>If we analyze the graph, we notice that the points of interest are the consecutive valleys and peaks.</p>
<p>Mathematically speaking:
<script type="math/tex; mode=display">
Total Profit= \sum_{i}(height(peak_i)-height(valley_i))
</script>
</p>
<p>The key point is we need to consider every peak immediately following a valley to maximize the profit. In case we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the transactions leading to an overall lesser profit.</p>
<p>For example, in the above case, if we skip <script type="math/tex; mode=display">peak_i</script> and <script type="math/tex; mode=display">valley_j</script> trying to obtain more profit by considering points with more difference in heights, the net profit obtained will always be lesser than the one obtained by including them, since <script type="math/tex; mode=display">C</script> will always be lesser than <script type="math/tex; mode=display">A+B</script>.</p>
<iframe src="https://leetcode.com/playground/Yrs8F9na/shared" frameborder="0" width="100%" height="361" name="Yrs8F9na"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single pass.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant space required.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-simple-one-pass">Approach 3: Simple One Pass</h4>
<p><strong>Algorithm</strong></p>
<p>This solution follows the logic used in <a href="#approach-2-peak-valley-approach">Approach 2</a> itself, but with only a slight variation. In this case, instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. In the end,we will be using the peaks and valleys effectively, but we need not track the costs corresponding to the peaks and valleys along with the maximum profit, but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit. This approach will simplify the solution.
This can be made clearer by taking this example:</p>
<p>[1, 7, 2, 3, 6, 7, 6, 7]</p>
<p>The graph corresponding to this array is:</p>
<p align="center"><img alt="Profit Graph" src="https://leetcode.com/media/original_images/122_maxprofit_2.PNG" width="539px"></p>
<p>From the above graph, we can observe that the sum <script type="math/tex; mode=display">A+B+C</script> is equal to the difference <script type="math/tex; mode=display">D</script> corresponding to the difference between the heights of the consecutive peak and valley.</p>
<iframe src="https://leetcode.com/playground/ppWUGTaj/shared" frameborder="0" width="100%" height="225" name="ppWUGTaj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Single pass.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script>. Constant space needed.</p>
</li>
</ul>
          </div>
        
      </div>
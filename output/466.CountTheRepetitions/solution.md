<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-a-better-brute-force-accepted">Approach #2 A better brute force [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute force [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>According to the question, we need to find <script type="math/tex; mode=display">m</script> such that <script type="math/tex; mode=display">[S2,m]</script> is the largest subsequence that can be found in <script type="math/tex; mode=display">S1</script>. <script type="math/tex; mode=display">S2</script> is essentially <script type="math/tex; mode=display">[s2,n2]</script> and <script type="math/tex; mode=display">S1</script> is <script type="math/tex; mode=display">[s1,n1]</script> and so, we can find the number of times <script type="math/tex; mode=display">s2</script> repeats in <script type="math/tex; mode=display">[s1,n1]</script>, say <script type="math/tex; mode=display">\text{repeat_count}</script>. And the number of times <script type="math/tex; mode=display">S2</script> repeats in <script type="math/tex; mode=display">S1</script> is therefore <script type="math/tex; mode=display">\text{(repeat_count/n2)}</script>. Simple.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize <script type="math/tex; mode=display">\text{index=0}</script> and <script type="math/tex; mode=display">\text{repeat_count=0}</script>. <script type="math/tex; mode=display">\text{index}</script> represents the current index in <script type="math/tex; mode=display">s2</script> to be checked against <script type="math/tex; mode=display">s1</script> and <script type="math/tex; mode=display">\text{repeat_count}</script> represents the number of times <script type="math/tex; mode=display">s2</script> repeats in <script type="math/tex; mode=display">S1</script>.</li>
<li>Iterate over the variable <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">n1-1</script>:<ul>
<li>Iterate over the variable <script type="math/tex; mode=display">j</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">\text{size(s1)}-1</script>:  <ul>
<li>If <script type="math/tex; mode=display">\text{s1[j] }</script> is equal to <script type="math/tex; mode=display">\text{s2[index]}</script>, increment <script type="math/tex; mode=display">\text{index}</script>.</li>
<li>If <script type="math/tex; mode=display">index</script> is equal to <script type="math/tex; mode=display">size(s2)</script>, this implies that <script type="math/tex; mode=display">s2</script> has completed one repartition and hence set <script type="math/tex; mode=display">\text{index=0}</script> and increment the <script type="math/tex; mode=display">\text{repeat_count}</script>.</li>
</ul>
</li>
</ul>
</li>
<li>Return <script type="math/tex; mode=display">\text{(repeat_count / n2)}</script> since, <script type="math/tex; mode=display">S2</script> is <script type="math/tex; mode=display">\text{[s2,n2]}</script>.</li>
</ul>
<iframe src="https://leetcode.com/playground/y5jtZgJj/shared" frameborder="0" name="y5jtZgJj" width="100%" height="326"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n1*size(s1))</script>.</p>
<ul>
<li>We iterate over the entire length of string <script type="math/tex; mode=display">s1</script> for <script type="math/tex; mode=display">n1</script> times.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script> extra space for <script type="math/tex; mode=display">\text{index}</script> and <script type="math/tex; mode=display">\text{repeat_count}</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-a-better-brute-force-accepted">Approach #2 A better brute force [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>In Approach #1, we simply checked for repetition over the entire <script type="math/tex; mode=display">[s1,n1]</script>. However, <script type="math/tex; mode=display">n1</script> could be quiet large and thus, is inefficient to iterate over complete <script type="math/tex; mode=display">S1</script>. We can take advantage of the fact that <script type="math/tex; mode=display">s1</script> is repeating and hence, we could find a pattern of repetition of <script type="math/tex; mode=display">s2</script> in <script type="math/tex; mode=display">S1</script>. Once, we get the repetition pattern, we can easy calculate how many times the pattern repeats in <script type="math/tex; mode=display">n2</script> in <script type="math/tex; mode=display">O(1)</script>.</p>
<p><em>But what's the pattern!</em></p>
<p>In approach #1, we kept <script type="math/tex; mode=display">\text{index}</script> which tells the index to search in <script type="math/tex; mode=display">s2</script>. We try to see in the below illustration if this <script type="math/tex; mode=display">\text{index}</script> repeats itself after some fixed iterations of <script type="math/tex; mode=display">s1</script> or not and if so, then how can we leverage it.</p>
<p align="center"><img alt="Count the repitition" src="../Figures/466/count_the_repititions.png" width="700px"></p>
<p>After finding the repitition pattern, we can calculate the sum of repeating pattern, part before repitition and part left after repitition as the result in <script type="math/tex; mode=display">O(1)</script>.   </p>
<p><em>But will this repitition always take place?</em></p>
<p>Yes! By <strong>Pigeonhole principle</strong>, which states that if <script type="math/tex; mode=display">n</script> items are put into <script type="math/tex; mode=display">m</script> containers, with <script type="math/tex; mode=display">n > m</script>, then at least one container must contain more than one item. So, according to this, we are sure to find 2 same <script type="math/tex; mode=display">index</script> after scanning at max <script type="math/tex; mode=display">\text{size(s2)}</script> blocks of <script type="math/tex; mode=display">s1</script>.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Intialize <script type="math/tex; mode=display">count=0</script> nd <script type="math/tex; mode=display">index=0</script>, which are same as in Approach #1.</li>
<li>Initialize 2 arrays, say <script type="math/tex; mode=display">\text{indexr}</script> and <script type="math/tex; mode=display">\text{countr}</script> of size <script type="math/tex; mode=display">(\text{size(s2)}+1)</script>, initialized with 0. The size <script type="math/tex; mode=display">(\text{size(s2)}+1)</script> is based on the Pigeonhole principle as discussed above. The 2 arrays specifies the <script type="math/tex; mode=display">\text{index}</script> and <script type="math/tex; mode=display">\text{count}</script> at the start of each <script type="math/tex; mode=display">s1</script> block.</li>
<li>Iterate over <script type="math/tex; mode=display">i</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">n1-1</script>:<ul>
<li>Iterate over <script type="math/tex; mode=display">j</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">\text{size(s1)}-1</script>:<ul>
<li>If <script type="math/tex; mode=display">\text{s1[j]} == \text{s2[index]}</script>, increment <script type="math/tex; mode=display">\text{index}</script>.</li>
<li>If <script type="math/tex; mode=display">\text{index}</script> is equal to <script type="math/tex; mode=display">\text{size(s2)}</script>, set <script type="math/tex; mode=display">\text{index} = 0</script> and increment <script type="math/tex; mode=display">\text{count}</script>.</li>
</ul>
</li>
<li>Set <script type="math/tex; mode=display">\text{countr[i]}=\text{count}</script> and <script type="math/tex; mode=display">\text{indexr[i]}=\text{index}</script>
</li>
<li>
<p>Iterate over <script type="math/tex; mode=display">k</script> from <script type="math/tex; mode=display">0</script> to <script type="math/tex; mode=display">i-1</script>:</p>
<ul>
<li>If we find the repitition, i.e. current <script type="math/tex; mode=display">\text{index} = \text{indexr[k]}</script>, we calculate the count for block before the repitition starts, the repeating block and the block left after repitition pattern, which can be calculated as:</li>
</ul>
<p>
<script type="math/tex; mode=display">
\begin{align}
\text{prev_count} &= \text{countr}[k] \\
\text{pattern_count} &= (\text{countr}[i] - \text{countr}[k]) * \frac{n1 - 1 - k}{i - k} \\
\text{remain_count} &= \text{countr}\left[k + \left(n1 - 1 - k\right) \% \left(i - k \right)\right] - \text{countr}[k]
\end{align}
</script>
</p>
<ul>
<li>Sum the 3 counts and return the sum divided by <script type="math/tex; mode=display">n2</script>, since <script type="math/tex; mode=display">\text{S2 = [s2,n2]}</script>
</li>
<li>If no repetition is found, return <script type="math/tex; mode=display">\text{countr[n1-1]/n2}</script>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/2UJEXG8V/shared" frameborder="0" name="2UJEXG8V" width="100%" height="515"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">\text{O(size(s1)*size(s2))}</script>.</p>
<ul>
<li>According to the Pigeonhole principle, we need to iterate over <script type="math/tex; mode=display">s1</script> only <script type="math/tex; mode=display">(\text{size(s2)+1})</script> times at max.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(\text{size(s2)})</script> extra space for <script type="math/tex; mode=display">\text{indexr}</script> and <script type="math/tex; mode=display">\text{countr}</script> string.</p>
</li>
</ul>
<hr>
<p>Analysis written by <a href="https://leetcode.com/abhinavbansal0">@abhinavbansal0</a>.</p>
          </div>
        
      </div>
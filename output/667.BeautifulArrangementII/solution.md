<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-construction-accepted">Approach #2: Construction [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1: Brute Force [Time Limit Exceeded]</h4>
<p><strong>Intuition</strong></p>
<p>For each permutation of <script type="math/tex; mode=display">\text{[1, 2, ..., n]}</script>, let's look at the set of differences of the adjacent elements.</p>
<p><strong>Algorithm</strong></p>
<p>For each permutation, we find the number of unique differences of adjacent elements.  If it is the desired number, we'll return that permutation.</p>
<p>To enumerate each permutation without using library functions, we use a recursive algorithm, where <code>permute</code> is responsible for permuting the indexes of <script type="math/tex; mode=display">\text{nums}</script> in the interval <script type="math/tex; mode=display">\text{[start, nums.length)}</script>.</p>
<iframe src="https://leetcode.com/playground/JvKeuMXb/shared" frameborder="0" name="JvKeuMXb" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(n!)</script> to generate every permutation in the outer loop, then <script type="math/tex; mode=display">O(n)</script> work to check differences.  In total taking <script type="math/tex; mode=display">O(n* n!)</script> time.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(n)</script>.  We use <script type="math/tex; mode=display">\text{seen}</script> to store whether we've seen the differences, and each generated permutation has a length equal to <script type="math/tex; mode=display">\text{n}</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-construction-accepted">Approach #2: Construction [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>When <script type="math/tex; mode=display">\text{k = n-1}</script>, a valid construction is <script type="math/tex; mode=display">\text{[1, n, 2, n-1, 3, n-2, ....]}</script>. One way to see this is, we need to have a difference of <script type="math/tex; mode=display">\text{n-1}</script>, which means we need <script type="math/tex; mode=display">\text{1}</script> and <script type="math/tex; mode=display">\text{n}</script> adjacent; then, we need a difference of <script type="math/tex; mode=display">\text{n-2}</script>, etc.</p>
<p>Also, when <script type="math/tex; mode=display">\text{k = 1}</script>, a valid construction is <script type="math/tex; mode=display">\text{[1, 2, 3, ..., n]}</script>. So we have a construction when <script type="math/tex; mode=display">\text{n-k}</script> is tiny, and when it is large.  This leads to the idea that we can stitch together these two constructions:  we can put <script type="math/tex; mode=display">\text{[1, 2, ..., n-k-1]}</script> first so that <script type="math/tex; mode=display">\text{n}</script> is effectively <script type="math/tex; mode=display">\text{k+1}</script>, and then finish the construction with the first <script type="math/tex; mode=display">\text{"k = n-1"}</script> method.</p>
<p>For example, when <script type="math/tex; mode=display">\text{n = 6}</script> and <script type="math/tex; mode=display">\text{k = 3}</script>, we will construct the array as <script type="math/tex; mode=display">\text{[1, 2, 3, 6, 4, 5]}</script>.  This consists of two parts: a construction of <script type="math/tex; mode=display">\text{[1, 2]}</script> and a construction of <script type="math/tex; mode=display">\text{[1, 4, 2, 3]}</script> where every element had <script type="math/tex; mode=display">\text{2}</script> added to it (i.e. <script type="math/tex; mode=display">\text{[3, 6, 4, 5]}</script>).</p>
<p><strong>Algorithm</strong></p>
<p>As before, write <script type="math/tex; mode=display">\text{[1, 2, ..., n-k-1]}</script> first.  The remaining <script type="math/tex; mode=display">\text{k+1}</script> elements to be written are <script type="math/tex; mode=display">\text{[n-k, n-k+1, ..., n]}</script>, and we'll write them in alternating head and tail order.</p>
<p>When we are writing the <script type="math/tex; mode=display">i^{th}</script> element from the remaining <script type="math/tex; mode=display">\text{k+1}</script>, every even <script type="math/tex; mode=display">i</script> is going to be chosen from the head, and will have value <script type="math/tex; mode=display">\text{n-k + i//2}</script>.  Every odd <script type="math/tex; mode=display">i</script> is going to be chosen from the tail, and will have value <script type="math/tex; mode=display">\text{n - i//2}</script>.</p>
<iframe src="https://leetcode.com/playground/knXdznYV/shared" frameborder="0" name="knXdznYV" width="100%" height="275"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(n)</script>.  We are making a list of size <script type="math/tex; mode=display">\text{n}</script>.</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(n)</script>.  Our answer has a length equal to <script type="math/tex; mode=display">\text{n}</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a></p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-using-extra-array-accepted">Approach #2 Using Extra Array [Accepted]</a></li>
<li><a href="#approach-3-using-hashmap-accepted">Approach #3 Using HashMap [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force-time-limit-exceeded">Approach #1 Brute Force [Time Limit Exceeded]</h4>
<p><strong>Algorithm</strong></p>
<p>The brute force approach is really simple. We consider every possible subarray within the given array and count the number of zeros and ones in each subarray. Then, we find out the maximum size subarray with equal no. of zeros and ones out of them.</p>
<iframe src="https://leetcode.com/playground/sPZqbexo/shared" frameborder="0" name="sPZqbexo" width="100%" height="428"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We consider every possible subarray by traversing over the complete array for every start point possible.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Only two variables <script type="math/tex; mode=display">zeroes</script> and <script type="math/tex; mode=display">ones</script> are required.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-extra-array-accepted">Approach #2 Using Extra Array [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In this approach, we make use of a <script type="math/tex; mode=display">count</script> variable, which is used to store the relative number of ones and zeros encountered so far while traversing the array. The <script type="math/tex; mode=display">count</script> variable is incremented by one for every <script type="math/tex; mode=display">\text{1}</script> encountered and the same is decremented by one for every <script type="math/tex; mode=display">\text{0}</script> encountered.</p>
<p>We start traversing the array from the beginning. If at any moment, the <script type="math/tex; mode=display">count</script> becomes zero, it implies that we've encountered equal number of zeros and ones from the beginning till the current index of the array(<script type="math/tex; mode=display">i</script>). Not only this, another point to be noted is that  if we encounter the same <script type="math/tex; mode=display">count</script> twice while traversing the array, it means that the number of zeros and ones are equal between the indices corresponding to the equal <script type="math/tex; mode=display">count</script> values. The following figure illustrates the observation for the sequence <code>[0 0 1 0 0 0 1 1]</code>:</p>
<p><img alt="Contiguous_Array" src="../Figures/535_Contiguous_Array.PNG"></p>
<p>In the above figure, the subarrays between (A,B), (B,C) and (A,C) (lying between indices corresponing to <script type="math/tex; mode=display">count = 2</script>) have equal number of zeros and ones.</p>
<p>Another point to be noted is that the largest subarray is the one between the points (A, C). Thus, if we keep a track of the indices corresponding to the same <script type="math/tex; mode=display">count</script> values that lie farthest apart, we can determine the size of the largest subarray with equal no. of zeros and ones easily.</p>
<p>Now, the <script type="math/tex; mode=display">count</script> values can range between <script type="math/tex; mode=display">\text{-n}</script> to <script type="math/tex; mode=display">\text{+n}</script>, with the extreme points corresponding to the complete array being filled with all 0's and all 1's respectively. Thus, we make use of an array <script type="math/tex; mode=display">arr</script>(of size <script type="math/tex; mode=display">\text{2n+1}</script>to keep a track of the various <script type="math/tex; mode=display">count</script>'s encountered so far. We make an entry containing the current element's index (<script type="math/tex; mode=display">i</script>) in the <script type="math/tex; mode=display">arr</script> for a new <script type="math/tex; mode=display">count</script> encountered everytime. Whenever, we come across the same <script type="math/tex; mode=display">count</script> value later while traversing the array, we determine the length of the subarray lying between the indices corresponding to the same <script type="math/tex; mode=display">count</script> values.</p>
<iframe src="https://leetcode.com/playground/Nvw6WnPN/shared" frameborder="0" name="Nvw6WnPN" width="100%" height="411"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The complete array is traversed only once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">arr</script> array of size <script type="math/tex; mode=display">\text{2n+1}</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-hashmap-accepted">Approach #3 Using HashMap [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>This approach relies on the same premise as the previous approach. But, we need not use an array of size <script type="math/tex; mode=display">\text{2n+1}</script>, since it isn't necessary that we'll encounter all the <script type="math/tex; mode=display">count</script> values possible. Thus, we make use of a HashMap <script type="math/tex; mode=display">map</script> to store the entries in the form of <script type="math/tex; mode=display">(index, count)</script>. We make an entry for a <script type="math/tex; mode=display">count</script> in the <script type="math/tex; mode=display">map</script> whenever the <script type="math/tex; mode=display">count</script> is encountered first, and later on use the correspoding index to find the length of the largest subarray with equal no. of zeros and ones when the same <script type="math/tex; mode=display">count</script> is encountered again.</p>
<p>The following animation depicts the process:
<!--<img alt="Contiguous_Array" src="../Figures/525_Contiguous_Array.gif" />-->
!?!../Documents/525_Contiguous_Array.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/nG5CTUD8/shared" frameborder="0" name="nG5CTUD8" width="100%" height="360"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The entire array is traversed only once.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Maximum size of the HashMap <script type="math/tex; mode=display">map</script> will be <script type="math/tex; mode=display">\text{n}</script>, if all the elements are either 1 or 0.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
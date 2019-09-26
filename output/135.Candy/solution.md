<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-using-two-arrays">Approach 2: Using two arrays</a></li>
<li><a href="#approach-3-using-one-array">Approach 3: Using one array</a></li>
<li><a href="#approach-4-single-pass-approach-with-constant-space">Approach 4: Single Pass Approach with Constant Space</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>The simplest approach makes use of a 1-d array, <script type="math/tex; mode=display">candies</script> to keep a track of the candies given to the students. Firstly, we give 1 candy to each student. Then, we start scanning the
array from left-to-right. At every element encountered, firstly, if the current element's ratings, <script type="math/tex; mode=display">ratings[i]</script>, is larger than the previous element <script type="math/tex; mode=display">ratings[i-1]</script> and <script type="math/tex; mode=display">candies[i]<=candies[i-1]</script>,
then we update <script type="math/tex; mode=display">candies[i]</script> as <script type="math/tex; mode=display">candies[i]=candies[i-1] + 1</script>. Thus, now the candy distribution for these two elements <script type="math/tex; mode=display">candies[i-1]</script> and <script type="math/tex; mode=display">candies[i]</script> becomes correct for the time being(locally).
 In the same step, we also check if the current element's ratings, <script type="math/tex; mode=display">ratings[i]</script>, is larger than the next element's ratings,
i.e. <script type="math/tex; mode=display">ratings[i]>ratings[i+1]</script>. If so, we again update <script type="math/tex; mode=display">candies[i]=candies[i+1] + 1</script>. We continue this process for the whole <script type="math/tex; mode=display">ratings</script> array. If in any traversal,
no updation of the <script type="math/tex; mode=display">candies</script> array occurs, it means we've reached at the final required distribution of the candies and we can stop the traversals. To keep a track of
this we make use of a <script type="math/tex; mode=display">flag</script> which is set to <script type="math/tex; mode=display">\text{True}</script> if any updation occurs in a traversal.</p>
<p>At the end, we can sum up all the elements of the <script type="math/tex; mode=display">candies</script> array to obtain the required minimum number of candies.</p>
<iframe src="https://leetcode.com/playground/gpKEkWCp/shared" frameborder="0" width="100%" height="480" name="gpKEkWCp"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We need to traverse the array at most <script type="math/tex; mode=display">n</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. One <script type="math/tex; mode=display">candies</script> array of size <script type="math/tex; mode=display">n</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-two-arrays">Approach 2: Using two arrays</h4>
<p><strong>Algorithm</strong></p>
<p>In this approach, we make use of two 1-d arrays <script type="math/tex; mode=display">left2right</script> and <script type="math/tex; mode=display">right2left</script>. The <script type="math/tex; mode=display">left2right</script> array is used to store the number of candies required by the
current student taking care of the distribution relative to the left neighbours only. i.e. Assuming the distribution rule is: The student with a higher ratings
than its left neighbour should always get more candies than its left neighbour. Similarly, the <script type="math/tex; mode=display">right2left</script> array is used to store the number of candies candies required by the
current student taking care of the distribution relative to the right neighbours only. i.e. Assuming the distribution rule to be: The student with a higher ratings
than its right neighbour should always get more candies than its right neighbour. To do so, firstly we assign 1 candy to each student in both <script type="math/tex; mode=display">left2right</script> and <script type="math/tex; mode=display">right2left</script> array.
 Then, we traverse the array from
left-to-right and whenever the current element's ratings is larger than the left neighbour we update the
current element's candies in the <script type="math/tex; mode=display">left2right</script> array as <script type="math/tex; mode=display">left2right[i] = left2right[i-1] + 1</script>, since the current element's candies are always less than or equal candies than its left neighbour before updation.
After the forward traversal, we traverse the array from left-to-right and
update <script type="math/tex; mode=display">right2left[i]</script> as <script type="math/tex; mode=display">right2left[i] = right2left[i + 1] + 1</script>, whenever the current ( <script type="math/tex; mode=display">i^{th}</script> ) element has a higher ratings than the right ( <script type="math/tex; mode=display">(i+1)^{th}</script> ) element.</p>
<p>Now, for the <script type="math/tex; mode=display">i^{th}</script> student in the array, we need to give <script type="math/tex; mode=display">\text{max}(left2right[i], right2left[i])</script> to it, in order to satisfy both the left and the right neighbour
relationship. Thus, at the end, we obtain the minimum number of candies required as:</p>
<p>
<script type="math/tex; mode=display">
\text{minimum_candies}=\sum_{i=0}^{n-1} \text{max}(left2right[i], right2left[i]), \text{where } n = \text{length of the ratings array.}
</script>
</p>
<p>The following animation illustrates the method:</p>
<p><img alt="Candy_Two_Arrays" src="../Figures/135_Candy_Two_Pass.gif"></p>
<iframe src="https://leetcode.com/playground/ZJvLfBzc/shared" frameborder="0" width="100%" height="446" name="ZJvLfBzc"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">left2right</script> and <script type="math/tex; mode=display">right2left</script> arrays are traversed thrice.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Two arrays <script type="math/tex; mode=display">left2right</script> and <script type="math/tex; mode=display">right2left</script> of size <script type="math/tex; mode=display">n</script> are used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-one-array">Approach 3: Using one array</h4>
<p><strong>Algorithm</strong></p>
<p>In the previous approach, we used two arrays to keep track of the left neighbour and the right neighbour relation individually and later on combined these two. Instead of this, we
can make use of a single array <script type="math/tex; mode=display">candies</script> to keep the count of the number of candies to be allocated to the current student. In order to do so, firstly we assign 1 candy to
each student. Then, we traverse the array from left-to-right and distribute the candies following only the left neighbour relation i.e. whenever the current element's ratings is
larger than the left neighbour and has less than or equal candies than its left neighbour, we update the
current element's candies in the <script type="math/tex; mode=display">candies</script> array as <script type="math/tex; mode=display">candies[i] = candies[i-1] + 1</script>. While updating we need not compare <script type="math/tex; mode=display">candies[i]</script> and <script type="math/tex; mode=display">candies[i - 1]</script>, since
 <script type="math/tex; mode=display">candies[i] \leq candies[i - 1]</script> before updation. After this, we traverse the array from right-to-left. Now, we need to
update the <script type="math/tex; mode=display">i^{th}</script> element's candies in order to satisfy both the left neighbour and the right neighbour relation. Now, during the backward traversal, if <script type="math/tex; mode=display">ratings[i]>ratings[i + 1]</script>,
considering only the right neighbour criteria, we could've updated <script type="math/tex; mode=display">candies[i]</script> as <script type="math/tex; mode=display">candies[i] = candies[i + 1] + 1</script>. But, this time we need to update the <script type="math/tex; mode=display">candies[i]</script> only
if <script type="math/tex; mode=display">candies[i] \leq candies[i + 1]</script>. This happens because, this time we've already altered the <script type="math/tex; mode=display">candies</script> array during the forward traversal and thus <script type="math/tex; mode=display">candies[i]</script> isn't
necessarily less than or equal to <script type="math/tex; mode=display">candies[i + 1]</script>. Thus, if <script type="math/tex; mode=display">ratings[i] > ratings[i + 1]</script>, we can update <script type="math/tex; mode=display">candies[i]</script> as <script type="math/tex; mode=display">candies[i] = \text{max}(candies[i], candies[i + 1] + 1)</script>, which makes
<script type="math/tex; mode=display">candies[i]</script> satisfy both the left neighbour and the right neighbour criteria.</p>
<p>Again, we need sum up all the elements of the <script type="math/tex; mode=display">candies</script> array to obtain the required result.</p>
<p>
<script type="math/tex; mode=display">
\text{minimum_candies} = \sum_{i=0}^{n-1} candies[i], \text{where } n = \text{length of the ratings array.}
</script>
</p>
<iframe src="https://leetcode.com/playground/U4XtvyuF/shared" frameborder="0" width="100%" height="378" name="U4XtvyuF"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. The array <script type="math/tex; mode=display">candies</script> of size <script type="math/tex; mode=display">n</script> is traversed thrice.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. An array <script type="math/tex; mode=display">candies</script> of size <script type="math/tex; mode=display">n</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-single-pass-approach-with-constant-space">Approach 4: Single Pass Approach with Constant Space</h4>
<p><strong>Algorithm</strong></p>
<p>This approach relies on the observation(as demonstrated in the figure below as well) that in order to distribute the candies as per the given criteria using
the minimum number of candies, the candies are always distributed in terms of increments of 1. Further, while distributing the candies, the local minimum number of candies
given to a student is 1. Thus, the sub-distributions always take the form: <script type="math/tex; mode=display">\text{1, 2, 3, ..., n}</script> or <script type="math/tex; mode=display">\text{n,..., 2, 1}</script>, whose sum is simply given by <script type="math/tex; mode=display">n(n+1)/2</script>.</p>
<p>Now, we can view the given <script type="math/tex; mode=display">rankings</script> as some
rising and falling slopes. Whenever the slope is rising, the distribution takes the form: <script type="math/tex; mode=display">\text{1, 2, 3, ..., m}</script>. Similarly, a falling slope takes the form:
<script type="math/tex; mode=display">\text{k,..., 2, 1}</script>. An issue that arises now is that the local peak point can be included in only one of the slopes.
Whether to include the local peak point(<script type="math/tex; mode=display">\text{n}</script>) in the rising slope or the falling slope?</p>
<p>In order to decide it,
we can observe that in order to satisfy both the right neighbour and the left neighbour criteria, the peak point's count needs to be the max. of the counts determined
by the rising and the falling slopes. Thus, in order to determine the number of candies required, the peak point needs to be included in the slope which contains more
number of points. The local valley point can also be included in only one of the slopes, but this issue can be resolved easily, since the local valley point will
always be assigned a candy count of 1(which can be subtracted from the next slope's count calculations).</p>
<p>Coming to the implementation, we maintain two variables <script type="math/tex; mode=display">old\_slope</script> and <script type="math/tex; mode=display">new\_slope</script> to determine the occurence of a peak or a valley. We also use
<script type="math/tex; mode=display">up</script> and <script type="math/tex; mode=display">down</script> variables to keep a track of the count of elements on the rising slope and on the falling slope respectively(without including the peak element). We always update the total count
of <script type="math/tex; mode=display">candies</script> at the end of a falling slope following a rising slope (or a mountain). The leveling of the points in <script type="math/tex; mode=display">rankings</script> also works as the end of a mountain. At the end of the mountain, we determine whether to include the peak point in the rising slope or in the falling slope by comparing the <script type="math/tex; mode=display">up</script> and <script type="math/tex; mode=display">down</script> variables up to that point. Thus, the count assigned to the peak element becomes: <script type="math/tex; mode=display">\text{max}(up, down) + 1</script>. At this point, we can reset the <script type="math/tex; mode=display">up</script> and <script type="math/tex; mode=display">down</script> variables indicating the start of a new mountain.</p>
<p>The following figure shows the cases that need to be handled for this example:</p>
<p><code>rankings: [1 2 3 4 5 3 2 1 2 6 5 4 3 3 2 1 1 3 3 3 4 2]</code></p>
<p><img alt="Candy_Two_Arrays" src="../Figures/135_Candy_Constant_Space.PNG"></p>
<p>From this figure, we can see that the candy distributions in the subregions always take the form <script type="math/tex; mode=display">\text{1, 2, ...n}</script> or <script type="math/tex; mode=display">\text{n, ..., 2, 1}</script>.
For the first mountain comprised by the regions <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script>, while assigning candies to the local peak point (<script type="math/tex; mode=display">pt. 5</script>), it needs to be included in
<script type="math/tex; mode=display">a</script> to satisfy the left neighbour criteria. The local valley point at the end of region <script type="math/tex; mode=display">b</script> (<script type="math/tex; mode=display">pt. 8</script>) marks the end of the first mountain (region <script type="math/tex; mode=display">c</script>).
 While performing the calculations, we can include this point in either the current or the following mountain. The <script type="math/tex; mode=display">pt. 13</script> marks the end of the second
 mountain due to levelling of the <script type="math/tex; mode=display">pt. 13</script> and <script type="math/tex; mode=display">pt. 14</script>. Since, region <script type="math/tex; mode=display">e</script> has more points than region <script type="math/tex; mode=display">d</script>, the local peak (<script type="math/tex; mode=display">pt. 10</script>) needs to be
 included in region <script type="math/tex; mode=display">e</script> to satisfy the right neighbour criteria. Now, the third mountain <script type="math/tex; mode=display">f</script> can be considered as a mountian with no rising slope (<script type="math/tex; mode=display">up=0</script>)
 but only a falling slope. Similarly, <script type="math/tex; mode=display">pt. 16, 18, 19</script> also act as the mountain ends due to the levelling of the points.</p>
<iframe src="https://leetcode.com/playground/9nSyErSr/shared" frameborder="0" width="100%" height="500" name="9nSyErSr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We traverse the <script type="math/tex; mode=display">rankings</script> array once only.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant Extra Space is used.</p>
</li>
</ul>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-better-brute-force">Approach 2: Better Brute Force</a></li>
<li><a href="#approach-3-searching-intervals">Approach 3: Searching Intervals</a></li>
<li><a href="#approach-4-stack">Approach 4: Stack</a></li>
<li><a href="#approach-5-binary-search">Approach 5: Binary Search</a></li>
<li><a href="#approach-6-using-array-as-a-stack">Approach 6: Using Array as a Stack</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p>The simplest solution is to consider every triplet <script type="math/tex; mode=display">(i, j, k)</script> and check if the corresponding numbers satisfy the 132 criteria. If any such triplet is found, we can return a True value. If no such triplet is found, we need to return a False value.</p>
<iframe src="https://leetcode.com/playground/JDN2Lqu5/shared" frameborder="0" width="100%" height="276" name="JDN2Lqu5"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^3)</script>. Three loops are used to consider every possible triplet. Here, <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-brute-force">Approach 2: Better Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>We can improve the last approach to some extent, if we make use of some observations. We can note that for a particular number <script type="math/tex; mode=display">nums[j]</script> chosen as 2nd element in the 132 pattern, if we don't consider <script type="math/tex; mode=display">nums[k]</script>(the 3rd element) for the time being, our job is to find out the first element, <script type="math/tex; mode=display">nums[i]</script>(<script type="math/tex; mode=display">i<j</script>) which is lesser than <script type="math/tex; mode=display">nums[j]</script>. </p>
<p>Now, assume that we have somehow found a <script type="math/tex; mode=display">nums[i],nums[j]</script> pair. Our task now reduces to finding out a <script type="math/tex; mode=display">nums[k]</script>(<script type="math/tex; mode=display">Kk>j>i)</script>, which falls in the range <script type="math/tex; mode=display">(nums[i], nums[j])</script>. Now, to maximize the likelihood of a <script type="math/tex; mode=display">nums[k]</script> falling in this range, we need to increase this range as much as possible. </p>
<p>Since, we started off by fixing a <script type="math/tex; mode=display">nums[j]</script>, the only option in our hand is to choose a minimum value of <script type="math/tex; mode=display">nums[i]</script> given a particular <script type="math/tex; mode=display">nums[j]</script>. Once, this pair <script type="math/tex; mode=display">nums[i],nums[j]</script>, has been found out, we simply need to traverse beyond the index <script type="math/tex; mode=display">j</script> to find if a <script type="math/tex; mode=display">nums[k]</script> exists for this pair satisfying the 132 criteria.</p>
<p>Based on the above observations, while traversing over the <script type="math/tex; mode=display">nums</script> array choosing various values of <script type="math/tex; mode=display">nums[j]</script>, we simultaneously keep a track of the minimum element found so far(excluding <script type="math/tex; mode=display">nums[j]</script>). This minimum element always serves as the <script type="math/tex; mode=display">nums[i]</script> for the current <script type="math/tex; mode=display">nums[j]</script>. Thus, we only need to traverse beyond the <script type="math/tex; mode=display">j^{th}</script> index to check the <script type="math/tex; mode=display">nums[k]</script>'s to determine if any of them satisfies the 132 criteria.</p>
<iframe src="https://leetcode.com/playground/4Wm3egZJ/shared" frameborder="0" width="100%" height="276" name="4Wm3egZJ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. Two loops are used to find the <script type="math/tex; mode=display">nums[j],nums[k]</script> pairs. Here, <script type="math/tex; mode=display">n</script> refers to the size of <script type="math/tex; mode=display">nums</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-searching-intervals">Approach 3: Searching Intervals</h4>
<p><strong>Algorithm</strong></p>
<p>As discussed in the last approach, once we've fixed a <script type="math/tex; mode=display">nums[i],nums[j]</script> pair, we just need to determine a <script type="math/tex; mode=display">nums[k]</script> which falls in the range <script type="math/tex; mode=display">(nums[i],nums[j])</script>. Further, to maximize the likelihood of any arbitrary <script type="math/tex; mode=display">nums[k]</script> falling in this range, we need to try to keep this range as much as possible. But, in the last approach, we tried to work only on <script type="math/tex; mode=display">nums[i]</script>. But, it'll be a better choice, if we can somehow work out on <script type="math/tex; mode=display">nums[j]</script> as well.</p>
<p>To do so, we can look at the given <script type="math/tex; mode=display">nums</script> array in the form of a graph, as shown below:</p>
<p align="center"><img alt="Graph" src="../Figures/456/456_132_Pattern.PNG"></p>
<p>From the above graph, which consists of rising and falling slopes, we know, the best qualifiers to act as the <script type="math/tex; mode=display">nums[i],nums[j]</script> pair,  as discussed above, to maximize the range <script type="math/tex; mode=display">nums[i], nums[j]</script>, at any instant, while traversing the <script type="math/tex; mode=display">nums</script> array, will be the points at the endpoints of a local rising slope. Thus, once we've found such points, we can traverse over the <script type="math/tex; mode=display">nums</script> array to find a <script type="math/tex; mode=display">nums[k]</script> satisfying the given 132 criteria. </p>
<p>To find these points at the ends of a local rising slope, we can traverse over the given <script type="math/tex; mode=display">nums</script> array. While traversing, we can keep a track of the minimum point found after the last peak(<script type="math/tex; mode=display">nums[s]</script>). </p>
<p>Now, whenever we encounter a falling slope, say, at index <script type="math/tex; mode=display">i</script>, we know, that <script type="math/tex; mode=display">nums[i-1]</script> was the endpoint of the last rising slope found. Thus, we can scan over the <script type="math/tex; mode=display">k</script> indices(k&gt;i), to find a 132 pattern.</p>
<p>But, instead of traversing over <script type="math/tex; mode=display">nums</script> to find a <script type="math/tex; mode=display">k</script> satisfying the 132 pattern for every such rising slope, we can store this range <script type="math/tex; mode=display">(nums[s], nums[i-1])</script>(acting as <script type="math/tex; mode=display">(nums[i], nums[j])</script>) in, say an <script type="math/tex; mode=display">intervals</script> array. </p>
<p>While traversing over the <script type="math/tex; mode=display">nums</script> array to check the rising/falling slopes, whenever we find any rising slope, we can keep adding the endpoint pairs to this <script type="math/tex; mode=display">intervals</script> array. At the same time, we can also check if the current element falls in any of the ranges found so far. If so, this element satisfies the 132 criteria for that range. </p>
<p>If no such element is found till the end, we need to return a False value.</p>
<iframe src="https://leetcode.com/playground/dmGBA85A/shared" frameborder="0" width="100%" height="361" name="dmGBA85A"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>. We traverse over the <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> once to find the slopes. But for every element, we also need to traverse over the <script type="math/tex; mode=display">intervals</script> to check if any element falls in any range found so far. This array can contain atmost <script type="math/tex; mode=display">(n/2)</script> pairs, in the case of an alternate increasing-decreasing sequence(worst case e.g.<code>[5 6 4 7 3 8 2 9]</code>). </p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">intervals</script> array can contain atmost <script type="math/tex; mode=display">n/2</script> pairs, in the worst case(alternate increasing-decreasing sequence).
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-stack">Approach 4: Stack</h4>
<p><strong>Algorithm</strong></p>
<p>In Approach 2, we found out <script type="math/tex; mode=display">nums[i]</script> corresponding to a particular <script type="math/tex; mode=display">nums[j]</script> directly without having to consider every pair possible in <script type="math/tex; mode=display">nums</script> to find this <script type="math/tex; mode=display">nums[i],nums[j]</script> pair. If we do some preprocessing, we can make the process of finding a <script type="math/tex; mode=display">nums[k]</script> corresponding to this <script type="math/tex; mode=display">nums[i],nums[j]</script> pair also easy.</p>
<p>The preprocessing required is to just find the best <script type="math/tex; mode=display">nums[i]</script> value corresponding to every <script type="math/tex; mode=display">nums[j]</script> value. This is done in the same manner as in the second approach i.e. we find the minimum element found till the <script type="math/tex; mode=display">j^{th}</script> element which acts as the <script type="math/tex; mode=display">nums[i]</script> for the current <script type="math/tex; mode=display">nums[j]</script>. We maintain thes values in a <script type="math/tex; mode=display">min</script> array. Thus, <script type="math/tex; mode=display">min[j]</script> now refers to the best <script type="math/tex; mode=display">nums[i]</script> value for a particular <script type="math/tex; mode=display">nums[j]</script>. </p>
<p>Now, we traverse back from the end of the <script type="math/tex; mode=display">nums</script> array to find the <script type="math/tex; mode=display">nums[k]</script>'s. Suppose, we keep a track of the <script type="math/tex; mode=display">nums[k]</script> values which can potentially satisfy the 132 criteria for the current <script type="math/tex; mode=display">nums[j]</script>. We know, one of the conditions to be satisfied by such a <script type="math/tex; mode=display">nums[k]</script> is that it must be greater than <script type="math/tex; mode=display">nums[i]</script>. Or in other words, we can also say that it must be greater than <script type="math/tex; mode=display">min[j]</script> for a particular <script type="math/tex; mode=display">nums[j]</script> chosen. </p>
<p>Once it is ensured that the elements left for competing for the <script type="math/tex; mode=display">nums[k]</script> are all greater than <script type="math/tex; mode=display">min[j]</script>(or <script type="math/tex; mode=display">nums[i]</script>), our only task is to ensure that it should be lesser than <script type="math/tex; mode=display">nums[j]</script>. Now, the best element from among the competitors, for satisfying this condition will be the minimum one from out of these elements. </p>
<p>If this element, <script type="math/tex; mode=display">nums[min]</script> satisfies <script type="math/tex; mode=display">nums[min] < nums[j]</script>, we've found a 132 pattern. If not, no other element will satisfy this criteria, since they are all greater than or equal to <script type="math/tex; mode=display">nums[min]</script> and thus greater than or equal to <script type="math/tex; mode=display">nums[j]</script> as well.</p>
<p>To keep a track of these potential <script type="math/tex; mode=display">nums[k]</script> values for a particular <script type="math/tex; mode=display">nums[i],nums[j]</script> considered currently, we maintain a <script type="math/tex; mode=display">stack</script> on which these potential <script type="math/tex; mode=display">nums[k]</script>'s satisfying the 132 criteria lie in a descending order(minimum element on the top). We need not sort these elements on the <script type="math/tex; mode=display">stack</script>, but they'll be sorted automatically as we'll discuss along with the process.</p>
<p>After creating a <script type="math/tex; mode=display">min</script> array, we start traversing the <script type="math/tex; mode=display">nums[j]</script> array in a backward manner. Let's say, we are currently at the <script type="math/tex; mode=display">j^{th}</script> element and let's also assume that the <script type="math/tex; mode=display">stack</script> is sorted right now. Now, firstly, we check if <script type="math/tex; mode=display">nums[j] > min[j]</script>. If not, we continue with the <script type="math/tex; mode=display">(j-1)^{th}</script> element and the <script type="math/tex; mode=display">stack</script> remains sorted. If not, we keep on popping the elements from the top of the <script type="math/tex; mode=display">stack</script> till we find an element, <script type="math/tex; mode=display">stack[top]</script> such that, <script type="math/tex; mode=display">stack[top] > min[j]</script>(or <script type="math/tex; mode=display">stack[top] > nums[i]</script>). </p>
<p>Once the popping is done, we're sure that all the elements pending on the <script type="math/tex; mode=display">stack</script> are greater than <script type="math/tex; mode=display">nums[i]</script> and are thus, the potential candidates for <script type="math/tex; mode=display">nums[k]</script> satisfying the 132 criteria. We can also note that the elements which have been popped from the <script type="math/tex; mode=display">stack</script>, all satisfy <script type="math/tex; mode=display">stack[top] &leq; min[j]</script>. </p>
<p>Since, in the <script type="math/tex; mode=display">min</script> array, <script type="math/tex; mode=display">min[p] &leq; min[q]</script>, for every <script type="math/tex; mode=display">p > q</script>, these popped elements also satisfy <script type="math/tex; mode=display">stack[top] &leq; min[k]</script>, for all <script type="math/tex; mode=display">0 &leq; k < j</script>. Thus, they are not the potential <script type="math/tex; mode=display">nums[k]</script> candidates for even the preceding elements. Even after  doing the popping, the <script type="math/tex; mode=display">stack</script> remains sorted.</p>
<p>After the popping is done, we've got the minimum element from amongst all the potential <script type="math/tex; mode=display">nums[k]</script>'s on the top of the <script type="math/tex; mode=display">stack</script>(as per the assumption). We can check if it is greater than <script type="math/tex; mode=display">nums[j]</script> to satisfy the 132 criteria(we've already checked <script type="math/tex; mode=display">stack[top] > nums[i]</script>). If this element satisfies the 132 criteria, we can return a True value. If not, we know that for the current <script type="math/tex; mode=display">j</script>, <script type="math/tex; mode=display">nums[j] > min[j]</script>. Thus, the element <script type="math/tex; mode=display">nums[j]</script> could be a potential <script type="math/tex; mode=display">nums[k]</script> value, for the preceding <script type="math/tex; mode=display">nums[i]'s</script>. </p>
<p>Thus, we push it over the <script type="math/tex; mode=display">stack</script>. We can note that, we need to push this element <script type="math/tex; mode=display">nums[j]</script> on the <script type="math/tex; mode=display">stack</script> only when it didn't satisfy <script type="math/tex; mode=display">stack[top]<nums[j]</script>. Thus, <script type="math/tex; mode=display">nums[j] &leq; stack[top]</script>. Thus, even after pushing this element on the <script type="math/tex; mode=display">stack</script>, the <script type="math/tex; mode=display">stack</script> remains sorted. Thus, we've seen by induction, that the <script type="math/tex; mode=display">stack</script> always remains sorted.</p>
<p>Also, note that in case <script type="math/tex; mode=display">nums[j] &leq; min[j]</script>, we don't push <script type="math/tex; mode=display">nums[j]</script> onto the <script type="math/tex; mode=display">stack</script>. This is because this <script type="math/tex; mode=display">nums[j]</script> isn't greater than even the minimum element lying towards its left and thus can't act as <script type="math/tex; mode=display">nums[k]</script> in the future.</p>
<p>If no element is found satisfying the 132 criteria till reaching the first element, we return a False value.</p>
<p>The following animation better illustrates the process.</p>
<p>!?!../Documents/456_132_Pattern.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/Jhct8Fg6/shared" frameborder="0" width="100%" height="412" name="Jhct8Fg6"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We travesre over the <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> once to fill the <script type="math/tex; mode=display">min</script> array. After this, we traverse over <script type="math/tex; mode=display">nums</script> to find the <script type="math/tex; mode=display">nums[k]</script>. During this process, we also push and pop the elements on the <script type="math/tex; mode=display">stack</script>. But, we can note that atmost <script type="math/tex; mode=display">n</script> elements can be pushed and popped off the <script type="math/tex; mode=display">stack</script> in total. Thus, the second traversal requires only <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The <script type="math/tex; mode=display">stack</script> can grow upto a maximum depth of <script type="math/tex; mode=display">n</script>. Furhter, <script type="math/tex; mode=display">min</script> array of size <script type="math/tex; mode=display">n</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-binary-search">Approach 5: Binary Search</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we've made use of a separate <script type="math/tex; mode=display">stack</script> to push and pop the <script type="math/tex; mode=display">nums[k]</script>'s. But, we can also note that when we reach the index <script type="math/tex; mode=display">j</script> while scanning backwards for finding <script type="math/tex; mode=display">nums[k]</script>, the <script type="math/tex; mode=display">stack</script> can contain atmost <script type="math/tex; mode=display">n-j-1</script> elements. Here, <script type="math/tex; mode=display">n</script> refers to the number of elements in <script type="math/tex; mode=display">nums</script> array. </p>
<p>We can also note that this is the same number of elements which lie beyond the <script type="math/tex; mode=display">j^{th}</script> index in <script type="math/tex; mode=display">nums</script> array. We also know that these elements lying beyond the <script type="math/tex; mode=display">j^{th}</script> index won't be needed in the future ever again. Thus, we can make use of this space in <script type="math/tex; mode=display">nums</script> array instead of using a separate <script type="math/tex; mode=display">stack</script>. The rest of the process can be carried on in the same manner as discussed in the last approach.</p>
<p>We can try to go for another optimization here. Since, we've got an array for storing the potential <script type="math/tex; mode=display">nums[k]</script> values now, we need not do the popping process for a <script type="math/tex; mode=display">min[j]</script> to find an element just larger than <script type="math/tex; mode=display">min[j]</script> from amongst these potential values. </p>
<p>Instead, we can make use of Binary Search to directly find an element, which is just larger than <script type="math/tex; mode=display">min[j]</script> in the required interval, if it exists. If such an element is found, we can compare it with <script type="math/tex; mode=display">nums[j]</script> to check the 132 criteria. Otherwise, we continue the process as in the last approach.</p>
<iframe src="https://leetcode.com/playground/mRqb3CLz/shared" frameborder="0" width="100%" height="412" name="mRqb3CLz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(n \log n\big)</script>. Filling <script type="math/tex; mode=display">min</script> array requires <script type="math/tex; mode=display">O(n)</script> time. The second traversal is done over the whole <script type="math/tex; mode=display">nums</script> array of length <script type="math/tex; mode=display">n</script>. For every current <script type="math/tex; mode=display">nums[j]</script> we need to do the Binary Search, which requires <script type="math/tex; mode=display">O\big(\log n\big)</script>. In the worst case, this Binary Search will be done for all the <script type="math/tex; mode=display">n</script> elements, and the required element won't be found in any case, leading to a complexity of <script type="math/tex; mode=display">O\big(n \log n\big)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">min</script> array of size <script type="math/tex; mode=display">n</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-6-using-array-as-a-stack">Approach 6: Using Array as a Stack</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we've seen that in the worst case, the required element won't be found for all the <script type="math/tex; mode=display">n</script> elements and thus Binary Search is done at every step increasing the time complexity. </p>
<p>To remove this problem, we can follow the same steps as in Approach 4 i.e. We can remove those elements(update the index <script type="math/tex; mode=display">k</script>) which aren't greater than <script type="math/tex; mode=display">nums[i]</script>(<script type="math/tex; mode=display">min[j]</script>). Thus, in case no element is larger than <script type="math/tex; mode=display">min[j]</script> the index <script type="math/tex; mode=display">k</script> reaches the last element. </p>
<p>Now, at every step, only <script type="math/tex; mode=display">nums[j]</script> will be added and removed from consideration in the next step, improving the time complexity in the worst case. The rest of the method remains the same as in Approach 4.</p>
<p>This approach is inspired by <a href="https://leetcode.com/fun4leetcode/">@fun4leetcode</a></p>
<iframe src="https://leetcode.com/playground/KZaQNZbi/shared" frameborder="0" width="100%" height="395" name="KZaQNZbi"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We travesre over the <script type="math/tex; mode=display">nums</script> array of size <script type="math/tex; mode=display">n</script> once to fill the <script type="math/tex; mode=display">min</script> array. After this, we traverse over <script type="math/tex; mode=display">nums</script> to find the <script type="math/tex; mode=display">nums[k]</script>. Atmost <script type="math/tex; mode=display">n</script> elements can be put in and out of the <script type="math/tex; mode=display">nums</script> array in total. Thus, the second traversal requires only <script type="math/tex; mode=display">O(n)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">min</script> array of size <script type="math/tex; mode=display">n</script> is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-hashmap-accepted">Approach #1 Using HashMap [Accepted]</a></li>
<li><a href="#approach-2-without-using-hashmap-accepted">Approach #2 Without Using HashMap [Accepted]</a></li>
<li><a href="#approach-3-using-hashmap-linear-accepted">Approach #3 Using HashMap (linear) [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-hashmap-accepted">Approach #1 Using HashMap [Accepted]</h4>
<p>In this approach, we compare every string in <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script> by traversing over the whole list <script type="math/tex; mode=display">list2</script> for every string chosen from <script type="math/tex; mode=display">list1</script>. We make use of a hashmap <script type="math/tex; mode=display">map</script>, which contains elements of the form <script type="math/tex; mode=display">(sum : list_{sum})</script>. Here, <script type="math/tex; mode=display">sum</script> refers to the sum of indices of matching elements and <script type="math/tex; mode=display">list_{sum}</script> refers to the list of matching strings whose indices' sum equals <script type="math/tex; mode=display">sum</script>. </p>
<p>Thus, while doing the comparisons, whenever a match between a string at <script type="math/tex; mode=display">i^{th}</script> index of <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">j^{th}</script> index of <script type="math/tex; mode=display">list2</script> is found, we make an entry in the <script type="math/tex; mode=display">map</script> corresponding to the sum <script type="math/tex; mode=display">i + j</script>, if this entry isn't already present. If an entry with this sum already exists, we need to keep a track of all the strings which lead to the same index sum. Thus, we append the current string to the list of strings corresponding to sum <script type="math/tex; mode=display">i + j</script>.</p>
<p>At the end, we traverse over the keys of the <script type="math/tex; mode=display">map</script> and find out the list of strings corresponding to the key reprsenting the minimum sum.</p>
<iframe src="https://leetcode.com/playground/Rxg7wbHW/shared" frameborder="0" name="Rxg7wbHW" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(l_1*l_2*x)</script>. Every item of <script type="math/tex; mode=display">list1</script> is compared with all the items of <script type="math/tex; mode=display">list2</script>. <script type="math/tex; mode=display">l_1</script> and <script type="math/tex; mode=display">l_2</script> are the lengths of <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script> respectively. And <script type="math/tex; mode=display">x</script> refers to average string length.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(l_1*l_2*x)</script>. In worst case all items of <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script> are same. In that case, hashmap size grows upto <script type="math/tex; mode=display">l_1*l_2*x</script>, where <script type="math/tex; mode=display">x</script> refers to average string length.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-without-using-hashmap-accepted">Approach #2 Without Using HashMap [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Another method could be to traverse over the various <script type="math/tex; mode=display">sum</script>(index sum) values and determine if any such string exists in <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script> such that the sum of its indices in the two lists equals <script type="math/tex; mode=display">sum</script>. </p>
<p>Now, we know that the value of index sum, <script type="math/tex; mode=display">sum</script> could range from 0 to <script type="math/tex; mode=display">m + n - 1</script>. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the length of lists <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script> respectively. Thus, we choose every value of <script type="math/tex; mode=display">sum</script> in ascending order. For every <script type="math/tex; mode=display">sum</script> chosen, we iterate over <script type="math/tex; mode=display">list1</script>. Suppose, currently the string at <script type="math/tex; mode=display">i^{th}</script> index in <script type="math/tex; mode=display">list1</script> is being considered. Now, in order for the index sum <script type="math/tex; mode=display">sum</script> to be the one corresponding to matching strings in <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script>, the string at index <script type="math/tex; mode=display">j</script> in <script type="math/tex; mode=display">list2</script> should match the string at index <script type="math/tex; mode=display">i</script> in <script type="math/tex; mode=display">list1</script>, such that <script type="math/tex; mode=display">sum = i + j</script>.</p>
<p>Or, stating in other terms, the string at index <script type="math/tex; mode=display">j</script> in <script type="math/tex; mode=display">list2</script> should be equal to the string at index <script type="math/tex; mode=display">i</script> in <script type="math/tex; mode=display">list1</script>, such that <script type="math/tex; mode=display">j = sum - i</script>. Thus, for a particular <script type="math/tex; mode=display">sum</script> and <script type="math/tex; mode=display">i</script>(from <script type="math/tex; mode=display">list1</script>), we can directly determine that we need to check the element at index <script type="math/tex; mode=display"> j= sum - i</script> in <script type="math/tex; mode=display">list2</script>, instead of traversing over the whole <script type="math/tex; mode=display">list2</script>. </p>
<p>Doing such checks/comparisons, iterate over all the indices of <script type="math/tex; mode=display">list1</script> for every <script type="math/tex; mode=display">sum</script> value chosen. Whenver a match occurs between <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script>, we put the matching string in a list <script type="math/tex; mode=display">res</script>. </p>
<p>We do the same process of checking the strings for all the  values of <script type="math/tex; mode=display">sum</script> in ascending order. After completing every iteration over <script type="math/tex; mode=display">list1</script> for a particular <script type="math/tex; mode=display">sum</script>, we check if the <script type="math/tex; mode=display">res</script> list is empty or not. If it is empty, we need to continue the process with the next <script type="math/tex; mode=display">sum</script> value considered. If not, the current <script type="math/tex; mode=display">res</script> gives the required list with minimum index sum. This is because we are already considering the index sum values in ascending order. So, the first list to be found is the required resultant list.</p>
<p>The following example depicts the process:</p>
<p>!?!../Documents/599_Min_Index_Sum.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/HhLorCYq/shared" frameborder="0" name="HhLorCYq" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O((l_1+l_2)^2*x)</script>. There are two nested loops upto <script type="math/tex; mode=display">l_1+l_2</script> and string comparison takes <script type="math/tex; mode=display">x</script> time. Here, <script type="math/tex; mode=display">x</script> refers to the average string length.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(r*x)</script>. <script type="math/tex; mode=display">res</script> list is used to store the result. Assuming <script type="math/tex; mode=display">r</script> is the length of <script type="math/tex; mode=display">res</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-hashmap-linear-accepted">Approach #3 Using HashMap (linear) [Accepted]</h4>
<p>We make use of a HashMap to solve the given problem in a different way in this approach. Firstly, we traverse over the whole <script type="math/tex; mode=display">list1</script> and create an entry for each element of <script type="math/tex; mode=display">list1</script> in a HashMap <script type="math/tex; mode=display">map</script>, of the form <script type="math/tex; mode=display">(list[i], i)</script>. Here, <script type="math/tex; mode=display">i</script> refers to the index of the <script type="math/tex; mode=display">i^{th}</script> element, and <script type="math/tex; mode=display">list[i]</script> is the <script type="math/tex; mode=display">i^{th}</script> element itself. Thus, we create a mapping from the elements of <script type="math/tex; mode=display">list1</script> to their indices.</p>
<p>Now, we traverse over <script type="math/tex; mode=display">list2</script>. For every element ,<script type="math/tex; mode=display">list2[j]</script>, of <script type="math/tex; mode=display">list2</script> encountered, we check if the same element already exists as a key in the <script type="math/tex; mode=display">map</script>. If so, it means that the element exists in both <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script>. Thus, we find out the sum of indices corresponding to this element in the two lists, given by <script type="math/tex; mode=display">sum = map.get(list[j]) + j</script>. If this <script type="math/tex; mode=display">sum</script> is lesser than the minimum sum  obtained till now, we update the resultant list to be returned, <script type="math/tex; mode=display">res</script>, with the element <script type="math/tex; mode=display">list2[j]</script> as the only entry in it. </p>
<p>If the <script type="math/tex; mode=display">sum</script> is equal to the minimum sum obtained till now, we put an extra entry corresponding to the element <script type="math/tex; mode=display">list2[j]</script> in the <script type="math/tex; mode=display">res</script> list.</p>
<p>Below code is inspired by <a href="https://leetcode.com/cloud.runner">@cloud.runner</a></p>
<iframe src="https://leetcode.com/playground/FatTyfy6/shared" frameborder="0" name="FatTyfy6" width="100%" height="411"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(l_1+l_2)</script>. Every item of <script type="math/tex; mode=display">list2</script> is checked in a map of <script type="math/tex; mode=display">list1</script>. <script type="math/tex; mode=display">l_1</script> and <script type="math/tex; mode=display">l_2</script> are the lengths of <script type="math/tex; mode=display">list1</script> and <script type="math/tex; mode=display">list2</script> respectively.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(l_1*x)</script>. hashmap size grows upto <script type="math/tex; mode=display">l_1*x</script>, where <script type="math/tex; mode=display">x</script> refers to average string length.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
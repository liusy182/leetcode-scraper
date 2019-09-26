<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute force</a></li>
<li><a href="#approach-2-dynamic-programming">Approach 2: Dynamic Programming</a></li>
<li><a href="#approach-3-using-stacks">Approach 3: Using stacks</a></li>
<li><a href="#approach-4-using-2-pointers">Approach 4: Using 2 pointers</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute force</h4>
<p><strong>Intuition</strong></p>
<p>Do as directed in question. For each element in the array, we find the maximum level of water it can trap after the rain, which is equal to the minimum of maximum height of bars on both the sides minus its own height.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize <script type="math/tex; mode=display">ans=0</script>
</li>
<li>Iterate the array from left to right:</li>
<li>Initialize <script type="math/tex; mode=display">\text{max\_left}=0</script> and <script type="math/tex; mode=display">\text{max\_right}=0</script>
</li>
<li>Iterate from the current element to the beginning of array updating:<ul>
<li>
<script type="math/tex; mode=display">\text{max\_left}=\max(\text{max\_left},\text{height}[j])</script>
</li>
</ul>
</li>
<li>Iterate from the current element to the end of array updating:<ul>
<li>
<script type="math/tex; mode=display">\text{max\_right}=\max(\text{max\_right},\text{height}[j])</script>
</li>
</ul>
</li>
<li>Add <script type="math/tex; mode=display">\min(\text{max\_left},\text{max\_right}) - \text{height}[i]</script> to <script type="math/tex; mode=display">\text{ans}</script>
</li>
</ul>
<iframe src="https://leetcode.com/playground/jHmznzhx/shared" frameborder="0" width="100%" height="0" name="jHmznzhx"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n^2)</script>. For each element of array, we iterate the left and right parts.</p>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(1)</script> extra space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-dynamic-programming">Approach 2: Dynamic Programming</h4>
<p><strong>Intuition</strong></p>
<p>In brute force, we iterate over the left and right parts again and again just to find the highest bar size upto that index. But, this could be stored. Voila, dynamic programming.</p>
<p>The concept is illustrated as shown:</p>
<p align="center"><img alt="Dynamic programming" src="../Figures/42/trapping_rain_water.png" width="500px"></p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Find maximum height of bar from the left end upto an index i in the array <script type="math/tex; mode=display">\text{left\_max}</script>.</li>
<li>Find maximum height of bar from the right end upto an index i in the array <script type="math/tex; mode=display">\text{right\_max}</script>.</li>
<li>Iterate over the <script type="math/tex; mode=display">\text{height}</script> array and update ans:<ul>
<li>Add <script type="math/tex; mode=display">\min(\text{max\_left}[i],\text{max\_right}[i]) - \text{height}[i]</script> to <script type="math/tex; mode=display">ans</script>
</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/QhhbiHR9/shared" frameborder="0" width="100%" height="395" name="QhhbiHR9"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>
<p>Time complexity: <script type="math/tex; mode=display">O(n)</script>.</p>
<ul>
<li>We store the maximum heights upto a point using 2 iterations of <script type="math/tex; mode=display">O(n)</script> each.</li>
<li>We finally update <script type="math/tex; mode=display">\text{ans}</script> using the stored values in <script type="math/tex; mode=display">O(n)</script>.</li>
</ul>
</li>
<li>
<p>Space complexity: <script type="math/tex; mode=display">O(n)</script> extra space.</p>
<ul>
<li>Additional <script type="math/tex; mode=display">O(n)</script> space for <script type="math/tex; mode=display">\text{left\_max}</script> and <script type="math/tex; mode=display">\text{right\_max}</script> arrays than in <a href="#approach-1-brute-force">Approach 1</a>.
<br>
<br></li>
</ul>
</li>
</ul>
<hr>
<h4 id="approach-3-using-stacks">Approach 3: Using stacks</h4>
<p><strong>Intuition</strong></p>
<p>Instead of storing the largest bar upto an index as in <a href="#approach-2-dynamic-programming">Approach 2</a>, we can use stack to keep track of the bars that are bounded by longer bars and hence, may store water. Using the stack, we can do the calculations in only one iteration.</p>
<p>We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to <script type="math/tex; mode=display">\text{ans}</script>.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Use stack to store the indices of the bars.</li>
<li>Iterate the array:<ul>
<li>While stack is not empty and <script type="math/tex; mode=display">\text{height}[current]>\text{height}[st.top()]</script>
<ul>
<li>It means that the stack element can be popped. Pop the top element as <script type="math/tex; mode=display">\text{top}</script>.</li>
<li>Find the distance between the current element and the element at top of stack, which is to be filled.
<script type="math/tex; mode=display">\text{distance} = \text{current} - \text{st.top}() - 1</script>
</li>
<li>Find the bounded height
<script type="math/tex; mode=display">\text{bounded\_height} = \min(\text{height[current]}, \text{height[st.top()]}) - \text{height[top]}</script>
</li>
<li>Add resulting trapped water to answer <script type="math/tex; mode=display">\text{ans} \mathrel{+}= \text{distance} \times \text{bounded\_height}</script>
</li>
</ul>
</li>
<li>Push current index to top of the stack</li>
<li>Move <script type="math/tex; mode=display">\text{current}</script> to the next position</li>
</ul>
</li>
</ul>
<iframe src="https://leetcode.com/playground/LnhnH382/shared" frameborder="0" width="100%" height="361" name="LnhnH382"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n)</script>.<ul>
<li>Single iteration of <script type="math/tex; mode=display">O(n)</script> in which each bar can be touched at most twice(due to  insertion and deletion from stack) and insertion and deletion from stack takes <script type="math/tex; mode=display">O(1)</script> time.</li>
</ul>
</li>
<li>Space complexity: <script type="math/tex; mode=display">O(n)</script>. Stack can take upto <script type="math/tex; mode=display">O(n)</script> space in case of stairs-like or flat structure.
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-4-using-2-pointers">Approach 4: Using 2 pointers</h4>
<p><strong>Intuition</strong></p>
<p>As in <a href="#approach-2-dynamic-programming">Approach 2</a>, instead of computing the left and right parts seperately, we may think of some way to do it in one iteration.
From the figure in dynamic programming approach, notice that as long as <script type="math/tex; mode=display">\text{right\_max}[i]>\text{left\_max}[i]</script> (from element 0 to 6), the water trapped depends upon the left_max, and similar is the case when <script type="math/tex; mode=display">\text{left\_max}[i]>\text{right\_max}[i]</script> (from element 8 to 11).
So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).
We must maintain <script type="math/tex; mode=display">\text{left\_max}</script> and <script type="math/tex; mode=display">\text{right\_max}</script> during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.</p>
<p><strong>Algorithm</strong></p>
<ul>
<li>Initialize <script type="math/tex; mode=display">\text{left}</script> pointer to 0 and <script type="math/tex; mode=display">\text{right}</script> pointer to size-1</li>
<li>While <script type="math/tex; mode=display">\text{left}< \text{right}</script>, do:<ul>
<li>If <script type="math/tex; mode=display">\text{height[left]}</script> is smaller than <script type="math/tex; mode=display">\text{height[right]}</script>
<ul>
<li>If <script type="math/tex; mode=display">\text{height[left]} \geq \text{left\_max}</script>, update <script type="math/tex; mode=display">\text{left\_max}</script>
</li>
<li>Else add <script type="math/tex; mode=display">\text{left\_max}-\text{height[left]}</script> to <script type="math/tex; mode=display">\text{ans}</script>
</li>
<li>Add 1 to <script type="math/tex; mode=display">\text{left}</script>.</li>
</ul>
</li>
<li>Else<ul>
<li>If <script type="math/tex; mode=display">\text{height[right]} \geq \text{right\_max}</script>, update <script type="math/tex; mode=display">\text{right\_max}</script>
</li>
<li>Else add <script type="math/tex; mode=display">\text{right\_max}-\text{height[right]}</script> to <script type="math/tex; mode=display">\text{ans}</script>
</li>
<li>Subtract 1 from <script type="math/tex; mode=display">\text{right}</script>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>Refer the example for better understanding:
!?!../Documents/42/42_trapping_rain_water.json:1000,662!?!</p>
<iframe src="https://leetcode.com/playground/oPWsbm9Q/shared" frameborder="0" width="100%" height="344" name="oPWsbm9Q"></iframe>

<p><strong>Complexity analysis</strong></p>
<ul>
<li>Time complexity: <script type="math/tex; mode=display">O(n)</script>. Single iteration of <script type="math/tex; mode=display">O(n)</script>.</li>
<li>Space complexity: <script type="math/tex; mode=display">O(1)</script> extra space. Only constant space required for <script type="math/tex; mode=display">\text{left}</script>, <script type="math/tex; mode=display">\text{right}</script>, <script type="math/tex; mode=display">\text{left\_max}</script> and <script type="math/tex; mode=display">\text{right\_max}</script>.</li>
</ul>
          </div>
        
      </div>
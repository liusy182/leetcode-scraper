<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-brute-force">Approach 1: Brute Force</a></li>
<li><a href="#approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</a></li>
<li><a href="#approach-3-iterative-solution">Approach 3: Iterative Solution</a></li>
<li><a href="#approach-4-optimized-iterative">Approach 4: Optimized Iterative</a></li>
<li><a href="#approach-5-extra-list">Approach 5: Extra List</a></li>
<li><a href="#approach-6-priority-queue">Approach 6: Priority Queue</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-brute-force">Approach 1: Brute Force</h4>
<p><strong>Algorithm</strong></p>
<p>The most naive solution will be to consider every possible permutation of the given courses and to try to take as much courses as possible by  taking the courses in a serial order in every permutation. We can find out the maximum number of courses that can be taken from out of values obtained from these permutations.</p>
<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big((n+1)!\big)</script>. A total of <script type="math/tex; mode=display">n!</script> permutations are possible for the <script type="math/tex; mode=display">courses</script> array of length <script type="math/tex; mode=display">n</script>. For every permutation, we scan over the <script type="math/tex; mode=display">n</script> elements of the permutation to find the number of courses that can be taken in each case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Each permutation needs <script type="math/tex; mode=display">n</script> space.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-recursion-with-memoization">Approach 2: Recursion with Memoization</h4>
<p><strong>Algorithm</strong></p>
<p>Before we move on to the better approaches, let's discuss one basic idea to solve the given problem. Suppose, we are considering only two courses <script type="math/tex; mode=display">(a,x)</script> and <script type="math/tex; mode=display">(b,y)</script>. Let's assume <script type="math/tex; mode=display">y>x</script>. Now, we'll look at the various relative values which <script type="math/tex; mode=display">a</script> and <script type="math/tex; mode=display">b</script> can take, and which course should be taken first in each of these cases. In all the cases, we assume that the course's duration is always lesser than its end day i.e. <script type="math/tex; mode=display">a<x</script> and <script type="math/tex; mode=display">b<y</script>.</p>
<ol>
<li>
<script type="math/tex; mode=display">(a+b) &le; x</script>: In this case, we can take the courses in any order. Both the courses can be taken irrespective of the order in which the courses are taken.</li>
</ol>
<p align="center"><img alt="Courses" src="../Figures/630/630_Course_Schedule_III_1.PNG"></p>
<ol>
<li>
<script type="math/tex; mode=display">(a+b)>x</script>, <script type="math/tex; mode=display">a>b</script>, <script type="math/tex; mode=display">(a+b) &leq; y</script>: In this case, as is evident from the figure, both the courses can be taken only by taking course <script type="math/tex; mode=display">a</script> before <script type="math/tex; mode=display">b</script>.</li>
</ol>
<p align="center"><img alt="Courses" src="../Figures/630/630_Course_Schedule_III_2.PNG"></p>
<ol>
<li>
<script type="math/tex; mode=display">(a+b)>x</script>, <script type="math/tex; mode=display">b>a</script>, <script type="math/tex; mode=display">(a+b) &leq; y</script>: In this case also, both the courses can be taken only by taking course <script type="math/tex; mode=display">a</script> before <script type="math/tex; mode=display">b</script>.</li>
</ol>
<p align="center"><img alt="Courses" src="../Figures/630/630_Course_Schedule_III_3.PNG"></p>
<ol>
<li>
<script type="math/tex; mode=display">(a+b)>y</script>: In this case, irrespective of the order in which we take the courses, only one course can be taken.</li>
</ol>
<p align="center"><img alt="Courses" src="../Figures/630/630_Course_Schedule_III_4.PNG"></p>
<p>From the above example, we can conclude that it is always profitable to take the course with a smaller end day prior to a course with a larger end day. This is because, the course with a smaller duration, if can be taken, can surely be taken only if it is taken prior to a course with a larger end day. </p>
<p>Based on this idea, firstly, we sort the given <script type="math/tex; mode=display">courses</script> array based on their end days. Then, we try to take the courses in a serial order from this sorted <script type="math/tex; mode=display">courses</script> array. </p>
<p>In order to solve the given problem, we make use of a recursive function <code>schedule(courses, i, time)</code> which returns the maximum number of courses that can be taken starting from the <script type="math/tex; mode=display">i^{th}</script> course(starting from 0), given the time aleady consumed by the other courses is <script type="math/tex; mode=display">time</script>, i.e. the current time is <script type="math/tex; mode=display">time</script>, given a <script type="math/tex; mode=display">courses</script> array as the schedule.</p>
<p>Now, in each function call to <code>schedule(courses, i, time)</code>, we try to include the current course in the taken courses. But, this can be done only if <script type="math/tex; mode=display">time + duration_i < end\_day_i</script>. Here, <script type="math/tex; mode=display">duration_i</script> refers to the duration of the <script type="math/tex; mode=display">i^{th}</script> course and <script type="math/tex; mode=display">end\_day_i</script> refers to the end day of the <script type="math/tex; mode=display">i^{th}</script> course. </p>
<p>If the course can be taken, we increment the number of courses taken and obtain the number of courses that can be taken by passing the updated time and courses' index. i.e. we make the function call <code>schedule(courses, i + 1, time + duration_i)</code>. Let's say, we store the number of courses that can be taken by taking the current course in <script type="math/tex; mode=display">taken</script> variable.</p>
<p>Further, for every current course, we also leave the current course, and find the number of courses that can be taken thereof. Now, we need not update the time, but we need to update the courses' index. Thus, we make the function call, <code>schedule(courses, i + 1, time)</code>. Let's say, we store the count obtained in <script type="math/tex; mode=display">not\_taken</script> variable. </p>
<p>While returning the number of courses at the end of each function call, we return the maximum value out of <script type="math/tex; mode=display">taken</script> and <script type="math/tex; mode=display">not\_taken</script>.</p>
<p>Thus, the function call <code>schedule(courses, 0, 0)</code> gives the required result.</p>
<p>In order to remove this redundancy, we make use of a memoization array <script type="math/tex; mode=display">memo</script>, such that <script type="math/tex; mode=display">memo[i][j]</script> is used to store the result of the function call <code>schedule(courses, i, time)</code>. Thus, whenever the same function call is made again, we can return the result directly from the <script type="math/tex; mode=display">memo</script> array. This helps to prune the search space to a great extent.</p>
<iframe src="https://leetcode.com/playground/cYQzzELZ/shared" frameborder="0" width="100%" height="378" name="cYQzzELZ"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n*d)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">d</script> is filled once. Here, <script type="math/tex; mode=display">n</script> refers to the number of courses in the given <script type="math/tex; mode=display">courses</script> array and <script type="math/tex; mode=display">d</script> refers to the maximum value of the end day from all the end days in the <script type="math/tex; mode=display">courses</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n*d)</script>. <script type="math/tex; mode=display">memo</script> array of size <script type="math/tex; mode=display">n</script>x<script type="math/tex; mode=display">d</script> is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-3-iterative-solution">Approach 3: Iterative Solution</h4>
<p>For the current approach, the idea goes as follows. As discussed in the previous approaches, we need to sort the given <script type="math/tex; mode=display">courses</script> array based on the end days. Thus, we consider the courses in the ascending order of their end days. We keep a track of the current time in a <script type="math/tex; mode=display">time</script> variable. Along with this, we also keep a track of the number of courses taken till now in <script type="math/tex; mode=display">count</script> variable.</p>
<p>For each course being considered currently(let's say <script type="math/tex; mode=display">i^{th}</script> course), we try to take this course. But, to be able to do so, the current course should end before its corresponding end day i.e. <script type="math/tex; mode=display">time + duration_i &leq; end\day_i</script>. Here, <script type="math/tex; mode=display">duration_i</script> refers to the duration of the <script type="math/tex; mode=display">i^{th}</script> course and <script type="math/tex; mode=display">end\_day_i</script> refers to the end day of the <script type="math/tex; mode=display">i^{th}</script> course. </p>
<p>If this course can be taken, we update the current time to <script type="math/tex; mode=display">time + duration_i</script> and also increment the current <script type="math/tex; mode=display">count</script> value to indicate that one more course has been taken. </p>
<p>But, if we aren't able to take the current course i.e. <script type="math/tex; mode=display">time + duration_i > end\_day_i</script>, we can try to take this course by removing some other course from amongst the courses that have already been taken. But, the current course can fit in by removing some other course, only if the duration of the course(<script type="math/tex; mode=display">j^{th}</script>) being removed <script type="math/tex; mode=display">duration_j</script> is larger than the current course's duration, <script type="math/tex; mode=display">duration_i</script> i.e. <script type="math/tex; mode=display">duration_j > duration_i</script>. </p>
<p>We are sure of the fact that by removing the <script type="math/tex; mode=display">j^{th}</script> course, we can fit in the current course, because, <script type="math/tex; mode=display">course_j</script> was already fitting in the duration available till now. Since, <script type="math/tex; mode=display">duration_i < duration_j</script>, the current course can surely take its place. Thus, we look for a course from amongst the taken courses having a duration larger than the current course.</p>
<p>But why are we doing this replacement? The answer to this question is as follows. By replacing the <script type="math/tex; mode=display">j^{th}</script> course, with the <script type="math/tex; mode=display">i^{th}</script> course of a relatively smaller duration, we can increase the time available for upcoming courses to be taken. An extra <script type="math/tex; mode=display">duration_j - duration_i</script> time can be made available by doing so. </p>
<p>Now, for this saving in time to be maximum, the course taken for the replacement should be the one with the maximum duration. Thus, from amongst the courses that have been taken till now, we find the course having the maximum duration which should be more than the duration of the current course(which can't be taken). </p>
<p>Let's say, this course be called as <script type="math/tex; mode=display">max\_i</script>. Thus, now, a saving of <script type="math/tex; mode=display">duration_{max\_i} - duration_i</script> can be achived, which could help later in fitting in more courses to be taken.</p>
<p>If such a course, <script type="math/tex; mode=display">max\_i</script>, is found, we remove this course from the taken courses and consider the current course as taekn. We also mark this course with <script type="math/tex; mode=display">\text{-1}</script> to indicate that this course has not been taken and should not be considered in the future again for replacement. </p>
<p>But, if such a course isn't found, we can't take the current course at any cost. Thus, we mark the current course with <script type="math/tex; mode=display">\text{-1}</script> to indicate that the current course has not been taken.</p>
<p>At the end, the value of <script type="math/tex; mode=display">count</script> gives the required result.</p>
<p>The following animation illustrates the process.</p>
<p>!?!../Documents/630_Course_Schedule_III.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/25HrpDuj/shared" frameborder="0" width="100%" height="463" name="25HrpDuj"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>.  We iterate over the <script type="math/tex; mode=display">count</script> array of size <script type="math/tex; mode=display">n</script> once. For every element currently considered, we could scan backwards till the first element, giving <script type="math/tex; mode=display">O(n^2)</script> complexity. Sorting the <script type="math/tex; mode=display">count</script> array takes <script type="math/tex; mode=display">O\big(n \log n\big)</script> time for <script type="math/tex; mode=display">count</script> array.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-4-optimized-iterative">Approach 4: Optimized Iterative</h4>
<p>In the last approach, we've seen that, in the case of current course which can't be taken direclty, i.e. for <script type="math/tex; mode=display">time + duration_i > end\_day_i</script>, we need to traverse back in the <script type="math/tex; mode=display">courses</script> array till the beginning to find a course with the maximum duration which is larger than the current course's duration. This backward traversal also goes through the courses which aren't  taken and thus, can't be replaced, and have been marked as <script type="math/tex; mode=display">\text{-1}</script>. </p>
<p>We can bring in some optimization here. For this, we should search among only those courses which have been taken(and not the ones which haven't been taken). </p>
<p>To do so, as we iterate over the <script type="math/tex; mode=display">courses</script> array, we also keep on updating it, such that the first <script type="math/tex; mode=display">count</script> number of elements in this array now correspond to only those <script type="math/tex; mode=display">count</script> number of courses which have been taken till now. </p>
<p>Thus, whenever we update the <script type="math/tex; mode=display">count</script> to indicate that one more course has been taken, we also update the <script type="math/tex; mode=display">courses[count]</script> entry to 
reflect the current course that has just been taken. </p>
<p>Whenever, we find a course for which <script type="math/tex; mode=display">time + duration_i > end\_day_i</script>, we find a <script type="math/tex; mode=display">max_i</script> course from only amongst these first <script type="math/tex; mode=display">count</script> number of courses in the <script type="math/tex; mode=display">courses</script> array, which indicate the courses that have been taken till now. </p>
<p>Also, instead of marking this <script type="math/tex; mode=display">max_i^{th}</script> course with a <script type="math/tex; mode=display">\text{-1}</script>, we can simply replace this course with the current course. Thus, the first <script type="math/tex; mode=display">count</script> courses still reflect the courses that have been taken till now.</p>
<iframe src="https://leetcode.com/playground/A9DLvJuL/shared" frameborder="0" width="100%" height="463" name="A9DLvJuL"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n*count)</script>. We iterate over a total of <script type="math/tex; mode=display">n</script> elements of the <script type="math/tex; mode=display">courses</script> array. For every element, we can traverse backwards upto atmost <script type="math/tex; mode=display">count</script>(final value) number of elements.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant extra space is used.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-5-extra-list">Approach 5: Extra List</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we updated the <script type="math/tex; mode=display">course</script> array itself so that the first <script type="math/tex; mode=display">count</script> elements indicate the <script type="math/tex; mode=display">count</script> number of courses that have been taken till now. If it is required to retain the <script type="math/tex; mode=display">courses</script> array as such, we can do the same job by maintaining a separate list <script type="math/tex; mode=display">valid\_list</script> which is the list of those courses that have been taken till now. </p>
<p>Thus, to find the <script type="math/tex; mode=display">max_i</script> course, we need to search in this list only. Further, when replacing this <script type="math/tex; mode=display">max_i^{th}</script> course with the current course, we can replace this <script type="math/tex; mode=display">max_i</script> course in the list with current course directly. The rest of the method remains the same as the last approach.</p>
<iframe src="https://leetcode.com/playground/QZbbEoDr/shared" frameborder="0" width="100%" height="463" name="QZbbEoDr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n*m)</script>. We iterate over a total of <script type="math/tex; mode=display">n</script> elements of the <script type="math/tex; mode=display">courses</script> array. For every element, we can traverse over atmost <script type="math/tex; mode=display">m</script> number of elements. Here, <script type="math/tex; mode=display">m</script> refers to the final length of the <script type="math/tex; mode=display">valid\_list</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The <script type="math/tex; mode=display">valid\_list</script> can contain atmost <script type="math/tex; mode=display">n</script> courses.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-6-priority-queue">Approach 6: Priority Queue</h4>
<p><strong>Algorithm</strong></p>
<p>This approach is inspired by <a href="https://leetcode.com/stomach_ache">@stomach_ache</a></p>
<p>In the last few approaches, we've seen that we needed to traverse over the courses which have been taken to find the course(with the maximum duration) which can be replaced by the current course(if it can't be taken directly). These traversals can be saved, if we make use of a Priority Queue, <script type="math/tex; mode=display">queue</script>(which is implemented as a Max-Heap) which contains the durations of all the courses that have been taken till now. </p>
<p>The iteration over the sorted <script type="math/tex; mode=display">courses</script> remains the same as in the last approaches. Whenver the current course(<script type="math/tex; mode=display">i^{th}</script> course) can be taken(<script type="math/tex; mode=display">time + duration_i &leq; end\_day_i</script>), it is added to the <script type="math/tex; mode=display">queue</script> and the value of the current time is updated to <script type="math/tex; mode=display">time + duration_i</script>. </p>
<p>If the current course can't be taken directly, as in the previous appraoches, we need to find a course whose duration <script type="math/tex; mode=display">duration_j</script> is maximum from amongst the courses taken till now. Now, since we are maintaing a Max-Heap, <script type="math/tex; mode=display">queue</script>, we can obtain this duration directly from this <script type="math/tex; mode=display">queue</script>. If the duration <script type="math/tex; mode=display">duration_j > duration_i</script>, we can replace the <script type="math/tex; mode=display">j^{th}</script> course, with the current one. </p>
<p>Thus, we remove the <script type="math/tex; mode=display">duration_j</script> from the <script type="math/tex; mode=display">queue</script> and add the current course's duration <script type="math/tex; mode=display">duration_i</script> to the <script type="math/tex; mode=display">queue</script>. We also need to make proper adjustments to the <script type="math/tex; mode=display">time</script> to account for this replacement done.</p>
<p>At the end, the number of elements in the <script type="math/tex; mode=display">queue</script> represent the number of courses that have been taken till now.</p>
<iframe src="https://leetcode.com/playground/sNifxG59/shared" frameborder="0" width="100%" height="344" name="sNifxG59"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(n \log n\big)</script>. At most <script type="math/tex; mode=display">n</script> elements are added to the <script type="math/tex; mode=display">queue</script>. Adding each element is followed by heapification, which takes <script type="math/tex; mode=display">O\big(\log n\big)</script> time.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The <script type="math/tex; mode=display">queue</script> containing the durations of the  courses taken can have atmost <script type="math/tex; mode=display">n</script> elements</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
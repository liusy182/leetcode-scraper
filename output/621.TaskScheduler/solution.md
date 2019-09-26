<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-sorting-accepted">Approach #1 Using Sorting [Accepted]</a></li>
<li><a href="#approach-2-using-priority-queue-accepted">Approach #2 Using Priority-Queue [Accepted]</a></li>
<li><a href="#approach-3-calculating-idle-slots-accepted">Approach #3 Calculating Idle slots [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-sorting-accepted">Approach #1 Using Sorting [Accepted]</h4>
<p>Before we start off with the solution, we can note that the names of the tasks are irrelevant for obtaining the solution of the given problem. The time taken for the tasks to be finished is only dependent on the number of instances of each task and not on the names of tasks. </p>
<p>The first solution that comes to the mind is to consider the tasks to be executed in the descending order of their number of instances. For every task executed, we can keep a track of the time at which this task was executed in order to consider the impact of cooling time in the future. We can execute all the tasks in the descending order of their number of instances and can keep on updating the number of instances pending for each task as well. After one cycle of the task list is executed, we can again start with the first task(largest count of instances) and keep on continuing the process by inserting idle cycles wherever appropriate by considering the last execution time of the task and the cooling time as well. </p>
<p>But, there is a flaw in the above idea. Consider the case, where say the number of instances of tasks A, B, C, D, E  are 6, 1, 1, 1, 1 respectively with n=2(cooling time). If we go by the above method, firstly we give 1 round to each A, B, C, D and E. Now, only 5 instances of A are pending, but each instance will take 3 time units to complete because of cooling time. But a better way to schedule the tasks will be this: A, B, C, A, D, E, ... . In this way, by giving turn to the task A as soon as its cooling time is over, we can save a good number of clock cycles.</p>
<p>From the above example, we are clear with one idea. It is that, the tasks with the currently maximum number of outstanding (pending)instances will contribute to a large number of idle cycles in the future, if not executed with appropriate interleavings with the other tasks. Thus, we need to re-execute such a task as soon as its cooling time is finished. </p>
<p>Thus, based on the above ideas, firstly, we obtain a count of the number of instances of each task in <script type="math/tex; mode=display">map</script> array. Then, we start executing the tasks in the order of descending number of their initial instances. As soon as we execute the first task, we start its cooling timer as well(<script type="math/tex; mode=display">i</script>). For every task executed, we update the pending number of instances of the current task. We update the current time, <script type="math/tex; mode=display">time</script>, at every instant as well. Now, as soon as the timer, <script type="math/tex; mode=display">i</script>'s value exceeds the cooling time, as discussed above, we again need to consider the task with the largest number of pending instances. Thus, we again sort the <script type="math/tex; mode=display">tasks</script> array with updated counts of instances and again pick up the tasks in the descending order of their number of instances. </p>
<p>Now, the task picked up first after the sorting, will either be the first task picked up in the last iteration(which will now be picked after its cooling time has been finished) or the task picked will be the one which lies at <script type="math/tex; mode=display">(n+1)^{th}</script> position in the previous descending <script type="math/tex; mode=display">tasks</script> array. In either of the cases, the cooling time won't cause any conflicts(it has been considered implicitly). Further, the task most critical currently will always be picked up which was the main requirement.</p>
<p>We stop this process, when the pending instances of all the tasks have been reduced to 0. At this moment, <script type="math/tex; mode=display">time</script> gives the required result.</p>
<iframe src="https://leetcode.com/playground/MxzSpcHY/shared" frameborder="0" name="MxzSpcHY" width="100%" height="428"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(time)</script>. Number of iterations will be equal to resultant time <script type="math/tex; mode=display">time</script>. </p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. Constant size array <script type="math/tex; mode=display">map</script> is used.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-using-priority-queue-accepted">Approach #2 Using Priority-Queue [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of making use of sorting as done in the last approach, we can also make use of a Max-Heap(<script type="math/tex; mode=display">queue</script>) to pick the order in which the tasks need to be executed. But we need to ensure that the heapification occurs only after the intervals of cooling time, <script type="math/tex; mode=display">n</script>, as done in the last approach.</p>
<p>To do so, firstly, we put only those elements from <script type="math/tex; mode=display">map</script> into the <script type="math/tex; mode=display">queue</script> which have non-zero number of instances. Then, we start picking up the largest task from the <script type="math/tex; mode=display">queue</script> for current execution. (Again, at every instant, we update the current <script type="math/tex; mode=display">time</script> as well.) We pop this element from the <script type="math/tex; mode=display">queue</script>. We also decrement its pending number of instances and if any more instances of the current task are pending, we store them(count) in a temporary <script type="math/tex; mode=display">temp</script> list, to be added later on back into the <script type="math/tex; mode=display">queue</script>. We keep on doing so, till a cycle of cooling time has been finished. After every such cycle, we add the generated <script type="math/tex; mode=display">temp</script> list back to the <script type="math/tex; mode=display">queue</script> for considering the most critical task again. </p>
<p>We keep on doing so till the <script type="math/tex; mode=display">queue</script>(and <script type="math/tex; mode=display">temp</script>) become totally empty. At this instant, the current value of <script type="math/tex; mode=display">time</script> gives the required result.</p>
<iframe src="https://leetcode.com/playground/cAjn8Sxo/shared" frameborder="0" name="cAjn8Sxo" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. Number of iterations will be equal to resultant time <script type="math/tex; mode=display">time</script>. </p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. <script type="math/tex; mode=display">queue</script> and <script type="math/tex; mode=display">temp</script> size will not exceed O(26).</p>
</li>
</ul>
<hr>
<h4 id="approach-3-calculating-idle-slots-accepted">Approach #3 Calculating Idle slots [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>This approach is inpired by <a href="https://leetcode.com/zhanzq">@zhanzq</a></p>
<p>If we are able to, somehow, determine the number of idle slots(<script type="math/tex; mode=display">idle\_slots</script>), we can find out the time required to execute all the tasks as <script type="math/tex; mode=display">idle\_slots + Total Number Of Tasks</script>. Thus, the idea is to find out the idle time first.</p>
<p>To find the idle time, consider figure 1 below.</p>
<p align="align"><img alt="Tasks" src="../Figures/621_Task_Scheduler_new.PNG"></p>
<p>From this figure, we can observe that the maximum number of idle slots will always be given by the product of the cooling time and the number of instances of the task with maximum count less 1(in case only multiple instances of the same task need to be executed, and each, then, is executed after lapse of every cooling time). The factor of 1 is deducted from the task's count with maximum number of instances, as is clear from the figure, is that in the last round of execution of the tasks, the idle slots need not be considered for insertion following the execution of the related task. Now, based on the count of the instances of the other tasks, we can reduce the number of idle slots from this maximum value, to determine the minimum number of idle slots needed.</p>
<p>To do so, consider figure 2 as shown above. From the figure above, assuming the tasks are executed in row-wise order, we can see that in case the number of instances of another task equal the number of instances of the task with maximum number of instances, the number of idle slots saved is equal to its number of instances less 1 as is clear for the case of task B above. But, if the count of the number of instances, say <script type="math/tex; mode=display">i</script> is lesser than the this maximum value, the number of idle slots saved is equal to the value <script type="math/tex; mode=display">i</script> itself as is clear for the case of task C. Further, we can observe that  for any arbitrary task other than A, B or C with the count of number of instances lesser than C, this task can be easily accomodated into the idle slots or if no more idle slot is available, this task can be appended after every row of tasks without interfering with the cooling time. In the first case, subtracting its number of intances from the number of idle slots leads to obtaining the correct number of available idle slots. In the second case, which will only occur if the number of idle slots pending is already zero, it leads to negative net idle slots, which can later be considered as zero for the purpose of calculations.</p>
<p>Thus, we can easily obtain the number of pending idle slots by subtracting appropriate number of slots from the available ones and at the end, we can obtain the total time required as the sum of pending idle slots and the total number of tasks.</p>
<iframe src="https://leetcode.com/playground/jC8vicao/shared" frameborder="0" name="jC8vicao" width="100%" height="275"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We iterate over <script type="math/tex; mode=display">tasks</script> array only once. (<script type="math/tex; mode=display">O(n)</script>).Sorting <script type="math/tex; mode=display">tasks</script> array of length <script type="math/tex; mode=display">n</script> takes <script type="math/tex; mode=display">O\big(26log(26)\big)= O(1)</script> time. After this, only one iteration over 26 elements of <script type="math/tex; mode=display">map</script> is done(<script type="math/tex; mode=display">O(1)</script>.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script>. <script type="math/tex; mode=display">map</script> array of constant size(26) is used.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
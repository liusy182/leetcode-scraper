<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-stack-time-limit-exceeded">Approach #1 Using Stack [Time Limit Exceeded]</a></li>
<li><a href="#approach-2-better-approach-accepted">Approach #2 Better Approach [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-stack-time-limit-exceeded">Approach #1 Using Stack [Time Limit Exceeded]</h4>
<p>Before starting off with the solution, let's discuss a simple idea. Suppose we have three functions <script type="math/tex; mode=display">func_1</script>, <script type="math/tex; mode=display">func_2</script> and <script type="math/tex; mode=display">func_3</script> such that <script type="math/tex; mode=display">func_1</script> calls <script type="math/tex; mode=display">func_2</script> and then <script type="math/tex; mode=display">func_2</script> calls <script type="math/tex; mode=display">func_3</script>. In this case, <script type="math/tex; mode=display">func_3</script> starts at the end and ends first, <script type="math/tex; mode=display">func_2</script> starts at 2nd position and ends at the 2nd last step. Similarly, <script type="math/tex; mode=display">func_1</script> starts first and ends at the last position. Thus, we can conclude that the function which is entered at the end finishes first and the one which is entered first ends at the last position. </p>
<p>From the above discussion, we can conclude that we can make use of a <script type="math/tex; mode=display">stack</script> to solve the given problem. We can start by pushing the first function's id from the given <script type="math/tex; mode=display">logs</script> list onto the array. We also keep a track of the current <script type="math/tex; mode=display">time</script>. We also make use of a <script type="math/tex; mode=display">res</script> array, such that <script type="math/tex; mode=display">res[i]</script> is to keep a track of the exclusive time spent by the Fucntion with function id <script type="math/tex; mode=display">i</script> till the current time. </p>
<p>Now, we can move on to the next function in <script type="math/tex; mode=display">logs</script>. The start/end time of the next function will obviously be larger than the start time of the function on the <script type="math/tex; mode=display">stack</script>. We keep on incrementing the current <script type="math/tex; mode=display">time</script> and the exclusive time for the function on the top of the <script type="math/tex; mode=display">stack</script> till the current time becomes equal to the start/end time of the next function in the <script type="math/tex; mode=display">logs</script> list. </p>
<p>Thus, now, we've reached a point, where the control shifts from the last function to a new function, due to a function call(indicated by a start label for the next function), or the last function could exit(indicated by the end label for the next function). Thus, we can no longer continue with the same old function. </p>
<p>If the next function includes a start label, we push this function on the top of the <script type="math/tex; mode=display">stack</script>, since the last function would need to be revisited again in the future. On the other hand, if the next function includes an end label, it means the last function on the top of the <script type="math/tex; mode=display">stack</script> is terminating.</p>
<p>We also know that an end label indicates that this function executes till the end of the given time. Thus, we need to increment the current <script type="math/tex; mode=display">time</script> and the exclusive time of the last function as well to account for this fact. Now, we can remove(pop) this function from the <script type="math/tex; mode=display">stack</script>.  We can continue this process for every function in the <script type="math/tex; mode=display">logs</script> list. </p>
<p>At the end, the <script type="math/tex; mode=display">res</script> array gives the exclusive times for each function.</p>
<p>Summarizing the above process, we need to do the following:</p>
<ol>
<li>
<p>Push the function id of the first function in the <script type="math/tex; mode=display">logs</script> list on the <script type="math/tex; mode=display">stack</script>.</p>
</li>
<li>
<p>Keep incrementing the exlusive time(along with the current time) corresponding to the function on the top of the <script type="math/tex; mode=display">stack</script>(in the <script type="math/tex; mode=display">res</script> array), till the current time equals the start/end time corresponding to the next function in the <script type="math/tex; mode=display">logs</script> list.</p>
</li>
<li>
<p>If the next function has a 'start' label, push this function's id onto the stack. Otherwise, increment the last function's exclusive time(along with the current time), and pop the function id from the top of the stack.</p>
</li>
<li>
<p>Repeat steps 2 and 3 till all the functions in the <script type="math/tex; mode=display">logs</script> list have been considered.</p>
</li>
<li>
<p>Return the resultant exlcusive time(<script type="math/tex; mode=display">res</script>).</p>
</li>
</ol>
<iframe src="https://leetcode.com/playground/RqRjdFmv/shared" frameborder="0" name="RqRjdFmv" width="100%" height="496"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(t)</script>. We increment the time till all the functions are done with the execution. Here, <script type="math/tex; mode=display">t</script> refers to the end time of the last function in the <script type="math/tex; mode=display">logs</script> list.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. The <script type="math/tex; mode=display">stack</script> can grow upto a depth of atmost <script type="math/tex; mode=display">n/2</script>. Here, <script type="math/tex; mode=display">n</script> refers to the number of elements in the given <script type="math/tex; mode=display">logs</script> list.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-better-approach-accepted">Approach #2 Better Approach [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, for every function on the top of the <script type="math/tex; mode=display">stack</script>, we incremented the current time and the exclusive time of this same function till the current time became equal to the start/end time of the next function. </p>
<p>Instead of doing this incrementing step by step, we can directly use the difference between the next function's start/stop time and the current function's start/stop time. The rest of the process remains the same as in the last approach. </p>
<p>The following animation illustrates the process.</p>
<p>!?!../Documents/636_Exclusive_Time_of_Functions.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/rZkuT7RU/shared" frameborder="0" name="rZkuT7RU" width="100%" height="462"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n)</script>. We iterate over the entire <script type="math/tex; mode=display">logs</script> array just once. Here, <script type="math/tex; mode=display">n</script> refers to the number of elements in the <script type="math/tex; mode=display">logs</script> list.</p>
</li>
<li>
<p>Space complexity : The <script type="math/tex; mode=display">stack</script> can grow upto a depth of atmost <script type="math/tex; mode=display">n/2</script>. Here, <script type="math/tex; mode=display">n</script> refers to the number of elements in the given <script type="math/tex; mode=display">logs</script> list.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
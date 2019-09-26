<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-queue-accepted">Approach #1 Using queue [Accepted]</a></li>
<li><a href="#approach-2-without-using-extra-space-accepted">Approach #2 Without using extra Space [Accepted]</a></li>
<li><a href="#approach-3-using-division-and-modulus-accepted">Approach #3  Using division and modulus [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-queue-accepted">Approach #1 Using queue [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>The simplest method is to extract all the elements of the given matrix by reading the elements in a row-wise fashion. In this implementation, we use a queue to put the extracted elements. Then, we can take out the elements of the queue formed in a serial order and arrange the elements in the resultant required matrix in a row-by-row order again.</p>
<p>The formation of the resultant matrix won't be possible if the number of elements in the original matrix isn't equal to the number of elements in the resultant matrix.</p>
<iframe src="https://leetcode.com/playground/QiYrHtjz/shared" frameborder="0" name="QiYrHtjz" width="100%" height="428"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. We traverse over <script type="math/tex; mode=display">m*n</script> elements twice. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refer to the number of rows and columns of the given matrix respectively.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. The queue formed will be of size <script type="math/tex; mode=display">m*n</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-without-using-extra-space-accepted">Approach #2 Without using extra Space [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Instead of unnecessarily using the queue as in the brute force approach, we can keep putting the numbers in the resultant matrix directly while iterating over the given matrix in a row-by-row order. While putting the numbers in the resultant array, we fix a particular row and keep on incrementing the column numbers only till we reach the end of the required columns indicated by <script type="math/tex; mode=display">c</script>. At this moment, we update the row index by incrementing it and reset the column index to start from 0 again. Thus, we can save the space consumed by the queue for storing the data that just needs to be copied into a new array.</p>
<iframe src="https://leetcode.com/playground/JvBHJ8mJ/shared" frameborder="0" name="JvBHJ8mJ" width="100%" height="394"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. We traverse the entire matrix of size <script type="math/tex; mode=display">m*n</script> once only. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refers to the number of rows and columns in the given matrix.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. The resultant matrix of size <script type="math/tex; mode=display">m*n</script> is used. </p>
</li>
</ul>
<hr>
<h4 id="approach-3-using-division-and-modulus-accepted">Approach #3  Using division and modulus [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we needed to keep a track of when we reached the end of columns for the resultant matrix and needed to update the current row and column number for putting the extracted elements by checking the current indices every time. Instead of doing these limit checks at every step, we can make use of maths to help ease the situation. </p>
<p>The idea behind this approach is as follows. Do you know how a 2-D array is stored in the main memory(which is 1-D  in nature)? It is internally represented as a 1-D array only. The element <script type="math/tex; mode=display">nums[i][j]</script> of <script type="math/tex; mode=display">nums</script> array is represented in the form of a one dimensional array by using the index in the form: <script type="math/tex; mode=display">nums[n*i + j]</script>, where <script type="math/tex; mode=display">m</script> is the number of columns in the given matrix. Looking at the same in the reverse order, while putting the elements in the elements in the resultant matrix, we can make use of a <script type="math/tex; mode=display">count</script> variable which gets incremented for every element traversed as if we are putting the elements in a 1-D resultant array. But, to convert the <script type="math/tex; mode=display">count</script> back into 2-D matrix indices with a column count of <script type="math/tex; mode=display">c</script>, we can obtain the indices as <script type="math/tex; mode=display">res[count/c][count\%c]</script> where <script type="math/tex; mode=display">count/c</script> is the row number and <script type="math/tex; mode=display">count\%c</script> is the coloumn number. Thus, we can save the extra checking required at each step.</p>
<iframe src="https://leetcode.com/playground/3U3C5txm/shared" frameborder="0" name="3U3C5txm" width="100%" height="309"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. We traverse the entire matrix of size <script type="math/tex; mode=display">m*n</script> once only. Here, <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> refers to the number of rows and columns in the given matrix.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m*n)</script>. The resultant matrix of size <script type="math/tex; mode=display">m*n</script> is used. </p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
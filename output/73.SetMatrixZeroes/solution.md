<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-additional-memory-approach">Approach 1: Additional Memory Approach</a></li>
<li><a href="#approach-2-brute-o1-space">Approach 2: Brute O(1) space.</a></li>
<li><a href="#approach-3-o1-space-efficient-solution">Approach 3: O(1) Space, Efficient Solution</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<p>The question seems to be pretty simple but the trick here is that we need to modify the given matrix in place i.e. our space complexity needs to <script type="math/tex; mode=display">O(1)</script>.</p>
<p>We will go through three different approaches to the question. The first approach makes use of additional memory while the other two don't.
<br>
<br></p>
<hr>
<h4 id="approach-1-additional-memory-approach">Approach 1: Additional Memory Approach</h4>
<p><strong>Intuition</strong></p>
<p>If any cell of the matrix has a zero we can record its row and column number. All the cells of this recorded row and column can be marked zero in the next iteration.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>We make a pass over our original array and look for zero entries.</li>
<li>If we find that an entry at <code>[i, j]</code> is 0, then we need to record somewhere the row <code>i</code> and column <code>j</code>.</li>
<li>
<p>So, we use two <code>sets</code>, one for the rows and one for the columns.
    </p><pre>
    if cell[i][j] == 0 {
        row_set.add(i)
        column_set.add(j)
    }</pre>
</li>
<li>
<p>Finally, we iterate over the original matrix. For every cell we check if the row <code>r</code> or column <code>c</code> had been marked earlier. If any of them was marked, we set the value in the cell to 0.
    </p><pre>
    if r in row_set or c in column_set {
        cell[r][c] = 0
    }</pre>
</li>
</ol>
<iframe src="https://leetcode.com/playground/kPV6bYHr/shared" frameborder="0" width="100%" height="500" name="kPV6bYHr"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M \times N)</script> where M and N are the number of rows and columns respectively.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M + N)</script>.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-brute-o1-space">Approach 2: Brute O(1) space.</h4>
<p><strong>Intuition</strong></p>
<p>In the above approach we use additional memory to keep a track of rows and columns which need to be set to zero. This additional use of space can be avoided by manipulating the original array instead.  </p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate over the original array and if we find an entry, say <code>cell[i][j]</code> to be 0, then we iterate over row <code>i</code> and column <code>j</code> separately and set all the <strong>non zero</strong> elements to some high negative dummy value (say <code>-1000000</code>). Note, choosing the right dummy value for your solution is dependent on the constraints of the problem. Any value outside the range of permissible values in the matrix will work as a dummy value. </li>
<li>Finally, we iterate over the original matrix and if we find an entry to be equal to the high negative value (constant defined initially in the code as <code>MODIFIED</code>), then we set the value in the cell to 0.</li>
</ol>
<iframe src="https://leetcode.com/playground/3qUZbzut/shared" frameborder="0" width="100%" height="500" name="3qUZbzut"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity : <script type="math/tex; mode=display">O((M \times N) \times (M + N))</script> where M and N are the number of rows and columns respectively. Even though this solution avoids using space, but is very inefficient since in worst case for every cell we might have to zero out its corresponding row and column. Thus for all <script type="math/tex; mode=display">(M \times N)</script> cells zeroing out <script type="math/tex; mode=display">(M +  N)</script> cells.  </li>
<li>Space Complexity : <script type="math/tex; mode=display">O(1)</script>
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-3-o1-space-efficient-solution">Approach 3: O(1) Space, Efficient Solution</h4>
<p><strong>Intuition</strong></p>
<p>The inefficiency in the second approach is that we might be repeatedly setting a row or column even if it was set to zero already. We can avoid this by postponing the step of setting a row or a column to zeroes.</p>
<blockquote>
<p>We can rather use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero. This means for every cell instead of going to <script type="math/tex; mode=display">M+N</script> cells and setting it to zero we just set the flag in two cells.</p>
</blockquote>
<pre>
if cell[i][j] == 0 {
    cell[i][0] = 0
    cell[0][j] = 0
}
</pre>

<p>These flags are used later to update the matrix. If the first cell of a row is set to zero this means the row should be marked zero. If the first cell of a column is set to zero this means the column should be marked zero.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>
<p>We iterate over the matrix and we mark the first cell of a row <code>i</code> and first cell of a column <code>j</code>, if the condition in the pseudo code above is satisfied. i.e. if <code>cell[i][j] == 0</code>.</p>
</li>
<li>
<p>The first cell of row and column for the first row and first column is the same i.e. <code>cell[0][0]</code>. Hence, we use an additional variable to tell us if the first column had been marked or not and the <code>cell[0][0]</code> would be used to tell the same for the first row.</p>
</li>
<li>
<p>Now, we iterate over the original matrix starting from second row and second column i.e. <code>matrix[1][1]</code> onwards. For every cell we check if the row <code>r</code> or column <code>c</code> had been marked earlier by checking the respective first row cell or first column cell. If any of them was marked, we set the value in the cell to 0. Note the first row and first column serve as the <code>row_set</code> and <code>column_set</code> that we used in the first approach.</p>
</li>
<li>
<p>We then check if <code>cell[0][0] == 0</code>, if this is the case, we mark the first row as zero.</p>
</li>
<li>
<p>And finally, we check if the first column was marked, we make all entries in it as zeros.</p>
</li>
</ol>
<p>!?!../Documents/73_Matrix_Zeroes.json:1000,400!?!</p>
<p>In the above animation we iterate all the cells and mark the corresponding first row/column cell incase of a cell with zero value.</p>
<p></p><center>
<img src="../Figures/73/MatrixZeros_18_1.png" width="400">
</center>
<p>We iterate the matrix we got from the above steps and mark respective cells zeroes.</p>
<p></p><center>
<img src="../Figures/73/MatrixZeros_18_2.png" width="400">
</center>
<p><br></p>
<iframe src="https://leetcode.com/playground/2tGE5XF8/shared" frameborder="0" width="100%" height="500" name="2tGE5XF8"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity : <script type="math/tex; mode=display">O(M \times N)</script>
</li>
<li>Space Complexity : <script type="math/tex; mode=display">O(1)</script>
</li>
</ul>
<p><br><br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>
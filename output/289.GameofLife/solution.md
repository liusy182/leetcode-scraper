<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-omn-space-solution">Approach 1: O(mn) Space Solution</a></li>
<li><a href="#approach-2-o1-space-solution">Approach 2: O(1) Space Solution</a></li>
<li><a href="#follow-up-2-infinite-board">Follow up 2 : Infinite Board</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>Before moving on to the actual solution, let us visually look at the rules to be applied to the cells to get a greater clarity.
</p><center>
<img src="../Figures/289/Game_of_life_1.png" width="600">
</center>
<center>
<img src="../Figures/289/Game_of_life_2.png" width="600">
</center>
<h4 id="approach-1-omn-space-solution">Approach 1: O(mn) Space Solution</h4>
<p><strong>Intuition</strong></p>
<p>The problem might look very easy at first, however, the most important catch in this problem is to realize that if you update the original array with the given rules, you won't be able to perform <em>simultaneous</em> updation as is required in the question. You might end up using the updated values for some cells to update the values of other cells. But the problem demands applying the given rules simultaneously to every cell.</p>
<p>Thus, you cannot update some cells first and then use their updated values to update other cells.</p>
<p></p><center>
<img src="../Figures/289/Game_of_life_3.png" width="600">
</center>
<p>In the above diagram it's evident that an update to a cell can impact the other neighboring cells. If we use the updated value of a cell while updating its neighbors, then we are not applying rules to all cells simultaneously.</p>
<p>Here <code>simultaneously</code> isn't about parallelism but using the original values of the neighbors instead of the updated values while applying rules to any cell. Hence the first approach could be as easy as having a copy of the board. The copy is never mutated. So, you never lose the original value for a cell.</p>
<p>Whenever a rule is applied to any of the cells, we look at its neighbors in the unmodified copy of the board and change the original board accordingly. Here we keep the copy unmodified since the problem asks us to make the changes to the original array in-place.</p>
<p></p><center>
<img src="../Figures/289/Game_of_life_4.png" width="600">
</center>
<p><strong>Algorithm</strong></p>
<ol>
<li>Make a copy of the original board which will remain unchanged throughout the process.</li>
<li>Iterate the cells of the <code>Board</code> one by one.</li>
<li>While computing the results of the rules, use the copy board and apply the result in the original board.</li>
</ol>
<iframe src="https://leetcode.com/playground/6cjUENkE/shared" frameborder="0" width="100%" height="500" name="6cjUENkE"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M \times N)</script>, where <script type="math/tex; mode=display">M</script> is the number of rows and <script type="math/tex; mode=display">N</script> is the number of columns of the <code>Board</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M \times N)</script>, where <script type="math/tex; mode=display">M</script> is the number of rows and <script type="math/tex; mode=display">N</script> is the number of columns of the <code>Board</code>. This is the space occupied by the copy board we created initially.
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-o1-space-solution">Approach 2: O(1) Space Solution</h4>
<p><strong>Intuition</strong></p>
<p>The problem could also be solved in-place. <script type="math/tex; mode=display">O(M \times N)</script> space complexity could be too expensive when the board is very large. We only have two states <code>live(1)</code> or <code>dead(0)</code> for a cell. We can use some dummy cell value to signify previous state of the cell along with the new changed value.</p>
<p>For e.g. If the value of the cell was <code>1</code> originally but it has now become <code>0</code> after applying the rule, then we can change the value to <code>-1</code>. The negative <code>sign</code> signifies the cell is now dead(0) but the <code>magnitude</code> signifies the cell was a live(1) cell originally.</p>
<p>Also, if the value of the cell was <code>0</code> originally but it has now become <code>1</code> after applying the rule, then we can change the value to <code>2</code>. The positive <code>sign</code> signifies the cell is now live(1) but the <code>magnitude</code> of 2 signifies the cell was a dead(0) cell originally.</p>
<p></p><center>
<img src="../Figures/289/Game_of_life_5.png" width="600">
</center>
<p><strong>Algorithm</strong></p>
<ol>
<li>Iterate the cells of the <code>Board</code> one by one.</li>
<li>The rules are computed and applied on the original board. The updated values signify both previous and updated value.</li>
<li>
<p>The updated rules can be seen as this:</p>
<ul>
<li>
<p>Rule 1: Any live cell with fewer than two live neighbors dies, as if caused by under-population. Hence, change the value of cell to <code>-1</code>. This means the cell was live before but now dead.</p>
</li>
<li>
<p>Rule 2: Any live cell with two or three live neighbors lives on to the next generation. Hence, no change in the value.</p>
</li>
<li>
<p>Rule 3: Any live cell with more than three live neighbors dies, as if by over-population. Hence, change the value of cell to <code>-1</code>. This means the cell was live before but now dead. Note that we don't need to differentiate between the rule 1 and 3. The start and end values are the same. Hence, we use the same dummy value.</p>
</li>
<li>
<p>Rule 4: Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. Hence, change the value of cell to 2. This means the cell was dead before but now live.</p>
</li>
</ul>
</li>
<li>
<p>Apply the new rules to the board.</p>
</li>
<li>Since the new values give an indication of the old values of the cell, we accomplish the same results as approach 1 but without saving a copy.</li>
<li>To get the <code>Board</code> in terms of binary values i.e. live(1) and dead(0), we iterate the board again and change the value of a cell to a <code>1</code> if its value currently is greater than <code>0</code> and change the value to a <code>0</code> if its current value is lesser than or equal to <code>0</code>.</li>
</ol>
<iframe src="https://leetcode.com/playground/5937zKqX/shared" frameborder="0" width="100%" height="500" name="5937zKqX"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M \times N)</script>, where <script type="math/tex; mode=display">M</script> is the number of rows and <script type="math/tex; mode=display">N</script> is the number of columns of the <code>Board</code>.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(1)</script>
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="follow-up-2-infinite-board">Follow up 2 : Infinite Board</h4>
<p>So far we've only addressed one of the follow-up questions for this problem statement. We saw how to perform the simulation according to the four rules in-place i.e. without using any additional memory. The problem statement also mentions another follow-up statement which is a bit open ended. We will look at two possible solutions to address it. Essentially, the second follow-up asks us to address the scalability aspect of the problem. What would happen if the board is infinitely large? Can we still use the same solution that we saw earlier or is there something else we will have to do different? If the board becomes infinitely large, there are multiple problems our current solution would run into:</p>
<ol>
<li>It would be computationally impossible to iterate a matrix that large.</li>
<li>It would not be possible to store that big a matrix entirely in memory. We have huge memory capacities these days i.e. of the order of hundreds of GBs. However, it still wouldn't be enough to store such a large matrix in memory.</li>
<li>We would be wasting a lot of space if such a huge board only has a few live cells and the rest of them are all dead. In such a case, we have an extremely sparse matrix and it wouldn't make sense to save the board as a "matrix".</li>
</ol>
<p>Such open ended problems are better suited to design discussions during programming interviews and it's a good habit to take into consideration the scalability aspect of the problem since your interviewer might be interested in talking about such problems. The discussion section already does a great job at addressing this specific portion of the problem. We will briefly go over two different solutions that have been provided in the discussion sections, as they broadly cover two main scenarios of this problem.</p>
<p>One aspect of the problem is addressed by a great solution provided by <a href="https://leetcode.com/stefanpochmann/">Stefan Pochmann</a>. So as mentioned before, it's quite possible that we have a gigantic matrix with a very few live cells. In that case it would be stupidity to save the entire board as is.</p>
<blockquote>
<p>If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells.</p>
</blockquote>
<p>Let's look at the sample code provided by <a href="https://leetcode.com/stefanpochmann/">Stefan</a> for handling this aspect of the problem.</p>
<iframe src="https://leetcode.com/playground/GWyvgQ5K/shared" frameborder="0" width="100%" height="327" name="GWyvgQ5K"></iframe>

<p>Essentially, we obtain only the live cells from the entire board and then apply the different rules using only the live cells and finally we update the board in-place. The only problem with this solution would be when the entire board cannot fit into memory. If that is indeed the case, then we would have to approach this problem in a different way. For that scenario, we assume that the contents of the matrix are stored in a file, one row at a time.</p>
<blockquote>
<p>In order for us to update a particular cell, we only have to look at its 8 neighbors which essentially lie in the row above and below it. So, for updating the cells of a row, we just need the row above and the row below. Thus, we read one row at a time from the file and at max we will have 3 rows in memory. We will keep discarding rows that are processed and then we will keep reading new rows from the file, one at a time.</p>
</blockquote>
<p><a href="https://leetcode.com/beagle/">@beagle's</a> solution revolves around this idea and you can refer to the code in the <a href="https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution/201780">discussion section</a> for the same. It's important to note that there is no single solution for solving this problem. Everybody might have a different viewpoint for addressing the scalability aspect of the problem and these two solutions just address the most basic problems with handling matrix based problems at scale.
<br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>
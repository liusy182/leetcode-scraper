<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-maintain-sorted-positions">Approach 1: Maintain Sorted Positions</a></li>
</ul>
</div>
<hr>
<h4 id="approach-1-maintain-sorted-positions">Approach 1: Maintain Sorted Positions</h4>
<p><strong>Intuition</strong></p>
<p>We'll maintain <code>ExamRoom.students</code>, a sorted <code>list</code> (or <code>TreeSet</code> in Java) of positions the students are currently seated in.</p>
<p><strong>Algorithm</strong></p>
<p>The <code>ExamRoom.leave(p)</code> operation is clear - we will just <code>list.remove</code> (or <code>TreeSet.remove</code>) the student from <code>ExamRoom.students</code>.</p>
<p>Let's focus on the <code>ExamRoom.seat() : int</code> operation.  For each pair of adjacent students <code>i</code> and <code>j</code>, the maximum distance to the closest student is <code>d = (j - i) / 2</code>, achieved in the left-most seat <code>i + d</code>.  Otherwise, we could also sit in the left-most seat, or the right-most seat.</p>
<p>Finally, we should handle the case when there are no students separately.</p>
<p>For more details, please review the comments made in the implementations.</p>
<iframe src="https://leetcode.com/playground/9bZc2mLh/shared" frameborder="0" width="100%" height="500" name="9bZc2mLh"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity:  Each <code>seat</code> operation is <script type="math/tex; mode=display">O(P)</script>, (where <script type="math/tex; mode=display">P</script> is the number of students sitting), as we iterate through every student.  Each <code>leave</code> operation is <script type="math/tex; mode=display">O(P)</script> (<script type="math/tex; mode=display">\log P</script> in Java).</p>
</li>
<li>
<p>Space Complexity:  <script type="math/tex; mode=display">O(P)</script>, the space used to store the positions of each student sitting.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/awice">@awice</a>.</p>
          </div>
        
      </div>
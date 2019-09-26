<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#summary">Summary</a></li>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-jarvis-algorithm-accepted">Approach #1 Jarvis Algorithm [Accepted]</a></li>
<li><a href="#approach-2-graham-scan-accepted">Approach #2 Graham Scan [Accepted]</a></li>
<li><a href="#approach-3-monotone-chain-accepted">Approach #3 Monotone Chain [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="summary">Summary</h2>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-jarvis-algorithm-accepted">Approach #1 Jarvis Algorithm [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>The idea behind Jarvis Algorithm is really simple. We start with the leftmost point among the given set of points and try to wrap up all the given points considering the boundary points in counterclockwise direction. </p>
<p>This means that for every point <script type="math/tex; mode=display">p</script> considered, we try to find out a point <script type="math/tex; mode=display">q</script>, such that this point <script type="math/tex; mode=display">q</script> is the most counterclockwise relative to <script type="math/tex; mode=display">p</script> than all the other points. For checking this, we make use of <code>orientation()</code> function in the current implementation. This function takes three arguments <script type="math/tex; mode=display">p</script>, the current point added in the hull; <script type="math/tex; mode=display">q</script>, the next point being considered to be added in the hull; <script type="math/tex; mode=display">r</script>, any other point in the given point space. This function returns a negative value if the point <script type="math/tex; mode=display">q</script> is more counterclockwise to <script type="math/tex; mode=display">p</script> than the point <script type="math/tex; mode=display">r</script>. </p>
<p>The following figure shows the concept. The point <script type="math/tex; mode=display">q</script> is more counterclockwise to <script type="math/tex; mode=display">p</script> than the point <script type="math/tex; mode=display">r</script>. </p>
<p><img alt="Erect_Fence" src="../Figures/587_Erect_Fence_Jarvis.PNG"></p>
<p>From the above figure, we can observe that in order for the points <script type="math/tex; mode=display">p</script>, <script type="math/tex; mode=display">q</script> and <script type="math/tex; mode=display">r</script> need to be traversed in the same order in a counterclockwise direction, the cross product of the vectors <script type="math/tex; mode=display">\vec{pq}</script> and <script type="math/tex; mode=display">\vec{qr}</script> should be in a direction out of the plane of the screen i.e. it should be positive.</p>
<p>
<script type="math/tex; mode=display">\vec{pq} </script>x<script type="math/tex; mode=display"> \vec{qr} > 0</script>
</p>
<p>
<script type="math/tex; mode=display">\begin{vmatrix} (q_x-p_x) & (q_y-p_y) \\ (r_x-q_x) & (r_y-p_y) \end{vmatrix} > 0</script>
</p>
<p>
<script type="math/tex; mode=display">(q_x - p_x)*(r_y - q_y) - (q_y - p_y)*(r_x - q_x) > 0</script>
</p>
<p>
<script type="math/tex; mode=display">(q_y - p_y)*(r_x - q_x) - (r_y - q_y)*(q_x - p_x) < 0</script>
</p>
<p>The above result is being calculated by the <code>orientation()</code> function.</p>
<p>Thus, we scan over all the points <script type="math/tex; mode=display">r</script> and find out the point <script type="math/tex; mode=display">q</script> which is the most counterclockwise relative to <script type="math/tex; mode=display">p</script> and add it to the convex hull. Further, if there exist two points(say <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script>) with the same relative orientation to <script type="math/tex; mode=display">p</script>, i.e. if the points <script type="math/tex; mode=display">i</script> and <script type="math/tex; mode=display">j</script> are collinear relative to <script type="math/tex; mode=display">p</script>, we need to consider the point <script type="math/tex; mode=display">i</script> which lies in between the two points <script type="math/tex; mode=display">p</script> and <script type="math/tex; mode=display">j</script>. For considering such a situation, we've made use of a function <code>inBetween()</code> in the current implementation. Even after finding out a point <script type="math/tex; mode=display">q</script>, we need to consider all the other points which are collinear to <script type="math/tex; mode=display">q</script> relative to <script type="math/tex; mode=display">p</script> so as to be able to consider all the points lying on the boundary.</p>
<p>Thus, we keep on including the points in the hull till we reach the beginning point. </p>
<p>The following animation depicts the process for a clearer understanding.</p>
<p>!?!../Documents/587_Erect_Fence_1.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/ho9e8Hs9/shared" frameborder="0" name="ho9e8Hs9" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(m*n)</script>. For every point on the hull we examine all the other points to determine the next point. Here n is number of input points and m is number of output or hull points ($$m &amp;leq; n). </p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(m)</script>. List <script type="math/tex; mode=display">hull</script> grows upto size <script type="math/tex; mode=display">m</script>.</p>
</li>
</ul>
<hr>
<h4 id="approach-2-graham-scan-accepted">Approach #2 Graham Scan [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Graham Scan Algorithm is also a standard algorithm for finding the convex hull of a given set of points. Consider the animation below to follow along with the discussion. </p>
<p>!?!../Documents/587_Erect_Fence_2.json:1000,563!?!</p>
<p>The method works as follows. Firsly we select an initial point(<script type="math/tex; mode=display">bm</script>) to start the hull with. This point is chosen as the point with the lowest y-coordinate. In case of a tie, we need to choose the point with the lowest x-coordinate, from among all the given set of points. This point is indicated as point 0 in the animation. Then, we sort the given set of points based on their polar angles formed w.r.t. a vertical line drawn throught the intial point. </p>
<p>This sorting of the points gives us a rough idea of the way in which we should consider the points to be included in the hull while considering the boundary in counter-clockwise order. In order to sort the points, we make use of <code>orientation</code> function which is the same as discussed in the last approach. The points with a lower polar angle relative to the vertical line come first in the sorted array. In case, if the orientation of two points happens to be the same, the points are sorted based on their distance from the beginning point(<script type="math/tex; mode=display">bm</script>). Later on we'll be considering the points in the sorted array in the same order. Because of this, we need to do the sorting based on distance for points collinear relative to <script type="math/tex; mode=display">bm</script>, so that all the collinear points lying on the hull are included in the boundary.</p>
<p>But, we need to consider another important case. In case, the collinear points lie on the closing(last) edge of the hull, we need to consider the points such that the points which lie farther from the initial point <script type="math/tex; mode=display">bm</script> are considered first. Thus, after sorting the array, we traverse the sorted array from the end and reverse the order of the points which are collinear and lie towards the end of the sorted array, since these will be the points which will be considered at the end while forming the hull and thus, will be considered at the end. Thus, after these preprocessing steps, we've got the points correctly arranged in the way that they need to be considered while forming the hull.</p>
<p>Now, as per the algorithm, we start off by considering the line formed by the first two points(0 and 1 in the animation) in the sorted array. We push the points on this line onto a <script type="math/tex; mode=display">stack</script>. After this, we start traversing over the sorted <script type="math/tex; mode=display">points</script> array from the third point onwards. If the current point being considered appears after taking a left turn(or straight path) relative to the previous line(line's direction), we push the point onto the stack, indicating that the point has been temporarily added to the hull boundary.</p>
<p>This checking of left or right turn is done by making use of <code>orientation</code> again. An orientation greater than 0, considering the points on the line and the current point, indicates a counterclockwise direction or a right turn. A negative orientation indicates a left turn similarly.</p>
<p>If the current point happens to be occuring by taking a right turn from the previous line's direction, it means that the last point included in the hull was incorrect, since it needs to lie inside the boundary and not on the boundary(as is indicated by point 4 in the animation). Thus, we pop off the last point from the stack and consider the second last line's direction with the current point. </p>
<p>Thus, the same process continues, and the popping keeps on continuing till we reach a state where the current point can be included in the hull by taking a right turn. Thus, in this way, we ensure that the hull includes only the boundary points and not the points inside the boundary. After all the points have been traversed, the points lying in the stack constitute the boundary of the convex hull. </p>
<p>The below code is inspired by <a href="https://leetcode.com/yuxiangmusic">@yuxiangmusic</a> solution.</p>
<iframe src="https://leetcode.com/playground/FRb4Wch9/shared" frameborder="0" name="FRb4Wch9" width="100%" height="515"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(nlog(n)\big)</script>. Sorting the given points takes <script type="math/tex; mode=display">O\big(nlog(n)\big)</script> time. Further, after sorting the points can be considered in two cases, while being pushed onto the <script type="math/tex; mode=display">stack</script> or while popping from the <script type="math/tex; mode=display">stack</script>. Atmost, every point is touched twice(both push and pop) taking <script type="math/tex; mode=display">2n</script>(<script type="math/tex; mode=display">O(n)</script>) time in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. Stack size grows upto <script type="math/tex; mode=display">n</script> in worst case.</p>
</li>
</ul>
<hr>
<h4 id="approach-3-monotone-chain-accepted">Approach #3 Monotone Chain [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>The idea behing Monotone Chain Algorithm is somewhat similar to Graham Scan Algorithm. It mainly differs in the order in which the points are considered while being included in the hull. Instead of sorting the points based on their polar angles as in Graham Scan, we sort the points on the basis of their x-coordinate values. If two points have the same x-coordinate values, the points are sorted based on their y-coordinate values. The reasoning behind this will be explained soon.</p>
<p>In this algorithm, we consider the hull as being comprised of two sub-boundaries- The upper hull and the lower hull. We form the two portions in a slightly different manner. </p>
<p>We traverse over the sorted <script type="math/tex; mode=display">points</script> array after adding the initial two points in the hull temporarily(which are pushed over the stack <script type="math/tex; mode=display">hull</script>). For every new point considered, we check if the current point lies in the counter-clockwise direction relative to the last two points. If so, the current point is staightaway pushed onto <script type="math/tex; mode=display">hull</script>. If not(indicated by a positive <code>orientation</code>), we again get the inference that the last point on the <script type="math/tex; mode=display">hull</script> needs to lie inside the boundary and not on the boundary. Thus, we keep on popping the points from <script type="math/tex; mode=display">hull</script> till the current point lies in a counterclockwise direction relative to the top two points on the <script type="math/tex; mode=display">hull</script>. </p>
<p>Note that this time, we need not consider the case of collinear points explicitly, since the points have already been sorted based on their x-coordinate values. So, the collinear points, if any, will implicitly be considered in the correct order.</p>
<p>Doing so, we reach a state such that we reach the point with the largest x-coordinate. But, the hull isn't complete yet. The portion of the hull formed till now constitutes the lower poriton of the hull. Now, we need to form the upper portion of the hull.</p>
<p>Thus, we continue the process of finding the next counterclockwise points and popping in case of a conflict, but this time we consider the points in the reverse order of their x-coordinate values. For this, we can simply traverse over the sorted <script type="math/tex; mode=display">points</script> array in the reverse order. We append the new upper hull values obtained to the previous <script type="math/tex; mode=display">hull</script> itself. At the end, <script type="math/tex; mode=display">hull</script> gives the points on the required boundary.</p>
<p>The following animation depicts the process for a better understanding of the process:</p>
<p>!?!../Documents/587_Erect_Fence_3.json:1000,563!?!</p>
<iframe src="https://leetcode.com/playground/vworasPc/shared" frameborder="0" name="vworasPc" width="100%" height="479"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O\big(nlog(n)\big)</script>. Sorting the given points takes <script type="math/tex; mode=display">O\big(nlog(n)\big)</script> time. Further, after sorting the points can be considered in two cases, while being pushed onto the <script type="math/tex; mode=display">hull</script> or while popping from the <script type="math/tex; mode=display">hull</script>. Atmost, every point is touched twice(both push and pop) taking <script type="math/tex; mode=display">2n</script>(<script type="math/tex; mode=display">O(n)</script>) time in the worst case.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n)</script>. <script type="math/tex; mode=display">hull</script> stack can grow upto size <script type="math/tex; mode=display">n</script>.</p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
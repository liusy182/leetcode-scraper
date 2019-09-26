<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-connected-components">Approach 1: Connected Components</a></li>
<li><a href="#approach-2-sorting">Approach 2: Sorting</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-connected-components">Approach 1: Connected Components</h4>
<p><strong>Intuition</strong></p>
<p>If we draw a graph (with intervals as nodes) that contains undirected edges
between all pairs of intervals that overlap, then all intervals in each
<em>connected component</em> of the graph can be merged into a single interval.</p>
<p><strong>Algorithm</strong></p>
<p>With the above intuition in mind, we can represent the graph as an adjacency
list, inserting directed edges in both directions to simulate undirected
edges. Then, to determine which connected component each node is it, we
perform graph traversals from arbitrary unvisited nodes until all nodes have
been visited. To do this efficiently, we store visited nodes in a <code>Set</code>,
allowing for constant time containment checks and insertion. Finally, we
consider each connected component, merging all of its intervals by
constructing a new <code>Interval</code> with <code>start</code> equal to the minimum start among
them and <code>end</code> equal to the maximum end.</p>
<p>This algorithm is correct simply because it is basically the brute force
solution. We compare every interval to every other interval, so we know
exactly which intervals overlap. The reason for the connected component
search is that two intervals may not directly overlap, but might overlap
indirectly via a third interval. See the example below to see this more
clearly.</p>
<p align="center"><img alt="Components Example" src="../Figures/56/component.png"></p>
<p>Although (1, 5) and (6, 10) do not directly overlap, either would overlap
with the other if first merged with (4, 7). There are two connected
components, so if we merge their nodes, we expect to get the following two
merged intervals:</p>
<p>(1, 10), (15, 20)</p>
<iframe src="https://leetcode.com/playground/FdD8vWwU/shared" frameborder="0" width="100%" height="500" name="FdD8vWwU"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n^2)</script>
</p>
<p>Building the graph costs <script type="math/tex; mode=display">O(V + E) = O(V) + O(E) = O(n) + O(n^2) = O(n^2)</script>
time, as in the worst case all intervals are mutually overlapping.
Traversing the graph has the same cost (although it might appear higher
at first) because our <code>visited</code> set guarantees that each node will be
visited exactly once. Finally, because each node is part of exactly one
component, the merge step costs <script type="math/tex; mode=display">O(V) = O(n)</script> time. This all adds up as
follows:</p>
<p>
<script type="math/tex; mode=display">
    O(n^2) + O(n^2) + O(n) = O(n^2)
</script>
</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(n^2)</script>
</p>
<p>As previously mentioned, in the worst case, all intervals are mutually
overlapping, so there will be an edge for every pair of intervals.
Therefore, the memory footprint is quadratic in the input size.</p>
</li>
</ul>
<p><br></p>
<hr>
<h4 id="approach-2-sorting">Approach 2: Sorting</h4>
<p><strong>Intuition</strong></p>
<p>If we sort the intervals by their <code>start</code> value, then each set of intervals
that can be merged will appear as a contiguous "run" in the sorted list.</p>
<p><strong>Algorithm</strong></p>
<p>First, we sort the list as described. Then, we insert the first interval into
our <code>merged</code> list and continue considering each interval in turn as follows:
If the current interval begins <em>after</em> the previous interval ends, then they
do not overlap and we can append the current interval to <code>merged</code>. Otherwise,
they do overlap, and we merge them by updating the <code>end</code> of the previous
interval if it is less than the <code>end</code> of the current interval.</p>
<p>A simple proof by contradiction shows that this algorithm always produces the
correct answer. First, suppose that the algorithm at some point fails to
merge two intervals that should be merged. This would imply that there exists
some triple of indices <script type="math/tex; mode=display">i</script>, <script type="math/tex; mode=display">j</script>, and <script type="math/tex; mode=display">k</script> in a list of intervals
<script type="math/tex; mode=display">ints</script> such that <script type="math/tex; mode=display">i < j < k</script> and (<script type="math/tex; mode=display">ints[i]</script>, <script type="math/tex; mode=display">ints[k]</script>) can be
merged, but neither (<script type="math/tex; mode=display">ints[i]</script>, <script type="math/tex; mode=display">ints[j]</script>) nor (<script type="math/tex; mode=display">ints[j]</script>, <script type="math/tex; mode=display">ints[k]</script>)
can be merged. From this scenario follow several inequalities:</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
    ints[i].end < ints[j].start \\
    ints[j].end < ints[k].start \\
    ints[i].end \geq ints[k].start \\
\end{aligned}
</script>
</p>
<p>We can chain these inequalities (along with the following inequality, implied
by the well-formedness of the intervals: <script type="math/tex; mode=display">ints[j].start \leq ints[j].end</script>) to
demonstrate a contradiction:</p>
<p>
<script type="math/tex; mode=display">
\begin{aligned}
    ints[i].end < ints[j].start \leq ints[j].end < ints[k].start \\
    ints[i].end \geq ints[k].start
\end{aligned}
</script>
</p>
<p>Therefore, all mergeable intervals must occur in a contiguous run of the
sorted list.</p>
<p align="center"><img alt="Sorting Example" src="../Figures/56/sort.png"></p>
<p>Consider the example above, where the intervals are sorted, and then all
mergeable intervals form contiguous blocks.</p>
<iframe src="https://leetcode.com/playground/Zum7wj5V/shared" frameborder="0" width="100%" height="500" name="Zum7wj5V"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(n\log{}n)</script>
</p>
<p>Other than the <code>sort</code> invocation, we do a simple linear scan of the list,
so the runtime is dominated by the <script type="math/tex; mode=display">O(nlgn)</script> complexity of sorting.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(1)</script> (or <script type="math/tex; mode=display">O(n)</script>)</p>
<p>If we can sort <code>intervals</code> in place, we do not need more than constant
additional space. Otherwise, we must allocate linear space to store a
copy of <code>intervals</code> and sort that.</p>
</li>
</ul>
          </div>
        
      </div>
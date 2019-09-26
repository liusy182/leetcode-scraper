<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-depth-first-search">Approach 1: Using Depth First Search</a></li>
<li><a href="#approach-2-using-node-indegree">Approach 2: Using Node Indegree</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>This is a very common problem that some of us might face during college. We might want to take up a certain set of courses that interest us. However, as we all know, most of the courses do tend to have a lot of prerequisites associated with them. Some of these would be hard requirements whereas others would be simply <code>suggested</code> prerequisites which you may or may not take. However, for us to be able to have an all round learning experience, we should follow the suggested set of prerequisites. How does one decide what order of courses they should follow so as not to miss out on any subjects?</p>
<p>As mentioned in the problem statement, such a problem is a natural fit for graph based algorithms and we can easily model the elements in the problem statement as a graph. First of all, let's look at the graphical representation of the problem and it's components and then we will move onto the solutions.</p>
<p>We can represent the information provided in the question in the form of a graph.</p>
<ul>
<li>Let <script type="math/tex; mode=display">G(V, E)</script> represent a <code>directed</code>, <code>unweighted</code> graph.</li>
<li>Each course would represent a vertex in the graph.</li>
<li>The edges are modeled after the prerequisite relationship between courses. So, we are given, that a pair such as <script type="math/tex; mode=display">[a, b]</script> in the question means the course <code>b</code> is a prerequisite for the course <code>a</code>. This can be represented as a <code>directed edge b ➔ a</code> in the graph.</li>
<li>The graph is a cyclic graph because there is a possibility of a cycle in the graph. If the graph would be acyclic, then an ordering of subjects as required in the question would <code>always</code> be possible. Since it's mentioned that such an ordering may not always be possible, that means we have a cyclic graph.</li>
</ul>
<p>Let's look at a sample graph representing a set of courses where such an ordering is possible and one where such an ordering is not possible. It will be easier to explain the approaches once we look at two sample graphs.</p>
<p></p><center>
<img src="../Figures/210_Course_Schedule_2/Fig-1.png">
</center>
<p>For the sample graph shown above, one of the possible ordering of courses is: <code>C6 ➔ C4 ➔ C1 ➔ C5 ➔ C2 ➔ C3</code> and another possible ordering of subjects is <code>C6 ➔ C4 ➔ C5 ➔ C1 ➔ C2 ➔ C3</code>. Now let's look at a graph where no such ordering of courses is possible.</p>
<p></p><center>
<img src="../Figures/210_Course_Schedule_2/Fig-2.png">
</center>
<p>Note that the edges that have changed from the previous graph have been highlighted in red.</p>
<blockquote>
<p>Clearly, the presence of a cycle in the graph shows us that a proper ordering of prerequisites is not possible at all. Intuitively, it is not possible to have e.g. two subjects S1 and S2 prerequisites of each other. Similar ideology applies to a larger cycle in the graph like we have above.</p>
</blockquote>
<p>Such an ordering of subjects is referred to as a <code>Topological Sorted Order</code> and this is a common algorithmic problem in the graph domain. There are two approaches that we will be looking at in this article to solve this problem.
<br>
<br></p>
<hr>
<h4 id="approach-1-using-depth-first-search">Approach 1: Using Depth First Search</h4>
<p><strong>Intuition</strong></p>
<p>Suppose we are at a node in our graph during the depth first traversal. Let's call this node <code>A</code>.</p>
<blockquote>
<p>The way DFS would work is that we would consider all possible paths stemming from A before finishing up the recursion for A and moving onto other nodes. All the nodes in the paths stemming from the node A would have A as an ancestor. The way this fits in our problem is, all the courses in the paths stemming from the course A would have A as a prerequisite.</p>
</blockquote>
<p>Now we know how to get all the courses that have a particular course as a prerequisite. If a valid ordering of courses is possible, the course <code>A</code> would come before all the other set of courses that have it as a prerequisite. This idea for solving the problem can be explored using depth first search. Let's look at the pseudo-code before looking at the formal algorithm.</p>
<pre>
➔ let S be a stack of courses
➔ function dfs(node)
➔     for each neighbor in adjacency list of node
➔          dfs(neighbor)
➔     add node to S  
</pre>

<p>Let's now look at the formal algorithm based on this idea.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize a stack <code>S</code> that will contain the topologically sorted order of the courses in our graph.</li>
<li>Construct the adjacency list using the edge pairs given in the input. An important thing to note about the input for the problem is that a pair such as <code>[a, b]</code> represents that the course <code>b</code> needs to be taken in order to do the course <code>a</code>. This implies an edge of the form <code>b ➔ a</code>. Please take note of this when implementing the algorithm.</li>
<li>For each of the nodes in our graph, we will run a depth first search in case that node was not already visited in some other node's DFS traversal.</li>
<li>Suppose we are executing the depth first search for a node <code>N</code>. We will recursively traverse all of the neighbors of node <code>N</code> which have not been processed before.</li>
<li>Once the processing of all the neighbors is done, we will add the node <code>N</code> to the stack. We are making use of a stack to simulate the ordering we need. When we add the node <code>N</code> to the stack, all the nodes that require the node <code>N</code> as a prerequisites (among others) will already be in the stack.</li>
<li>Once all the nodes have been processed, we will simply return the nodes as they are present in the stack from top to bottom.</li>
</ol>
<p>Let's look at an animated dry run of the algorithm on a sample graph before moving onto the formal implementations.</p>
<p></p><center>
<p>!?!../Documents/210_Anim1.json:640,370!?!</p>
<p></p></center>
<blockquote>
<p>An important thing to note about topologically sorted order is that there won't be just one ordering of nodes (courses). There can be multiple. For e.g. in the above graph, we could have processed the node "D" before we did "B" and hence have a different ordering.</p>
</blockquote>
<iframe src="https://leetcode.com/playground/cbLU5sGa/shared" frameborder="0" width="100%" height="500" name="cbLU5sGa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N)</script> considering there are <script type="math/tex; mode=display">N</script> courses in all. We essentially perform a complete depth first search covering all the nodes in the forest. It's a forest and not a graph because not all nodes will be connected together. There can be disjoint components as well.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(N)</script>, the space utilized by the recursion stack (not the stack we used to maintain the topologically sorted order)
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-using-node-indegree">Approach 2: Using Node Indegree</h4>
<p><strong>Intuition</strong></p>
<p>This approach is much easier to think about intuitively as will be clear from the following point/fact about topological ordering.</p>
<blockquote>
<p>The first node in the topological ordering will be the node that doesn't have any incoming edges. Essentially, any node that has an in-degree of 0 can start the topologically sorted order. If there are multiple such nodes, their relative order doesn't matter and they can appear in any order.</p>
</blockquote>
<p>Our current algorithm is based on this idea. We first process all the nodes/course with 0 in-degree implying no prerequisite courses
required. If we remove all these courses from the graph, along with their outgoing edges, we can find out the courses/nodes that should be processed next. These would again be the nodes with 0 in-degree. We can continuously do this until all the courses have been accounted for.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize a queue, <code>Q</code> to keep a track of all the nodes in the graph with 0 in-degree.</li>
<li>Iterate over all the edges in the input and create an adjacency list and also a map of node v/s in-degree.</li>
<li>Add all the nodes with 0 in-degree to <code>Q</code>.</li>
<li>The following steps are to be done until the <code>Q</code> becomes empty.<ol>
<li>Pop a node from the <code>Q</code>. Let's call this node, <code>N</code>.</li>
<li>For all the neighbors of this node, <code>N</code>, reduce their in-degree by 1. If any of the nodes' in-degree reaches 0, add it to the <code>Q</code>.</li>
<li>Add the node <code>N</code> to the list maintaining topologically sorted order.</li>
<li>Continue from step 4.1.</li>
</ol>
</li>
</ol>
<p>Let us now look at an animation depicting this algorithm and then we will get to the implementations.</p>
<p></p><center>
<p>!?!../Documents/210_Anim2.json:640,400!?!</p>
<p></p></center>
<p>An important thing to note here is, using a queue is not a hard requirement for this algorithm. We can make use of a stack. That however, will give us a different ordering than what we might get from the queue because of the difference in access patterns between the two data-structures.</p>
<iframe src="https://leetcode.com/playground/vNWFTrPq/shared" frameborder="0" width="100%" height="500" name="vNWFTrPq"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N)</script> since we process each node exactly once and end up processing the entire graph given to us.</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(N)</script> since we use an intermediate queue data structure to keep all the nodes with 0 in-degree. In the worst case, there won't be any prerequisite relationship and the queue will contain all the vertices initially since all of them will have 0 in-degree.</li>
</ul>
<p><br></p>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/sachinmalhotra1993">@sachinmalhotra1993</a>.</p>
          </div>
        
      </div>
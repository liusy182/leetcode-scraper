<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-breadth-first-search">Approach 1: Breadth First Search</a></li>
<li><a href="#approach-2-bidirectional-breadth-first-search">Approach 2: Bidirectional Breadth First Search</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<p>We are given a <code>beginWord</code> and an <code>endWord</code>. Let these two represent <code>start node</code> and <code>end node</code> of a graph. We have to reach from the start node to the end node using some intermediate nodes/words. The intermediate nodes are determined by the <code>wordList</code> given to us. The only condition for every step we take on this ladder of words is the current word should change by just <code>one letter</code>.</p>
<p></p><center>
<img src="../Figures/127/Word_Ladder_1.png" width="400">
</center>
<p>We will essentially be working with an undirected and unweighted graph with words as nodes and edges between words which differ by just one letter. The problem boils down to finding the shortest path from a start node to a destination node, if there exists one. Hence it can be solved using <code>Breadth First Search</code> approach.</p>
<p>One of the most important step here is to figure out how to find adjacent nodes i.e. words which differ by one letter. To efficiently find the neighboring nodes for any given word we do some pre-processing on the words of the given <code>wordList</code>. The pre-processing involves replacing the letter of a word by a non-alphabet say, <code>*</code>.</p>
<p></p><center>
<img src="../Figures/127/Word_Ladder_2.png" width="400">
</center>
<p>This pre-processing helps to form generic states to represent a single letter change.</p>
<p>For e.g. <code>Dog ----&gt; D*g &lt;---- Dig</code></p>
<p>Both <code>Dog</code> and <code>Dig</code> map to the same intermediate or generic state <code>D*g</code>.</p>
<p>The preprocessing step helps us find out the generic one letter away nodes for any word of the word list and hence making it easier and quicker to get the adjacent nodes. Otherwise, for every word we will have to iterate over the entire word list and find words that differ by one letter. That would take a lot of time. This preprocessing step essentially builds the adjacency list first before beginning the breadth first search algorithm.</p>
<p>For eg. While doing BFS if we have to find the adjacent nodes for <code>Dug</code> we can first find all the generic states for <code>Dug</code>.</p>
<ol>
<li><code>Dug =&gt; *ug</code></li>
<li><code>Dug =&gt; D*g</code></li>
<li><code>Dug =&gt; Du*</code></li>
</ol>
<p>The second transformation <code>D*g</code> could then be mapped to <code>Dog</code> or <code>Dig</code>, since all of them share the same generic state. Having a common generic transformation means two words are connected and differ by one letter.</p>
<h4 id="approach-1-breadth-first-search">Approach 1: Breadth First Search</h4>
<p><strong>Intuition</strong></p>
<p>Start from <code>beginWord</code> and search the <code>endWord</code> using BFS.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Do the pre-processing on the given <code>wordList</code> and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.</li>
<li>Push a tuple containing the <code>beginWord</code> and <code>1</code> in a queue. The <code>1</code> represents the level number of a node. We have to return the level of the <code>endNode</code> as that would represent the shortest sequence/distance from the <code>beginWord</code>.</li>
<li>To prevent cycles, use a visited dictionary.</li>
<li>While the queue has elements, get the front element of the queue. Let's call this word as <code>current_word</code>.</li>
<li>Find all the generic transformations of the <code>current_word</code> and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the <code>all_combo_dict</code>.</li>
<li>The list of words we get from <code>all_combo_dict</code> are all the words which have a common intermediate state with the <code>current_word</code>. These new set of words will be the adjacent nodes/words to <code>current_word</code> and hence added to the queue.</li>
<li>Hence, for each word in this list of intermediate words, append <code>(word, level + 1)</code> into the queue where <code>level</code> is the level for the <code>current_word</code>.</li>
<li>
<p>Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.</p>
<blockquote>
<p>Termination condition for standard BFS is finding the end word.</p>
</blockquote>
</li>
</ol>
<iframe src="https://leetcode.com/playground/9qj48p7V/shared" frameborder="0" width="100%" height="500" name="9qj48p7V"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M \times N)</script>, where <script type="math/tex; mode=display">M</script> is the length of words and <script type="math/tex; mode=display">N</script> is the total number of words in the input word list. Finding out all the transformations takes <script type="math/tex; mode=display">M</script> iterations for each of the <script type="math/tex; mode=display">N</script> words. Also, breadth first search in the worst case might go to each of the <script type="math/tex; mode=display">N</script> words.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M \times N)</script>, to store all <script type="math/tex; mode=display">M</script> transformations for each of the <script type="math/tex; mode=display">N</script> words, in the <code>all_combo_dict</code> dictionary. Visited dictionary is of <script type="math/tex; mode=display">N</script> size. Queue for BFS in worst case would need space for all <script type="math/tex; mode=display">N</script> words.<br>
<br>
<br></p>
</li>
</ul>
<hr>
<h4 id="approach-2-bidirectional-breadth-first-search">Approach 2: Bidirectional Breadth First Search</h4>
<p><strong>Intuition</strong></p>
<p>The graph formed from the nodes in the dictionary might be too big. The search space considered by the breadth first search algorithm depends upon the branching factor of the nodes at each level. If the branching factor remains the same for all the nodes, the search space increases exponentially along with the number of levels. Consider a simple example of a binary tree. With each passing level in a complete binary tree, the number of nodes increase in powers of <code>2</code>.</p>
<p>We can considerably cut down the search space of the standard breadth first search algorithm if we launch two simultaneous BFS. One from the <code>beginWord</code> and one from the <code>endWord</code>. We progress one node at a time from both sides and at any point in time if we find a common node in both the searches, we stop the search. This is known as <code>bidirectional BFS</code> and it considerably cuts down on the search space and hence reduces the time and space complexity.</p>
<p></p><center>
<img src="../Figures/127/Word_Ladder_3.png" width="600">
</center>
<p><strong>Algorithm</strong></p>
<ol>
<li>The algorithm is very similar to the standard BFS based approach we saw earlier.</li>
<li>The only difference is we now do BFS starting two nodes instead of one. This also changes the termination condition of our search.</li>
<li>We now have two visited dictionaries to keep track of nodes visited from the search starting at the respective ends.</li>
<li>
<p>If we ever find a node/word which is in the visited dictionary of the parallel search we terminate our search, since we have found the meet point of this bidirectional search. It's more like meeting in the middle instead of going all the way through.</p>
<blockquote>
<p>Termination condition for bidirectional search is finding a word which is already been seen by the parallel search.</p>
</blockquote>
</li>
<li>
<p>The shortest transformation sequence is the sum of levels of the meet point node from both the ends. Thus, for every visited node we save its level as value in the visited dictionary.</p>
</li>
</ol>
<p></p><center>
<img src="../Figures/127/Word_Ladder_4.png" width="600">
</center>
<iframe src="https://leetcode.com/playground/QwU5MtQa/shared" frameborder="0" width="100%" height="500" name="QwU5MtQa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time Complexity: <script type="math/tex; mode=display">O(M \times N)</script>, where <script type="math/tex; mode=display">M</script> is the length of words and <script type="math/tex; mode=display">N</script> is the total number of words in the input word list. Similar to one directional, bidirectional also takes <script type="math/tex; mode=display">M*N</script> for finding out all the transformations. But the search time reduces to half, since the two parallel searches meet somewhere in the middle.</p>
</li>
<li>
<p>Space Complexity: <script type="math/tex; mode=display">O(M \times N)</script>, to store all <script type="math/tex; mode=display">M</script> transformations for each of the <script type="math/tex; mode=display">N</script> words, in the <code>all_combo_dict</code> dictionary, same as one directional. But bidirectional reduces the search space. It narrows down because of meeting in the middle.<br>
<br></p>
</li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>
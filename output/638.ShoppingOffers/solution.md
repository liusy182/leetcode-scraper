<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</a></li>
<li><a href="#approach-2-using-recursion-with-memoization-accepted">Approach #2 Using Recursion with memoization [Accepted]</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-using-recursion-accepted">Approach #1 Using Recursion [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>Before discussing the steps involved in the process, we need to note a few points. Firstly, whenever an offer is used from amongst the ones available in the <script type="math/tex; mode=display">special</script> list, we need to update the <script type="math/tex; mode=display">needs</script> appropriately, such that the number of items in the current offer of each type are deducted from the ones in the corresponding entry in <script type="math/tex; mode=display">needs</script>.</p>
<p>Further, an offer can be used only if the number of items, of each type, required for using the offer, is lesser than or equal to the ones available in the current <script type="math/tex; mode=display">needs</script>. </p>
<p>Now, let's discuss the algorithm. We make use of a <code>shopping(price,special,needs)</code> function, which takes the <script type="math/tex; mode=display">price</script> and <script type="math/tex; mode=display">special</script> list along with the current(updated) <script type="math/tex; mode=display">needs</script> as the input and returns the minimum cost of buying these items as required by this <script type="math/tex; mode=display">needs</script> list. </p>
<p>In every call of the function <code>shopping(price,special,needs)</code>, we do as follows:</p>
<ol>
<li>
<p>Determine the cost of buying items as per the <script type="math/tex; mode=display">needs</script> array, without applying any offer. Store the result in <script type="math/tex; mode=display">res</script>.</p>
</li>
<li>
<p>Iterate over every offer in the <script type="math/tex; mode=display">special</script> list. For every offer chosen, repeat steps 3 to 5.</p>
</li>
<li>
<p>Create a copy of the current <script type="math/tex; mode=display">needs</script> in a <script type="math/tex; mode=display">clone</script> list(so that the original needs can be used again, while selecting the next offer).</p>
</li>
<li>
<p>Try to apply the current offer. If possible, update the required number of items in <script type="math/tex; mode=display">clone</script>.</p>
</li>
<li>
<p>If the current offer could be applied, find the minimum cost out of <script type="math/tex; mode=display">res</script> and <script type="math/tex; mode=display">offer_\current</script> + <code>shopping(price,special,clone)</code>. Here, <script type="math/tex; mode=display">offer_\current</script> refers to the price that needs to be paid for the current offer. Update the <script type="math/tex; mode=display">res</script> with the minimum value.</p>
</li>
<li>
<p>Return the <script type="math/tex; mode=display">res</script> corresponding to the minimum cost.</p>
</li>
</ol>
<p>We need to note that the <script type="math/tex; mode=display">clone</script> needs to be updated afresh from <script type="math/tex; mode=display">needs</script>(coming to the current function call) when we choose a new offer. This needs to be done, because solely applying the next offer could result in a lesser cost than the one resulting by using the previous offer first.</p>
<iframe src="https://leetcode.com/playground/b6RfW7x4/shared" frameborder="0" name="b6RfW7x4" width="100%" height="515"></iframe>

<hr>
<h4 id="approach-2-using-recursion-with-memoization-accepted">Approach #2 Using Recursion with memoization [Accepted]</h4>
<p><strong>Algorithm</strong></p>
<p>In the last approach, we can observe that the same <script type="math/tex; mode=display">needs</script> can be reached by applying the offers in various orders. e.g. We can choose the first offer followed by the second offer or vice-versa. But, both lead to the same requirement of updated <script type="math/tex; mode=display">needs</script> and the cost as well. Thus, instead of repeating the whole process for the same <script type="math/tex; mode=display">needs</script> state through various recursive paths, we can create an entry corresponding to the current set of <script type="math/tex; mode=display">needs</script> in a HashMap, <script type="math/tex; mode=display">map</script>, which stores the minimum cost corresponding to this set of <script type="math/tex; mode=display">needs</script>. Thus, whenever the same call is made again in the future through a different path, we need not repeat the whole process over, and we can directly return the result stored in the <script type="math/tex; mode=display">map</script>.</p>
<iframe src="https://leetcode.com/playground/aPHtk8QK/shared" frameborder="0" name="aPHtk8QK" width="100%" height="515"></iframe>

<hr>
<p>Analysis written by: <a href="https://leetcode.com/vinod23">@vinod23</a></p>
          </div>
        
      </div>
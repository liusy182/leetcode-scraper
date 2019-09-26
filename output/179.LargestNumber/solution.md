<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#approach-1-sorting-via-custom-comparator-accepted">Approach #1 Sorting via Custom Comparator [Accepted]</a></li>
</ul>
</div>
<h4 id="approach-1-sorting-via-custom-comparator-accepted">Approach #1 Sorting via Custom Comparator [Accepted]</h4>
<p><strong>Intuition</strong></p>
<p>To construct the largest number, we want to ensure that the most significant
digits are occupied by the largest digits.</p>
<p><strong>Algorithm</strong></p>
<p>First, we convert each integer to a string. Then, we sort the array of strings.</p>
<p>While it might be tempting to simply sort the numbers in descending order,
this causes problems for sets of numbers with the same leading digit. For
example, sorting the problem example in descending order would produce the
number <script type="math/tex; mode=display">9534303</script>, while the correct answer can be achieved by transposing
the <script type="math/tex; mode=display">3</script> and the <script type="math/tex; mode=display">30</script>. Therefore, for each pairwise comparison during the
sort, we compare the numbers achieved by concatenating the pair in both
orders. We can prove that this sorts into the proper order as follows: </p>
<p>Assume that (without loss of generality), for some pair of integers <script type="math/tex; mode=display">a</script> and
<script type="math/tex; mode=display">b</script>, our comparator dictates that <script type="math/tex; mode=display">a</script> should precede <script type="math/tex; mode=display">b</script> in sorted
order. This means that <script type="math/tex; mode=display">a\frown b > b\frown a</script> (where <script type="math/tex; mode=display">\frown</script> represents
concatenation). For the sort to produce an incorrect ordering, there must be
some <script type="math/tex; mode=display">c</script> for which <script type="math/tex; mode=display">b</script> precedes <script type="math/tex; mode=display">c</script> and <script type="math/tex; mode=display">c</script> precedes <script type="math/tex; mode=display">a</script>. This is a
contradiction because <script type="math/tex; mode=display">a\frown b > b\frown a</script> and <script type="math/tex; mode=display">b\frown c > c\frown b</script>
implies <script type="math/tex; mode=display">a\frown c > c\frown a</script>. In other words, our custom comparator
preserves transitivity, so the sort is correct.</p>
<p>Once the array is sorted, the most "signficant" number will be at the front.
There is a minor edge case that comes up when the array consists of only
zeroes, so if the most significant number is <script type="math/tex; mode=display">0</script>, we can simply return
<script type="math/tex; mode=display">0</script>. Otherwise, we build a string out of the sorted array and return it.</p>
<iframe src="https://leetcode.com/playground/wVZb2DmS/shared" frameborder="0" width="100%" height="500" name="wVZb2DmS"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">\mathcal{O}(nlgn)</script>
</p>
<p>Although we are doing extra work in our comparator, it is only by a
constant factor. Therefore, the overall runtime is dominated by the
complexity of <code>sort</code>, which is <script type="math/tex; mode=display">\mathcal{O}(nlgn)</script> in Python and Java.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">\mathcal{O}(n)</script>
</p>
<p>Here, we allocate <script type="math/tex; mode=display">\mathcal{O}(n)</script> additional space to store the copy of <code>nums</code>.
Although we could do that work in place (if we decide that it is okay to
modify <code>nums</code>), we must allocate <script type="math/tex; mode=display">\mathcal{O}(n)</script> space for the final return
string. Therefore, the overall memory footprint is linear in the length
of <code>nums</code>.</p>
</li>
</ul>
<hr>
<p>Analysis and solutions written by: <a href="https://leetcode.com/emptyset">@emptyset</a></p>
          </div>
        
      </div>
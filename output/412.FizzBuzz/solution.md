<div class="article-body">
        
          <div class="block-markdown">
            <div class="toc">
<ul>
<li><a href="#solution">Solution</a><ul>
<li><a href="#approach-1-naive-approach">Approach 1: Naive Approach</a></li>
<li><a href="#approach-2-string-concatenation">Approach 2: String Concatenation</a></li>
<li><a href="#approach-3-hash-it">Approach 3: Hash it!</a></li>
</ul>
</li>
</ul>
</div>
<h2 id="solution">Solution</h2>
<hr>
<p>You must have played FizzBuzz as kids. FizzBuzz charm never gets old. And so here we are looking at how you can take on one step at a time and impress your interviewer with a better and neat approach to solve this problem.</p>
<h4 id="approach-1-naive-approach">Approach 1: Naive Approach</h4>
<p><strong>Intuition</strong></p>
<p>The moment you hear of FizzBuzz you think whether the number is divisible by <code>3</code>, <code>5</code> or both.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Initialize an empty answer list.</li>
<li>Iterate on the numbers from <script type="math/tex; mode=display">1 ... N</script>.</li>
<li>For every number, if it is divisible by both 3 and 5, add FizzBuzz to the answer list.</li>
<li>Else, Check if the number is divisible by 3, add Fizz.</li>
<li>Else, Check if the number is divisible by 5, add Buzz.</li>
<li>Else, add the number.
</li>
</ol>
<p><br></p>
<iframe src="https://leetcode.com/playground/kohPDrYw/shared" frameborder="0" width="100%" height="500" name="kohPDrYw"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N)</script>
</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(1)</script>
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-2-string-concatenation">Approach 2: String Concatenation</h4>
<p><strong>Intuition</strong></p>
<p>This approach won't reduce the asymptotic complexity, but proves to be a neater solution when <code>FizzBuzz</code> comes with a twist.
What if <code>FizzBuzz</code> is now <code>FizzBuzzJazz</code> i.e.
</p><pre>
3 ---&gt; "Fizz" , 5 ---&gt; "Buzz", 7 ---&gt; "Jazz"
</pre>
<p>If you try to solve this with the previous approach the program would have too many conditions to check:</p>
<ol>
<li>Divisible by 3</li>
<li>Divisible by 5</li>
<li>Divisible by 7</li>
<li>Divisible by 3 and 5</li>
<li>Divisible by 3 and 7</li>
<li>Divisible by 7 and 3</li>
<li>Divisible by 3 and 5 and 7</li>
<li>Not divisible by 3 or 5 or 7.</li>
</ol>
<p>This way if the <code>FizzBuzz</code> mappings increase, the conditions would grow exponentially in your program.  </p>
<p><strong>Algorithm</strong></p>
<p>Instead of checking for every combination of these conditions, check for divisibility by given numbers i.e. 3, 5 as given in the problem. If the number is divisible, concatenate the corresponding string mapping <code>Fizz</code> or <code>Buzz</code> to the current answer string.</p>
<p>For eg. If we are checking for the number 15, the steps would be:
</p><pre>
Condition 1: 15 % 3 == 0 , num_ans_str = "Fizz"
Condition 2: 15 % 5 == 0 , num_ans_str += "Buzz"
=&gt; num_ans_str = "FizzBuzz"
</pre>
<p>So for <code>FizzBuzz</code> we just check for two conditions instead of three conditions as in the first approach.</p>
<p>Similarly, for <code>FizzBuzzJazz</code> now we would just have three conditions to check for divisibility.</p>
<iframe src="https://leetcode.com/playground/kpRjpMFa/shared" frameborder="0" width="100%" height="500" name="kpRjpMFa"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity: <script type="math/tex; mode=display">O(N)</script>
</li>
<li>Space Complexity: <script type="math/tex; mode=display">O(1)</script>
<br>
<br></li>
</ul>
<hr>
<h4 id="approach-3-hash-it">Approach 3: Hash it!</h4>
<p><strong>Intuition</strong></p>
<p>This approach is an optimization over approach 2. When the number of mappings are limited, approach 2 looks good. But what if you face a tricky interviewer and he decides to add too many mappings?</p>
<p>Having a condition for every mapping is not feasible or may be we can say the code might get ugly and tough to maintain.</p>
<p>What if tomorrow we have to change a mapping or may be delete a mapping? Are we going to change the code every time we have a modification in the mappings?</p>
<p>We don't have to. We can put all these mappings in a <code>Hash Table</code>.</p>
<p><strong>Algorithm</strong></p>
<ol>
<li>Put all the mappings in a hash table. The hash table <code>fizzBuzzHash</code> would look something like <code>{ 3: 'Fizz', 5: 'Buzz' }</code></li>
<li>Iterate on the numbers from <script type="math/tex; mode=display">1 ... N</script>.</li>
<li>For every number, iterate over the <code>fizzBuzzHash</code> keys and check for divisibility.</li>
<li>If the number is divisible by the key, concatenate the corresponding hash value to the answer string for current number. We do this for every entry in the hash table.</li>
<li>Add the answer string to the answer list.</li>
</ol>
<blockquote>
<p>This way you can add/delete mappings to/from to the hash table and not worry about changing the code.</p>
</blockquote>
<p>So, for <code>FizzBuzzJazz</code> the hash table would look something like <code>{ 3: 'Fizz', 5: 'Buzz', 7: 'Jazz' }</code></p>
<iframe src="https://leetcode.com/playground/yRV2JDsz/shared" frameborder="0" width="100%" height="500" name="yRV2JDsz"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>Time Complexity : <script type="math/tex; mode=display">O(N)</script>
</li>
<li>Space Complexity : <script type="math/tex; mode=display">O(1)</script>
<br><br></li>
</ul>
<hr>
<p>Analysis written by: <a href="https://leetcode.com/godayaldivya/">@godayaldivya</a>.</p>
          </div>
        
      </div>
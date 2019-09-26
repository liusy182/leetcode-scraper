<div class="article-body">
        
          <div class="block-markdown">
            <h2 id="solution">Solution</h2>
<hr>
<h4 id="approach-1-elementary-math">Approach 1: Elementary Math</h4>
<p><strong>Intuition</strong></p>
<p>Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.</p>
<p align="center"><img alt="Illustration of Adding two numbers" src="../Figures/2_add_two_numbers.svg" width="539px"></p>
<p align="center"><em>Figure 1. Visualization of the addition of two numbers: <script type="math/tex; mode=display">342 + 465 = 807</script>.<br>
Each node contains a single digit and the digits are stored in reverse order.</em></p>
<p><strong>Algorithm</strong></p>
<p>Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of <script type="math/tex; mode=display">l1</script> and <script type="math/tex; mode=display">l2</script>. Since each digit is in the range of <script type="math/tex; mode=display">0 \ldots 9</script>, summing two digits may "overflow". For example <script type="math/tex; mode=display">5 + 7 = 12</script>. In this case, we set the current digit to <script type="math/tex; mode=display">2</script> and bring over the <script type="math/tex; mode=display">carry = 1</script> to the next iteration. <script type="math/tex; mode=display">carry</script> must be either <script type="math/tex; mode=display">0</script> or <script type="math/tex; mode=display">1</script> because the largest possible sum of two digits (including the carry) is <script type="math/tex; mode=display">9 + 9 + 1 = 19</script>.</p>
<p>The pseudocode is as following:</p>
<ul>
<li>Initialize current node to dummy head of the returning list.</li>
<li>Initialize carry to <script type="math/tex; mode=display">0</script>.</li>
<li>Initialize <script type="math/tex; mode=display">p</script> and <script type="math/tex; mode=display">q</script> to head of <script type="math/tex; mode=display">l1</script> and <script type="math/tex; mode=display">l2</script> respectively.</li>
<li>Loop through lists <script type="math/tex; mode=display">l1</script> and <script type="math/tex; mode=display">l2</script> until you reach both ends.<ul>
<li>Set <script type="math/tex; mode=display">x</script> to node <script type="math/tex; mode=display">p</script>'s value. If <script type="math/tex; mode=display">p</script> has reached the end of <script type="math/tex; mode=display">l1</script>, set to <script type="math/tex; mode=display">0</script>.</li>
<li>Set <script type="math/tex; mode=display">y</script> to node <script type="math/tex; mode=display">q</script>'s value. If <script type="math/tex; mode=display">q</script> has reached the end of <script type="math/tex; mode=display">l2</script>, set to <script type="math/tex; mode=display">0</script>.</li>
<li>Set <script type="math/tex; mode=display">sum = x + y + carry</script>.</li>
<li>Update <script type="math/tex; mode=display">carry = sum / 10</script>.</li>
<li>Create a new node with the digit value of <script type="math/tex; mode=display">(sum \bmod 10)</script> and set it to current node's next, then advance current node to next.</li>
<li>Advance both <script type="math/tex; mode=display">p</script> and <script type="math/tex; mode=display">q</script>.</li>
</ul>
</li>
<li>Check if <script type="math/tex; mode=display">carry = 1</script>, if so append a new node with digit <script type="math/tex; mode=display">1</script> to the returning list.</li>
<li>Return dummy head's next node.</li>
</ul>
<p>Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.</p>
<p>Take extra caution of the following cases:</p>
<table>
<thead>
<tr>
<th>Test case</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<script type="math/tex; mode=display">l1=[0,1]</script><br><script type="math/tex; mode=display">l2=[0,1,2]</script>
</td>
<td>When one list is longer than the other.</td>
</tr>
<tr>
<td>
<script type="math/tex; mode=display">l1=[]</script><br><script type="math/tex; mode=display">l2=[0,1]</script>
</td>
<td>When one list is null, which means an empty list.</td>
</tr>
<tr>
<td>
<script type="math/tex; mode=display">l1=[9,9]</script><br><script type="math/tex; mode=display">l2=[1]</script>
</td>
<td>The sum could have an extra carry of one at the end, which is easy to forget.</td>
</tr>
</tbody>
</table>
<iframe src="https://leetcode.com/playground/5onAHA8v/shared" frameborder="0" width="100%" height="378" name="5onAHA8v"></iframe>

<p><strong>Complexity Analysis</strong></p>
<ul>
<li>
<p>Time complexity : <script type="math/tex; mode=display">O(\max(m, n))</script>. Assume that <script type="math/tex; mode=display">m</script> and <script type="math/tex; mode=display">n</script> represents the length of <script type="math/tex; mode=display">l1</script> and <script type="math/tex; mode=display">l2</script> respectively, the algorithm above iterates at most <script type="math/tex; mode=display">\max(m, n)</script> times.</p>
</li>
<li>
<p>Space complexity : <script type="math/tex; mode=display">O(\max(m, n))</script>. The length of the new list is at most <script type="math/tex; mode=display">\max(m,n) + 1</script>.</p>
</li>
</ul>
<p><strong>Follow up</strong></p>
<p>What if the the digits in the linked list are stored in non-reversed order? For example:</p>
<p>
<script type="math/tex; mode=display">
(3 \to 4 \to 2) + (4 \to 6 \to 5) = 8 \to 0 \to 7
</script>
</p>
          </div>
        
      </div>
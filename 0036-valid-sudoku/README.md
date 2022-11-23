<h2><a href="https://leetcode.com/problems/valid-sudoku/">36. Valid Sudoku</a></h2><h3>Medium</h3><hr><div><p>Determine if a&nbsp;<code>9 x 9</code> Sudoku board&nbsp;is valid.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [9 x 9 스도쿠 보드가 유효한지 확인합니다.] </inliner>&nbsp;Only the filled cells need to be validated&nbsp;<strong>according to the following rules</strong>:<inliner class="im-inliner-dst-text" style="color: #239e23;"> [다음 규칙에 따라 채워진 셀만 확인하면 됩니다.] </inliner></p>

<ol>
	<li>Each row&nbsp;must contain the&nbsp;digits&nbsp;<code>1-9</code> without repetition.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [각 행에는 1~9의 숫자가 반복 없이 포함되어야 합니다.] </inliner></li>
	<li>Each column must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [각 열에는 1~9의 숫자가 반복 없이 포함되어야 합니다.] </inliner></li>
	<li>Each of the nine&nbsp;<code>3 x 3</code> sub-boxes of the grid must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [그리드의 9개의 3 x 3 하위 상자는 각각 반복 없이 1-9의 숫자를 포함해야 합니다.] </inliner></li>
</ol>

<p><strong>Note:<inliner class="im-inliner-dst-text" style="color: #239e23;"> [메모:] </inliner></strong></p>

<ul>
	<li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [스도쿠 보드(부분적으로 채워진)는 유효할 수 있지만 반드시 풀 수 있는 것은 아닙니다.] </inliner></li>
	<li>Only the filled cells need to be validated according to the mentioned&nbsp;rules.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [언급된 규칙에 따라 채워진 셀만 검증하면 됩니다.] </inliner></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px">
<pre><strong>Input:</strong> board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being modified to <strong>8</strong>. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> is a digit <code>1-9</code> or <code>'.'</code>.</li>
</ul>
</div>
<h2><a href="https://leetcode.com/problems/house-robber/">198. House Robber</a></h2><h3>Medium</h3><hr><div><p>You are a professional robber planning to rob houses along a street.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [당신은 거리를 따라 집을 털려는 전문 강도입니다.] </inliner> Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [각 집에는 일정 금액의 돈이 숨겨져 있습니다. 각각의 집을 강탈하지 못하도록 막는 유일한 제약은 인접한 집에 보안 시스템이 연결되어 있고 같은 밤에 두 개의 인접한 집이 침입한 경우 자동으로 경찰에 연락한다는 것입니다.] </inliner></p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <b>without alerting the police</b></em>.<inliner class="im-inliner-dst-text" style="color: #239e23;"> [각 집의 금액을 나타내는 정수 배열 숫자가 주어지면 오늘 밤 경찰에 알리지 않고 훔칠 수 있는 최대 금액을 반환합니다.] </inliner></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>
</div>
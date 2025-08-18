Library Book Circulation Tracker
Problem

Process a sequence of operations describing library activity. Each book belongs to a category and each copy has an insurance value (an integer “price”).
Return an array with the total insurance value for each checkout operation, in order.

Operation Formats

Acquisition

["acquisition", <category>, <quantity>, <price>]


Add <quantity> copies to <category>, each valued at <price>.

Checkout

["checkout", <category>, <quantity>]


Borrow <quantity> copies from <category>.
If multiple price levels exist in that category, remove the least valuable copies first.
You may assume the library always has enough copies to fulfill every checkout.

Reclassify

["reclassify", <category>, <quantity>, <original_price>, <new_price>]


Increase the value of <quantity> copies in <category> from <original_price> to <new_price>.
It’s guaranteed that at least <quantity> copies at original_price exist when this operation appears.

Input

operations: List[List[str]] — each inner list is one of the three operation formats above.

All numeric fields (quantity, price) are non-negative integers given as strings.

Constraints

1 ≤ len(operations) ≤ 100

3 ≤ len(operations[i]) ≤ 5

A solution with time complexity ≤ O(len(operations)^2) is acceptable.

Output

List[int] — one integer per checkout, the total insurance value of the books checked out by that operation.

Example

Input

operations = [
  ["acquisition", "fiction", "2", "100"],
  ["acquisition", "reference", "3", "60"],
  ["checkout", "fiction", "1"],
  ["checkout", "reference", "1"],
  ["reclassify", "reference", "1", "60", "100"],
  ["checkout", "reference", "1"],
  ["checkout", "reference", "1"]
]


Output

[100, 60, 60, 100]


Explanation

Acquire 2 fiction @100; acquire 3 reference @60.

Checkout 1 fiction → 100.

Checkout 1 reference (cheapest is 60) → 60.

Reclassify 1 reference 60→100.

Checkout 1 reference (cheapest among {60,100} is 60) → 60.

Checkout final reference (100) → 100.

Function Signature
def solution(operations: list[list[str]]) -> list[int]:
    ...

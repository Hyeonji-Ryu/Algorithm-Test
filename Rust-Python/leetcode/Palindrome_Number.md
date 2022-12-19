## Question
Given an integer x, return true if x is a palindrome, and false otherwise.



## Python code

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == ''.join(list(str(x))[::-1]) else False
```


## Rust code

```rust
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        format!("{x}").chars().rev().collect::<String>().parse().unwrap_or(0) == x
    }
}
```

# Python-Challenges

It's just a compilation of challenges of python that you can learn how to code and the logic of it.

<br>

## 🏆 Challenge 1: Recursive Function
### 📌 Topics: Recursion, String Manipulation

#### 🔹 Problem Statement
Given an **encoded string**, return its **decoded output** by following the pattern:

- A number `N` followed by `[ ]` means that the string inside the brackets should be **repeated `N` times**.
- The input string may contain **nested brackets**, which must be resolved **from the innermost to the outermost level**.

---

## 📥 Input & 📤 Output Examples

| Input            | Expected Output |
|-----------------|----------------|
| `"3[a]2[bc]"`  | `"aaabcbc"`     |
| `"3[a2[c]]"`   | `"accaccacc"`   |

---

## 🛠 Constraints
- The input string contains **only lowercase letters (`a-z`)**, digits (`0-9`), and square brackets (`[]`).
- The input is always **well-formed** (no unmatched brackets).
- The numbers **represent positive integers**.

---

## ✅ Expected Function Signature (Python)
```python
def decode_string(input: str) -> str:
    pass  # Implement the function here
```
<br>

---
---
## 🏅 Challenge 2: Reverse a String  
### 📌 Topics: String Manipulation  
#### 🔹 Problem Statement  
Write a function to **reverse a given string** without using `[::-1]` or `reversed()`.  

#### 📥 Input & 📤 Output Examples  
| Input       | Expected Output |
|------------|----------------|
| `"hello"`  | `"olleh"`       |
| `"Python"` | `"nohtyP"`       |

#### ✅ Expected Function Signature  
```python
def reverse_string(input: str) -> str:
    pass  # Implement functio


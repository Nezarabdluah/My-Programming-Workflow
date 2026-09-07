# Debugging Prompts — General Debugging Prompts

> Ready-to-use prompts for diagnosing and fixing errors with any stack.

---

## 1. General error diagnosis
```
This error appeared: [full error message]
In this file: [file name]

I want:
1. Root-cause analysis
2. The fix
3. A test preventing recurrence
4. Does it expose a wider gap in the code?
```

## 2. Slowness diagnosis
```
This part is slow: [description]
Response time: [X seconds]

Analyze:
1. Is the problem in the DB? (query plan, N+1, missing index)
2. Is the problem in the network? (large payload, too many requests)
3. Is the problem in the code? (heavy loop, memory)

Give me evidence before any solution.
```

## 3. Stack trace analysis
```
Here is the stack trace: [full stack trace]

Analyze:
1. What is the actual error?
2. Where exactly does it occur? (file + line)
3. What is the likely cause?
4. What is the fix?
```

## 4. Environment problem
```
The code works locally but fails in [environment]:
Error: [message]

Check:
1. Environment differences (environment variables, config)
2. Dependency versions
3. File/network permissions
4. DNS / connection strings
```

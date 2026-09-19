---
id: rules-testing
description: Behavior-driven testing, mocking discipline, black-box vs white-box balance, structured logging, tracing, resilience patterns, and the pre-delivery checklist. Load for test or quality work.
alwaysApply: false
globs: ["**/*test*/**", "**/*spec*/**", "**/Tests/**"]
requires: [REF-TEST-BEHAV, REF-TEST-MOCK, REF-OBS-LOG, REF-OBS-TRACE, REF-RES-CIRCUIT]
---

# Testing & Quality

> Load this file when the task concerns testing or quality assurance.

---

## 1. Test Strategy

### Test behavior, not implementation:
- ✅ Write tests that verify the functional outcome / contract
- ❌ Never test internal details or private methods
- ✅ If a behavior-preserving refactor breaks a test ← the test is badly designed

### Mocking discipline:
- ✅ Mock only external dependencies: mail servers, third-party APIs, files, network
- ❌ **Never** mock your own core logic or domain entities
- ✅ Use real domain objects in tests

### Black-box vs White-box balance:
- ✅ **Black-Box** (API/E2E): verify system boundaries, middleware, permissions
- ✅ **White-Box** (Unit): cover complex logical branches and edge cases

### Test quality:
- ✅ Tests = production code. Same quality bar
- ✅ Descriptive naming + AAA structure (Arrange, Act, Assert)
- ❌ No commented-out code in tests

---

## 2. Observability & Logging

### Structured Logging:
- ❌ Never log flat unstructured strings
- ✅ Use structured JSON including:
  - `timestamp` (ISO 8601)
  - `correlation_id` / `trace_id`
  - `user_id` (anonymized when needed)
  - `log_level` (Info, Warn, Error, Critical)
  - `exception_details`

### Distributed Tracing:
- ✅ Every service propagates and publishes `trace_id` in headers (W3C Trace Context)

### Metrics:
- ✅ **Latency**: track p95 and p99 (averages hide problems)
- ✅ **Errors**: error rate classified by type
- ✅ **Throughput**: request volume over time

---

## 3. Resilience

### Transient failure handling:
- Define timeouts for remote/external operations where hanging would harm the system.
- Retry only failures known to be transient and only when the operation is safe/idempotent or protected against duplicate effects.
- Use exponential backoff/jitter when retries are appropriate.
- Use circuit breakers primarily for unstable remote dependencies where failing fast improves resilience.
- Do not mechanically retry non-idempotent writes or wrap every database call in a circuit breaker.

### Graceful degradation:
- Provide graceful degradation/fallback only when stale/default behavior is safe and useful.
- Expose health/readiness signals appropriate to the deployment platform and critical dependencies; avoid health checks that create cascading load.

---

## 4. Pre-Delivery Checklist

> This list grows automatically as repeated mistakes escalate from learned-mistakes.md

- [ ] Build succeeds with zero errors
- [ ] All tests pass
- [ ] No new lint errors
- [ ] No console.log or debug print statements
- [ ] No exposed secrets in code
- [ ] No stack traces shown to the user
- [ ] Large/unbounded data lists have an appropriate server/client loading strategy
- [ ] New external input boundaries have appropriate validation
<!-- new items are added here when repeated mistakes escalate from learned-mistakes.md -->

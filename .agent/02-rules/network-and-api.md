---
id: rules-network-api
description: Payload optimization, chunky-vs-chatty request design, evidence-based latency diagnosis, and API design best practices. Load for API design or network performance work.
alwaysApply: false
globs: ["**/Controllers/**", "**/api/**", "**/*Client*"]
requires: [REF-NET-EVIDENCE, REF-NET-PAYLOAD, REF-NET-BATCH, REF-NET-LATENCY, REF-NET-COMPRESS]
---

# Network & API

> Load this file when the task concerns API design or network performance.

---

## 1. Payload Optimization

### Strict DTO pruning:
- ❌ Never send full domain entities or unused fields over the wire
- ✅ Design flat, small DTOs containing only the fields the UI requires

### Compression:
- ✅ Enable HTTP compression (GZIP, Brotli) for responses and APIs
- ✅ Static assets and scripts are served compressed

---

## 2. Request Design (Chunky vs Chatty)

### No queries in loops:
- ❌ **Never** write client code sending HTTP requests inside a loop
- ✅ Use the BFF (Backend For Frontend) pattern or an API Gateway to aggregate queries

### Aggregated endpoints:
- ✅ Design "chunky" endpoints returning aggregated data in one round-trip
- ❌ Never force the client into multiple "chatty" requests to assemble data

---

## 3. Evidence-Based Diagnosis

### No blind guessing:
- ❌ Never propose code or DB changes to fix slowness without evidence
- ✅ Request and analyze first:
  - Payload size
  - Response time
  - Browser Network tab metrics
  - TTFB (Time to First Byte)

### Latency isolation:
- ✅ Differentiate between:
  - **Server Response Time** — delay in DB or server logic
  - **Network Latency** — delay in packet transmission

---

## 4. API Design Best Practices

- ✅ Use HTTP verbs correctly: GET for reads, POST for creation, PUT for updates, DELETE for deletion
- ✅ Return appropriate HTTP status codes (200, 201, 400, 401, 403, 404, 500)
- ✅ Use API versioning (e.g. `/api/v1/`)
- ✅ Document every endpoint (OpenAPI/Swagger)
- ✅ Add rate limiting to every public endpoint
- ✅ Use pagination on every endpoint returning lists

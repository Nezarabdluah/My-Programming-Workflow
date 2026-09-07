# Master Pipeline — Stage 8: Post-Launch Monitoring

> This is stage 8 of 8 (final stage).
> Required for: 🔴 | Skipped for: 🟢 🟡

---

## Decision Gate

```yaml
gate:
  stage_number: 8
  stage_name: "Post-Launch Monitoring"
  classification_required: [🔴]
  previous_stage_status: passed       # stage 7 must pass
  requires:
    - successful deployment (stage 7)
    - monitoring infrastructure active
  resources_loaded:
    - "⚠️ MANDATORY: read 05-references/books/00-master-index.md → Stage 8 row"
    - constitutions: perf-constitution (query performance in production)
    - wiring-registry → OPS-DORA, OPS-SIGNALS, OPS-OBSERVABILITY
  decision: proceed | skip

# Skip condition: classification ∈ {🟢, 🟡}
#   → ⛔ GATE SKIPPED — classification does not require post-launch monitoring
```

---

## Task: post-launch observation and metrics

### 8.1 — Health Monitoring (first 24-72 hours)

```
□ Monitor key signals (grep [OPS-SIGNALS]):
  - Error rate: baseline vs current
  - Latency: p50, p95, p99 vs SLO targets (stage 6)
  - Throughput: requests per second vs expected
  - Resource utilization: CPU, memory, disk, connections

□ Check alerting:
  - Are alerts firing? → investigate and resolve
  - Are alerts silent? → verify they are correctly configured (not a false negative)
```

### 8.2 — DORA Metrics Capture

```
□ Record DORA metrics for this release (grep [OPS-DORA]):

  | Metric                   | Value |
  |--------------------------|-------|
  | Deployment Frequency     |       |
  | Lead Time for Changes    |       |
  | Mean Time to Recovery    |       |
  | Change Failure Rate      |       |

□ Compare against team baselines (if available)
```

### 8.3 — User Impact Assessment

```
□ Assess the user-facing impact:
  - Feature adoption rate (if measurable)
  - User-reported issues (support tickets, error reports)
  - Performance impact on existing features
  - Any unexpected behavior or side effects
```

### 8.4 — Retrospective & Lessons Learned

```
□ Conduct a brief retrospective:
  - What went well?
  - What could be improved?
  - Were there any surprises?
  - Any near-misses or close calls?

□ Record lessons in 04-memory/learned-mistakes.md (Type B mistakes)
□ Update 04-memory/project-knowledge.md with new patterns discovered
```

### 8.5 — Pipeline Closure

```
□ Mark the pipeline as complete:
  → ✅ GATE PASSED — pipeline complete

□ If critical issues found post-launch:
  → Open a new pipeline iteration (return to stage 0 with the issue as input)
  → ⛔ GATE FAILED — post-launch issue requires immediate attention
```

---

## Resource Injection (from wiring-registry)

| Resource | When |
|----------|------|
| DevOps: grep `[OPS-DORA]` | DORA metrics capture |
| DevOps: grep `[OPS-SIGNALS]` | Health signal monitoring |
| DevOps: grep `[OPS-OBSERVABILITY]` | Observability verification |
| DevOps: grep `[OPS-SLO]` | SLO compliance check |

---

## Gate Output

```yaml
gate_result:
  stage: 8
  status: ✅ GATE PASSED | ⛔ GATE FAILED
  monitoring_period: "24h | 48h | 72h"
  error_rate_stable: true | false
  latency_within_slo: true | false
  dora_metrics_captured: true | false
  retrospective_completed: true | false
  pipeline_status: complete | requires_iteration
  blockers: []
```

> After gate passes → pipeline is DONE. Update all memory files with final status.
> Execute `03-workflows/end-session.md` closeout protocol.

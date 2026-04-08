import os
import sys

import wandb


run_id = sys.argv[1]

api = wandb.Api()

ENTITY = "prachwanikanchan1-thomson-reuters"
PROJECT = "mlops-course-project"

# Fetch baseline run
runs = api.runs(f"{ENTITY}/{PROJECT}")
baseline_run = None

for r in runs:
    if "baseline" in r.tags:
        baseline_run = r
        break

if not baseline_run:
    raise Exception("No baseline run found")

target_run = api.run(f"{ENTITY}/{PROJECT}/{run_id}")

# Simple comparison
baseline_metrics = baseline_run.summary
target_metrics = target_run.summary

report = f"""
## W&B Run Comparison

**Baseline Run:** {baseline_run.id}  
**Target Run:** {target_run.id}

### Metrics Comparison:
"""

for key in baseline_metrics:
    if key in target_metrics:
        report += f"- {key}: baseline={baseline_metrics[key]}, target={target_metrics[key]}\n"

# Save report
with open("report.md", "w") as f:
    f.write(report)

report_url = f"https://wandb.ai/{ENTITY}/{PROJECT}/runs/{target_run.id}"

print("REPORT_URL=" + report_url)

# Export for GitHub Action Workflow
with open(os.environ["GITHUB_ENV"], "a") as f:
    f.write(f"REPORT_URL={report_url}\n")
    

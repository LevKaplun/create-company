# What the roles read

Read at the time of use, only the parts the task needs. Never copy any of it into this repo.{{EXCLUDED_LINE}}

## The living docs: company facts

| Doc | Where | How to read |
| --- | --- | --- |
{{LIVING_DOCS_ROWS}}

## The strategy files: plans, briefs and what has been thought so far

Knowledge, not rules: where things stand, what was considered and why. Weigh it with your own judgment.

| File | Where | What it holds |
| --- | --- | --- |
{{STRATEGY_ROWS}}

## Evidence: dated research

| What | Where |
| --- | --- |
{{EVIDENCE_ROWS}}

## When sources disagree

On facts the newest information wins, and what {{OWNER_NAME}} just said is the newest. Plans and advice are never a
rule. When it is still unclear, say so and ask. Pipe a long doc through `grep -n` to find the section you need.
When a doc gets a new version or file name, only this index changes.

<!-- How to read common formats (pick the right command per row):
  .md .txt .csv         Read tool
  .docx .doc .rtf       macOS: textutil -convert txt -stdout "<path>"   Linux: pandoc -t plain "<path>"
  .pdf                  pdftotext "<path>" -   (poppler)   or the Read tool, which reads PDFs page by page
  a file in a git repo  git -C <repo> show origin/<branch>:<path>   (the merged version, never a work branch)
-->

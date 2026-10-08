# What the roles read

Read at the time of use, only the parts the task needs. Never copy any of it into this repo.{{EXCLUDED_LINE}}

## The living docs: company facts

| Doc | Where | How to read |
| --- | --- | --- |
{{LIVING_DOCS_ROWS}}

## Decision records: what was decided, and when

| Record | Where | Read it for |
| --- | --- | --- |
{{RECORD_ROWS}}

## Evidence: dated research

| What | Where |
| --- | --- |
{{EVIDENCE_ROWS}}

## When sources disagree

The living docs win on facts; a dated fact found only in a record may be used, cited with its record and date. On
decisions, the newest dated record wins. When it is still unclear, say so and ask. Pipe a long doc through
`grep -n` to find the section you need. When a doc gets a new version or file name, only this index changes.

<!-- How to read common formats (pick the right command per row):
  .md .txt .csv         Read tool
  .docx .doc .rtf       macOS: textutil -convert txt -stdout "<path>"   Linux: pandoc -t plain "<path>"
  .pdf                  pdftotext "<path>" -   (poppler)   or the Read tool, which reads PDFs page by page
  a file in a git repo  git -C <repo> show origin/<branch>:<path>   (the merged version, never a work branch)
-->

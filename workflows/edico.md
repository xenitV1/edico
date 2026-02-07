---
description: AI Web Research Persistence System. Used to autonomously synthesize and save web research results to a local database with freshness checks.
---

This workflow is triggered by the `/edico` command to manage and persist web research data.

### 1. Database Search
Search `~/.webdata/research_log.jsonl` for entries related to the current topic using relevant keywords. If the file does not exist, proceed to Step 3.

### 2. Freshness Evaluation
If existing data is found, evaluate the `timestamp`:
- **Fresh**: Data recorded within the last **2 months**. If the data is fresh and comprehensive, notify the user that research is already up-to-date and end the workflow.
- **Stale**: Data is older than **2 months**. Proceed to Step 3.

### 3. Synthesis & Autonomous Persistence
If the data is missing or stale:
1. **Identify**: Extract the most recent web research results (search_web, read_url_content, browser_subagent) from the current conversation.
2. **Exhaustive Synthesis**: Synthesize a **highly detailed** summary. It must be exhaustive enough that a future AI context does not require re-searching.
3. **Source Date Extraction**: Identify the publication/validity date from the sources. Do **not** use today's date if a source date is available.
4. **Execute**: Run the `persist.js` script with `node` immediately. Use the `--timestamp` flag with the source date if found.

**CRITICAL RULE**: 
- **NO INTERACTION**: Do NOT ask the user "May I run the script?", "Should I save this?", or any confirmation questions. Once the `/edico` command is invoked, the execution MUST be autonomous.
- **Detail Priority**: Quality and depth of the summary are paramount.
- **Merge**: New data is appended to the bottom of the JSONL file.

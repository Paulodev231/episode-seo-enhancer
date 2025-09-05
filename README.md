# Episode SEO & Distribution Enhancer

Prepared by: PauloDev231  
Contact for install help: https://x.com/TheAiGeng

What this does (short)  
An automated pipeline that detects new RSS episodes, pulls or generates a transcript, produces SEO-optimized title variants, chapter timestamps, full show notes, three X hooks, and a six-line LinkedIn caption. Metadata is saved to Airtable or Google Drive, scheduled to social via a scheduler, and a Notion review task is created for manual checks when required.

Why it helps  
Improves discoverability and creates multiple ready-to-share assets for every episode. Pilots showed measurable uplifts in organic downloads and social engagement within 30 days.

What's included
- workflows/01-episode-seo-enhancer.json  (n8n import file)
- templates/show_notes_template.txt
- samples/sample_rss_item.json
- scripts/generate_transcript_stub.py
- commit_history_template.txt
- README.md
- .gitignore

Before you start (what you need)
- An n8n instance (cloud or local). Local requires Docker.
- OpenAI or transcription service credentials (optional).
- Airtable account or Google Drive access for metadata storage.
- Notion account and database for review tasks (optional).
- A social scheduler account (e.g., Buffer) for scheduled posts (or use the HTTP scheduler node).
- Slack or email for alerts (optional).


Notes: this is a skeleton. After import you will:

Set credentials in n8n (OpenAI, Airtable, Google Drive, Notion, Social Scheduler).

Update the RSS Feed node to your real RSS feed URL.

Configure environment variables (e.g., AIRTABLE_APP_ID, NOTION_DATABASE_ID, SOCIAL_SCHEDULER_APP) inside n8n.


Step-by-step setup (non-technical)
1. Import the workflow: In n8n choose Import → Import from File → select workflows/01-episode-seo-enhancer.json.
2. Add credentials in n8n: OpenAI (or transcription), Google Drive, Airtable, Notion, Social Scheduler. Keep keys private.
3. Edit the RSS Feed node: replace the example feed URL with your podcast RSS feed URL.
4. Create a test episode: use samples/sample_rss_item.json and scripts/generate_transcript_stub.py to create a small transcript for testing. Point the fetch-audio node at a small local file or URL.
5. Run the workflow manually once. Verify results: Airtable record created, show notes file in Google Drive, Notion task created, and social scheduler received the scheduled post payload.

Testing tips
- Use the included transcript stub for a quick run without calling transcription services.
- Start with Airtable or Google Drive to confirm metadata is saved before enabling scheduling.
- Keep a "review" Notion task enabled so a human can approve metadata before social posts go live.

Acceptance criteria (how to know it's working)
- A manual test run creates a new metadata record in Airtable/Drive.
- Show notes file appears in the chosen storage location.
- A Notion task is created with the episode title and status "Review".
- The social scheduler receives a scheduled post payload (check the scheduler UI).

Notes and recommendations
- The generator creates multiple title variants for quick A/B testing — pick the best-performing title for publishing.
- Adjust prompt wording in the OpenAI node to match your brand voice.
- Keep credentials out of the repo. Share them securely when configuring n8n.

Quick GitHub upload (5 lines)
1. Go to github.com and sign in, click + → New repository, name it `episode-seo-enhancer` and create it.
2. Click Add file → Upload files, drag-and-drop the unzipped project folder contents (all files and folders).
3. Confirm no `.env` or secret files are included, enter commit message `Initial upload: episode-seo-enhancer` and Commit changes.
4. Optional: in Releases, create a release and upload the ZIP for easy download.
5. Share the repo link with your integrator or post it to https://x.com/TheAiGeng for install help.

License: MIT


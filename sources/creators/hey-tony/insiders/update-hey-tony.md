# Update Runbook: fold new HeyTony calls into the /heyTony skill

Run this weekly-ish (daily calls drop, but the playbook only needs a weekly fold-in). Any Claude
session with the logged-in `htinsiders.com` browser tab can execute it end to end. It is designed
to be cheap on a small delta (a handful of new calls), not a full 144-agent rebuild every time.

**The one manual dependency:** pulling transcripts needs the authenticated membership.io session
(httpOnly cookie in the chrome-devtools browser profile). If the session has expired, log in first
at `htinsiders.com/login` (Rahul's membership). A headless cloud/cron agent cannot do this step,
which is why updates run in a browser-capable session, not an unattended cloud routine.

## Step 1 - Ensure logged in
Open `https://htinsiders.com/` via chrome-devtools. If redirected to `/login`, sign in
(email `rahul.lalia23@gmail.com`; Rahul provides the password). If `pkill -f chrome-profile`
is needed to free a stuck browser, do that first (known gotcha).

## Step 2 - Enumerate the Call Replays playlist (htinsiders.com origin)
Run this `evaluate_script` on the `htinsiders.com` tab; it saves the fresh listing to disk:
```js
async () => {
  const hub='JkjwBkopdD', playlist='NjLAZpDgOq';
  const j=async u=>{const r=await fetch(u,{headers:{accept:'application/json','x-requested-with':'XMLHttpRequest'},credentials:'include'});return r.ok?r.json():{__err:r.status};};
  let page=1, all=[], guard=0;
  while(guard++<20){
    const resp=await j(`/api/hub/${hub}/${playlist}/files?page=${page}&sort=position`);
    const data=resp.data||[]; if(!data.length) break;
    for(const f of data) all.push({hash:f.hash,title:f.title,len:Math.round(f.meta?.length||0),tr:f.has_transcription,desc:f.description||null});
    if(resp.meta?.last_page && page>=resp.meta.last_page) break; page++;
  }
  return {count:all.length, items:all};
}
```
Save the returned JSON to `build/freshPlaylist.json` (use the evaluate_script `filePath` arg).

## Step 3 - Detect new calls
`python3 build/deltaDetect.py` -> writes `build/newCalls.json` and lists what's new. If zero, stop.

## Step 4 - Pull transcripts for the new calls (app.membership.io origin)
Open a tab on `https://app.membership.io/` (any embed URL works), then `evaluate_script` a loop
that fetches `/file/{hash}/embed/caption?type=vtt` for each hash in `build/newCalls.json`
(same pattern as the original pull - MUST be from the app.membership.io origin or CORS blocks it;
cookies ride along automatically). Save raw results, then clean with the same VTT->txt logic used
in the original build (strip WEBVTT/timestamps/cue-numbers, dedupe consecutive lines). Write clean
`.txt` into `transcripts/` (continue the NNN_ numbering) and raw `.vtt` into `transcriptsRaw/`.
Update `inventory.json` (append the new items with their AI summaries) and `summaries.md`.

## Step 5 - Fold into the playbook (incremental, cheap)
For a small delta, do NOT rerun the whole workflow. Instead:
1. Extract each new call to a digest in `build/extractions/` (one sonnet agent per call, same
   extraction prompt as `build/synthesisWorkflow.js`).
2. Categorize each new call (see `deltaDetect`/title -> technical / webDesign / rankWeek / content /
   diagnostics / workSession / misc) and dispatch ONE agent per affected Part of
   `hey-tony-playbook.md` to integrate the new digests in place: merge genuinely new tactics/numbers/
   cases, dedupe against what's already there, keep structure and the no-em/en-dash rule. Parts:
   I philosophy/system · II keywords/content · III on-page/money-pages ·
   IV technical/web-design/internal-linking · V off-page/AI-search · VI tools/local/ecom/mindset.
3. Rebuild only if warranted (many new calls, or quarterly): rerun `build/synthesisWorkflow.js`
   after regenerating `build/build_plan.json` from the updated inventory.

## Step 6 - Publish to the skill + log
- Copy the updated playbook into the skill: `cp hey-tony-playbook.md ../../skills/skills/heyTony/reference/heyTonyPlaybook.md`
- Append a dated line to `log.md` (how many calls folded in, which Parts touched).
- Confirm no em/en dashes: the playbook and SKILL.md must stay dash-clean.

## Cadence
Weekly or biweekly is plenty. If several weeks are skipped, deltaDetect still catches everything
since the last capture - it diffs against `inventory.json`, not against a date.

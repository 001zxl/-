# Production Loop

Use this to turn repeated image work into a growing ecommerce visual knowledge base.

## Project Lifecycle

### 1. Intake Record

Capture:
- Product/category.
- Brand and packaging facts.
- Platform/use.
- Target audience.
- Required image count and ratios.
- User preferences and disliked styles.
- Source image paths.

### 2. Reference Study

Do:
- Search or inspect references when current style matters.
- Extract reusable patterns.
- Separate market pattern from copyable design.
- Note source and date in `source-log.md` when the reference meaningfully changes the skill.

### 3. Image Map

Build before generation:

```text
Image 01: role, ratio, style, product preservation, core copy.
Image 02: role, ratio, style, proof point, core copy.
Image 03: role, ratio, style, scene/use, core copy.
```

For batches of 6+ images, use an experiment matrix before prompting:
- Role: main image, detail first screen, proof, scene, trust, variant, promo, cover.
- Style territory: no adjacent images should share the same composition, background, prop system, headline rhythm, and color story.
- Product lock: choose the strongest source photo for brand/packaging identity, then add secondary references only for shape, back label, variants, or scene cues.
- Copy plan: one headline, one subhead, up to three labels; make each image own a different selling angle.
- Fatigue check: flag repeated wood tables, warm side light, sticker badges, macro piles, or identical claims before generation.
- QA cadence: inspect every 1-3 generations; repair drift before continuing the batch.

### 3A. Claim Confidence

Assign every claim a confidence level before it appears in a prompt or final note:
- Source-visible: directly visible in supplied product images.
- User-provided: explicitly provided by the user.
- Verified external: confirmed from a current source and logged when needed.
- Inferred: reasonable visual/category inference; mark as draft-only.
- Speculative: do not use unless the user approves or evidence is found.

Never treat AI-generated labels, barcodes, nutrition tables, certifications, rankings, medical/health benefits, origin, factory-direct wording, or price/discount text as verified.

### 4. Generation Notes

For each generated image, record:
- Prompt summary.
- Reference images used.
- Model/tool used.
- Output path.
- What worked.
- What failed.
- Whether text is final or needs compositing.
- Claim confidence notes.
- Recommended use: main image, detail module, livestream cover, carousel, ad test, or experiment only.

### 5. QA Score

Score from 1-5:
- Product identity.
- Platform fit.
- Style freshness.
- Mobile readability.
- Claim safety.
- Conversion clarity.

Keep images scoring below 3 as experiments unless the user explicitly accepts them.

### 5A. Text And Label Handling

For listing-ready ecommerce assets, prefer one of two paths:
- Minimal generated text: let the model create the scene and reserve clean negative space, then composite final text manually.
- Draft generated text: allow large, simple Chinese text for exploration, but mark all text as needing final human/post-production review.

For regulated or label-heavy categories such as food, supplements, beauty, baby, electronics, and appliances, small generated text should never be used as the final legal label.

### 6. Knowledge Update

Update:
- `pattern-library.md` for visual patterns.
- `model-capabilities.md` for model/tool behavior.
- `category-playbook.md` for category-specific discoveries.
- `image-specs.md` for platform/spec findings.
- `source-log.md` for external references.

## Update Discipline

Only add concise, reusable lessons. Avoid storing one-off project details unless they reveal a general rule.

## Autonomous Maintenance

For this user's ecommerce visual work, Codex is responsible for judging when the skill should be improved. Do not wait for the user to supervise every update.

After each relevant product-image, prompt-engineering, market-reference, QA, or generation task:
- Decide whether the work produced a reusable lesson, not just a one-off result.
- Update the local skill when a new pattern, category rule, platform rule, compliance risk, model behavior, or workflow improvement is likely to help future projects.
- Sync the repository copy and push to GitHub when the user has asked for GitHub-backed continuity or when the change materially improves the shared skill.
- Keep updates concise and evidence-based; do not add private product details unless they teach a general rule.
- Mention in the final response whether the skill was updated and whether it was synced to GitHub.

Useful update examples:
- "For transparent pouches, identity lock works better when front and back packaging photos are both provided."
- "For skincare, request texture swatch separately from product packshot to avoid distorted labels."
- "For Douyin snack covers, sticker labels work best when limited to 3 short phrases."

Bad update examples:
- Long diary entries.
- Exact private product copy.
- Unverified claims.
- Entire prompts that only work for one SKU.

## Periodic Refresh

When the user asks for latest/current/hot styles:
1. Browse current sources.
2. Update `trend-watch.md` or `source-log.md` only if a reusable pattern is found.
3. Mention whether the answer is refreshed live or based on local knowledge.

## Suggested Future Additions

- Platform-specific exact export presets when verified.
- Category-specific compliance notes.
- Before/after prompt repair examples.
- Brand-kit ingestion workflow.
- Text-compositing templates for final copy accuracy.
- A/B variant naming and scoring system.

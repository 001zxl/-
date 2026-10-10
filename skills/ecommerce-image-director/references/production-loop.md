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

### 2A. Placement And Market Gate

Classify every deliverable before choosing a style:
- Marketplace PDP/listing image.
- Paid or organic social creative.
- Short-video or livestream cover.
- In-video or in-livestream visual.
- Storefront, banner, or independent-site module.

Record the exact market or seller region when platform rules differ. Do not transfer a high-conversion ad style directly into a strict listing slot. A platform may allow bold text and generated scenes in promotional creative while requiring a plain physical product photo for the PDP main image.

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

### 4A. Editable-Master Handoff

When the tool supports structured or layered output, preserve a reusable campaign master instead of keeping only a flattened AI image:

- Keep the verified product photo or product lock separate from generated background, lighting, props, text, badges, and legal copy.
- Keep headlines, prices, claims, specifications, and logos as editable objects so they can be corrected or localized without regenerating the product.
- Export platform-ready raster files from the approved master, but archive the layered source, source product photos, font information, and copy version together.
- Canva now says Magic Layers is available to all users through its ChatGPT and Gemini connections and can convert a flat AI image into live text and selectable objects. Use it as an editable-master handoff when available, but inspect layer boundaries, background regeneration, product edges, packaging, and copy; availability does not make the decomposed result accurate or listing-ready.

### 4B. Revision Lineage And Recipe Reuse

When a generation is close to approval, continue from that asset and its exact recipe instead of rebuilding the concept from a fresh prompt:

- Save the parent output, full prompt and negative prompt, model and version, reference files and their roles, aspect ratio, resolution, seed or other exposed settings, and the specific edit request. A prompt summary alone is not enough to reproduce a packaging-sensitive result.
- Change one deliberate variable per revision when diagnosing product drift, layout changes, or style changes. Link every child output to its parent so the approved product lock and the cause of regressions remain visible.
- Separate creation from finalization. Record the approved generation before upscaling, cropping, format conversion, metadata insertion, or export, then run product, text, claim, and metadata QA on the final delivery derivative.
- Prefer tools that expose the recipe behind a selected image and can reuse it for a new generation. Recraft Studio's August 2026 interface surfaces the prompt, model, and settings through Modify, copies them through Reuse, and separates upscaling/export under Finalize. Treat this as a convenient implementation of the lineage rule, not a substitute for an external campaign manifest.

### 4B.1 Conversational Adobe Batch-Finishing Handoff

Adobe's September 2026 Gemini and Claude integrations add a guarded finishing route after the product identity and copy are approved:

- Use Adobe in Gemini to normalize lighting, color, and crop across a rights-cleared product-photo set, then derive storefront, website, and social-channel variants from the approved master. Do not ask the connector to invent missing pack views, labels, accessories, or SKU facts.
- Use the Adobe for Claude layer-based Express editor when a channel variant needs direct control over images, copy, colors, or fonts without regenerating the entire design. Keep the canonical packshot and approved copy version linked to every derivative.
- Treat conversational orchestration as a production convenience, not an approval step. Record the Adobe surface, connected account, source assets, requested operations, output dimensions, and derivative lineage; then rerun product, text, claim, crop, color, and metadata QA on every exported channel file.
- Verify live setup, entitlement, compatibility, and availability before scheduling a batch. Adobe says both integrations began a global rollout on September 24, but compatibility and availability can vary.

### 4B.2 Provider Asset-Registry Handoff

When a generation provider exposes a reusable asset registry, link it to the campaign manifest instead of replacing the campaign archive with it:

- Record provider, workspace, asset ID, model, source SKU, prompt/parameter record, rights basis, approval state, and file hash. Reusing an ID is an input convenience, not evidence that the asset is correct or approved.
- Confirm that the output exists in the correct provider workspace before another job depends on it. Alibaba Cloud's Asset Center is now open to all users and includes Qwen Image 3.0/3.0 Pro plus selected Qwen Image 2.0, Z-Image Turbo, and Wan 2.7 routes, but the live console list still determines coverage.
- Do not assume a newly released route is captured. The current Asset Center list does not name `qwen-image-2.1-pro` or `qwen-image-2.1-turbo`; for those routes, download the 24-hour result URL immediately, hash and archive the file, and retain the references, prompt, parameters, model, region, workspace, rights basis, and approval in the external manifest until live coverage is explicitly confirmed.
- Separate read/delete access from transfer administration. Alibaba's current Reader role can browse, inspect, and delete assets, while the Admin role additionally controls OSS transfer; grant the narrowest role that fits the operator and record who can release or permanently delete campaign assets.
- For automatic provider-to-object-storage transfer, include the workspace in the destination path, review failures and retries, and verify the destination object before releasing the provider copy. Alibaba's OSS transfer setting is global across workspaces even though Asset Center browsing is workspace-scoped.
- Keep the original product source, approved editable master, final delivery derivative, and disclosure/provenance metadata under the campaign's own retention policy. Platform storage is currently limited and may become billable above the advertised 5 GB free allowance; recycle-bin items remain stored for 30 days and are not the rollback plan.

### 4C. Style-Locked Batch And Protected Local Edit

When a campaign needs a stable visual system across different products or placements, maintain two independent locks:

- Product lock: real SKU photos and verified copy control package geometry, logo, label, colorway, included items, and claims.
- Style lock: rights-cleared references control rendering technique, palette, texture, composition, and lighting. For Recraft V4 Styles, begin with one clean reference; add similar references to narrow the look or diverse references to widen it, then save the `style_id`, compatible model, and `precise` or `flexible` match mode.
- Batch gate: generate a small set with deliberately different compositions before scaling. Reject the style route if it preserves the look but weakens SKU identity, text accuracy, category proof, or placement diversity.
- Repair gate: once a product asset is approved, edit only the intended region. A masked instruction or visual markup should leave verified logos, faces, packaging, and legal copy outside the mask; keep the edit as a separate layer and inspect mask edges plus the final flattened derivative before export. When a route promises exact copying outside the edited area, such as Ideogram 4.5 Precise Edit, archive the source and mask, compare the protected region pixel by pixel, and separately inspect fine detail because oversized inputs may still be internally scaled.

### 4D. Shopify Agentic Storefront Syndication Gate

When a Shopify store is eligible for Agentic Storefronts, treat the product-media library as a multi-channel feed rather than a theme-only gallery:

- Record the Shopify product, variant or option mapping, source image ID, rights basis, approved claims, alt text, and channel availability for every syndicated image. Shopify Catalog can send product images together with structured product data to supported AI shopping channels, so a correct storefront crop is not proof that the image is mapped or presented correctly elsewhere.
- Preview the product card or conversational result in each available channel when possible. Check exact SKU, selected color or size, product identity, crop, stale price/offer text baked into the image, and whether an image intended only for a secondary explanation is being promoted as the lead visual.
- Keep visibility governance separate from image editing. Turning off Shopify Catalog access for a channel does not prevent public web crawling or other external feeds from discovering the product. If the product or its images must be hidden, escalate the product-status and indexing decision; do not represent a Catalog toggle as universal removal.

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

### 5B. AI Disclosure And Product-Truth Gate

For Google Merchant Center and Google advertising derivatives, retain the required AI provenance on the final file. Use IPTC `DigitalSourceType=TrainedAlgorithmicMedia` for output created with a trained generative model, `CompositeSynthetic` for a composite that includes synthetic elements, and `AlgorithmicMedia` only for imagery created purely by an algorithm that is not based on sampled training data. Choose from the real creation path instead of treating the values as interchangeable. Verify the field after every resize, compression, format conversion, DAM, or CDN step. This requirement and any visible AI label are separate checks; neither removes the need for an accurate, unobstructed product image.

For hosted model dependencies, add lifecycle status to the production manifest beside model ID, region, and snapshot. Block new recurring catalog work on deprecated endpoints even before their retirement date when the provider withdraws normal availability coverage; Alibaba Cloud's Model Inference Service SLA amendment effective September 28, 2026 excludes errors caused by officially deprecated models from the SLA calculation. Move the job to a supported route only after representative-SKU regression for package geometry, text, color, material, edit drift, batch consistency, latency, and cost.

For Google advertising delivery, also record the AI-label decision per campaign, asset, and target geography. Google exposes a platform AI-label setting across Google Ads, Display & Video 360, Campaign Manager 360, Merchant Center, and Google Ads Editor; designated assets appear in the global `How this ad was made` panel, and ads targeting the European Union, India, or New York can receive a visible overlay. If the label is composited into the creative, keep it clear of responsive-crop edges and turn off enhancement options that can crop it. Verify the final label status in the live asset library or report because the setting, visible overlay, SynthID/C2PA, and Merchant Center IPTC provenance are distinct controls.

For Google Ads creative automation, record whether each campaign uses Suggested assets review, individual asset-optimization controls, or full automation. Review Suggested assets before adding them, but do not assume that review tab is a universal approval queue: enabled text customization or image-enhancement controls can add derivatives directly to campaigns. Save Google AI source and lineage before accepting a suggestion because an accepted asset is subsequently reported as advertiser-created. Audit the live Asset report and responsive placements after launch, including exact SKU, copy, claims, crop, disclosure, and brand consistency.

For TikTok Automated Creative, freeze the selected optimization features in the campaign manifest before publishing because the platform says they cannot be changed afterward. Treat upscaling, full-width image resizing, and TikTok Ad Network's black-edge or Gaussian-blur fills as new delivery derivatives; preview each real placement and create native-ratio source assets when automation weakens product prominence, text safety, disclosure, or brand quality.

For TikTok Smart+ Catalog Ads, separate manually uploaded catalog creative from assets sourced by Catalog Image & Video Auto-Crawl. Enabling Auto-Crawl allows TikTok to scan public landing pages, filter for product-relevant media, and make eligible images or videos available for delivery; public availability is not a rights, freshness, or SKU-accuracy approval. Archive the allowed domains and source URLs, crawl time, asset IDs or hashes, linked SKUs, ownership or license evidence, claim/disclosure status, and the accepted launch pool. Creative Upgrades can rank historical, trending, and AI-generated assets for setup review, and auto-add can introduce fresh creative after launch, so record that toggle and run a scheduled served-asset audit instead of treating launch approval as final. Exclude or disable any asset with stale offers, wrong variants, unsupported claims, unclear rights, missing disclosure, unsafe crops, or brand-fit failure.

Before publishing AI-assisted ecommerce creative:
- Check whether the specific platform, market, and placement requires AI disclosure or automatic labeling.
- Check whether disclosure is carried in visible copy, an upload control, or embedded file metadata. Record the required field and value in the export manifest instead of treating a visual label as a universal solution.
- Preserve the physical product's size, color, shape, features, contents, and realistic result. Do not let a generated scene turn into a product-not-as-described claim.
- Treat lighting, cleanup, noise reduction, restrained color correction, and background changes as lower-risk only when they do not change product information.
- For TikTok Shop United States promotional content, disclose fully generated or significantly AI-altered content using the platform setting or an in-content notice. Do not create fake experts, endorsements, or unrealistic effects.
- TikTok's September 2026 AIGC guidance says official TikTok AI effects may be labeled automatically, but third-party AI tools still require a disclosure decision. Technical metadata may trigger a platform label, yet the absence of an automatic label does not remove the creator's duty to self-disclose when required. Do not mark non-AI content as AI-generated merely to be safe: false disclosure is also a violation. Record the generation/editing source, disclosure route, posting surface, and visible/automatic label outcome for the final asset.
- For TikTok Shop US video, image, and cover promotion, compare the depicted physical SKU with the PDP and reliable evidence: size, material, color, quantity, accessories, compatibility, installation, safety, and result claims. Product-realism QA is distinct from disclosure; a correctly labeled AI visual can still violate the product-truth rule.
- For TikTok Shop US listing images, run a separate September 24 AIGC preflight against the exact selected SKU. Compare the final image with the real product and PDP for geometry, scale, thickness, material, color, count, bundle contents, included parts, installation position, compatibility, supported environments, and performance. Reject false 3D relief on flat goods, perspective or reference-object tricks that distort size, a person or animal substituted for the sold item, duplicated units, unsupported accessories, and glow/motion/special effects that imply functions the product lacks.
- For all Amazon buyer-facing media in worldwide stores, tag a final export containing a photorealistic person generated entirely by AI with `contains-synthetic-performer` in the `dc:subject` XMP field. Include partially visible people when the depicted person is still photorealistic and entirely AI-generated. Read the metadata back after resize, compression, or conversion and before upload; keep the verified tagged derivative distinct from the editable master.
- Route Amazon disclosure by placement. A+ Content can use the tagged file or the `AI-generated people` checkbox in A+ Content Manager Creative Assets, and A+ Creative Studio output is tagged automatically. For non-A+ product-listing, Store, and advertising media, tag the delivery file before upload. Do not assume that a visible label or an A+ upload control carries across tools.
- Add a retroactive Amazon audit to asset maintenance: inventory affected buyer-facing media published before June 6, 2026, update and verify the final derivative, re-upload it through the relevant placement tool, and record asset ID, ASIN or campaign, surface, tagging route, verification result, and replacement date.
- Keep the real product visible in promotional video. A cover or PDP screenshot does not satisfy in-video or LIVE requirements, and current TikTok Shop US guidance restricts static/PDP-image-heavy LIVE content.

#### TikTok Shop US Original Main-Image Rights Gate

For sellers eligible for TikTok Shop US Originality Protection, treat first publication as part of the asset-release plan rather than an afterthought:

- Protect only seller-created, rights-cleared main product images; competitor images may inform pattern research but must never become production references to copy or upload. TikTok Shop US explicitly treats an AI-modified version of another seller's original product image as unauthorized use when written permission is absent, so do not treat cropping, background replacement, retouching, style transfer, or generative restaging as rights clearance.
- When third-party imagery is legitimately licensed, archive the image owner, written authorization or license, authorized seller/account, permitted market and surfaces, validity period, and source file before generation or upload. If those terms are unclear, extract only abstract visual attributes and rebuild from the seller's own rights-cleared SKU photos.
- Before first publication, archive the source capture, layered master, final export hash, photographer or creator rights, product ID, and planned publication time. Keep authorized reuse evidence when an agency, distributor, or affiliate also receives the asset.
- Publish the intended canonical main image from the owning shop first, then confirm the weekly Seller Center summary or IPPC asset record when the account is enrolled. TikTok says qualifying images must be main product images, first published on TikTok Shop, and clear enough for verification; secondary images, detail shots, and videos are not covered, and protection lasts one year.
- Treat enrollment as eligibility-based and recheck the live account. A failed verification does not remove the listing and is not appealable, while a recall for alleged unauthorized use can be appealed with ownership or authorization evidence.

### 5C. Photo-Commerce Measurement Loop

For placements with photo-level analytics, connect visual decisions to performance instead of treating a carousel as one undifferentiated asset:

1. Record the placement, linked product or shop, opening-image hook, slide roles, style territory, and publication date for each variant.
2. Compare views and product impressions first, then CTR, SKU orders or CTOR, GMV, and product-level sales. Do not call a visual style successful from views alone.
3. Use product-level detail to identify which pictured SKU actually converted; do not attribute a multi-product post's result equally to every slide.
4. Compare photo and video formats over matched windows, and preserve the platform's timezone and attribution definitions in the experiment note.

TikTok Shop US currently exposes these metrics in Shoppable Photo Analytics for selected beta sellers. Its navigation is in transition and the beta currently reports timing in UTC, so verify account access and the current interface before building an automated reporting flow.

### 5D. PDP-To-Image-Ad Handoff

Treat product-listing images as possible paid-media source assets, not an isolated gallery. TikTok's current global Image Ads material says VSA Carousel can use catalog images and Product Shopping Ads can automatically use PDP images plus Seller Center information as ad creative.

Before enabling or scaling catalog-driven image ads:
- Record whether Catalog Image & Video Auto-Crawl and Creative Upgrades auto-add are enabled. Audit the public landing-page source pool before launch, save the approved asset set, and compare it with actually served assets after launch so automatic ingestion or refresh cannot silently introduce a stale SKU, expired promotion, unsupported claim, rights problem, or unapproved visual.
- Record the exact catalog format and campaign objective before choosing asset count. For TikTok's Image Catalog Carousel in the upgraded Smart+ Traffic flow, QA a 2-10-card eligible catalog pool; do not substitute the 2-20-card VSA specification or assume the format is available in every account.
- Check whether Collage Carousel is enabled before approving an upgraded Smart+ Catalog Sales campaign. TikTok says the enhancement is on by default for newly created and duplicated campaigns and can show one main image plus three supporting images; preview the real four-image combination, SKU links, crop, text density, color/variant consistency, and product hierarchy, then disable it when the grouped view creates ambiguity or clutter.
- Keep the PDP first image clean and listing-compliant, then give each additional image one distinct benefit, proof, angle, bundle, or use-context job so an automated carousel does not become a repetitive gallery.
- Verify the Seller Center title, attributes, price, offer, variant mapping, and linked SKU against the same physical product shown in the images; automation can amplify stale or mismatched data.
- Preview the actual ad placement for crop, safe zones, sequence, mobile readability, product prominence, and claim context. Listing compliance does not guarantee ad effectiveness, and a persuasive feed image is not automatically suitable as a PDP main image.
- Build a TikTok-first vertical variant rather than relying on automatic conversion of square PDP assets. Keep the opening hook, product, verified offer, and CTA context in the safe zone; attach cleared music because the current Standard and VSA Carousel playbook requires it.
- Keep format limits distinct: Standard Carousel accepts 2-35 uploaded images, while catalog-driven VSA Carousel displays 2-20. Use the playbook's 3 or 7-9 image recommendation as an experiment starting point, not a fixed rule.
- When the account exposes Smart Order, test it against a controlled manual sequence. Save the original order and resulting metrics so automated reordering does not hide which opening image or evidence sequence actually worked.
- Record market, ad format, catalog/PDP source, image order, linked SKU, creative ID, eligibility, and measurement window. Evaluate CTR, conversion, orders, and GMV by image role instead of assuming that automatic reuse saves production without a performance cost.
- Treat TikTok's human-model, customer-POV, promotion, and before/after suggestions as optional creative guidance. Apply category and claims rules first; do not use restricted before/after or synthetic efficacy proof for health, beauty, body, baby, pet, or medical-adjacent products.

### 5E. Product-Image-To-Video Handoff

When a platform can turn PDP images into shoppable or carousel video, treat still-image production as an upstream video input rather than a separate endpoint:

1. Keep a clean, centered, high-resolution product view plus alternate angles and real use/detail shots in the source library. Do not rely on a typography-heavy cover as the only usable product asset.
2. Preserve exact PDP attributes and descriptions. An automatic video may derive rotation, zoom, pan, overlay text, narration, or category styling from those fields, so a source-data error can spread into motion output.
3. For controllable generation, review the script, overlay text, product truth, promotion dates, voiceover, and first-frame crop before publishing; save the source stills and prompt with the video record.
4. For automatic generation that cannot be previewed or edited, audit the live PDP and account enrollment, then use the platform's product-level or account-level opt-out path when the result creates brand, claim, or accuracy risk.
5. Keep platform-generated video distinct from seller-uploaded video and from feed creative. Record its placement, AI label, aspect ratio, moderation status, and whether it appears early in the PDP carousel.

TikTok Shop US currently documents both a Seller Center AI Video Maker, which can use synced product images and lets sellers review or edit generated scripts, and a separate select-seller Auto-Generated Product Video feature that can publish from PDP images, attributes, and descriptions without pre-publication review. Verify account availability because both features are still account- and product-dependent.

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

## Daily Trend Radar

The user expects this skill to keep learning from frontier image-generation models and current ecommerce visual practice. A recurring radar should monitor:
- New or materially changed image models: product identity preservation, multi-reference fusion, local editing, text rendering, batch consistency, upscaling, transparent background, and image-to-video/product-video handoff.
- Ecommerce style shifts: platform-native main images, detail-page modules, live-shopping covers, short-video thumbnails, UGC/product hybrid scenes, AI studio photography, surreal product worlds, and category-specific proof patterns.
- Platform and compliance changes: image size/crop, prohibited claims, label accuracy, before-after restrictions, health/efficacy risk, origin/factory wording, sale/ranking claims, and legal label handling.

Write updates only when they are reusable:
- Model behavior -> `references/model-capabilities.md`.
- Visual/style pattern -> `references/trend-watch.md` or `references/pattern-library.md`.
- Workflow/process improvement -> `references/production-loop.md`.
- Category-specific rule -> `references/category-playbook.md`.
- Platform/spec change -> `references/image-specs.md`.
- External source trail -> `references/source-log.md`.

Do not update the skill for hype, one-off examples, unverified social posts, or copied brand layouts. Prefer official model releases, platform documentation, credible ecommerce/design analysis, and repeated cross-source patterns.

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

For scheduled radar runs, use the same rule: no meaningful reusable change means no commit.

## Suggested Future Additions

- Platform-specific exact export presets when verified.
- Category-specific compliance notes.
- Before/after prompt repair examples.
- Brand-kit ingestion workflow.
- Text-compositing templates for final copy accuracy.
- A/B variant naming and scoring system.

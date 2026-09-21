# Model Capabilities Playbook

Use this before choosing how to generate, edit, resize, or repair ecommerce visuals.

## Principle

Do not bind the skill to one image model. Borrow capabilities and workflows from strong tools, then choose the available tool that best fits the task.

## Capability Matrix

### Product Identity Preservation

Goal: keep brand, packaging, material, shape, color, and visible product texture.

Use when: real product photos are supplied; user says "保留实物"; packaging accuracy matters.

Prompt tactic:
- Put preservation first: "Use the reference product as the real product identity source."
- Specify what may change: background, lighting, props, text layout.
- Specify what must not change: logo, package shape, SKU color, material, product contents.

QA:
- Compare against original product photo before delivery.
- Treat tiny generated label text as draft unless composited from real source.

### Multi-Reference Fusion

Goal: combine product photo, style reference, layout reference, and ingredient/scene reference.

Use when: user provides multiple images or wants to borrow market style while preserving own brand.

Prompt tactic:
- Assign roles to each reference: "Image 1 locks product", "Image 2 informs style", "Image 3 informs layout".
- Never let style references overwrite brand identity.

### Template-To-Product Adaptation

Goal: adapt an excellent ecommerce layout to a new product/category.

Use when: user shares a competitor/Picell/layout reference.

Prompt tactic:
- Extract layout logic rather than copying: title zone, product scale, callout style, proof module, crop.
- Apply the logic to the user's brand, category, proof needs, and platform.

### Local Object Editing

Goal: fix one part without changing the whole image.

Use when: background is wrong, text is wrong, product needs repositioning, prop is unwanted, label needs cleanup.

Workflow:
1. Identify exact region/object to change.
2. Preserve everything else.
3. Use short edit instruction.
4. Re-QA product identity.

### Size/Ratio Transformation

Goal: convert one approved visual into multiple platform ratios.

Use when: one image must become 1:1, 3:4, 4:5, 9:16, or banner.

Workflow:
1. Lock product and important text.
2. Expand or crop background first.
3. Reposition text for safe zones.
4. Export target ratios.

### Upscale And Sharpen

Goal: improve final listing clarity.

Use when: output is good but not sharp enough or platform requires higher resolution.

Workflow:
1. Upscale after composition and final crop.
2. Preserve product texture and text edges.
3. Avoid inventing small label/legal text.

### Batch Consistency

Goal: make a campaign/set feel unified while each image has a distinct purpose.

Use when: generating main image + detail images + covers.

Workflow:
1. Define brand anchors: product scale, palette, type, recurring shape/icon.
2. Rotate style territories: loud hook, clean trust, macro proof, lifestyle, comparison.
3. Keep one visual language thread across the set.

### AI Asset Provenance For Commerce Feeds

Goal: keep an AI-assisted asset publishable where a commerce feed requires provenance or AI disclosure.

Use when: exporting AI-generated or materially AI-edited product images to Google Merchant Center, Google Ads, or another channel with an equivalent disclosure rule.

Workflow:
1. Keep the source product image and the final delivery derivative separate; do not confuse a working canvas with the uploaded file.
2. Preserve or add the platform-required provenance field at the final export stage. For Google Merchant Center, generative images require IPTC `DigitalSourceType` metadata (for example, `TrainedAlgorithmicMedia`; composites may use `CompositeSynthetic`).
3. Read the final compressed/resized file back before upload: conversion, export optimization, and some DAM/CDN paths can strip metadata.
4. Save the asset ID, destination, metadata value, export date, and source-product reference in the delivery manifest.

QA: confirm that metadata survives the actual listing derivative; separately confirm that the image still accurately depicts the sold SKU. Metadata is not a substitute for product truth.

## Verified Model Notes (Checked through 2026-09-21)

Treat these as capability-routing notes, not guarantees of packaging fidelity. Re-check the live model documentation before production because model IDs, limits, and availability can change.

### GPT Image 2.5: Fast Concepts Versus Precise Edits

- OpenAI's September 8 release exposes `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst` in the Image API and Responses API image-generation tool. Use Flare for fast, everyday concept or batch-variant exploration; reserve Sunburst for detail-sensitive editing and final-candidate comparison. This is a routing hypothesis to benchmark on the actual SKU, not a measured guarantee of package or text fidelity.
- Both accept text and image inputs for generation/editing and add `xhigh` and `max` to the usual quality choices. Start with a lower-cost/latency setting for composition experiments, then test a higher setting only where it changes observable product, material, or display-type quality. Do not assume a higher setting repairs wrong packaging or legal text.
- The current Image API supports custom `WIDTHxHEIGHT` sizes with both dimensions divisible by 16 and aspect ratios from 1:3 to 3:1; sizes above 2560 x 1440 are experimental and the documented maximum is 3840 x 2160, subject to pixel/edge limits. Use a final platform crop and pixel check rather than assuming an arbitrary request is accepted or delivered exactly.
- Both routes support transparent background with PNG or WebP output. Inspect cutout edges, translucency, shadows, package text, and the final composited delivery file; transparent output is not an identity lock. OpenAI describes improved edit consistency and infographic layout, but verify every brand mark, SKU, claim, and tiny label from the physical source.
- Pin a dated model snapshot when reproducibility matters, and compare Flare/Sunburst against one approved packshot and a small representative SKU set before switching a production catalog. ChatGPT's template, sketch, and comment interfaces are product features; do not imply that they are separate Image API parameters.

### Wan 2.7 Image Pro

- Prefer `wan2.7-image-pro` when a task needs multi-reference editing, bounded local edits, brand-color control, or a coherent image set.
- The official Model Studio guide supports up to 9 input reference images for editing, bounding-box edits, and character-consistent multi-image generation.
- Text-to-image can reach 4096 x 4096. Editing is limited to 2048 x 2048.
- Sequential image-set mode can request up to 12 coherent outputs, but it cannot be combined with thinking mode or custom color palettes.
- For ecommerce batches, assign each reference a role before upload and still compare every package, label, colorway, and included item against the real product photos.

### Qwen Image 3.0 And 3.0 Pro

- Alibaba Cloud's current model selector now says to start with `qwen-image-3.0-pro` for image generation and editing. Use Pro for complex layouts and typography; use `qwen-image-3.0` when the same generation/editing workflow needs faster output.
- Both routes support generation and editing, 1-3 input references, negative prompts, up to 6 outputs per call, and a documented maximum of 2048 x 2048. Availability can still differ by region or account, so confirm the live console before promising delivery.
- Route complex ecommerce layouts, multilingual display-type exploration, dense comparison cards, menu-like modules, and storyboard sheets to this family. The official release note advertises prompts up to 4.5k tokens, 10 px small-text rendering, 12-language typography, and realistic fine detail.
- The API reference documents PNG output with total pixels between 512 x 512 and 2048 x 2048. Upscale or composite into the exact platform master rather than assuming a 4K final.
- Stronger small-text rendering is a layout capability, not a compliance guarantee. Rebuild packaging copy, prices, claims, ingredients, warnings, barcodes, and legal text from verified source data.
- Run a representative-SKU regression before replacing Qwen Image 2.0 in a catalog workflow: compare package geometry, logo spelling, colorway, multilingual type, material detail, local-edit drift, and batch consistency.
- Plan batch throughput by route instead of assuming Pro and fast aliases share the same capacity. Alibaba Cloud's current public default limit table lists 5 task submissions per minute for `qwen-image-3.0-pro` and 20 per minute for `qwen-image-3.0`, with 10 asynchronous tasks processing concurrently in Beijing, Singapore, Frankfurt, and Tokyo. Treat these as planning ceilings, not guaranteed account entitlement; re-check the live quota before a catalog run.

### Ideogram 4.0 Structured Layout Route

- Use Ideogram 4.0 as a candidate for typography-heavy campaign concepts, comparison cards, posters, and other layouts that benefit from explicit spatial control. Its hosted API accepts either a natural-language prompt or a structured JSON prompt, supports 1K and 2K generation, and exposes transparent-background, remix, and advertisement-resizing routes.
- The structured prompt can assign bounding boxes, literal text elements, element descriptions, and color palettes. Use those controls to lock hierarchy and reserve a verified product zone instead of asking a single prose prompt to infer the entire layout.
- Treat the model as a layout and display-type route, not proof that packaging or regulated copy is correct. Keep the approved packshot separate, compare product geometry and color against the real SKU, and rebuild logos, prices, claims, ingredients, warnings, and legal text from verified sources.
- Choose the license path before production: hosted API use includes commercial production rights, while the freely downloadable quantized weights are research/prototyping only unless a self-serve commercial or enterprise license is obtained. Do not describe the open-weight download as unrestricted commercial open source.

### Alibaba Cloud Image-Model Retirement Gate

- Do not start new production dependencies on `qwen-image`, `qwen-image-edit`, `qwen-image-edit-max`, `qwen-image-edit-plus`, `qwen-image-max`, `qwen-image-plus`, their listed historical snapshots, or the other legacy image utilities in Alibaba Cloud's October 10, 2026 retirement batch.
- The official retirement table routes the retiring Qwen image family to `qwen-image-2.0` and older background/editing utilities to `wan2.7-image`. Prefer the newer Qwen Image 3.0 family for a new complex-layout workflow, but benchmark it against the official replacement and the current production model rather than treating “newer” as automatic product-fidelity improvement.
- Before migration, inventory model IDs and regions, save prompts and approved outputs, then regression-test real SKUs for package geometry, text, color, material, local-edit drift, batch consistency, latency, and cost. Retired endpoints fail after the cutoff, and rate limits may be reduced during the notice period.

### ViduQ3 Fast Reference-To-Image

- Use `vidu/viduq3-fast_reference2image` as a candidate when a concept needs many product, scene, or style references at lower cost. Alibaba Cloud documents text-to-image, image editing, and reference-image generation with up to 14 references, 1K/2K/4K output, and one PNG result per task.
- Assign references by role and remove conflicts before upload. A 14-image allowance does not mean that 14 equally weighted references improve product identity.
- The current API guide is limited to the China (Beijing) region and requires model activation. Verify region, service access, pricing, and watermark settings before choosing it for a production batch.
- Benchmark against the real SKU and a smaller-reference baseline. Treat product labels and embedded text as draft until deterministic compositing and QA are complete.

### Vidu Image Pro And Lite Reference-To-Image

- Alibaba Cloud's August 24 China (Beijing) release adds `vidu/vidu-image-pro_reference2image` and `vidu/vidu-image-lite_reference2image`. Both accept text or up to 14 reference images for text-to-image, reference-to-image, and editing, and the current API guide lists one PNG output at 1K, 2K, or 4K.
- Treat the pair as a benchmark route for reference-heavy ecommerce posters, information cards, and bilingual display-type concepts. The official description highlights Chinese/English text plus UI/chart detail, but this is not proof that packaging, prices, ingredients, claims, warnings, barcodes, or legal copy are accurate; rebuild critical copy from verified source data.
- Use Lite as the cost-sensitive batch candidate and include Pro as the quality-ceiling comparison rather than assuming the model names establish product-fidelity performance. The published Beijing list price is time-specific and materially different: Lite is CNY 0.3125/0.34375/0.40625 per 1K/2K/4K image, while Pro is CNY 1.6875/3.1875/5.125. Re-check the live console and run a representative-SKU A/B before selecting either route.
- Assign every reference a role and start with the smallest sufficient set. The API accepts PNG, JPG, or WEBP inputs from 1:4 to 4:1, with all reference files totaling no more than 50 MB; a 14-image allowance does not make conflicting packaging, style, and layout references safe.
- The current route is asynchronous, limited to China (Beijing), requires model activation and a regional API key, and shares a five-task processing-concurrency pool across the Vidu reference-image family. Verify live access, price, quota, seed behavior, watermark setting, output size, and the 24-hour download-link window before a catalog batch.

### Kling V3 Image And Omni Sequence Route

- Use `kling/kling-v3-image-generation` as a China (Beijing) candidate for text-to-image or a single-reference concept when 1K/2K output and up to 9 independent variants are sufficient. Use `kling/kling-v3-omni-image-generation` when the task needs multiple references, 4K output, or a 2-9-image storyboard with narrative and visual continuity.
- Route coherent campaign sequences to Omni's `series` mode only after defining each frame's job and shared product anchors. The API distinguishes independent `single` outputs, which are only style-similar, from `series` outputs intended to preserve scene and narrative continuity; neither mode guarantees exact packaging or SKU consistency.
- The current operational API overview limits the standard model's reference-image route to one input, while the broader lifecycle description advertises up to 10 references. For production, follow the live API/console contract and use Omni for multi-reference work; the total of Omni reference images plus saved subject IDs must not exceed 10.
- Both routes are asynchronous and require Beijing-region activation. Verify account access, reference count, aspect ratio, resolution, watermark setting, price, and the shared Kling image/video concurrency pool before a batch, then compare every logo, label, colorway, included item, and frame against the real product source.

### Wan 3.0 Approved-Still-To-Video Handoff

- Treat `wan3.0-video` as a candidate for turning an approved ecommerce still, first/last-frame pair, or product reference into motion. Alibaba Cloud's current lifecycle page lists it in China (Beijing) as an all-in-one text-to-video, image-to-video, and reference-to-video model with output up to 30 seconds.
- Do not treat the 30-second allowance as a reason to skip shot-level control. For packaging-critical work, start from clean approved product views, prototype short shots first, and inspect logo, label, color, shape, included items, camera continuity, and every frame that carries a claim before assembly.
- Verify the live console, region, API route, resolution, reference limits, price, watermark, and audio behavior before committing a production job. The lifecycle listing can precede full synchronization across overview and API pages.

### PixVerse V6 R2V Omni Mixed-Reference Handoff

- Treat `pixverse/pixverse-v6-r2v-omni` as a guarded China-mainland candidate when an approved ecommerce still must be combined with motion or scene cues from reference video. Alibaba Cloud's August 13 lifecycle entry says the route accepts mixed image and video references and fuses multiple subjects with motion information across multiple resolutions and aspect ratios.
- Assign each still or clip one role: product identity, hand interaction, camera move, environment, or performance cue. Never let a motion reference replace verified packaging geometry, color, label, included items, or real product behavior.
- Keep this route experimental until its dedicated API and pricing documentation is synchronized. Verify access, input counts and durations, output length, resolution, audio, watermark, price, and region before spending on a production task.

### Qwen Image 2.0 Pro And Z-Image Turbo

- Use `qwen-image-2.0-pro` when negative prompts or up to 6 variants per request are more useful than Wan's sequential set workflow. Its documented maximum is 2048 x 2048 for generation and editing.
- Pin `qwen-image-2.0-pro-2026-06-22` when a production campaign needs repeatable model behavior. Alibaba's June 25 release note says this snapshot improves text rendering, supports instructions up to 1k tokens, and improves photorealistic detail and semantic adherence over the April 22 snapshot.
- Before moving a catalog from the rolling `qwen-image-2.0-pro` alias to the pinned snapshot, regression-test real packaging, Chinese/English display text, material texture, and local edits on representative SKUs. Better text rendering does not make labels, claims, prices, or legal copy final.
- Use `z-image-turbo` only for fast, low-cost generation such as early product-photo concepts; the official capability table does not support editing.
- Do not choose a fast generation-only model for a workflow that depends on local repair or repeated identity-preserving edits.

## Shopify Native Media Editing (Checked 2026-08-10)

- Use Shopify's built-in AI media generation for quick background, lighting, or scene variations inside the merchant workflow, not as the only high-resolution production master.
- The current help guide says generated edits default to about 1 megapixel: larger inputs are scaled down and smaller inputs are scaled up. Re-check final pixel dimensions and product detail before storefront use, especially when zoom or packaging text matters.
- The editor produces one AI-generated scene at a time. Save promising variants before closing because unused scenes can be discarded.
- Modified images keep the original format; save transparent-background outputs as PNG. Shopify applies a non-removable invisible watermark to generated images, although the guide says it does not restrict commercial use.
- Keep the original product photo and an editable master outside the generated scene. Composite exact packaging, labels, prices, and legal copy deterministically when the native edit cannot preserve them.

## Canva Magic Layers Handoff (Checked 2026-08-14)

- Canva says Magic Layers is now available to all users inside ChatGPT and Gemini through the Canva connection. It can turn a flat AI-generated image into a Canva design with live-editable text and separately selectable objects, then support repositioning, background repair, translation, resizing, and team handoff.
- Use it after concept approval to recover an editable campaign master, localize copy, and adapt ratios without regenerating the entire product scene. Keep the original SKU photo and verified copy beside the layered file.
- Layer extraction is an editing aid, not a fidelity guarantee. Inspect masks, regenerated gaps, product edges, logos, packaging text, color, and legal copy before export; rebuild critical product and claim layers from verified sources when decomposition is imperfect.

## Recraft V4 Styles Routing (Checked 2026-08-28)

- Use Recraft V4 Styles as a candidate when a campaign needs repeatable art direction across many different compositions. The current API documentation supports one to ten style-reference images and dedicated raster/vector, standard/Pro routes; a saved `style_id` or references attached directly to a generation can carry the style into later requests.
- Choose `precise` when rendering technique, palette, composition, and lighting should stay tightly aligned; choose `flexible` when the campaign needs more variation around the same mood. Start with one clean, rights-cleared reference, then add similar references to sharpen the match or deliberately diverse references to widen its range.
- Keep style consistency separate from product identity. A style reference may govern lighting, texture, color, and composition, but the real SKU photos still govern package shape, logo, label, colorway, included items, and claims. Benchmark both locks together before scaling a catalog batch.
- Record the resolved `style_id`, compatible model, match mode, reference files, and rights status in the campaign manifest. The API rejects simultaneous `style_id` and inline style references, and a custom style must be reused with a compatible model.

## Adobe Photoshop Protected Local Editing (Checked 2026-08-28)

- Use Photoshop's Firefly Image 5 `Instruct Edit with Masks` as a candidate for narrow production repairs when approved faces, logos, or brand assets outside the change region must remain untouched. Keep those verified elements unmasked, describe one precise change, and preserve the result as a separate generative layer.
- Use Markup when text alone is ambiguous: point to the exact recolor, move, addition, or removal with a region, arrow, or rough shape. This is especially useful for background and prop repair around a locked product.
- Treat protected-area behavior as an editing control, not proof of SKU fidelity. Compare the final derivative with the original packshot at pixel level around mask edges, packaging text, logo, color, and product geometry; retain the original and layered master for rollback.
- Verify the live Photoshop surface and entitlement before committing a production job. Adobe labels the AI Assisted Editor as beta and Firefly Image 5 as Preview in the August 27 announcement, so availability and behavior can change.

## Google Gemini Image Routing (Checked 2026-08-26)

Use the exact model route instead of treating every Nano Banana workflow as equivalent. These are official capability limits, not guarantees that generated packaging, labels, or claims are accurate.

### Nano Banana 2 And Pro

- Use `gemini-3.1-flash-image` as the general production route when ecommerce work needs multiple product/style references, multi-turn editing, reliable display-text exploration, 1K-4K output, or a speed/quality balance. It supports up to 10 high-fidelity object references plus up to 4 character references within the 14-image limit.
- Google's current model page also adds 0.5K output and the 1:4, 4:1, 1:8, and 8:1 aspect ratios to this route, alongside improved aspect-ratio adherence, image consistency, and internationalized text rendering. Use 0.5K only for inexpensive layout/proportion rehearsal; use the extreme ratios for a deliberate banner, shelf-strip, or long-form module prototype, then inspect crop, legibility, and final platform pixel requirements before delivery.
- `gemini-3.1-flash-image` can also use Google Web Search and Image Search together, with retrieved web images passed as visual context. Use this as a research-grounded route for current category, ingredient, location, or scene context; do not let search results replace the real SKU as the product-identity source or silently import a competitor's packaging, logo, protected design, or unlicensed person.
- Preserve the returned citations and attribution metadata and display Google's required search suggestions in any user-facing grounded result. Google's current guide says real-world images of people from web search are not supported in this image-generation route, so supply properly authorized person references directly when a human likeness matters.
- Use `gemini-3-pro-image` for the most complex professional assets when brand consistency, localization, search grounding, and precise creative control matter more than speed. It supports up to 6 object references, 5 character references, and 3 style references within the 14-image limit.
- Assign every reference a role before generation. More references can improve coverage, but irrelevant or conflicting references can weaken the product lock.
- Treat model-rendered marketing text as a layout draft until spelling, claims, prices, and legal copy are verified and composited deterministically.

### Nano Banana 2 Lite And Legacy Routes

- Use `gemini-3.1-flash-lite-image` for low-cost, high-volume ideation and simple single-step variations. Although the guide lists up to 14 high-fidelity object references and the model card describes fast local edits, Google's updated image-generation guide explicitly says Lite is **not optimized for multiple reference inputs or multi-turn sequential editing**. Route reference-heavy product locks and chained repair to Flash Image or a benchmarked alternative; do not treat a supported input count as recommended production behavior.
- Lite only outputs 1K, has no separate character- or style-reference allocation in the official 14-reference table, and does not support Google Search grounding. Benchmark identity drift on representative SKUs and upscale or composite into the exact delivery master rather than treating 1K output as final.
- Treat `gemini-2.5-flash-image` as a legacy 1024 px route. Google recommends moving workloads to the Nano Banana 2 family.
- Do not start new production on Imagen 4. Google's Gemini API deprecation table has reached its August 17, 2026 earliest shutdown date and names `gemini-3.1-flash-image` as the replacement for all three Imagen 4 GA routes.
- Treat any Imagen 4 endpoint that still responds as transition-only and migrate immediately. Google's table says listed dates are the earliest possible shutdown dates; without an authenticated endpoint check or a newer explicit status notice, do not claim that operational shutdown has been independently confirmed.
- All Nano Banana outputs include a SynthID watermark; do not promise a watermark-free master without checking the actual delivery route and platform requirements.

### Video-To-Cover Handoff

- `gemini-3.1-flash-image` can use a video as context to generate a thumbnail, poster, or summary image. Use this when a short-video or livestream cover should reflect the actual footage rather than a disconnected prompt.
- Still compare the generated cover against the real SKU, on-screen claims, featured people, and footage. Video context reduces creative drift but does not make product details or claims automatically final.

## Picell-Inspired Workflow

Borrow this sequence from product-image platforms:

1. Upload or identify product references.
2. Parse product/category/platform requirements.
3. Generate a visual blueprint before image generation.
4. Choose a template/style direction.
5. Generate.
6. Inspect and iterate.
7. Export in platform-ready ratios.

Key lesson: separate "demand understanding" from "image generation".

## Nano Banana-Inspired Workflow

Borrow these capability assumptions when a Nano Banana-like model/tool is available:

1. Identity lock: use reference images to preserve product/person/object consistency.
2. Multi-image composition: combine product with scene/style/layout references.
3. Precise edit: modify background, props, text space, or lighting without replacing product.
4. Style transfer: change visual style while retaining the product.
5. Ratio and resize: generate alternate crops after a good master image.
6. Upscale: create higher-resolution export for listing use.

Use this as a workflow pattern even if the actual tool is GPT Image 2 or another image model.

## Tool Selection Heuristics

- Use GPT Image 2 when the user explicitly asks for it or when local Codex image generation is available.
- Use a Nano Banana-like workflow when identity consistency, editing, multi-reference composition, resizing, or upscaling is central.
- Use deterministic post-production tools when text must be exact, dimensions must be exact, or product photos must remain pixel-faithful.
- Use manual compositing after image generation when legal labels, barcodes, QR codes, precise specs, or final ad copy must be accurate.

## Failure Modes

- Product logo changes: strengthen identity lock or composite original packshot.
- Tiny text gibberish: reserve text area and add text later.
- Style overwhelms product: reduce style reference priority and increase product scale.
- Set looks repetitive: rotate style territory and purpose per image.
- Image looks fake: add real product photo reference and ask for product photography realism.
- Platform crop breaks layout: regenerate from approved master ratio or extend background.

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

## Verified Model Notes (2026-08-03)

Treat these as capability-routing notes, not guarantees of packaging fidelity. Re-check the live model documentation before production because model IDs, limits, and availability can change.

### Wan 2.7 Image Pro

- Prefer `wan2.7-image-pro` when a task needs multi-reference editing, bounded local edits, brand-color control, or a coherent image set.
- The official Model Studio guide supports up to 9 input reference images for editing, bounding-box edits, and character-consistent multi-image generation.
- Text-to-image can reach 4096 x 4096. Editing is limited to 2048 x 2048.
- Sequential image-set mode can request up to 12 coherent outputs, but it cannot be combined with thinking mode or custom color palettes.
- For ecommerce batches, assign each reference a role before upload and still compare every package, label, colorway, and included item against the real product photos.

### Qwen Image 2.0 Pro And Z-Image Turbo

- Use `qwen-image-2.0-pro` when negative prompts or up to 6 variants per request are more useful than Wan's sequential set workflow. Its documented maximum is 2048 x 2048 for generation and editing.
- Use `z-image-turbo` only for fast, low-cost generation such as early product-photo concepts; the official capability table does not support editing.
- Do not choose a fast generation-only model for a workflow that depends on local repair or repeated identity-preserving edits.

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

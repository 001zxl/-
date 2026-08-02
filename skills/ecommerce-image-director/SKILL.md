---
name: ecommerce-image-director
description: End-to-end ecommerce image direction for product main images, detail-page modules, carousel images, livestream covers, social commerce ads, and AI-generated product visuals. Use when Codex needs to turn product photos, brand information, platform requirements, competitor/reference inspiration, or design guidelines into structured visual briefs, image-generation prompts, QA criteria, and generated images for Douyin/TikTok, Taobao/Tmall, JD, Xiaohongshu, Amazon, Shopify, or similar ecommerce contexts.
---

# Ecommerce Image Director

## Core Rule

Do not start from a raw prompt. Start from a product-and-platform design brief, produce a visual blueprint, then generate images.

This skill is category-agnostic. Never assume the next project is similar to the previous one. Re-identify the category, buyer psychology, proof needs, compliance risks, and platform norms for every new product.

When product photos are provided, preserve product truth first: brand, packaging shape, visible SKU, material, color, and real product texture. Treat generated text, claims, labels, barcodes, and legal information as draft-only unless verified from the source images or user-provided copy.

Proactively add missing but useful design requirements when the user does not mention them: aspect ratio, platform crop, mobile readability, product safety zone, claim safety, style diversity, post-production text needs, and whether the product should be preserved as real photo or re-rendered.

## Required Workflow

1. **Intake**
   - Identify product name, brand, category, SKU/spec, flavor/model, target platform, image type, target audience, purchase scene, and required claims.
   - Classify the category before choosing style: food, beauty, apparel, electronics, home goods, baby/pet, health, digital service, local service, or other.
   - Identify what proof matters for the category: taste/texture, ingredient, before-after, material, fit, compatibility, size, installation, durability, certification, review/social proof, or scene utility.
   - Inspect all supplied product images before writing prompts. Prefer original product photos over previously generated images when product accuracy matters.

2. **Reference Learning**
   - Read `references/design-system.md` for the overall design framework.
   - Read `references/category-playbook.md` when category strategy, proof needs, or product-specific image modules are unclear.
   - Read `references/image-specs.md` before producing platform-bound images, listing-ready files, or image sets with size/resolution requirements.
   - Read `references/trend-watch.md` when the user asks for current, popular, fresh, or less repetitive styles.
   - Read `references/model-capabilities.md` before choosing a generation/editing approach, especially when product consistency, multi-reference fusion, local edits, resizing, upscaling, or batch catalog consistency matters.
   - Read `references/production-loop.md` when creating a reusable campaign system, multi-project knowledge update, or post-generation review.
   - Read `references/research-playbook.md` when the user asks for fresh styles, competitor learning, market-popular design, or less repetitive output.
   - If current trend/reference learning matters, browse or image-search current platform/competitor examples before prompt writing. Extract patterns; do not copy a single design.

3. **Image Map**
   - Decide the set of images before generation: main image, detail first screen, feature proof, close-up, packaging/trust, variant/group shot, use-scene, promo/cover.
   - For listing-ready sets, define dimensions, aspect ratio, file format, and which images need strict clean-background compliance.
   - Assign one core job to each image. Avoid making every image repeat the same background, props, headline, and selling points.
   - For batches of 6+ images, create a diversity matrix across role, style, background, prop system, copy angle, and proof type before generating.

4. **Visual Blueprint**
   For each image, define:
   - Purpose: click, trust, proof, comparison, scene, conversion, or brand mood.
   - Layout: product position, text hierarchy, foreground/background, negative space, and props.
   - Style territory: choose one from the library or invent a new one intentionally.
   - Product preservation plan: which reference image locks the product, which areas may change.
   - Packaging plan: front/back/side, box/bottle/bag/tube/can, label visibility, material, closure, included accessories, unboxing if relevant.
   - Output spec: aspect ratio, target resolution, crop safety, sharpness, background compliance, and post-production text needs.
   - Copy: 1 headline, 1 subhead, up to 3 labels. Keep text large and simple.
   - Restrictions: no wrong brand, no unsupported claims, no clutter, no platform-forbidden or extreme words.

5. **Prompt Construction**
   - Use `scripts/build_prompt.py` when a structured prompt is useful.
   - For GPT Image 2, pass product photos as references and put product preservation in the first sentence.
   - For Nano Banana-like workflows, decompose into identity lock -> scene/template transformation -> local fixes -> resize/upscale/export.
   - When image text accuracy is important, either request minimal text or reserve clean text areas for later compositing.

6. **Generation**
   - If the user explicitly asks for GPT Image 2, use the `gpt-image-2` skill and its local CLI flow.
   - Generate in small batches. Inspect each result before continuing if style diversity or product preservation is uncertain.

7. **QA**
   Check every image against:
   - Product likeness: packaging, logo, flavor/spec, product material.
   - Platform fit: crop, aspect ratio, readability on mobile, visual hook.
   - Design diversity: each image has a different role and style rhythm.
   - Claim safety: no unverified origin, health, ranking, absolute, or price claims.
   - Text quality: large text readable; small generated text treated as non-final.
   - Batch fatigue: no accidental repetition of the same color story, table setup, headline structure, prop set, or selling point.

8. **Knowledge Update**
   - When a new pattern works well, append a concise note to `references/pattern-library.md` if writing to the skill directory is permitted.
   - Capture: date, category, platform, style territory, what worked, prompt tactic, and output path.
   - Also update the skill when the user points out a blind spot, repeated failure, category-specific risk, or reusable design rule.
   - Keep model-specific lessons separate from visual-style lessons: model behavior goes to `references/model-capabilities.md`; visual patterns go to `references/pattern-library.md`; workflow lessons go to `references/production-loop.md`.

## Style Territory Rotation

Use this to prevent aesthetic fatigue:

- Clean trust: white/gray background, large product, subtle lines, few words.
- High-conversion platform: bold headline, sticker labels, strong contrast, product centered.
- Close-up proof: macro texture, magnifier/callouts, detail validation.
- Lifestyle scene: real use context, restrained props, product still dominant.
- UGC real-use: casual creator-like scene, phone-shot authenticity, cleaned ecommerce readability.
- Pop/viral: comic, collage, bold blocks, motion cues, short-video cover energy.
- Premium dark: black/charcoal background, rim light, metallic accents, texture hero.
- Surreal product world: oversized hero product, floating ingredients, abstract stage, premium novelty.
- Ingredient/process: origin/procedure cards, raw ingredient cues, before/after logic.
- Variant/group: multi-SKU lineup, bundle sense, cross-sell rhythm.

## Output Habit

Before generating, briefly show the planned image map when the batch has more than two images. After generating, show the image paths and a short use recommendation for each image.

For experiments or multi-image batches, save a concise generation note beside the outputs when possible: filename, recommended use, style territory, references, QA/risk, and whether text is final or draft-only.

# Image Specs And Quality

Always verify exact platform requirements when the task is listing-ready. Platform rules can change. Use these as working defaults.

## Common Aspect Ratios

- **1:1 square**: marketplace main image, product carousel, store thumbnails.
- **3:4 portrait**: detail modules, mobile ecommerce browsing, product proof cards.
- **4:5 portrait**: social feed and paid/social commerce creatives.
- **9:16 vertical**: livestream cover, short-video cover, story/reel/ad creative.
- **16:9 horizontal**: banner, store header, desktop landing module.
- **2:3 or 3:2**: editorial/lifestyle variants when platform permits.

## Resolution Defaults

- Main image: at least 1500 x 1500 px; prefer 2000 x 2000 px or higher for clean crops.
- Detail image: at least 1200 px wide; prefer 1600-2000 px wide for sharp mobile viewing.
- Short-video/livestream cover: 1080 x 1920 px minimum.
- Social feed portrait: 1080 x 1350 px minimum.
- Banner: define platform size before design; keep product and text within mobile crop safe zones.

## Clarity Rules

- Product edges must be sharp and not hidden by background.
- Logo, product name, SKU/flavor, and main packaging shape should be readable in the target crop.
- Use the highest-quality source product photo available. Avoid using screenshots or compressed social images as the only identity reference when exact packaging matters.
- For final listing images, prefer lossless or high-quality export and avoid repeated compression.
- Avoid asking image generation to reproduce tiny legal copy, barcode, nutrition tables, QR codes, or certificates.
- If text must be final, generate a clean background/space and composite text afterward.
- Use high contrast for mobile text: white/black/gold/red depending on background.
- Keep headline short enough to read at thumbnail size.

## Platform-Specific Working Notes

- **Douyin/TikTok Shop**: prioritize mobile-first crops, strong hook text, product scale, and 1:1 or 3:4/4:5 creatives depending on placement. Verify seller center rules before final upload.
- **Taobao/Tmall/JD**: square main images and long/mobile detail modules are common. Keep first screen clear and trust-oriented. Verify category-specific size limits.
- **Xiaohongshu**: 3:4 or 4:5 portrait works well for feed-style content; softer lifestyle imagery often performs better than hard-sell layouts.
- **Amazon**: main image commonly requires clean white background and high-resolution product clarity. Verify marketplace rules before final export.
- **Shopify/Independent sites**: match theme layout; prepare square product cards, portrait detail blocks, and horizontal hero/banner variants as needed.

## Verified Marketplace And Paid-Image Notes (Checked through 2026-08-18)

Keep marketplace listing assets separate from feed posts, ads, livestream covers, and other promotional creative. The rules below are placement- and market-specific.

### TikTok Shop United States Product Detail Page

- The technical upload floor is 1 image, but TikTok Shop's current listing course recommends at least 5 high-resolution images for a strong listing; upload no more than 9 square images. All images must be at least 600 x 600 px.
- Use a front physical view of the product on a pure white background as the main image.
- Do not add overlay logos, text, borders, watermarks, or graphics to listing images. Preserve the real brand marks printed on the physical product.
- Show only what the customer receives. Placeholders and digital renderings are not allowed as product-listing images.
- Build the recommended 5-image baseline around distinct evidence roles: front, back, another physical angle, feature/detail, and included accessories or use/scale context. Use remaining slots for variations or additional proof; do not repeat the same angle.
- Show realistic product proportions and avoid backgrounds or compositions that exaggerate size, especially for home decor, toys, and festive or party supplies. Do not use generated or rendered dimensional, visual, or material effects that the physical product does not have.
- For new Food & Beverage listings, the complete ingredient list must also appear as clear PDP text, in descending order by weight, and match the physical label. An ingredient photo or generated ingredient graphic does not replace this structured disclosure.

This does not prohibit bold text, stickers, generated scenes, or creator-style hooks in separate promotional placements when those placements allow them. Never reuse a promotional cover as a PDP main image without a fresh compliance check.

### TikTok Image Ads Carousels

Keep these paid-media specifications separate from TikTok Shop PDP requirements. Verify the live Ads Manager account and market before export because format availability can vary.

- Standard Carousel accepts 2-35 JPG/JPEG or PNG images. TikTok's current playbook lists 1200 x 628 px horizontal, 640 x 640 px square, and 720 x 1280 px vertical assets; a file size of 100 KB or less is suggested rather than stated as a universal hard upload limit.
- VSA Carousel displays 2-20 catalog-driven product images. It uses one caption and one call to action for the carousel, while each product image can lead to its own catalog product link.
- Both formats require music in the cited playbook. Record the audio source and rights with the creative even though the visual team may hand off still images separately.
- Prefer vertical 9:16 and at least 720p for TikTok-first delivery. Keep the product, verified copy, offer, and other critical elements inside the placement safe zone; horizontal or square sources can show black cut-off areas in feed.
- Treat 3 or 7-9 images per carousel as TikTok's current performance-oriented best practice, not an upload rule. Test the count, order, and opening image against the specific product and objective.

### Xiaohongshu Merchant Product Images

- The current Xiaohongshu Open Platform product API documentation accepts 800 x 800 or 750 x 1000 product images in JPG, PNG, or JPEG, corresponding to 1:1 and 3:4.
- Product-detail images must be 750-1242 px wide, no more than 1546 px high, and no more than 2 MB each.
- Treat these as merchant product-listing specifications, not Xiaohongshu feed-post creative guidance.

### Amazon Product Images

- Current public Amazon seller guidance requires at least 1 product image and recommends at least 6; the listing workflow supports up to 9 photos.
- Keep the longest side between 500 and 10,000 px. Accepted public-guidance formats are JPEG, TIFF, PNG, and non-animated GIF.
- Use clear, unpixelated product views without jagged edges. Verify the current marketplace, category, and main-image background/content rules in Seller Central before upload because the public guidance is not a complete category policy.
- For any listing or A+ image or video in Amazon's worldwide stores that contains a photorealistic person generated entirely by AI, use an IPTC-compatible metadata editor before upload and add the exact keyword `contains-synthetic-performer` to the `dc:subject` XMP field. Amazon says it can use this metadata to display a customer-facing indicator where applicable.
- This exact metadata requirement does not apply when the media only shows real people, even if they were AI-altered, or when it has no people or no photorealistic people. Do not generalize those exceptions beyond this tag; image accuracy, rights, advertising, and other disclosure rules still apply.
- Verify the metadata on the final exported file after resizing, optimization, or format conversion, because those steps can strip XMP. Upload that verified derivative rather than assuming the layered master and delivery file carry the same metadata.

### Shopify Product And Collection Images

- Product and collection images can be up to 5000 x 5000 px or 25 megapixels and must be smaller than 20 MB.
- Prefer PNG, followed by JPEG, for most product images. Shopify also accepts PSD, TIFF, BMP, GIF, SVG, HEIC, and WebP, including animated GIF/WebP where appropriate.
- Use 2048 x 2048 px as the usual square product-image target and keep featured images at a consistent aspect ratio so collection grids align.
- Shopify creates multiple delivery sizes and the active theme controls display behavior. Check the theme crop, focal point, zoom, and mobile layout instead of exporting one universal storefront crop.

## Export Checklist

Before final delivery, report:

- Output path.
- Intended platform/use.
- Aspect ratio.
- Approximate resolution.
- Whether text is final or should be post-edited.
- Any product/label detail that needs manual verification.
- Whether exact platform upload specs were verified this turn or only default working specs were used.

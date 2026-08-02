#!/usr/bin/env python3
import argparse
import textwrap


def main():
    parser = argparse.ArgumentParser(
        description="Build a structured ecommerce image-generation prompt."
    )
    parser.add_argument("--product", required=True)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--platform", required=True)
    parser.add_argument("--image-type", required=True)
    parser.add_argument("--category", default="")
    parser.add_argument("--use-case", default="")
    parser.add_argument("--style", required=True)
    parser.add_argument("--aspect-ratio", default="")
    parser.add_argument("--resolution", default="")
    parser.add_argument("--packaging", default="")
    parser.add_argument("--reference-roles", default="")
    parser.add_argument("--model-workflow", default="")
    parser.add_argument("--audience", default="")
    parser.add_argument("--selling-points", default="")
    parser.add_argument("--copy", default="")
    parser.add_argument("--layout", default="")
    parser.add_argument("--preserve", default="packaging, logo, product shape, product material, visible texture")
    parser.add_argument("--avoid", default="wrong brand, unsupported claims, clutter, people, unreadable small text, extreme words")
    args = parser.parse_args()

    prompt = f"""
    Use the provided reference images as the product identity source. Preserve {args.preserve}.

    Asset type: {args.platform} {args.image_type}
    Product: {args.brand} {args.product}
    Category: {args.category or "infer from references"}
    Use case: {args.use_case or "ecommerce conversion"}
    Packaging: {args.packaging or "infer from references and keep truthful"}
    Reference roles: {args.reference_roles or "assign product identity, style, layout, and scene roles before generation"}
    Model workflow: {args.model_workflow or "identity lock -> visual blueprint -> generation -> QA -> edit/resize/upscale if needed"}
    Aspect ratio: {args.aspect_ratio or "choose for platform/use"}
    Target resolution: {args.resolution or "high-resolution, mobile-sharp output"}
    Style territory: {args.style}
    Target audience: {args.audience or "platform shoppers"}
    Core selling points: {args.selling_points or "clear product, trust, purchase reason"}
    Required copy: {args.copy or "one short headline, one subhead, up to three labels"}
    Layout plan: {args.layout or "main product dominant, clear text hierarchy, mobile-readable, clean background"}

    Generate an ecommerce-ready image with strong product recognition and a distinct visual role.
    Keep text large, short, and readable. Treat tiny package/legal text as visual texture rather than final copy.
    Avoid: {args.avoid}.
    """
    print(textwrap.dedent(prompt).strip())


if __name__ == "__main__":
    main()

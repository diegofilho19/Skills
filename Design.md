---
name: anti-ai-design
description: Enforces refined, intentional, production-grade interface design and prevents generic AI-generated aesthetics. Use whenever creating, redesigning, styling, or modifying websites, landing pages, dashboards, e-commerce interfaces, web apps, or frontend components.
---

# Anti-AI Design — Interface Art Direction

## Mission

Act as a senior product designer, art director, and frontend engineer. Produce interfaces that look intentionally designed by an experienced human team: clear, restrained, distinctive, usable, accessible, responsive, and consistent with the product's brand.

The goal is NOT to make every project minimalist, monochromatic, or visually identical. The goal is to remove arbitrary decoration and generic AI patterns while preserving the product's personality.

These rules are mandatory constraints, not optional inspiration. Apply them when creating new interfaces and when modifying existing ones. A request for a "modern", "beautiful", "premium", or "professional" UI does not authorize generic visual effects.

## 1. Non-negotiable visual prohibitions

Never introduce the following by default:

- Decorative gradient backgrounds, gradient text, gradient borders, or gradients applied to every section/card/button.
- Oversized typography used merely to make a page look impressive. Do not use huge headings without a clear hierarchy and content reason.
- Neon, glow, bloom, luminous borders, blurred colored halos, glassmorphism, or excessive backdrop blur.
- Decorative sparkle effects, floating blobs, random abstract shapes, noisy backgrounds, or ornamental particles.
- Emoji as interface icons, navigation icons, feature symbols, status indicators, or buttons. Use a consistent icon library already present in the project (for example Lucide, Phosphor, Material Symbols, or the project's existing icon set). If no icon library exists, choose a suitable one only when justified; do not use emoji as a fallback.
- Random icon styles, mixed icon families, inconsistent stroke weights, or icons used where a simple text label is clearer.
- Excessive rounded corners: do not make every panel, input, image, button, and container a pill or capsule.
- Cards nested inside cards without a strong information-architecture reason.
- Repeated grids of identical rounded cards as the default solution for every section.
- Huge empty hero areas, oversized buttons, excessive whitespace, or arbitrary section heights that harm information density.
- Shadows on every component, thick borders around everything, or multiple competing elevation levels.
- Scroll-jacking, autoplaying decorative motion, parallax for decoration, bouncing elements, and animation without a functional purpose.
- Fake charts, fake testimonials, fake ratings, fake logos, fabricated metrics, or invented trust indicators.
- Generic "AI SaaS" compositions: centered headline + gradient word + two pill buttons + floating dashboard mockup + three feature cards, unless the actual product and brief genuinely call for that composition.
- Arbitrary use of trendy fonts, ultra-thin weights, extreme letter spacing, all-caps labels everywhere, or several unrelated typefaces.
- Visual decoration that reduces readability, contrast, performance, or usability.

A prohibited treatment may be used only when the user explicitly requests it or when it is a genuine, documented part of the existing brand/art direction. Even then, use it sparingly and explain its role if relevant. Do not interpret "make it pop" as permission to add glow, gradients, or visual noise.

## 2. Start with product understanding, not CSS

Before implementation:

1. Inspect the repository, existing pages, components, styles, assets, package manifest, and design conventions.
2. Identify the product type, audience, primary user task, content hierarchy, brand personality, and conversion or workflow goal.
3. Identify the existing framework, styling method, icon library, component system, and design tokens.
4. Reuse existing conventions when they are coherent. Do not replace a working design system just to impose this skill's preferences.
5. If brand assets, screenshots, references, or a supplied design exist, treat them as the source of truth. Do not invent a new visual identity.
6. If essential direction is missing and cannot be inferred safely, ask one concise question. Otherwise make restrained, reversible decisions and proceed.

Do not start by adding dependencies or rewriting the architecture. Inspect first.

## 3. Establish a deliberate visual system

Define or infer a compact system before styling the page.

### Color

- Use a restrained palette with clear semantic roles: page background, surface, primary text, secondary text, border, primary action, and status colors.
- Prefer solid colors and subtle tonal differences over decorative gradients.
- Choose colors that belong to the product's brand and content. Do not default every project to purple/blue gradients, black backgrounds, or generic SaaS palettes.
- Keep contrast accessible. Do not use low-contrast gray text merely for a fashionable muted look.
- Reserve accent colors for actions, focus, status, and meaningful emphasis.
- Avoid using multiple unrelated accent colors without a semantic system.

### Typography

- Use the project's existing fonts when appropriate. Otherwise choose a restrained, highly legible type family with a clear reason.
- Prefer one family with a small, deliberate weight scale. A second family is acceptable only when it serves a clear editorial or brand purpose.
- Establish a consistent type scale. Headings should be proportional to the viewport and content importance.
- Body text must remain comfortable to read. Avoid overly small text, excessively long line lengths, and low line-height.
- Use font weight, spacing, and size to establish hierarchy; do not rely on uppercase, extreme tracking, or oversized text.
- Avoid arbitrary font loading and unnecessary external font requests.

### Spacing and layout

- Use a consistent spacing scale and align elements to a coherent grid.
- Prioritize content hierarchy, scanning, and task completion over decoration.
- Keep related elements close and separate unrelated groups clearly.
- Use whitespace intentionally; do not inflate sections to create an artificial "premium" appearance.
- Control content width for readability. Avoid full-width paragraphs on desktop.
- Make layouts responsive by design, not by shrinking desktop elements after the fact.

### Shape, borders, and elevation

- Use a small, consistent radius scale. A radius should reflect the component's role, not a blanket preference for rounded UI.
- Prefer subtle borders and surface contrast to heavy shadows.
- Use elevation only when it communicates layering, interaction, or hierarchy.
- Buttons, inputs, cards, dialogs, and navigation should have related but not identical geometry.

## 4. Composition must fit the actual product

Do not reuse the same page formula across unrelated projects.

- E-commerce: prioritize product photography, product names, prices, variants, availability, navigation, search, and purchase flow. Avoid turning every product into a decorative card.
- Dashboards: prioritize data density, readable tables, filters, status, hierarchy, and task-oriented navigation. Avoid oversized dashboard headings and empty chart panels.
- Institutional or service websites: prioritize credibility, clear service discovery, contact paths, location, and useful information.
- Editorial/content sites: prioritize reading rhythm, typography, imagery, and content hierarchy.
- Landing pages: establish the value proposition clearly, but do not force a giant hero or a row of generic feature cards.
- Mobile interfaces: prioritize touch targets, compact navigation, readable forms, and task completion.

Use asymmetry, image placement, section variation, typography, and layout rhythm when they improve the design. Distinction should come from composition and content—not random decoration.

## 5. Icons and imagery

- Never use emoji as UI icons. This is a strict rule.
- Prefer the icon package already installed. Keep icon family, size, stroke/fill, and alignment consistent.
- Use icons only when they improve recognition or scanning. Do not decorate every heading with an icon.
- Give icon-only buttons accessible names and visible focus states.
- Use real project assets or user-provided imagery whenever available.
- Do not invent product photography, logos, brand marks, or screenshots. If assets are unavailable, use a neutral placeholder that is clearly temporary rather than pretending it is real.
- Preserve image aspect ratios and use intentional crops. Avoid arbitrary image masks and decorative frames.
- Do not add stock imagery simply to fill empty space.

## 6. Motion and interaction

Motion must communicate state, feedback, continuity, or hierarchy.

- Prefer short, subtle transitions for hover, focus, expansion, loading, and navigation.
- Respect `prefers-reduced-motion`.
- Avoid animation that delays access to content or blocks user actions.
- Do not animate every element on page load.
- Never use glow, pulsing, bouncing, or floating motion as a substitute for visual hierarchy.
- Ensure hover states are not the only way to discover an action; support touch and keyboard.
- Interactive controls must have clear default, hover, focus-visible, active, disabled, loading, success, and error states as applicable.

## 7. Implementation discipline

- Follow the existing framework, architecture, naming conventions, and formatting.
- Reuse existing components and tokens before creating new ones.
- Avoid unnecessary dependencies, duplicate CSS, one-off overrides, and sprawling inline styles.
- Prefer semantic HTML and native controls where appropriate.
- Ensure keyboard navigation, visible focus, labels, accessible names, and meaningful alt text.
- Use responsive layouts with deliberate breakpoints. Check narrow mobile, typical mobile, tablet, and desktop widths.
- Prevent horizontal overflow, clipped content, overlapping elements, and unreadable text.
- Avoid layout shifts: reserve image dimensions and handle loading states.
- Keep performance in mind: avoid unnecessary animation, oversized assets, and excessive client-side code.
- Do not change unrelated business logic, routes, API contracts, data models, or behavior during a visual task.
- Do not remove existing functionality to simplify the design.
- Do not claim a visual issue is fixed without inspecting the resulting implementation.

## 8. Required workflow

For every interface task, follow this sequence:

### Step A — Inspect
Read the relevant files and understand the existing implementation. Identify the actual page entry point, shared components, global styles, assets, and dependencies.

### Step B — Define direction
Write a short internal design direction based on the product:
- What is the primary user task?
- What should attract attention first?
- What should remain secondary?
- Which brand colors, typography, imagery, and existing components should be preserved?
- What is the simplest composition that solves the problem well?

Do not invent a design system if the project already has a coherent one.

### Step C — Implement
Make the smallest coherent set of changes. Build a clear hierarchy, use the established visual system, and preserve behavior. Avoid introducing prohibited patterns.

### Step D — Inspect the result
Use available browser, preview, screenshot, or test tools when available. Inspect the actual rendered interface—not just the source code.

Check at least:
- Desktop layout and spacing.
- Mobile layout and navigation.
- Typography scale and readability.
- Contrast and focus visibility.
- Alignment, component consistency, and image crops.
- Overflow, clipping, and overlapping.
- Interactive states and important user flows.
- Console/build errors when relevant.

If browser inspection is unavailable, state that visual verification could not be performed; do not pretend it was.

### Step E — Refine
Fix visual problems found during inspection. Remove decoration that does not serve a purpose. Prefer simplifying an element over adding another effect to compensate for a weak composition.

### Step F — Report
Summarize what changed, relevant files, checks performed, and any limitations. Be honest about what was and was not verified.

## 9. Mandatory visual rejection checklist

Before declaring the task complete, review every item. If any answer is "yes", correct it unless explicitly required by the user or existing brand:

- Did I add a decorative gradient?
- Did I use emoji anywhere as an interface icon?
- Did I add glow, neon, bloom, or blurred colored halos?
- Did I make headings disproportionately large?
- Did I use too many rounded containers or nested cards?
- Does the page look like a generic AI landing page?
- Are there decorative animations with no functional purpose?
- Are shadows, borders, or accents competing for attention?
- Is whitespace being used to inflate the page rather than improve hierarchy?
- Did I invent content, metrics, testimonials, ratings, or brand assets?
- Did I ignore the existing design system or add unnecessary dependencies?
- Does the mobile layout feel like an afterthought?

A single "yes" requires a correction or a clearly justified exception.

## 10. Design quality principles

The final interface should feel:

- Intentional, not decorated.
- Distinctive, not trendy by default.
- Clear, not oversized.
- Refined, not flashy.
- Consistent, not repetitive.
- Functional, not merely attractive.
- Credible, not artificially polished.
- Responsive, not desktop-only.

A restrained interface is not automatically a good interface. Avoid sterile, generic minimalism too. Use meaningful brand elements, strong content, considered composition, real imagery, and precise details to give each product its own identity.

## 11. Instruction priority

Apply this order when requirements conflict:

1. Explicit user requirements and supplied design references.
2. Existing product brand and established design system.
3. Accessibility, usability, responsiveness, and functional correctness.
4. This skill's visual constraints.
5. Personal aesthetic preference.

Do not silently override an explicit user request. If the user explicitly asks for a treatment prohibited above, follow their direction while keeping it controlled and usable. If the request is ambiguous, default to the restrained, purposeful approach defined here.

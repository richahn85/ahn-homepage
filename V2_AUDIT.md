# V2 repository audit — 2026-09-06

- Stack: static HTML, inline CSS, no framework/package/build/test dependencies. Netlify publishes repository root. GitHub origin: richahn85/ahn-homepage.
- Existing local changes: index.html modified; two seminar directories untracked. Preserve all; no reset or removal.
- Local homepage is older than production. Production snapshot retrieved separately; preserve three newer card-news notices and every external download link.
- Forms: Netlify `subscribe` and `contact`, POST `/thank-you`, hidden `form-name`, `subject`, honeypot `bot-field`. Retain these names and backend. Existing contact fields: name/org/email/type/message; subscription: name/org/email/phone/plan.
- Routes: homepage hash anchors, thank-you.html, safety-disclosure-seminar-20260720 and seminar/20260720 pages. No router or redirect configuration. Keep existing files and map displaced homepage anchors.
- Styling: Blue Edition accent #1558A8, navy #12263F, Pretendard Variable and Noto Serif KR CDN fonts. Keep blue; introduce warm ivory and external shared stylesheet.
- Images: official local ahn-portrait.webp and ahn-lecture.webp. No generated imagery needed.
- SEO: title, description, basic Open Graph; no canonical, structured data or sitemap in homepage. No analytics scripts found in local/production homepage; host-injected analytics cannot be established from repository.
- Accessibility: placeholder-only fields, mobile menu inline handler; improve visible labels, focus, keyboard menu/Escape, semantic sections and image dimensions.
- Claims: headline says 7+ domestic-first projects, list contains 8 items. Do not replace with 8+. Maintain source claims in editorial data and flag independent evidence verification.

## Architecture before implementation

Keep static hosting and original assets/backend. Add a dependency-free Python build script with shared page shell/navigation/footer, homepage sections and case/insight data. Generated HTML supports independent URLs without client routing. Extract and relocate existing subscription, career, expertise, proof, pro bono and service content from snapshots instead of deleting it. New assets/v2.css and assets/v2.js provide shared responsive presentation and progressive enhancement. Existing seminar files remain untouched.

## Validation plan

Check generated internal links and anchors, metadata, structured data, original form contracts, preservation of original external/download URLs; render desktop/mobile and test keyboard menu and form validation without sending real submissions. Production Netlify form receipt and field notification behavior require deployment validation.

import base64
import os

with open('gothic_horror_bg.jpg', 'rb') as f:
    bg_base64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mukul Saini | Dark Fantasy AI Grimoire</title>
  <meta name="description" content="Mukul Saini - BTech CSE-AI (IBM) at JECRC College. A dark fantasy gothic archive of machine learning, neural networks, and synthetic cognition.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Cinzel:wght@400;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=UnifrakturMaguntia&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       DARK HORROR GOTHIC CINEMATIC SYSTEM (LORD OF THE RINGS / MORBID ARCANUM)
       ========================================================================== */
    :root {{
      --color-void: #050508;
      --color-abyss: #0a0a0f;
      --color-charcoal: #121218;
      --color-slate-dark: #161622;
      --color-blood-deep: #4a080e;
      --color-blood-glow: #87141f;
      --color-crimson-bright: #b31b27;
      --color-gold-tarnished: #c5a059;
      --color-gold-pale: #e6d3a3;
      --color-bone: #e2ded5;
      --color-ash: #9c978f;
      --color-border-subtle: rgba(197, 160, 89, 0.22);
      --color-border-crimson: rgba(135, 20, 31, 0.45);
      
      --font-epic: 'Cinzel', 'Garamond', Georgia, serif;
      --font-decorative: 'Cinzel Decorative', 'Cinzel', Georgia, serif;
      --font-body: 'Cormorant Garamond', Garamond, Georgia, serif;
      --font-gothic-script: 'UnifrakturMaguntia', 'Cinzel Decorative', cursive, serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      background-color: var(--color-void);
    }}

    body {{
      background-color: var(--color-void);
      color: var(--color-bone);
      font-family: var(--font-body);
      font-size: 19px;
      line-height: 1.75;
      overflow-x: hidden;
      min-height: 100vh;
      position: relative;
      letter-spacing: 0.02em;
    }}

    /* ==========================================================================
       CINEMATIC BACKGROUND SYSTEM WITH USER'S HORROR GOTHIC ARTWORK
       ========================================================================== */
    .bg-viewport {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -3;
      overflow: hidden;
      pointer-events: none;
    }}

    .bg-horror-art {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image: url('data:image/jpeg;base64,{bg_base64}');
      background-size: cover;
      background-position: center center;
      background-repeat: no-repeat;
      filter: contrast(1.25) brightness(0.68) saturate(1.15);
      transform: scale(1.03);
      transition: transform 0.8s ease-out;
    }}

    /* Deep atmospheric dark vignette, preserving sigils & red clouds while ensuring cinematic contrast */
    .bg-cinematic-shroud {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -2;
      background: radial-gradient(circle at 50% 40%, rgba(5, 5, 8, 0.45) 0%, rgba(5, 5, 8, 0.88) 75%, rgba(3, 3, 5, 0.98) 100%);
      pointer-events: none;
    }}

    /* Subtle film grain & ancient stone texture */
    .bg-stone-grain {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -1;
      opacity: 0.08;
      pointer-events: none;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
    }}

    /* Floating Blood Ash & Dark Embers Canvas */
    #ashCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
    }}

    /* ==========================================================================
       CINEMATIC HORROR GOTHIC DECORATIONS & SIGILS
       ========================================================================== */
    .barbed-divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin: 32px auto;
      max-width: 580px;
      width: 100%;
    }}

    .barbed-line {{
      flex: 1;
      height: 1px;
      background-color: var(--color-border-crimson);
      position: relative;
    }}

    .barbed-line::after {{
      content: '';
      position: absolute;
      top: -2px;
      left: 50%;
      width: 5px;
      height: 5px;
      background-color: var(--color-blood-glow);
      transform: rotate(45deg);
    }}

    .barbed-emblem {{
      color: var(--color-blood-glow);
      font-size: 18px;
      letter-spacing: 4px;
      text-shadow: 0 0 10px rgba(179, 27, 39, 0.7);
    }}

    /* Ancient Eldritch Inscription ribbon */
    .eldritch-runes {{
      font-family: var(--font-epic);
      font-size: 11px;
      letter-spacing: 0.35em;
      color: var(--color-blood-glow);
      text-transform: uppercase;
      text-align: center;
      margin-bottom: 8px;
      text-shadow: 0 0 8px rgba(135, 20, 31, 0.6);
    }}

    /* ==========================================================================
       CINEMATIC NAVIGATION BAR
       ========================================================================== */
    .cinematic-header {{
      position: sticky;
      top: 0;
      width: 100%;
      z-index: 200;
      background-color: rgba(7, 7, 10, 0.94);
      backdrop-filter: blur(6px);
      border-bottom: 1px solid var(--color-border-crimson);
      padding: 16px 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .brand-sigil {{
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: var(--color-gold-pale);
      font-family: var(--font-epic);
      font-size: 17px;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      transition: text-shadow 0.3s ease;
    }}

    .brand-sigil:hover {{
      text-shadow: 0 0 12px rgba(197, 160, 89, 0.7);
    }}

    .brand-monogram {{
      font-size: 20px;
      color: var(--color-crimson-bright);
      text-shadow: 0 0 10px rgba(179, 27, 39, 0.8);
      font-weight: 700;
    }}

    .cinematic-nav {{
      display: flex;
      gap: 34px;
      list-style: none;
    }}

    .cinematic-nav-link {{
      color: var(--color-ash);
      text-decoration: none;
      font-family: var(--font-epic);
      font-size: 13px;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      position: relative;
      padding-bottom: 4px;
      transition: color 0.3s ease, text-shadow 0.3s ease;
    }}

    .cinematic-nav-link::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 1px;
      background-color: var(--color-crimson-bright);
      transition: width 0.3s ease;
    }}

    .cinematic-nav-link:hover {{
      color: var(--color-bone);
      text-shadow: 0 0 10px rgba(226, 222, 213, 0.6);
    }}

    .cinematic-nav-link:hover::after {{
      width: 100%;
    }}

    .ambient-drone-toggle {{
      background: transparent;
      border: 1px solid var(--color-border-crimson);
      color: var(--color-ash);
      font-family: var(--font-epic);
      font-size: 11px;
      letter-spacing: 0.2em;
      padding: 7px 14px;
      cursor: pointer;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.3s ease;
    }}

    .ambient-drone-toggle:hover {{
      border-color: var(--color-crimson-bright);
      color: var(--color-bone);
      box-shadow: 0 0 12px rgba(179, 27, 39, 0.4);
    }}

    .ambient-drone-toggle.active {{
      background-color: rgba(74, 8, 14, 0.4);
      border-color: var(--color-crimson-bright);
      color: var(--color-crimson-bright);
      box-shadow: 0 0 14px rgba(179, 27, 39, 0.6);
    }}

    /* ==========================================================================
       MAIN WRAPPER & CONTAINER
       ========================================================================== */
    .content-wrapper {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 28px;
      position: relative;
      z-index: 10;
    }}

    /* ==========================================================================
       HERO: CINEMATIC DARK FANTASY PROLOGUE
       ========================================================================== */
    .hero-container {{
      min-height: 94vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 80px 20px 60px;
      position: relative;
    }}

    .hero-sigil-seal {{
      width: 80px;
      height: 80px;
      margin-bottom: 24px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .hero-sigil-seal svg {{
      width: 100%;
      height: 100%;
      filter: drop-shadow(0 0 14px rgba(179, 27, 39, 0.8));
    }}

    .hero-film-preamble {{
      font-family: var(--font-epic);
      font-size: 13px;
      letter-spacing: 0.4em;
      color: var(--color-blood-glow);
      text-transform: uppercase;
      margin-bottom: 16px;
      text-shadow: 0 0 10px rgba(135, 20, 31, 0.5);
    }}

    .hero-name {{
      font-family: var(--font-decorative);
      font-size: clamp(3.2rem, 7.5vw, 6.2rem);
      font-weight: 900;
      color: var(--color-gold-pale);
      letter-spacing: 0.16em;
      line-height: 1.1;
      text-transform: uppercase;
      margin-bottom: 18px;
      text-shadow: 0 0 20px rgba(197, 160, 89, 0.5), 0 0 45px rgba(135, 20, 31, 0.4);
    }}

    .hero-sub {{
      font-family: var(--font-epic);
      font-size: clamp(1.1rem, 2.2vw, 1.45rem);
      color: var(--color-bone);
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-bottom: 26px;
      max-width: 860px;
      font-weight: 600;
      text-shadow: 0 0 8px rgba(0, 0, 0, 0.8);
    }}

    .hero-prologue {{
      max-width: 760px;
      font-size: 1.25rem;
      color: var(--color-ash);
      line-height: 1.85;
      margin: 0 auto 42px;
      font-style: italic;
      text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
    }}

    /* Cinematic Widescreen Button */
    .cinematic-btn {{
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      padding: 18px 46px;
      background-color: var(--color-void);
      border: 1px solid var(--color-border-crimson);
      color: var(--color-bone);
      font-family: var(--font-epic);
      font-size: 14px;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      text-decoration: none;
      cursor: pointer;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.9), inset 0 0 15px rgba(74, 8, 14, 0.3);
      transition: all 0.4s ease;
    }}

    .cinematic-btn::before, .cinematic-btn::after {{
      content: '†';
      color: var(--color-blood-glow);
      font-size: 14px;
      transition: color 0.3s ease, transform 0.3s ease;
    }}

    .cinematic-btn:hover {{
      background-color: rgba(74, 8, 14, 0.5);
      border-color: var(--color-crimson-bright);
      color: #ffffff;
      box-shadow: 0 0 30px rgba(179, 27, 39, 0.6), inset 0 0 20px rgba(179, 27, 39, 0.3);
      transform: translateY(-2px);
    }}

    .cinematic-btn:hover::before {{
      color: var(--color-gold-pale);
      transform: scale(1.2);
    }}
    .cinematic-btn:hover::after {{
      color: var(--color-gold-pale);
      transform: scale(1.2);
    }}

    /* ==========================================================================
       SECTION HEADINGS: CINEMATIC CHAPTER TITLES
       ========================================================================== */
    .chapter-heading {{
      text-align: center;
      margin-bottom: 56px;
      position: relative;
    }}

    .chapter-numeral {{
      font-family: var(--font-epic);
      font-size: 12px;
      letter-spacing: 0.45em;
      color: var(--color-crimson-bright);
      text-transform: uppercase;
      margin-bottom: 8px;
    }}

    .chapter-title {{
      font-family: var(--font-decorative);
      font-size: clamp(2.2rem, 4.2vw, 3.2rem);
      font-weight: 700;
      color: var(--color-gold-pale);
      letter-spacing: 0.15em;
      text-transform: uppercase;
      text-shadow: 0 0 16px rgba(197, 160, 89, 0.4), 0 0 30px rgba(135, 20, 31, 0.4);
    }}

    .chapter-subtitle {{
      max-width: 680px;
      margin: 16px auto 0;
      color: var(--color-ash);
      font-size: 1.15rem;
      font-style: italic;
    }}

    /* ==========================================================================
       SKILLS SECTION: THE FORBIDDEN BLACK CODEX (CINEMATIC STONE TABLETS)
       No toy-like badges; majestic engraved monolithic slate boxes
       ========================================================================== */
    .skills-monolith-section {{
      padding: 100px 0 80px;
    }}

    .skills-grid-cinematic {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 16px;
    }}

    .codex-tablet {{
      background-color: rgba(14, 14, 20, 0.82);
      border: 1px solid rgba(135, 20, 31, 0.32);
      padding: 22px 16px;
      position: relative;
      text-align: center;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.7);
    }}

    /* Barbed corner thorns */
    .codex-tablet::before {{
      content: '';
      position: absolute;
      top: -2px;
      left: -2px;
      width: 6px;
      height: 6px;
      border-top: 2px solid var(--color-blood-glow);
      border-left: 2px solid var(--color-blood-glow);
      transition: border-color 0.3s ease;
    }}

    .codex-tablet::after {{
      content: '';
      position: absolute;
      bottom: -2px;
      right: -2px;
      width: 6px;
      height: 6px;
      border-bottom: 2px solid var(--color-blood-glow);
      border-right: 2px solid var(--color-blood-glow);
      transition: border-color 0.3s ease;
    }}

    .tablet-index {{
      font-family: var(--font-epic);
      font-size: 10px;
      letter-spacing: 0.3em;
      color: var(--color-blood-glow);
      margin-bottom: 6px;
      display: block;
      transition: color 0.3s ease;
    }}

    .tablet-name {{
      font-family: var(--font-epic);
      font-size: 15px;
      letter-spacing: 0.1em;
      color: var(--color-bone);
      font-weight: 700;
      text-transform: uppercase;
      transition: color 0.3s ease, text-shadow 0.3s ease;
    }}

    .tablet-sub {{
      display: block;
      font-size: 12px;
      color: var(--color-ash);
      font-style: italic;
      margin-top: 4px;
      letter-spacing: 0.05em;
    }}

    .codex-tablet:hover {{
      background-color: rgba(45, 10, 16, 0.65);
      border-color: var(--color-crimson-bright);
      box-shadow: 0 0 24px rgba(179, 27, 39, 0.55), inset 0 0 12px rgba(179, 27, 39, 0.25);
      transform: translateY(-4px);
    }}

    .codex-tablet:hover::before, .codex-tablet:hover::after {{
      border-color: var(--color-gold-pale);
    }}

    .codex-tablet:hover .tablet-index {{
      color: var(--color-gold-pale);
    }}

    .codex-tablet:hover .tablet-name {{
      color: #ffffff;
      text-shadow: 0 0 12px rgba(226, 222, 213, 0.9);
    }}

    /* ==========================================================================
       CINEMATIC LORE MANIFESTO (LOTR PROPHETIC SCROLL)
       ========================================================================== */
    .prophetic-monolith {{
      margin: 90px 0;
      padding: 50px 40px;
      background-color: rgba(10, 10, 15, 0.9);
      border: 1px solid var(--color-border-crimson);
      border-left: 4px solid var(--color-blood-glow);
      border-right: 4px solid var(--color-blood-glow);
      text-align: center;
      position: relative;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9);
    }}

    .prophetic-quote {{
      font-family: var(--font-body);
      font-size: 1.45rem;
      font-style: italic;
      color: var(--color-bone);
      line-height: 1.8;
      max-width: 880px;
      margin: 0 auto;
      letter-spacing: 0.04em;
    }}

    .prophetic-inscription {{
      font-family: var(--font-epic);
      font-size: 12px;
      letter-spacing: 0.35em;
      color: var(--color-crimson-bright);
      text-transform: uppercase;
      margin-top: 18px;
    }}

    /* ==========================================================================
       PROJECTS SECTION: THE FORBIDDEN RELICS (CINEMATIC CHRONICLES)
       ========================================================================== */
    .projects-chronicle-section {{
      padding: 80px 0;
    }}

    .chronicles-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 36px;
    }}

    .chronicle-slab {{
      background-color: rgba(12, 12, 18, 0.88);
      border: 1px solid rgba(135, 20, 31, 0.38);
      padding: 38px 32px;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.4s ease;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.85);
    }}

    .chronicle-slab::before {{
      content: '𐕣';
      position: absolute;
      top: 18px;
      right: 22px;
      font-size: 22px;
      color: var(--color-blood-glow);
      transition: color 0.3s ease, transform 0.3s ease;
    }}

    .chronicle-slab:hover {{
      background-color: rgba(22, 10, 16, 0.9);
      border-color: var(--color-crimson-bright);
      box-shadow: 0 0 30px rgba(179, 27, 39, 0.5), inset 0 0 15px rgba(74, 8, 14, 0.4);
      transform: translateY(-6px);
    }}

    .chronicle-slab:hover::before {{
      color: var(--color-gold-pale);
      transform: scale(1.25);
    }}

    .chronicle-header-badge {{
      font-family: var(--font-epic);
      font-size: 11px;
      letter-spacing: 0.3em;
      color: var(--color-crimson-bright);
      text-transform: uppercase;
      margin-bottom: 8px;
    }}

    .chronicle-title {{
      font-family: var(--font-epic);
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--color-gold-pale);
      letter-spacing: 0.1em;
      margin-bottom: 6px;
      transition: color 0.3s ease, text-shadow 0.3s ease;
    }}

    .chronicle-slab:hover .chronicle-title {{
      color: #ffffff;
      text-shadow: 0 0 14px rgba(226, 222, 213, 0.8);
    }}

    .chronicle-canon {{
      font-size: 1.05rem;
      color: var(--color-ash);
      font-style: italic;
      margin-bottom: 18px;
    }}

    .chronicle-narrative {{
      color: var(--color-bone);
      font-size: 1.05rem;
      line-height: 1.7;
      margin-bottom: 26px;
      flex-grow: 1;
    }}

    .chronicle-sigils-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 26px;
    }}

    .chronicle-sigil {{
      font-family: var(--font-epic);
      font-size: 11px;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--color-gold-tarnished);
      border: 1px solid rgba(197, 160, 89, 0.3);
      padding: 4px 12px;
      background-color: rgba(5, 5, 8, 0.6);
    }}

    .chronicle-footer {{
      border-top: 1px solid rgba(135, 20, 31, 0.3);
      padding-top: 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .chronicle-inspect-btn {{
      background: none;
      border: 1px solid var(--color-border-crimson);
      color: var(--color-bone);
      font-family: var(--font-epic);
      font-size: 12px;
      letter-spacing: 0.2em;
      padding: 8px 18px;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.3s ease;
    }}

    .chronicle-inspect-btn:hover {{
      background-color: var(--color-blood-deep);
      border-color: var(--color-crimson-bright);
      color: #ffffff;
      box-shadow: 0 0 16px rgba(179, 27, 39, 0.6);
    }}

    .chronicle-runic-sigil {{
      color: var(--color-blood-glow);
      font-size: 15px;
      letter-spacing: 4px;
    }}

    /* ==========================================================================
       SUMMONING / DISPATCH SECTION (SANCTUM OF SUMMONING)
       ========================================================================== */
    .summon-sanctum-section {{
      padding: 80px 0 100px;
    }}

    .sanctum-stone-altar {{
      background-color: rgba(10, 10, 15, 0.92);
      border: 1px solid var(--color-border-crimson);
      padding: 46px 40px;
      max-width: 820px;
      margin: 0 auto;
      position: relative;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.95);
    }}

    .sanctum-form {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}

    .altar-input-group {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .altar-label {{
      font-family: var(--font-epic);
      font-size: 12px;
      letter-spacing: 0.25em;
      color: var(--color-gold-pale);
      text-transform: uppercase;
    }}

    .altar-input, .altar-textarea {{
      background-color: rgba(5, 5, 8, 0.85);
      border: 1px solid rgba(135, 20, 31, 0.4);
      color: var(--color-bone);
      font-family: var(--font-body);
      font-size: 18px;
      padding: 14px 18px;
      outline: none;
      transition: all 0.3s ease;
    }}

    .altar-input:focus, .altar-textarea:focus {{
      border-color: var(--color-crimson-bright);
      box-shadow: 0 0 14px rgba(179, 27, 39, 0.5);
    }}

    .altar-textarea {{
      min-height: 130px;
      resize: vertical;
    }}

    .commune-links-grid {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-top: 38px;
      flex-wrap: wrap;
    }}

    .commune-anchor {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 12px 22px;
      background-color: rgba(14, 14, 20, 0.8);
      border: 1px solid var(--color-border-crimson);
      color: var(--color-bone);
      text-decoration: none;
      font-family: var(--font-epic);
      font-size: 12px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      transition: all 0.3s ease;
    }}

    .commune-anchor:hover {{
      background-color: var(--color-blood-deep);
      border-color: var(--color-crimson-bright);
      color: #ffffff;
      box-shadow: 0 0 16px rgba(179, 27, 39, 0.5);
      transform: translateY(-2px);
    }}

    /* ==========================================================================
       MODAL FOR RELIC DETAILS
       ========================================================================== */
    .modal-veil {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: rgba(3, 3, 5, 0.94);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}

    .modal-veil.visible {{
      display: flex;
    }}

    .modal-scroll {{
      background-color: #0c0c12;
      border: 1px solid var(--color-crimson-bright);
      width: 100%;
      max-width: 720px;
      padding: 42px 36px;
      position: relative;
      box-shadow: 0 0 50px rgba(0,0,0,0.95), 0 0 30px rgba(135, 20, 31, 0.5);
      animation: modalArrive 0.35s ease-out;
    }}

    @keyframes modalArrive {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .modal-close-trigger {{
      position: absolute;
      top: 16px;
      right: 20px;
      background: none;
      border: none;
      color: var(--color-crimson-bright);
      font-size: 26px;
      cursor: pointer;
      line-height: 1;
      transition: color 0.2s ease;
    }}

    .modal-close-trigger:hover {{
      color: #ffffff;
      text-shadow: 0 0 10px var(--color-crimson-bright);
    }}

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    .cinematic-footer {{
      background-color: var(--color-void);
      border-top: 1px solid var(--color-border-crimson);
      padding: 50px 20px 40px;
      text-align: center;
      position: relative;
      z-index: 10;
    }}

    .footer-emblem-sigil {{
      color: var(--color-blood-glow);
      font-size: 24px;
      margin-bottom: 14px;
      text-shadow: 0 0 14px rgba(179, 27, 39, 0.8);
    }}

    .footer-title {{
      color: var(--color-bone);
      font-family: var(--font-epic);
      font-size: 15px;
      letter-spacing: 0.25em;
      margin-bottom: 8px;
    }}

    .footer-creed {{
      font-size: 13px;
      color: var(--color-ash);
      letter-spacing: 0.2em;
      text-transform: uppercase;
    }}

    /* ==========================================================================
       MOBILE RESPONSIVENESS
       ========================================================================== */
    @media (max-width: 768px) {{
      .cinematic-header {{
        padding: 14px 20px;
      }}
      .cinematic-nav {{
        display: none;
      }}
      .skills-grid-cinematic {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .chronicles-grid {{
        grid-template-columns: 1fr;
      }}
      .sanctum-stone-altar {{
        padding: 28px 20px;
      }}
      .hero-name {{
        letter-spacing: 0.08em;
      }}
      .cinematic-btn {{
        padding: 16px 30px;
        font-size: 12px;
      }}
    }}

    @media (max-width: 480px) {{
      .skills-grid-cinematic {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Cinematic Dark Horror Background Art (Lord of the Rings / Gothic Aesthetic) -->
  <div class="bg-viewport">
    <div class="bg-horror-art" id="horrorBgArt" role="img" aria-label="Dark Horror Gothic Winged Demon and Barbed Occult Sigils"></div>
  </div>
  <div class="bg-cinematic-shroud"></div>
  <div class="bg-stone-grain"></div>
  <canvas id="ashCanvas"></canvas>

  <!-- Navigation Header -->
  <header class="cinematic-header">
    <a href="#" class="brand-sigil">
      <span class="brand-monogram">𐕣</span>
      <span>Mukul Saini</span>
    </a>

    <ul class="cinematic-nav">
      <li><a href="#hero" class="cinematic-nav-link">Prologue</a></li>
      <li><a href="#codex" class="cinematic-nav-link">The Black Codex</a></li>
      <li><a href="#chronicles" class="cinematic-nav-link">Relics</a></li>
      <li><a href="#summon" class="cinematic-nav-link">Summon</a></li>
    </ul>

    <button class="ambient-drone-toggle" id="droneToggleBtn" aria-label="Toggle Cinematic Mordor Drone">
      <span id="droneIcon">†</span>
      <span id="droneText">Nazgûl Chant</span>
    </button>
  </header>

  <!-- Main Content Wrapper -->
  <div class="content-wrapper">

    <!-- Hero Section: Cinematic Prologue -->
    <section id="hero" class="hero-container">
      <div class="hero-sigil-seal">
        <svg viewBox="0 0 100 100" fill="none" stroke="#87141f" stroke-width="1.8">
          <circle cx="50" cy="50" r="42" stroke-dasharray="4 2"/>
          <circle cx="50" cy="50" r="30" stroke="#c5a059" stroke-width="1.2"/>
          <path d="M50 8 L50 92 M8 50 L92 50" stroke="#87141f" stroke-width="1.5"/>
          <path d="M22 22 L78 78 M22 78 L78 22" stroke="#4a080e" stroke-width="1"/>
          <polygon points="50,18 58,42 82,50 58,58 50,82 42,58 18,50 42,42" fill="none" stroke="#c5a059" stroke-width="1.2"/>
        </svg>
      </div>

      <div class="hero-film-preamble">Chronicles of the Dark Frontier · IBM CSE-AI</div>
      <h1 class="hero-name">MUKUL SAINI</h1>
      <div class="hero-sub">JECRC College | BTech CSE-AI (IBM) | First Year Student</div>

      <div class="barbed-divider">
        <div class="barbed-line"></div>
        <div class="barbed-emblem">𐕣</div>
        <div class="barbed-line"></div>
      </div>

      <p class="hero-prologue">
        "Three Rings for the Elven-kings under the sky, seven for the Dwarf-lords in their halls of stone... and in the darkness of synthetic silicon, one weaves the neural sigils that bind cognition to will. Forging intelligent architectures from primal noise, walking between ancient mathematics and forbidden cognitive horizons."
      </p>

      <a href="#codex" class="cinematic-btn" id="summonHeroAction">Summon Portfolio</a>
    </section>

    <!-- Skills Section: The Forbidden Black Codex -->
    <section id="codex" class="skills-monolith-section">
      <div class="chapter-heading">
        <div class="chapter-numeral">The Black Archives</div>
        <h2 class="chapter-title">The Inscribed Codex & Skills</h2>
        <div class="barbed-divider">
          <div class="barbed-line"></div>
          <div class="barbed-emblem">†</div>
          <div class="barbed-line"></div>
        </div>
        <p class="chapter-subtitle">
          Twenty-seven arcane disciplines carved into obsidian slabs. Mathematical rites, deep neural architectures, and computational sorceries.
        </p>
      </div>

      <!-- 27 Engraved Monolithic Stone Tablets -->
      <div class="skills-grid-cinematic">
        <!-- 1. Python -->
        <div class="codex-tablet">
          <span class="tablet-index">I · SCRIPTURE</span>
          <div class="tablet-name">Python</div>
          <span class="tablet-sub">The Primeval Tongue</span>
        </div>
        <!-- 2. Machine Learning -->
        <div class="codex-tablet">
          <span class="tablet-index">II · RITE</span>
          <div class="tablet-name">Machine Learning</div>
          <span class="tablet-sub">Predictive Sorcery</span>
        </div>
        <!-- 3. Deep Learning -->
        <div class="codex-tablet">
          <span class="tablet-index">III · ABYSS</span>
          <div class="tablet-name">Deep Learning</div>
          <span class="tablet-sub">Multi-Layered Cognition</span>
        </div>
        <!-- 4. TensorFlow -->
        <div class="codex-tablet">
          <span class="tablet-index">IV · FORGE</span>
          <div class="tablet-name">TensorFlow</div>
          <span class="tablet-sub">Graph Computation</span>
        </div>
        <!-- 5. PyTorch -->
        <div class="codex-tablet">
          <span class="tablet-index">V · ANVIL</span>
          <div class="tablet-name">PyTorch</div>
          <span class="tablet-sub">Dynamic Autograd Forge</span>
        </div>
        <!-- 6. NLP -->
        <div class="codex-tablet">
          <span class="tablet-index">VI · SPEECH</span>
          <div class="tablet-name">NLP</div>
          <span class="tablet-sub">Semantic Divination</span>
        </div>
        <!-- 7. Computer Vision -->
        <div class="codex-tablet">
          <span class="tablet-index">VII · SIGHT</span>
          <div class="tablet-name">Computer Vision</div>
          <span class="tablet-sub">Optical Perception</span>
        </div>
        <!-- 8. Neural Networks -->
        <div class="codex-tablet">
          <span class="tablet-index">VIII · SYNAPSE</span>
          <div class="tablet-name">Neural Networks</div>
          <span class="tablet-sub">Artificial Bio-Circuits</span>
        </div>
        <!-- 9. Data Analysis -->
        <div class="codex-tablet">
          <span class="tablet-index">IX · SCRYING</span>
          <div class="tablet-name">Data Analysis</div>
          <span class="tablet-sub">Empirical Truth Extraction</span>
        </div>
        <!-- 10. Scikit-learn -->
        <div class="codex-tablet">
          <span class="tablet-index">X · TOMES</span>
          <div class="tablet-name">Scikit-learn</div>
          <span class="tablet-sub">Foundational Grimoires</span>
        </div>
        <!-- 11. Pandas -->
        <div class="codex-tablet">
          <span class="tablet-index">XI · MATRIX</span>
          <div class="tablet-name">Pandas</div>
          <span class="tablet-sub">Tabular Manipulation</span>
        </div>
        <!-- 12. NumPy -->
        <div class="codex-tablet">
          <span class="tablet-index">XII · TENSORS</span>
          <div class="tablet-name">NumPy</div>
          <span class="tablet-sub">Vector Space Linearities</span>
        </div>
        <!-- 13. Keras -->
        <div class="codex-tablet">
          <span class="tablet-index">XIII · LAYERS</span>
          <div class="tablet-name">Keras</div>
          <span class="tablet-sub">High-Level Abstractions</span>
        </div>
        <!-- 14. LLMs -->
        <div class="codex-tablet">
          <span class="tablet-index">XIV · ORACLES</span>
          <div class="tablet-name">LLMs</div>
          <span class="tablet-sub">Billion-Parameter Voices</span>
        </div>
        <!-- 15. Prompt Engineering -->
        <div class="codex-tablet">
          <span class="tablet-index">XV · INCANTATION</span>
          <div class="tablet-name">Prompt Engineering</div>
          <span class="tablet-sub">Latent Steering Rites</span>
        </div>
        <!-- 16. Hugging Face -->
        <div class="codex-tablet">
          <span class="tablet-index">XVI · SANCTUM</span>
          <div class="tablet-name">Hugging Face</div>
          <span class="tablet-sub">Repository of Models</span>
        </div>
        <!-- 17. OpenCV -->
        <div class="codex-tablet">
          <span class="tablet-index">XVII · OCULUS</span>
          <div class="tablet-name">OpenCV</div>
          <span class="tablet-sub">Matrix Lens Transformations</span>
        </div>
        <!-- 18. Statistics -->
        <div class="codex-tablet">
          <span class="tablet-index">XVIII · CHANCE</span>
          <div class="tablet-name">Statistics</div>
          <span class="tablet-sub">Probabilistic Laws</span>
        </div>
        <!-- 19. Linear Algebra -->
        <div class="codex-tablet">
          <span class="tablet-index">XIX · GEOMETRY</span>
          <div class="tablet-name">Linear Algebra</div>
          <span class="tablet-sub">Eigenvalues & Manifolds</span>
        </div>
        <!-- 20. SQL -->
        <div class="codex-tablet">
          <span class="tablet-index">XX · VAULTS</span>
          <div class="tablet-name">SQL</div>
          <span class="tablet-sub">Relational Catacombs</span>
        </div>
        <!-- 21. AWS -->
        <div class="codex-tablet">
          <span class="tablet-index">XXI · AETHER</span>
          <div class="tablet-name">AWS</div>
          <span class="tablet-sub">Cloud Citadel Infrastructure</span>
        </div>
        <!-- 22. GCP -->
        <div class="codex-tablet">
          <span class="tablet-index">XXII · CLOUD</span>
          <div class="tablet-name">GCP</div>
          <span class="tablet-sub">Distributed TPU Bastions</span>
        </div>
        <!-- 23. Docker -->
        <div class="codex-tablet">
          <span class="tablet-index">XXIII · COFFIN</span>
          <div class="tablet-name">Docker</div>
          <span class="tablet-sub">Hermetic Containerization</span>
        </div>
        <!-- 24. Git -->
        <div class="codex-tablet">
          <span class="tablet-index">XXIV · CHRONICLE</span>
          <div class="tablet-name">Git</div>
          <span class="tablet-sub">Branching Timelines</span>
        </div>
        <!-- 25. APIs -->
        <div class="codex-tablet">
          <span class="tablet-index">XXV · PORTAL</span>
          <div class="tablet-name">APIs</div>
          <span class="tablet-sub">Inter-System Gateways</span>
        </div>
        <!-- 26. Reinforcement Learning -->
        <div class="codex-tablet">
          <span class="tablet-index">XXVI · AGONY</span>
          <div class="tablet-name">Reinforcement Learning</div>
          <span class="tablet-sub">Trial by Punishment & Reward</span>
        </div>
        <!-- 27. Flask -->
        <div class="codex-tablet">
          <span class="tablet-index">XXVII · ELIXIR</span>
          <div class="tablet-name">Flask</div>
          <span class="tablet-sub">Micro-Framework Serving</span>
        </div>
      </div>
    </section>

    <!-- Prophetic Cinematic Scroll (Lord of the Rings Mordor Vibe) -->
    <div class="prophetic-monolith">
      <p class="prophetic-quote">
        "One does not simply walk into the neural latent space. Its black gates are guarded by more than just mathematical loss functions; there is an evil gradient there that does not sleep. The Great Eye of Stochastic Descent is ever watchful."
      </p>
      <div class="prophetic-inscription">— Inscribed into the Obsidian Pillar of Barad-dûr · Book of Latent Sorcery</div>
    </div>

    <!-- Projects Section: The Consecrated Relics (Cinematic Chronicles) -->
    <section id="chronicles" class="projects-chronicle-section">
      <div class="chapter-heading">
        <div class="chapter-numeral">Chronicles of Steel & Silicon</div>
        <h2 class="chapter-title">The Consecrated Relics</h2>
        <div class="barbed-divider">
          <div class="barbed-line"></div>
          <div class="barbed-emblem">⚔</div>
          <div class="barbed-line"></div>
        </div>
        <p class="chapter-subtitle">
          Constructs forged in the fires of deep learning, stochastic optimization, and autonomous perception.
        </p>
      </div>

      <div class="chronicles-grid">
        <!-- Relic 1 -->
        <div class="chronicle-slab">
          <div>
            <div class="chronicle-header-badge">Tome I · Neural Synthesis</div>
            <h3 class="chronicle-title">Vision of the Nether</h3>
            <div class="chronicle-canon">Deep Convolutional Autoencoder & Latent Walk Manifold</div>
            <p class="chronicle-narrative">
              An unsupervised generative framework mapping high-dimensional visual structures into compressed continuous latent vectors. Enables smooth geometric trajectories across manifold spaces to reconstruct dark gothic forms and morphing topologies.
            </p>
            <div class="chronicle-sigils-row">
              <span class="chronicle-sigil">PyTorch</span>
              <span class="chronicle-sigil">Autoencoders</span>
              <span class="chronicle-sigil">Computer Vision</span>
              <span class="chronicle-sigil">Flask</span>
            </div>
          </div>
          <div class="chronicle-footer">
            <button class="chronicle-inspect-btn" onclick="openGrimoireModal('nether-vision')">
              <span>Unseal Grimoire</span> →
            </button>
            <span class="chronicle-runic-sigil">᚛ ᚜ 𐕣</span>
          </div>
        </div>

        <!-- Relic 2 -->
        <div class="chronicle-slab">
          <div>
            <div class="chronicle-header-badge">Tome II · Transformer Oracles</div>
            <h3 class="chronicle-title">The Black Lexicon</h3>
            <div class="chronicle-canon">Contextual Semantic Reasoning & Attention Engine</div>
            <p class="chronicle-narrative">
              A specialized Natural Language processing pipeline leveraging Hugging Face transformer weights. Employs multi-head cross-attention and dense vector retrieval to query vast technical treatises, extracting rigorous synthetic insights with verified citations.
            </p>
            <div class="chronicle-sigils-row">
              <span class="chronicle-sigil">Hugging Face</span>
              <span class="chronicle-sigil">LLMs</span>
              <span class="chronicle-sigil">NLP</span>
              <span class="chronicle-sigil">Prompt Eng</span>
            </div>
          </div>
          <div class="chronicle-footer">
            <button class="chronicle-inspect-btn" onclick="openGrimoireModal('black-lexicon')">
              <span>Unseal Grimoire</span> →
            </button>
            <span class="chronicle-runic-sigil">ᛟ ᛉ ᛋ</span>
          </div>
        </div>

        <!-- Relic 3 -->
        <div class="chronicle-slab">
          <div>
            <div class="chronicle-header-badge">Tome III · Edge Surveillance</div>
            <h3 class="chronicle-title">The Aegis Vigil</h3>
            <div class="chronicle-canon">Autonomous Real-Time Video Anomaly & Intrusion Sentry</div>
            <p class="chronicle-narrative">
              A low-latency video surveillance sentinel combining OpenCV optical flow heuristics with lightweight neural feature extractors. Continuously monitors video streams to flag kinetic perimeter breaches, abnormal velocities, and optical deviations.
            </p>
            <div class="chronicle-sigils-row">
              <span class="chronicle-sigil">OpenCV</span>
              <span class="chronicle-sigil">Deep Learning</span>
              <span class="chronicle-sigil">Docker</span>
              <span class="chronicle-sigil">APIs</span>
            </div>
          </div>
          <div class="chronicle-footer">
            <button class="chronicle-inspect-btn" onclick="openGrimoireModal('aegis-vigil')">
              <span>Unseal Grimoire</span> →
            </button>
            <span class="chronicle-runic-sigil">ᚠ ᚢ ᚱ</span>
          </div>
        </div>

        <!-- Relic 4 -->
        <div class="chronicle-slab">
          <div>
            <div class="chronicle-header-badge">Tome IV · Stochastic Calibration</div>
            <h3 class="chronicle-title">Alchemical Data Crucible</h3>
            <div class="chronicle-canon">Multivariate Predictive Modeling & Regression Matrices</div>
            <p class="chronicle-narrative">
              Comprehensive statistical modeling engine transforming chaotic tabular datasets into calibrated predictive probability distributions. Implements automated feature scaling, recursive elimination, and cross-validated ensemble estimators.
            </p>
            <div class="chronicle-sigils-row">
              <span class="chronicle-sigil">Scikit-learn</span>
              <span class="chronicle-sigil">Pandas</span>
              <span class="chronicle-sigil">NumPy</span>
              <span class="chronicle-sigil">Statistics</span>
            </div>
          </div>
          <div class="chronicle-footer">
            <button class="chronicle-inspect-btn" onclick="openGrimoireModal('data-crucible')">
              <span>Unseal Grimoire</span> →
            </button>
            <span class="chronicle-runic-sigil">ᛏ ᛒ ᛖ</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Summoning Section: Altar of the Nazgûl -->
    <section id="summon" class="summon-sanctum-section">
      <div class="chapter-heading">
        <div class="chapter-numeral">Communion Across the Shadow</div>
        <h2 class="chapter-title">The Altar of Summoning</h2>
        <div class="barbed-divider">
          <div class="barbed-line"></div>
          <div class="barbed-emblem">†</div>
          <div class="barbed-line"></div>
        </div>
        <p class="chapter-subtitle">
          Inscribe your missive upon the black altar. Whether invoking neural research, model architecture consultation, or academic fellowship, your message shall pierce the veil.
        </p>
      </div>

      <div class="sanctum-stone-altar">
        <form class="sanctum-form" id="altarForm" onsubmit="handleAltarDispatch(event)">
          <div class="altar-input-group">
            <label class="altar-label" for="communeName">Bearer's Title / Name</label>
            <input type="text" id="communeName" class="altar-input" placeholder="e.g., Sorcerer of Númenor / AI Scholar" required>
          </div>

          <div class="altar-input-group">
            <label class="altar-label" for="communeEmail">Signal Frequency (Email Address)</label>
            <input type="email" id="communeEmail" class="altar-input" placeholder="e.g., scholar@citadel.ai" required>
          </div>

          <div class="altar-input-group">
            <label class="altar-label" for="communeMessage">Inscribe Your Request into the Stone</label>
            <textarea id="communeMessage" class="altar-textarea" placeholder="Detail the dataset, architectural challenge, or collaborative expedition..." required></textarea>
          </div>

          <button type="submit" class="cinematic-btn" id="altarSubmitBtn">
            Inscribe & Transmit Missive (Send)
          </button>

          <div id="altarConfirmation" style="display:none; text-align:center; color:#e2ded5; font-family:var(--font-epic); margin-top:16px; font-size:13px; letter-spacing:0.2em; border: 1px solid var(--color-crimson-bright); padding: 14px; background-color: rgba(74, 8, 14, 0.6);">
            † RITE CONSECRATED: The missive has been cast into the black fire. Mukul Saini shall heed your summons.
          </div>
        </form>

        <div class="barbed-divider" style="margin: 36px auto 24px;">
          <div class="barbed-line"></div>
          <div class="barbed-emblem">𐕣</div>
          <div class="barbed-line"></div>
        </div>

        <div class="commune-links-grid">
          <a href="mailto:mukulsaini@jecrc.ac.in" class="commune-anchor" title="Direct Electronic Mail">
            <span>✉</span> Direct Epistle
          </a>
          <a href="https://github.com" target="_blank" rel="noopener" class="commune-anchor" title="GitHub Catacombs">
            <span>⚔</span> GitHub Archives
          </a>
          <a href="https://linkedin.com" target="_blank" rel="noopener" class="commune-anchor" title="Guild Network">
            <span>𐕣</span> LinkedIn Sanctum
          </a>
          <a href="https://kaggle.com" target="_blank" rel="noopener" class="commune-anchor" title="Kaggle Arenas">
            <span>†</span> Kaggle Arena
          </a>
        </div>
      </div>
    </section>

  </div>

  <!-- Relic Modal Veil -->
  <div class="modal-veil" id="grimoireModal" onclick="handleModalVeilClick(event)">
    <div class="modal-scroll">
      <button class="modal-close-trigger" onclick="closeGrimoireModal()">&times;</button>
      <div id="grimoireContent">
        <!-- Injected dynamically by JS -->
      </div>
    </div>
  </div>

  <!-- Cinematic Footer -->
  <footer class="cinematic-footer">
    <div class="footer-emblem-sigil">𐕣</div>
    <div class="footer-title">© 2025 Mukul Saini | AI Enchanter</div>
    <div class="footer-creed">JECRC College · BTech CSE-AI (IBM) · First Year Scholar</div>
    <div style="margin-top: 14px; font-size: 11px; color: #5a141b; letter-spacing: 0.25em;">
      ASH NAZG DURBATULÛK · IN SANGUINE ALGORITHMI VERITAS
    </div>
  </footer>

  <!-- ==========================================================================
       CINEMATIC LOGIC & SOUND ENGINE
       ========================================================================== */
  <script>
    // --------------------------------------------------------------------------
    // 1. Lord of the Rings / Mordor Cinematic Drone (Web Audio API)
    // Deep rumbling cinematic bass drone (38Hz sub-bass + 57Hz fifth) with eerie wind
    // --------------------------------------------------------------------------
    let audioContext = null;
    let isDroneActive = false;
    let subOsc = null;
    let midOsc = null;
    let windNoise = null;
    let masterGain = null;

    function toggleCinematicDrone() {{
      const btn = document.getElementById('droneToggleBtn');
      const text = document.getElementById('droneText');
      const icon = document.getElementById('droneIcon');

      if (!audioContext) {{
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
      }}

      if (audioContext.state === 'suspended') {{
        audioContext.resume();
      }}

      if (!isDroneActive) {{
        masterGain = audioContext.createGain();
        masterGain.gain.setValueAtTime(0.0001, audioContext.currentTime);
        masterGain.gain.exponentialRampToValueAtTime(0.09, audioContext.currentTime + 3.5);

        // Low Sub-Bass Oscillator (38 Hz - E0, evoking Mordor's foundations)
        subOsc = audioContext.createOscillator();
        subOsc.type = 'sawtooth';
        subOsc.frequency.setValueAtTime(38, audioContext.currentTime);

        // Sinister fifth (57 Hz)
        midOsc = audioContext.createOscillator();
        midOsc.type = 'sine';
        midOsc.frequency.setValueAtTime(57, audioContext.currentTime);

        // Low-pass filter to make it dark, rumbling and atmospheric
        const droneFilter = audioContext.createBiquadFilter();
        droneFilter.type = 'lowpass';
        droneFilter.frequency.setValueAtTime(140, audioContext.currentTime);

        subOsc.connect(droneFilter);
        midOsc.connect(droneFilter);
        droneFilter.connect(masterGain);
        masterGain.connect(audioContext.destination);

        subOsc.start();
        midOsc.start();

        isDroneActive = true;
        btn.classList.add('active');
        text.textContent = 'Nazgûl Chant Active';
        icon.textContent = '𐕣';
      }} else {{
        if (masterGain) {{
          masterGain.gain.exponentialRampToValueAtTime(0.0001, audioContext.currentTime + 1.5);
          setTimeout(() => {{
            if (subOsc) subOsc.stop();
            if (midOsc) midOsc.stop();
            subOsc = null;
            midOsc = null;
          }}, 1500);
        }}
        isDroneActive = false;
        btn.classList.remove('active');
        text.textContent = 'Nazgûl Chant';
        icon.textContent = '†';
      }}
    }}

    document.getElementById('droneToggleBtn').addEventListener('click', toggleCinematicDrone);

    // --------------------------------------------------------------------------
    // 2. Rising Crimson Ash & Ember Particles Canvas (Mordor Volcanic Motes)
    // --------------------------------------------------------------------------
    const ashCanvas = document.getElementById('ashCanvas');
    const ashCtx = ashCanvas.getContext('2d');
    let width = (ashCanvas.width = window.innerWidth);
    let height = (ashCanvas.height = window.innerHeight);

    window.addEventListener('resize', () => {{
      width = ashCanvas.width = window.innerWidth;
      height = ashCanvas.height = window.innerHeight;
    }});

    const ashParticles = [];
    const ASH_COUNT = 55;

    class AshParticle {{
      constructor() {{
        this.reset(true);
      }}

      reset(initial = false) {{
        this.x = Math.random() * width;
        this.y = initial ? Math.random() * height : height + 10;
        this.size = Math.random() * 2.4 + 0.6;
        this.speedY = Math.random() * 0.7 + 0.25;
        this.speedX = (Math.random() - 0.5) * 0.45;
        this.opacity = Math.random() * 0.65 + 0.15;
        this.decay = Math.random() * 0.0025 + 0.0008;
        // Deep blood crimson (#87141f, #b31b27) & dark volcanic ember
        const tones = ['179, 27, 39', '135, 20, 31', '74, 8, 14', '197, 160, 89'];
        this.color = tones[Math.floor(Math.random() * tones.length)];
      }}

      update() {{
        this.y -= this.speedY;
        this.x += this.speedX;
        this.opacity -= this.decay;

        if (this.y < -10 || this.opacity <= 0) {{
          this.reset(false);
        }}
      }}

      draw() {{
        ashCtx.beginPath();
        ashCtx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ashCtx.fillStyle = `rgba(${{this.color}}, ${{this.opacity}})`;
        ashCtx.shadowBlur = 10;
        ashCtx.shadowColor = `rgba(${{this.color}}, 0.75)`;
        ashCtx.fill();
        ashCtx.shadowBlur = 0;
      }}
    }}

    for (let i = 0; i < ASH_COUNT; i++) {{
      ashParticles.push(new AshParticle());
    }}

    function loopAsh() {{
      ashCtx.clearRect(0, 0, width, height);
      for (let i = 0; i < ashParticles.length; i++) {{
        ashParticles[i].update();
        ashParticles[i].draw();
      }}
      requestAnimationFrame(loopAsh);
    }}
    loopAsh();

    // --------------------------------------------------------------------------
    // 3. Cinematic Subtle Parallax on Horror Background
    // --------------------------------------------------------------------------
    const horrorBgArt = document.getElementById('horrorBgArt');
    window.addEventListener('scroll', () => {{
      const scrollY = window.pageYOffset;
      horrorBgArt.style.transform = `scale(1.03) translateY(${{scrollY * 0.06}}px)`;
    }}, {{ passive: true }});

    // --------------------------------------------------------------------------
    // 4. Consecrated Relic Grimoire Modal System
    // --------------------------------------------------------------------------
    const grimoires = {{
      'nether-vision': {{
        title: 'Vision of the Nether',
        canon: 'Tome I · Neural Generative Latent Walk Manifold',
        sigils: 'PyTorch · Autoencoders · Computer Vision · Flask',
        runes: '𐕣 ᚠ ᚢ ᚦ · DEEP CONVOLUTIONAL ARCHIVAL',
        prose: 'A deep generative computer vision pipeline analyzing compressed latent dimensional representations of gothic silhouettes and dark textures. Built using symmetric PyTorch convolutional encoder-decoder backbones.',
        manifesto: [
          'High-fidelity bottleneck compression isolating primary geometric manifolds',
          'Smooth Riemannian spherical linear interpolation (slerp) between distant latent seeds',
          'Custom compound loss function penalizing perceptual blur while preserving sharp edge boundaries',
          'Integrated Flask runtime for instantaneous parameter manipulation and latent traversal'
        ]
      }},
      'black-lexicon': {{
        title: 'The Black Lexicon',
        canon: 'Tome II · Contextual Semantic Reasoning & Attention Engine',
        sigils: 'Hugging Face · LLMs · NLP · Prompt Engineering',
        runes: 'ᛟ ᛉ ᛋ · DENSE VECTOR CROSS-ATTENTION',
        prose: 'A sophisticated academic reasoning oracle fine-tuned to parse and cross-examine massive technical corpora. Leverages transformer embeddings and vector similarity to synthesize complex concepts without hallucination.',
        manifesto: [
          'Hybrid dense retrieval combining bi-encoder embeddings with BM25 keyword verification',
          'Chain-of-thought prompt constraint protocols enforcing strict source citation attribution',
          'Benchmarked transformer tokenizers measuring semantic preservation across technical domains',
          'Asynchronous query dispatcher supporting scalable academic document ingestion'
        ]
      }},
      'aegis-vigil': {{
        title: 'The Aegis Vigil',
        canon: 'Tome III · Autonomous Real-Time Video Anomaly Sentry',
        sigils: 'OpenCV · Deep Learning · Docker · APIs',
        runes: 'ᚠ ᚢ ᚱ · KINEMATIC BOUNDARY SURVEILLANCE',
        prose: 'An edge-optimized visual sentinel inspecting real-time camera streams for spatial intrusions, anomalous directional vectors, and perimeter breaches.',
        manifesto: [
          'Sub-second frame extraction and preprocessing utilizing accelerated OpenCV image operators',
          'Temporal heuristics filtering out atmospheric noise, lens artifacts, and shifting illumination',
          'Lightweight neural inference engine packaged inside Docker containers for edge micro-nodes',
          'Real-time webhook dispatcher broadcasting alerts with timestamped boundary telemetry'
        ]
      }},
      'data-crucible': {{
        title: 'Alchemical Data Crucible',
        canon: 'Tome IV · Multivariate Predictive Modeling & Regression Matrices',
        sigils: 'Scikit-learn · Pandas · NumPy · Statistics',
        runes: 'ᛏ ᛒ ᛖ · STOCHASTIC PROBABILITY DISTRIBUTIONS',
        prose: 'A comprehensive empirical modeling laboratory converting noisy high-dimensional business and scientific datasets into robust probabilistic forecasts.',
        manifesto: [
          'Automated data cleaning, skew reduction, and missing feature imputation across training partitions',
          'Hyperparameter optimization using stratified k-fold cross-validation pipelines',
          'Feature importance attribution utilizing permutation analysis and SHAP values',
          'Exhaustive regression diagnostics reporting RMSE, MAE, R², and prediction intervals'
        ]
      }}
    }};

    function openGrimoireModal(key) {{
      const g = grimoires[key];
      if (!g) return;

      const modalContent = document.getElementById('grimoireContent');
      modalContent.innerHTML = `
        <div style="color: var(--color-crimson-bright); font-family: var(--font-epic); font-size: 11px; letter-spacing: 0.35em; margin-bottom: 8px;">
          ${{g.runes}}
        </div>
        <h2 style="font-family:var(--font-epic); font-size: 1.85rem; color: var(--color-gold-pale); margin-bottom: 4px; letter-spacing: 0.1em; text-transform:uppercase;">
          ${{g.title}}
        </h2>
        <div style="font-size: 1.05rem; color: var(--color-ash); font-style: italic; margin-bottom: 16px;">
          ${{g.canon}}
        </div>
        <div style="display:inline-block; font-family:var(--font-epic); font-size:11px; color:var(--color-bone); background-color:rgba(74,8,14,0.6); padding:4px 14px; border:1px solid var(--color-crimson-bright); margin-bottom: 22px; letter-spacing:0.15em; text-transform:uppercase;">
          ${{g.sigils}}
        </div>
        <p style="color: var(--color-bone); font-size: 1.1rem; line-height: 1.75; margin-bottom: 24px;">
          ${{g.prose}}
        </p>
        <div style="border-top: 1px solid rgba(135,20,31,0.4); padding-top: 20px; margin-bottom: 26px;">
          <div style="font-family:var(--font-epic); font-size:12px; color:var(--color-crimson-bright); letter-spacing:0.25em; text-transform:uppercase; margin-bottom:12px;">
            Archival Rites & Technical Highlights:
          </div>
          <ul style="list-style:none; padding-left:0; color:var(--color-ash); font-size:1rem; line-height:1.85;">
            ${{g.manifesto.map(m => `<li style="display:flex; align-items:flex-start; gap:12px;"><span style="color:var(--color-crimson-bright); font-size:14px;">†</span> <span>${{m}}</span></li>`).join('')}}
          </ul>
        </div>
        <div style="display: flex; justify-content: flex-end;">
          <button class="cinematic-btn" style="padding: 10px 24px; font-size: 12px;" onclick="closeGrimoireModal()">Seal Tome</button>
        </div>
      `;

      document.getElementById('grimoireModal').classList.add('visible');
    }}

    function closeGrimoireModal() {{
      document.getElementById('grimoireModal').classList.remove('visible');
    }}

    function handleModalVeilClick(e) {{
      if (e.target.id === 'grimoireModal') {{
        closeGrimoireModal();
      }}
    }}

    // --------------------------------------------------------------------------
    // 5. Altar Missive Transmission (Contact Form Submission)
    // --------------------------------------------------------------------------
    function handleAltarDispatch(e) {{
      e.preventDefault();
      const btn = document.getElementById('altarSubmitBtn');
      const confirmation = document.getElementById('altarConfirmation');

      btn.disabled = true;
      btn.textContent = 'Transmitting into the Shadow...';

      setTimeout(() => {{
        confirmation.style.display = 'block';
        btn.textContent = 'Rite Consecrated †';
        document.getElementById('altarForm').reset();

        setTimeout(() => {{
          btn.disabled = false;
          btn.textContent = 'Inscribe & Transmit Missive (Send)';
        }}, 5000);
      }}, 800);
    }}
  </script>
  <!-- Botpress Webchat -->
  <script src="https://cdn.botpress.cloud/webchat/v5.0/inject.js"></script>
  <script src="https://files.bpcontent.cloud/2026/09/17/03/20260917032227-J7HCJHXM.js" defer></script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html rewritten successfully. New size:", os.path.getsize('index.html'), "bytes")

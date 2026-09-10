import base64
import os

with open('background.jpg', 'rb') as f:
    bg_base64 = base64.b64encode(f.read()).decode('utf-8')

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mukul Saini | AI Enchanter & Researcher</title>
  <meta name="description" content="Portfolio of Mukul Saini - First Year BTech CSE-AI (IBM) Student at JECRC College. Machine Learning, Deep Learning, and AI Craftsman.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       DARK FANTASY GOTHIC THEME SYSTEM
       Colors:
         Deep Purple:   #2d1b4e
         Charcoal Black: #1a1a2e
         Dark Slate:     #16213e
         Accent Gold:    #d4af37
         Deep Orange:    #8b4513
         Pale Gold Text: #e8d4a8
         Muted Slate:    #9e9eb3
       No gradients, flat dark colors, nostalgic 80s dark fantasy atmosphere.
       ========================================================================== */
    :root {{
      --color-purple: #2d1b4e;
      --color-charcoal: #1a1a2e;
      --color-slate: #16213e;
      --color-gold: #d4af37;
      --color-deep-orange: #8b4513;
      --color-text-gold: #e8d4a8;
      --color-text-dim: #b8a893;
      --color-border-gold: rgba(212, 175, 55, 0.4);
      --color-border-subtle: rgba(212, 175, 55, 0.2);
      
      --font-display: 'Cinzel', 'Garamond', 'Georgia', serif;
      --font-body: 'EB Garamond', 'Garamond', 'Georgia', serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      background-color: var(--color-charcoal);
      color: var(--color-text-gold);
      font-family: var(--font-body);
      font-size: 18px;
      line-height: 1.7;
      overflow-x: hidden;
      min-height: 100vh;
      position: relative;
    }}

    /* ==========================================================================
       ENHANCED BACKGROUND SYSTEM (DIO HOLY DIVER 1983 ARTWORK)
       Enhanced with rich contrast, atmospheric depth & dark vignette
       ========================================================================== */
    .bg-canvas-container {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -3;
      overflow: hidden;
      pointer-events: none;
    }}

    .bg-image {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image: url('data:image/jpeg;base64,{bg_base64}');
      background-size: cover;
      background-position: center top;
      background-repeat: no-repeat;
      /* Visual enhancement: punchy contrast, saturated twilight hues, deep shadows */
      filter: contrast(1.18) brightness(0.78) saturate(1.22);
      transform: scale(1.02);
      transition: transform 0.6s ease-out;
    }}

    /* Dark atmospheric tinted shield for text legibility without losing the epic painting */
    .bg-darkness-scrim {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -2;
      background-color: rgba(26, 26, 46, 0.82);
      pointer-events: none;
    }}

    /* Subtle rocky / mystical noise texture overlay */
    .bg-rocky-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -1;
      opacity: 0.12;
      pointer-events: none;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
    }}

    /* Interactive ember particles canvas */
    #emberCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
    }}

    /* ==========================================================================
       GOTHIC ORNAMENTS, FRAMES & TYPOGRAPHY
       ========================================================================== */
    h1, h2, h3, h4, .gothic-title {{
      font-family: var(--font-display);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-weight: 700;
    }}

    .gold-text {{
      color: var(--color-gold);
      text-shadow: 0 0 10px rgba(212, 175, 55, 0.45);
    }}

    .gothic-divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin: 28px auto;
      width: 100%;
      max-width: 480px;
    }}

    .gothic-divider-line {{
      flex: 1;
      height: 1px;
      background-color: var(--color-border-gold);
    }}

    .gothic-divider-symbol {{
      color: var(--color-gold);
      font-size: 16px;
      line-height: 1;
      text-shadow: 0 0 8px rgba(212, 175, 55, 0.6);
    }}

    /* Gothic Corner Frame brackets */
    .gothic-box {{
      position: relative;
      background-color: var(--color-charcoal);
      border: 1px solid var(--color-border-gold);
      transition: all 0.3s ease;
    }}

    .gothic-box::before, .gothic-box::after {{
      content: '';
      position: absolute;
      width: 8px;
      height: 8px;
      border-color: var(--color-gold);
      pointer-events: none;
    }}

    .gothic-box::before {{
      top: -2px;
      left: -2px;
      border-top: 2px solid var(--color-gold);
      border-left: 2px solid var(--color-gold);
    }}

    .gothic-box::after {{
      bottom: -2px;
      right: -2px;
      border-bottom: 2px solid var(--color-gold);
      border-right: 2px solid var(--color-gold);
    }}

    /* ==========================================================================
       TOP NAVIGATION BAR
       ========================================================================== */
    .top-nav {{
      position: sticky;
      top: 0;
      width: 100%;
      z-index: 100;
      background-color: var(--color-charcoal);
      border-bottom: 1px solid var(--color-border-gold);
      padding: 14px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--color-gold);
      font-family: var(--font-display);
      font-size: 19px;
      letter-spacing: 0.15em;
    }}

    .nav-brand-seal {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border: 1px solid var(--color-gold);
      background-color: var(--color-purple);
      color: var(--color-gold);
      font-size: 15px;
      transform: rotate(45deg);
    }}
    .nav-brand-seal span {{
      transform: rotate(-45deg);
      font-weight: 700;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 28px;
      list-style: none;
    }}

    .nav-link {{
      color: var(--color-text-gold);
      text-decoration: none;
      font-family: var(--font-display);
      font-size: 14px;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      position: relative;
      transition: color 0.25s ease, text-shadow 0.25s ease;
    }}

    .nav-link:hover {{
      color: #fff4d1;
      text-shadow: 0 0 10px var(--color-gold);
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .ambient-btn {{
      background-color: var(--color-slate);
      border: 1px solid var(--color-border-gold);
      color: var(--color-text-gold);
      padding: 6px 12px;
      font-family: var(--font-display);
      font-size: 12px;
      letter-spacing: 0.1em;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.3s ease;
    }}

    .ambient-btn:hover {{
      border-color: var(--color-gold);
      color: #ffffff;
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.4);
    }}

    .ambient-btn.active {{
      background-color: var(--color-purple);
      border-color: var(--color-gold);
      color: var(--color-gold);
    }}

    /* ==========================================================================
       MAIN CONTAINER
       ========================================================================== */
    .wrapper {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 10;
    }}

    /* ==========================================================================
       HERO SECTION
       ========================================================================== */
    .hero-section {{
      min-height: 90vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 80px 20px 60px;
      position: relative;
    }}

    .hero-emblem {{
      width: 72px;
      height: 72px;
      margin-bottom: 24px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .hero-emblem-outer {{
      position: absolute;
      width: 100%;
      height: 100%;
      border: 1px solid var(--color-gold);
      transform: rotate(45deg);
      background-color: var(--color-purple);
      box-shadow: 0 0 16px rgba(212, 175, 55, 0.25);
    }}

    .hero-emblem-inner {{
      position: absolute;
      width: 76%;
      height: 76%;
      border: 1px dashed var(--color-gold);
      transform: rotate(45deg);
    }}

    .hero-emblem-icon {{
      position: relative;
      z-index: 2;
      color: var(--color-gold);
      font-size: 26px;
      text-shadow: 0 0 12px rgba(212, 175, 55, 0.8);
    }}

    .hero-tagline {{
      font-family: var(--font-display);
      font-size: 13px;
      letter-spacing: 0.3em;
      color: var(--color-deep-orange);
      text-transform: uppercase;
      margin-bottom: 12px;
      font-weight: 600;
    }}

    .hero-title {{
      font-size: clamp(2.8rem, 6vw, 4.8rem);
      color: var(--color-gold);
      letter-spacing: 0.16em;
      margin-bottom: 16px;
      line-height: 1.15;
      text-shadow: 0 0 18px rgba(212, 175, 55, 0.5), 0 0 35px rgba(212, 175, 55, 0.2);
    }}

    .hero-subtitle {{
      font-family: var(--font-display);
      font-size: clamp(1.05rem, 2.2vw, 1.35rem);
      color: #dfd2be;
      letter-spacing: 0.08em;
      margin-bottom: 22px;
      max-width: 800px;
    }}

    .hero-bio {{
      max-width: 680px;
      font-size: 1.15rem;
      color: var(--color-text-dim);
      margin: 0 auto 36px;
      font-style: italic;
      line-height: 1.8;
    }}

    /* Gothic CTA Button */
    .gothic-btn {{
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      padding: 16px 38px;
      background-color: var(--color-purple);
      border: 1px solid var(--color-gold);
      color: var(--color-gold);
      font-family: var(--font-display);
      font-size: 15px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      text-decoration: none;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
      transition: all 0.3s ease;
    }}

    .gothic-btn::before, .gothic-btn::after {{
      content: '❖';
      font-size: 12px;
      color: var(--color-gold);
      transition: transform 0.3s ease;
    }}

    .gothic-btn:hover {{
      background-color: var(--color-slate);
      color: #fff8e1;
      border-color: #f7e096;
      box-shadow: 0 0 20px rgba(212, 175, 55, 0.55), inset 0 0 10px rgba(212, 175, 55, 0.2);
      transform: translateY(-2px);
    }}

    .gothic-btn:hover::before {{
      transform: rotate(45deg);
    }}
    .gothic-btn:hover::after {{
      transform: rotate(-45deg);
    }}

    /* ==========================================================================
       SECTION HEADERS
       ========================================================================== */
    .section-header {{
      text-align: center;
      margin-bottom: 48px;
    }}

    .section-pretitle {{
      font-family: var(--font-display);
      font-size: 12px;
      letter-spacing: 0.3em;
      color: var(--color-deep-orange);
      text-transform: uppercase;
      margin-bottom: 6px;
    }}

    .section-title {{
      font-size: clamp(1.8rem, 3.5vw, 2.5rem);
      color: var(--color-gold);
      letter-spacing: 0.12em;
      text-shadow: 0 0 12px rgba(212, 175, 55, 0.35);
    }}

    .section-description {{
      max-width: 620px;
      margin: 12px auto 0;
      color: var(--color-text-dim);
      font-size: 1.05rem;
    }}

    /* ==========================================================================
       SKILLS SECTION (ARCANE DISCIPLINES)
       ========================================================================== */
    .skills-section {{
      padding: 90px 0 60px;
    }}

    .skills-filter-container {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 36px;
    }}

    .filter-btn {{
      background-color: var(--color-charcoal);
      border: 1px solid var(--color-border-gold);
      color: var(--color-text-dim);
      padding: 8px 18px;
      font-family: var(--font-display);
      font-size: 12px;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.25s ease;
    }}

    .filter-btn:hover, .filter-btn.active {{
      background-color: var(--color-purple);
      color: var(--color-gold);
      border-color: var(--color-gold);
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
    }}

    .skills-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 16px;
    }}

    .skill-card {{
      background-color: var(--color-slate);
      border: 1px solid var(--color-border-gold);
      padding: 18px 14px;
      text-align: center;
      position: relative;
      cursor: default;
      transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease, background-color 0.25s ease;
    }}

    .skill-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 4px;
      border-top: 1px solid var(--color-gold);
      border-left: 1px solid var(--color-gold);
    }}
    .skill-card::after {{
      content: '';
      position: absolute;
      bottom: 0;
      right: 0;
      width: 4px;
      height: 4px;
      border-bottom: 1px solid var(--color-gold);
      border-right: 1px solid var(--color-gold);
    }}

    .skill-sigil {{
      font-size: 14px;
      color: var(--color-deep-orange);
      margin-bottom: 6px;
      display: block;
      transition: color 0.25s ease;
    }}

    .skill-name {{
      font-family: var(--font-display);
      font-size: 14px;
      letter-spacing: 0.08em;
      color: var(--color-text-gold);
      font-weight: 600;
      transition: color 0.25s ease;
    }}

    .skill-category-tag {{
      display: block;
      font-size: 11px;
      color: #8c8c9e;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-top: 4px;
    }}

    .skill-card:hover {{
      background-color: var(--color-purple);
      border-color: var(--color-gold);
      box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
      transform: translateY(-3px);
    }}

    .skill-card:hover .skill-sigil {{
      color: var(--color-gold);
    }}

    .skill-card:hover .skill-name {{
      color: #ffffff;
      text-shadow: 0 0 8px rgba(212, 175, 55, 0.7);
    }}

    /* ==========================================================================
       PROJECTS SECTION (RELICS & WORKS)
       ========================================================================== */
    .projects-section {{
      padding: 80px 0;
    }}

    .projects-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 30px;
    }}

    .project-card {{
      background-color: var(--color-slate);
      border: 1px solid var(--color-border-gold);
      padding: 30px;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.35s ease;
    }}

    .project-card::before {{
      content: '☩';
      position: absolute;
      top: 14px;
      right: 18px;
      font-size: 18px;
      color: var(--color-deep-orange);
      transition: color 0.3s ease, transform 0.3s ease;
    }}

    .project-card:hover {{
      background-color: var(--color-charcoal);
      border-color: var(--color-gold);
      box-shadow: 0 0 22px rgba(212, 175, 55, 0.35);
      transform: translateY(-5px);
    }}

    .project-card:hover::before {{
      color: var(--color-gold);
      transform: scale(1.2);
    }}

    .project-relic-num {{
      font-family: var(--font-display);
      font-size: 11px;
      letter-spacing: 0.25em;
      color: var(--color-gold);
      text-transform: uppercase;
      margin-bottom: 8px;
    }}

    .project-title {{
      font-size: 1.4rem;
      color: var(--color-gold);
      margin-bottom: 8px;
      letter-spacing: 0.06em;
      transition: color 0.3s ease;
    }}

    .project-card:hover .project-title {{
      color: #fff9e6;
      text-shadow: 0 0 10px rgba(212, 175, 55, 0.6);
    }}

    .project-subtitle {{
      font-size: 0.95rem;
      color: #c99363;
      font-style: italic;
      margin-bottom: 16px;
    }}

    .project-desc {{
      color: var(--color-text-dim);
      font-size: 1rem;
      line-height: 1.65;
      margin-bottom: 24px;
      flex-grow: 1;
    }}

    .project-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
    }}

    .project-tag {{
      background-color: var(--color-purple);
      border: 1px solid var(--color-border-subtle);
      color: var(--color-text-gold);
      font-size: 11px;
      font-family: var(--font-display);
      padding: 4px 10px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .project-actions {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--color-border-subtle);
      padding-top: 16px;
    }}

    .project-link-btn {{
      background: none;
      border: 1px solid var(--color-border-gold);
      color: var(--color-gold);
      font-family: var(--font-display);
      font-size: 12px;
      letter-spacing: 0.15em;
      padding: 7px 16px;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.25s ease;
    }}

    .project-link-btn:hover {{
      background-color: var(--color-purple);
      border-color: var(--color-gold);
      color: #ffffff;
      box-shadow: 0 0 12px rgba(212, 175, 55, 0.4);
    }}

    .project-runes {{
      font-size: 14px;
      color: var(--color-deep-orange);
      letter-spacing: 3px;
    }}

    /* ==========================================================================
       PHILOSOPHY / COGNITIVE GRIMOIRE BANNER
       ========================================================================== */
    .lore-banner {{
      margin: 60px 0;
      background-color: var(--color-purple);
      border: 1px solid var(--color-gold);
      padding: 36px 30px;
      text-align: center;
      position: relative;
    }}

    .lore-quote {{
      font-family: var(--font-display);
      font-size: 1.25rem;
      letter-spacing: 0.08em;
      color: #fff3d4;
      line-height: 1.8;
      max-width: 820px;
      margin: 0 auto;
    }}

    .lore-author {{
      margin-top: 14px;
      font-size: 0.95rem;
      color: var(--color-gold);
      letter-spacing: 0.2em;
      text-transform: uppercase;
    }}

    /* ==========================================================================
       CONTACT / SUMMONING SECTION
       ========================================================================== */
    .summon-section {{
      padding: 70px 0 90px;
    }}

    .summon-panel {{
      background-color: var(--color-charcoal);
      border: 1px solid var(--color-border-gold);
      padding: 40px;
      max-width: 800px;
      margin: 0 auto;
      position: relative;
    }}

    .summon-form {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .form-label {{
      font-family: var(--font-display);
      font-size: 12px;
      letter-spacing: 0.15em;
      color: var(--color-gold);
      text-transform: uppercase;
    }}

    .form-input, .form-textarea {{
      background-color: var(--color-slate);
      border: 1px solid var(--color-border-gold);
      color: var(--color-text-gold);
      font-family: var(--font-body);
      font-size: 16px;
      padding: 12px 16px;
      outline: none;
      transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }}

    .form-input:focus, .form-textarea:focus {{
      border-color: var(--color-gold);
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.4);
    }}

    .form-textarea {{
      resize: vertical;
      min-height: 120px;
    }}

    .summon-channels {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-top: 36px;
      flex-wrap: wrap;
    }}

    .channel-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      background-color: var(--color-slate);
      border: 1px solid var(--color-border-gold);
      color: var(--color-text-gold);
      text-decoration: none;
      font-family: var(--font-display);
      font-size: 12px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      transition: all 0.25s ease;
    }}

    .channel-link:hover {{
      background-color: var(--color-purple);
      border-color: var(--color-gold);
      color: #ffffff;
      box-shadow: 0 0 12px rgba(212, 175, 55, 0.4);
      transform: translateY(-2px);
    }}

    /* ==========================================================================
       MODAL FOR RELIC DETAILS
       ========================================================================== */
    .modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: rgba(10, 10, 20, 0.88);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .modal-backdrop.open {{
      display: flex;
    }}

    .modal-parchment {{
      background-color: var(--color-charcoal);
      border: 1px solid var(--color-gold);
      width: 100%;
      max-width: 680px;
      padding: 36px 32px;
      position: relative;
      box-shadow: 0 0 40px rgba(0,0,0,0.9), 0 0 20px rgba(212, 175, 55, 0.35);
      animation: modalFadeIn 0.3s ease-out;
    }}

    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .modal-close-btn {{
      position: absolute;
      top: 14px;
      right: 18px;
      background: none;
      border: none;
      color: var(--color-gold);
      font-size: 24px;
      cursor: pointer;
      line-height: 1;
    }}

    .modal-close-btn:hover {{
      color: #ffffff;
      text-shadow: 0 0 8px var(--color-gold);
    }}

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    .gothic-footer {{
      background-color: var(--color-charcoal);
      border-top: 1px solid var(--color-border-gold);
      padding: 40px 20px;
      text-align: center;
      position: relative;
      z-index: 10;
    }}

    .footer-seal {{
      color: var(--color-gold);
      font-size: 20px;
      margin-bottom: 12px;
      text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
    }}

    .footer-text {{
      color: var(--color-text-gold);
      font-family: var(--font-display);
      font-size: 14px;
      letter-spacing: 0.15em;
      margin-bottom: 6px;
    }}

    .footer-subtext {{
      font-size: 12px;
      color: var(--color-deep-orange);
      letter-spacing: 0.2em;
      text-transform: uppercase;
    }}

    /* ==========================================================================
       RESPONSIVENESS
       ========================================================================== */
    @media (max-width: 768px) {{
      .top-nav {{
        padding: 12px 18px;
      }}
      .nav-links {{
        display: none; /* simple sleek mobile setup */
      }}
      .hero-title {{
        letter-spacing: 0.08em;
      }}
      .skills-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .summon-panel {{
        padding: 24px 18px;
      }}
      .gothic-btn {{
        padding: 14px 24px;
        font-size: 13px;
      }}
    }}

    @media (max-width: 480px) {{
      .skills-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Enhanced Holy Diver Background Art (Dio 1983) -->
  <div class="bg-canvas-container">
    <div class="bg-image" id="bgArt" role="img" aria-label="Dark Fantasy Gothic Scene - Titan Over Stormy Ocean"></div>
  </div>
  <div class="bg-darkness-scrim"></div>
  <div class="bg-rocky-overlay"></div>
  <canvas id="emberCanvas"></canvas>

  <!-- Top Navigation -->
  <header class="top-nav">
    <a href="#" class="nav-brand">
      <div class="nav-brand-seal"><span>MS</span></div>
      <span>MUKUL SAINI</span>
    </a>
    
    <ul class="nav-links">
      <li><a href="#hero" class="nav-link">Codex</a></li>
      <li><a href="#skills" class="nav-link">Disciplines</a></li>
      <li><a href="#projects" class="nav-link">Relics</a></li>
      <li><a href="#summon" class="nav-link">Summon</a></li>
    </ul>

    <div class="nav-actions">
      <button class="ambient-btn" id="audioToggle" aria-label="Toggle Gothic Ambient Resonance">
        <span id="audioIcon">🕯️</span>
        <span id="audioLabel">Resonance</span>
      </button>
    </div>
  </header>

  <!-- Content Container -->
  <div class="wrapper">
    
    <!-- Hero Section -->
    <section id="hero" class="hero-section">
      <div class="hero-emblem">
        <div class="hero-emblem-outer"></div>
        <div class="hero-emblem-inner"></div>
        <div class="hero-emblem-icon">⚜</div>
      </div>

      <div class="hero-tagline">Arcane Machine Intelligence</div>
      <h1 class="hero-title">MUKUL SAINI</h1>
      <div class="hero-subtitle">JECRC College | BTech CSE-AI (IBM) | First Year Student</div>

      <div class="gothic-divider">
        <div class="gothic-divider-line"></div>
        <div class="gothic-divider-symbol">❖</div>
        <div class="gothic-divider-line"></div>
      </div>

      <p class="hero-bio">
        A novice weaver of arcane algorithms and deep neural sigils, venturing into the labyrinth of machine consciousness. Wandering between ancient mathematical foundations and modern cognitive architectures to conjure synthetic intelligence from raw entropy.
      </p>

      <a href="#skills" class="gothic-btn" id="summonHeroBtn">Summon Portfolio</a>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills-section">
      <div class="section-header">
        <div class="section-pretitle">The Spellbook of Capabilities</div>
        <h2 class="section-title">Arcane Disciplines & Skills</h2>
        <div class="gothic-divider">
          <div class="gothic-divider-line"></div>
          <div class="gothic-divider-symbol">⚔</div>
          <div class="gothic-divider-line"></div>
        </div>
        <p class="section-description">
          A codified inventory of computational incantations, mathematical rites, and machine learning architectures wielded in the pursuit of cognitive automation.
        </p>
      </div>

      <!-- Skill Category Filter -->
      <div class="skills-filter-container">
        <button class="filter-btn active" data-filter="all">All Invocations (27)</button>
        <button class="filter-btn" data-filter="neural">Neural & Deep Learning</button>
        <button class="filter-btn" data-filter="vision-nlp">Vision & NLP</button>
        <button class="filter-btn" data-filter="data-math">Data & Mathematics</button>
        <button class="filter-btn" data-filter="infra">Cloud & Infrastructure</button>
      </div>

      <!-- Grid of dark bordered skill boxes -->
      <div class="skills-grid" id="skillsGrid">
        <!-- Python -->
        <div class="skill-card" data-category="data-math">
          <span class="skill-sigil">✦</span>
          <div class="skill-name">Python</div>
          <span class="skill-category-tag">Core Tongue</span>
        </div>
        <!-- Machine Learning -->
        <div class="skill-card" data-category="neural">
          <span class="skill-sigil">❖</span>
          <div class="skill-name">Machine Learning</div>
          <span class="skill-category-tag">Algorithmic Rite</span>
        </div>
        <!-- Deep Learning -->
        <div class="skill-card" data-category="neural">
          <span class="skill-sigil">☩</span>
          <div class="skill-name">Deep Learning</div>
          <span class="skill-category-tag">Deep Arcana</span>
        </div>
        <!-- TensorFlow -->
        <div class="skill-card" data-category="neural">
          <span class="skill-sigil">⚜</span>
          <div class="skill-name">TensorFlow</div>
          <span class="skill-category-tag">Framework</span>
        </div>
        <!-- PyTorch -->
        <div class="skill-card" data-category="neural">
          <span class="skill-sigil">⚔</span>
          <div class="skill-name">PyTorch</div>
          <span class="skill-category-tag">Tensor Forge</span>
        </div>
        <!-- NLP -->
        <div class="skill-card" data-category="vision-nlp">
          <span class="skill-sigil">✦</span>
          <div class="skill-name">NLP</div>
          <span class="skill-category-tag">Text Divination</span>
        </div>
        <!-- Computer Vision -->
        <div class="skill-card" data-category="vision-nlp">
          <span class="skill-sigil">❖</span>
          <div class="skill-name">Computer Vision</div>
          <span class="skill-category-tag">Visual Perception</span>
        </div>
        <!-- Neural Networks -->
        <div class="skill-card" data-category="neural">
          <span class="skill-sigil">☩</span>
          <div class="skill-name">Neural Networks</div>
          <span class="skill-category-tag">Synaptic Weaving</span>
        </div>
        <!-- Data Analysis -->
        <div class="skill-card" data-category="data-math">
          <span class="skill-sigil">⚜</span>
          <div class="skill-name">Data Analysis</div>
          <span class="skill-category-tag">Empirical Scrying</span>
        </div>
        <!-- Scikit-learn -->
        <div class="skill-card" data-category="neural data-math">
          <span class="skill-sigil">⚔</span>
          <div class="skill-name">Scikit-learn</div>
          <span class="skill-category-tag">Classic Grimoire</span>
        </div>
        <!-- Pandas -->
        <div class="skill-card" data-category="data-math">
          <span class="skill-sigil">✦</span>
          <div class="skill-name">Pandas</div>
          <span class="skill-category-tag">Tabular Crucible</span>
        </div>
        <!-- NumPy -->
        <div class="skill-card" data-category="data-math">
          <span class="skill-sigil">❖</span>
          <div class="skill-name">NumPy</div>
          <span class="skill-category-tag">Vector Matrices</span>
        </div>
        <!-- Keras -->
        <div class="skill-card" data-category="neural">
          <span class="skill-sigil">☩</span>
          <div class="skill-name">Keras</div>
          <span class="skill-category-tag">Neural Architecture</span>
        </div>
        <!-- LLMs -->
        <div class="skill-card" data-category="vision-nlp">
          <span class="skill-sigil">⚜</span>
          <div class="skill-name">LLMs</div>
          <span class="skill-category-tag">Cognitive Oracles</span>
        </div>
        <!-- Prompt Engineering -->
        <div class="skill-card" data-category="vision-nlp">
          <span class="skill-sigil">⚔</span>
          <div class="skill-name">Prompt Engineering</div>
          <span class="skill-category-tag">Sigil Inscription</span>
        </div>
        <!-- Hugging Face -->
        <div class="skill-card" data-category="vision-nlp neural">
          <span class="skill-sigil">✦</span>
          <div class="skill-name">Hugging Face</div>
          <span class="skill-category-tag">Model Sanctum</span>
        </div>
        <!-- OpenCV -->
        <div class="skill-card" data-category="vision-nlp">
          <span class="skill-sigil">❖</span>
          <div class="skill-name">OpenCV</div>
          <span class="skill-category-tag">Optical Sensory</span>
        </div>
        <!-- Statistics -->
        <div class="skill-card" data-category="data-math">
          <span class="skill-sigil">☩</span>
          <div class="skill-name">Statistics</div>
          <span class="skill-category-tag">Stochastic Laws</span>
        </div>
        <!-- Linear Algebra -->
        <div class="skill-card" data-category="data-math">
          <span class="skill-sigil">⚜</span>
          <div class="skill-name">Linear Algebra</div>
          <span class="skill-category-tag">Dimensional Geometry</span>
        </div>
        <!-- SQL -->
        <div class="skill-card" data-category="data-math infra">
          <span class="skill-sigil">⚔</span>
          <div class="skill-name">SQL</div>
          <span class="skill-category-tag">Vault Querying</span>
        </div>
        <!-- AWS -->
        <div class="skill-card" data-category="infra">
          <span class="skill-sigil">✦</span>
          <div class="skill-name">AWS</div>
          <span class="skill-category-tag">Celestial Cloud</span>
        </div>
        <!-- GCP -->
        <div class="skill-card" data-category="infra">
          <span class="skill-sigil">❖</span>
          <div class="skill-name">GCP</div>
          <span class="skill-category-tag">Aether Infrastructure</span>
        </div>
        <!-- Docker -->
        <div class="skill-card" data-category="infra">
          <span class="skill-sigil">☩</span>
          <div class="skill-name">Docker</div>
          <span class="skill-category-tag">Rune Containment</span>
        </div>
        <!-- Git -->
        <div class="skill-card" data-category="infra">
          <span class="skill-sigil">⚜</span>
          <div class="skill-name">Git</div>
          <span class="skill-category-tag">Chronicle Versioning</span>
        </div>
        <!-- APIs -->
        <div class="skill-card" data-category="infra">
          <span class="skill-sigil">⚔</span>
          <div class="skill-name">APIs</div>
          <span class="skill-category-tag">Planar Portals</span>
        </div>
        <!-- Reinforcement Learning -->
        <div class="skill-card" data-category="neural">
          <span class="skill-sigil">✦</span>
          <div class="skill-name">Reinforcement Learning</div>
          <span class="skill-category-tag">Trial by Fire</span>
        </div>
        <!-- Flask -->
        <div class="skill-card" data-category="infra">
          <span class="skill-sigil">❖</span>
          <div class="skill-name">Flask</div>
          <span class="skill-category-tag">Apothecary Serving</span>
        </div>
      </div>
    </section>

    <!-- Philosophy Banner -->
    <div class="lore-banner">
      <p class="lore-quote">
        "He who seeks wisdom in the silicon depths must fear neither the dark matrices nor the infinite gradients. For in the heart of the void, every neuron awaits illumination."
      </p>
      <div class="lore-author">— Grimoire of Synthetic Mind, Verse I</div>
    </div>

    <!-- Projects Section -->
    <section id="projects" class="projects-section">
      <div class="section-header">
        <div class="section-pretitle">Consecrated Creations</div>
        <h2 class="section-title">Enchanted Relics & Projects</h2>
        <div class="gothic-divider">
          <div class="gothic-divider-line"></div>
          <div class="gothic-divider-symbol">⚜</div>
          <div class="gothic-divider-line"></div>
        </div>
        <p class="section-description">
          Engineered computational artifacts forged with deep neural weights, mathematical precision, and scalable server backends.
        </p>
      </div>

      <div class="projects-grid">
        <!-- Project 1 -->
        <div class="project-card" data-project="latent-visions">
          <div>
            <div class="project-relic-num">Relic I · Computer Vision</div>
            <h3 class="project-title">Grimoire of Latent Visions</h3>
            <div class="project-subtitle">Neural Generative Synthesis & Latent Walk Engine</div>
            <p class="project-desc">
              An unsupervised deep convolutional autoencoder and latent-space explorer trained on gothic iconography and structural forms. Synthesizes unseen visual permutations through smooth Riemannian manifold trajectories.
            </p>
            <div class="project-tags">
              <span class="project-tag">PyTorch</span>
              <span class="project-tag">Computer Vision</span>
              <span class="project-tag">Autoencoders</span>
              <span class="project-tag">Flask</span>
            </div>
          </div>
          <div class="project-actions">
            <button class="project-link-btn" onclick="openRelicModal('latent-visions')">
              <span>Examine Relic</span> →
            </button>
            <span class="project-runes">ᚠ ᚢ ᚦ</span>
          </div>
        </div>

        <!-- Project 2 -->
        <div class="project-card" data-project="arcane-lexicon">
          <div>
            <div class="project-relic-num">Relic II · Natural Language</div>
            <h3 class="project-title">Arcane Lexicon NLP</h3>
            <div class="project-subtitle">Contextual Transformer & Semantic Reasoning Oracle</div>
            <p class="project-desc">
              A specialized semantic query system integrating Hugging Face Transformers and prompt chains to synthesize, summarize, and cross-examine dense academic machine learning literature with source-grounded references.
            </p>
            <div class="project-tags">
              <span class="project-tag">Hugging Face</span>
              <span class="project-tag">LLMs</span>
              <span class="project-tag">Prompt Eng</span>
              <span class="project-tag">Python</span>
            </div>
          </div>
          <div class="project-actions">
            <button class="project-link-btn" onclick="openRelicModal('arcane-lexicon')">
              <span>Examine Relic</span> →
            </button>
            <span class="project-runes">ᚨ ᚱ ᚲ</span>
          </div>
        </div>

        <!-- Project 3 -->
        <div class="project-card" data-project="aegis-sentry">
          <div>
            <div class="project-relic-num">Relic III · Edge Vision</div>
            <h3 class="project-title">The Aegis Neural Sentry</h3>
            <div class="project-subtitle">Autonomous Real-Time Anomaly & Object Detection</div>
            <p class="project-desc">
              Low-latency edge perception system utilizing OpenCV filters and lightweight neural backbones to identify spatial intrusions, geometric anomalies, and real-time tracking across continuous video streams.
            </p>
            <div class="project-tags">
              <span class="project-tag">OpenCV</span>
              <span class="project-tag">Deep Learning</span>
              <span class="project-tag">Docker</span>
              <span class="project-tag">APIs</span>
            </div>
          </div>
          <div class="project-actions">
            <button class="project-link-btn" onclick="openRelicModal('aegis-sentry')">
              <span>Examine Relic</span> →
            </button>
            <span class="project-runes">ᛋ ᛖ ᚾ</span>
          </div>
        </div>

        <!-- Project 4 -->
        <div class="project-card" data-project="alchemical-crucible">
          <div>
            <div class="project-relic-num">Relic IV · Predictive Modeling</div>
            <h3 class="project-title">Alchemical Data Crucible</h3>
            <div class="project-subtitle">Multivariate Stochastic Forecaster & Statistical Engine</div>
            <p class="project-desc">
              End-to-end data analysis pipeline distilling complex high-dimensional datasets into predictive insight distributions using Scikit-Learn regressors, cross-validation kernels, and automated feature engineering.
            </p>
            <div class="project-tags">
              <span class="project-tag">Scikit-learn</span>
              <span class="project-tag">Pandas</span>
              <span class="project-tag">NumPy</span>
              <span class="project-tag">Statistics</span>
            </div>
          </div>
          <div class="project-actions">
            <button class="project-link-btn" onclick="openRelicModal('alchemical-crucible')">
              <span>Examine Relic</span> →
            </button>
            <span class="project-runes">ᛞ ᚨ ᛏ</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Summoning / Contact Section -->
    <section id="summon" class="summon-section">
      <div class="section-header">
        <div class="section-pretitle">Commune with the Enchanter</div>
        <h2 class="section-title">The Summoning Circle</h2>
        <div class="gothic-divider">
          <div class="gothic-divider-line"></div>
          <div class="gothic-divider-symbol">🕯️</div>
          <div class="gothic-divider-line"></div>
        </div>
        <p class="section-description">
          Whether seeking collaborative artificial intelligence research, algorithmic consultation, or apprentice rites, dispatch your missive into the ether.
        </p>
      </div>

      <div class="summon-panel">
        <form class="summon-form" id="summonForm" onsubmit="handleSummon(event)">
          <div class="form-group">
            <label class="form-label" for="seekerName">Seeker's Name / Title</label>
            <input type="text" id="seekerName" class="form-input" placeholder="e.g., Lord Alden or AI Scholar" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="seekerEmail">Ether Address (Email)</label>
            <input type="email" id="seekerEmail" class="form-input" placeholder="e.g., seeker@citadel.edu" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="seekerMessage">Inscribe Your Message</label>
            <textarea id="seekerMessage" class="form-textarea" placeholder="Speak of your quest, dataset, or alliance proposal..." required></textarea>
          </div>

          <button type="submit" class="gothic-btn" id="dispatchBtn">
            Dispatch Raven (Send Message)
          </button>
          
          <div id="summonConfirmation" style="display:none; text-align:center; color:#e8d4a8; font-family:var(--font-display); margin-top:14px; font-size:14px; letter-spacing:0.1em; border: 1px solid var(--color-gold); padding: 12px; background-color: var(--color-purple);">
            ✦ Missive Transmitted across the Ether. The Enchanter shall heed your call.
          </div>
        </form>

        <div class="gothic-divider" style="margin: 32px auto 20px;">
          <div class="gothic-divider-line"></div>
          <div class="gothic-divider-symbol">❖</div>
          <div class="gothic-divider-line"></div>
        </div>

        <div class="summon-channels">
          <a href="mailto:mukulsaini@jecrc.ac.in" class="channel-link" title="Direct Electronic Mail">
            <span>✉</span> Email Raven
          </a>
          <a href="https://github.com" target="_blank" rel="noopener" class="channel-link" title="GitHub Codex">
            <span>⚔</span> GitHub Repository
          </a>
          <a href="https://linkedin.com" target="_blank" rel="noopener" class="channel-link" title="Guild Network">
            <span>⚜</span> LinkedIn Realm
          </a>
          <a href="https://kaggle.com" target="_blank" rel="noopener" class="channel-link" title="Kaggle Arenas">
            <span>☩</span> Kaggle Grimoire
          </a>
        </div>
      </div>
    </section>

  </div>

  <!-- Relic Detail Modal -->
  <div class="modal-backdrop" id="relicModal" onclick="handleBackdropClick(event)">
    <div class="modal-parchment gothic-box">
      <button class="modal-close-btn" onclick="closeRelicModal()">&times;</button>
      <div id="modalContent">
        <!-- Injected dynamically by JS -->
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="gothic-footer">
    <div class="footer-seal">⚜</div>
    <div class="footer-text">© 2025 Mukul Saini | AI Enchanter</div>
    <div class="footer-subtext">JECRC College · BTech CSE-AI (IBM) · First Year Student</div>
    <div style="margin-top: 14px; font-size: 11px; color: #7f7f94; letter-spacing: 0.15em;">
      IN UMBRA ALGORITHMI, LUX INTELLIGENTIAE
    </div>
  </footer>

  <!-- ==========================================================================
       VANILLA JAVASCRIPT LOGIC
       ========================================================================== -->
  <script>
    // --------------------------------------------------------------------------
    // 1. Interactive Ambient Audio Synthesizer (Web Audio API)
    // Produces a low atmospheric gothic drone with warm harmonic resonance
    // --------------------------------------------------------------------------
    let audioCtx = null;
    let isPlayingAudio = false;
    let droneGain = null;
    let osc1 = null, osc2 = null, filter = null;

    function toggleGothicAudio() {{
      const btn = document.getElementById('audioToggle');
      const label = document.getElementById('audioLabel');
      const icon = document.getElementById('audioIcon');

      if (!audioCtx) {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }}

      if (audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}

      if (!isPlayingAudio) {{
        // Start atmospheric harmonic drone (reminiscent of ancient cathedral / dungeon wind)
        droneGain = audioCtx.createGain();
        droneGain.gain.setValueAtTime(0.001, audioCtx.currentTime);
        droneGain.gain.exponentialRampToValueAtTime(0.07, audioCtx.currentTime + 3);

        filter = audioCtx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(280, audioCtx.currentTime);

        // Fundamental deep note (55Hz - A1) & mystic fifth (82.4Hz - E2)
        osc1 = audioCtx.createOscillator();
        osc1.type = 'sawtooth';
        osc1.frequency.setValueAtTime(55, audioCtx.currentTime);

        osc2 = audioCtx.createOscillator();
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(82.41, audioCtx.currentTime);

        osc1.connect(filter);
        osc2.connect(filter);
        filter.connect(droneGain);
        droneGain.connect(audioCtx.destination);

        osc1.start();
        osc2.start();

        isPlayingAudio = true;
        btn.classList.add('active');
        label.textContent = 'Chant Active';
        icon.textContent = '🔥';
      }} else {{
        if (droneGain) {{
          droneGain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 1.2);
          setTimeout(() => {{
            if (osc1) osc1.stop();
            if (osc2) osc2.stop();
            osc1 = null;
            osc2 = null;
          }}, 1200);
        }}
        isPlayingAudio = false;
        btn.classList.remove('active');
        label.textContent = 'Resonance';
        icon.textContent = '🕯️';
      }}
    }}

    document.getElementById('audioToggle').addEventListener('click', toggleGothicAudio);

    // --------------------------------------------------------------------------
    // 2. Rising Mystical Ember Particle System
    // Simulates embers floating up from the stormy oceanic abyss & sunset horizon
    // --------------------------------------------------------------------------
    const canvas = document.getElementById('emberCanvas');
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {{
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }});

    const embers = [];
    const EMBER_COUNT = 45;

    class Ember {{
      constructor() {{
        this.reset(true);
      }}

      reset(initial = false) {{
        this.x = Math.random() * width;
        this.y = initial ? Math.random() * height : height + 10;
        this.size = Math.random() * 2.2 + 0.8;
        this.speedY = Math.random() * 0.8 + 0.35;
        this.speedX = (Math.random() - 0.48) * 0.5;
        this.opacity = Math.random() * 0.6 + 0.2;
        this.decay = Math.random() * 0.003 + 0.001;
        // Ember palette: gold (#d4af37), amber (#e8972c), deep orange (#8b4513)
        const colors = ['212, 175, 55', '232, 151, 44', '139, 69, 19'];
        this.color = colors[Math.floor(Math.random() * colors.length)];
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
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${{this.color}}, ${{this.opacity}})`;
        ctx.shadowBlur = 8;
        ctx.shadowColor = `rgba(${{this.color}}, 0.8)`;
        ctx.fill();
        ctx.shadowBlur = 0;
      }}
    }}

    for (let i = 0; i < EMBER_COUNT; i++) {{
      embers.push(new Ember());
    }}

    function animateEmbers() {{
      ctx.clearRect(0, 0, width, height);
      for (let i = 0; i < embers.length; i++) {{
        embers[i].update();
        embers[i].draw();
      }}
      requestAnimationFrame(animateEmbers);
    }}
    animateEmbers();

    // --------------------------------------------------------------------------
    // 3. Subtle Parallax Effect on Background
    // --------------------------------------------------------------------------
    const bgArt = document.getElementById('bgArt');
    window.addEventListener('scroll', () => {{
      const scrollY = window.pageYOffset;
      bgArt.style.transform = `scale(1.02) translateY(${{scrollY * 0.08}}px)`;
    }}, {{ passive: true }});

    // --------------------------------------------------------------------------
    // 4. Skills Category Filter
    // --------------------------------------------------------------------------
    const filterButtons = document.querySelectorAll('.filter-btn');
    const skillCards = document.querySelectorAll('.skill-card');

    filterButtons.forEach(btn => {{
      btn.addEventListener('click', () => {{
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');

        skillCards.forEach(card => {{
          const categories = card.getAttribute('data-category') || '';
          if (filter === 'all' || categories.includes(filter)) {{
            card.style.display = 'block';
            card.style.opacity = '1';
          }} else {{
            card.style.display = 'none';
            card.style.opacity = '0';
          }}
        }});
      }});
    }});

    // --------------------------------------------------------------------------
    // 5. Relic Modal Data & Handler
    // --------------------------------------------------------------------------
    const relicDetails = {{
      'latent-visions': {{
        title: 'Grimoire of Latent Visions',
        subtitle: 'Generative Latent Manifold Explorer',
        tags: 'PyTorch · Computer Vision · Autoencoders · Flask',
        runes: 'ᚠ ᚢ ᚦ · CONVOLUTIONAL SYNTHESIS',
        summary: 'A deep generative computer vision project examining visual feature representation across compressed latent latent dimensions. Built with PyTorch and served with a responsive Flask backend interface.',
        features: [
          'Unsupervised feature distillation through symmetric encoder-decoder networks',
          'Smooth mathematical interpolation between diametrically opposed aesthetic representations',
          'Custom loss formulation balancing reconstruction fidelity with structural perceptual loss',
          'Interactive exploration portal allowing real-time parameter tweaking'
        ]
      }},
      'arcane-lexicon': {{
        title: 'Arcane Lexicon NLP',
        subtitle: 'Semantic Reasoning & Knowledge Retrieval',
        tags: 'Hugging Face · LLMs · Prompt Engineering · Python',
        runes: 'ᚨ ᚱ ᚲ · ATTENTION MECHANISMS',
        summary: 'A contextual information synthesis pipeline tailored for complex research documents. Utilizes transformer embeddings and vector similarity to extract nuanced answers from extensive corpora.',
        features: [
          'Dual encoder dense retrieval combining semantic search with lexical token matching',
          'Prompt decomposition strategies reducing hallucinations and enforcing citation rigor',
          'Integrated tokenizer pipeline benchmarking diverse open-source model weights',
          'Lightweight REST endpoint for seamless client dispatching'
        ]
      }},
      'aegis-sentry': {{
        title: 'The Aegis Neural Sentry',
        subtitle: 'Autonomous Real-Time Video Anomaly Engine',
        tags: 'OpenCV · Deep Learning · Docker · REST APIs',
        runes: 'ᛋ ᛖ ᚾ · PERCEPTUAL SURVEILLANCE',
        summary: 'A high-throughput computer vision sentry detecting anomalous spatial movements, perimeter breaches, and kinematic deviations in real-time camera streams.',
        features: [
          'Optimized frame extraction with OpenCV image preprocessing pipeline',
          'Spatial-temporal heuristic filtering suppressing environmental noise and light shifts',
          'Containerized deployment via Docker for rapid provisioning on edge accelerators',
          'Automated webhook dispatcher alerting remote operators upon confirmed anomaly'
        ]
      }},
      'alchemical-crucible': {{
        title: 'Alchemical Data Crucible',
        subtitle: 'Multivariate Stochastic Forecaster',
        tags: 'Scikit-learn · Pandas · NumPy · Statistics',
        runes: 'ᛞ ᚨ ᛏ · STOCHASTIC CALIBRATION',
        summary: 'An end-to-end data analytics and predictive modeling suite transforming raw noisy features into clear probability estimates and trend forecasts.',
        features: [
          'Robust outlier identification and imputation techniques preserved across tabular splits',
          'Hyperparameter grid searching paired with stratified k-fold cross validation',
          'Feature importance attribution maps exposing predictive model drivers',
          'Comprehensive metric reporting across RMSE, ROC-AUC, and F1 confidence intervals'
        ]
      }}
    }};

    function openRelicModal(relicKey) {{
      const data = relicDetails[relicKey];
      if (!data) return;

      const modalContent = document.getElementById('modalContent');
      modalContent.innerHTML = `
        <div style="color: var(--color-deep-orange); font-family: var(--font-display); font-size: 11px; letter-spacing: 0.25em; margin-bottom: 8px;">
          ${{data.runes}}
        </div>
        <h2 style="font-size: 1.8rem; color: var(--color-gold); margin-bottom: 6px; letter-spacing: 0.08em;">
          ${{data.title}}
        </h2>
        <div style="font-size: 1rem; color: #c99363; font-style: italic; margin-bottom: 14px;">
          ${{data.subtitle}}
        </div>
        <div style="display:inline-block; font-family:var(--font-display); font-size:11px; color:var(--color-text-gold); background-color:var(--color-purple); padding:4px 12px; border:1px solid var(--color-border-gold); margin-bottom: 20px; letter-spacing:0.1em;">
          ${{data.tags}}
        </div>
        <p style="color: var(--color-text-gold); font-size: 1.05rem; line-height: 1.7; margin-bottom: 20px;">
          ${{data.summary}}
        </p>
        <div style="border-top: 1px solid var(--color-border-gold); padding-top: 16px; margin-bottom: 22px;">
          <div style="font-family:var(--font-display); font-size:12px; color:var(--color-gold); letter-spacing:0.15em; text-transform:uppercase; margin-bottom:10px;">
            Archival Rites & Capabilities:
          </div>
          <ul style="list-style:none; padding-left:0; color:var(--color-text-dim); font-size:0.95rem; line-height:1.8;">
            ${{data.features.map(f => `<li style="display:flex; align-items:flex-start; gap:10px;"><span style="color:var(--color-gold);">✦</span> <span>${{f}}</span></li>`).join('')}}
          </ul>
        </div>
        <div style="display: flex; gap: 14px; justify-content: flex-end;">
          <button class="gothic-btn" style="padding: 10px 22px; font-size: 12px;" onclick="closeRelicModal()">Close Tome</button>
        </div>
      `;

      document.getElementById('relicModal').classList.add('open');
    }}

    function closeRelicModal() {{
      document.getElementById('relicModal').classList.remove('open');
    }}

    function handleBackdropClick(e) {{
      if (e.target.id === 'relicModal') {{
        closeRelicModal();
      }}
    }}

    // --------------------------------------------------------------------------
    // 6. Missive Dispatch (Contact Form Simulation)
    // --------------------------------------------------------------------------
    function handleSummon(event) {{
      event.preventDefault();
      const btn = document.getElementById('dispatchBtn');
      const confirmation = document.getElementById('summonConfirmation');

      btn.disabled = true;
      btn.textContent = 'Transmitting Missive...';

      setTimeout(() => {{
        confirmation.style.display = 'block';
        btn.textContent = 'Missive Consecrated ❖';
        document.getElementById('summonForm').reset();

        setTimeout(() => {{
          btn.disabled = false;
          btn.textContent = 'Dispatch Raven (Send Message)';
        }}, 4000);
      }}, 700);
    }}
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("index.html created successfully. File size:", os.path.getsize('index.html'), "bytes")

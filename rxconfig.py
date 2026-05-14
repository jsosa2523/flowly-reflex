<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flowly — Gestiona tu equipo sin fricciones</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,400&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #0a0a0f;
    --bg2: #111118;
    --bg3: #16161f;
    --border: rgba(255,255,255,0.07);
    --border2: rgba(255,255,255,0.12);
    --text: #f0f0f8;
    --text2: rgba(240,240,248,0.55);
    --text3: rgba(240,240,248,0.3);
    --violet: #7c6ff7;
    --violet-light: #a89ef9;
    --violet-dark: #5a52d5;
    --violet-bg: rgba(124,111,247,0.1);
    --violet-bg2: rgba(124,111,247,0.18);
    --green: #4ade80;
    --green-bg: rgba(74,222,128,0.1);
    --amber: #fbbf24;
    --teal: #2dd4bf;
    --font-display: 'Syne', sans-serif;
    --font-body: 'DM Sans', sans-serif;
    --r-sm: 8px;
    --r-md: 12px;
    --r-lg: 18px;
    --r-xl: 24px;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-body);
    font-size: 16px;
    line-height: 1.6;
    overflow-x: hidden;
  }

  /* ─── NOISE TEXTURE OVERLAY ─── */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none; z-index: 0;
  }

  /* ─── GLOW ORBS ─── */
  .orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(120px);
    pointer-events: none;
    z-index: 0;
  }
  .orb-1 { width: 600px; height: 600px; background: rgba(124,111,247,0.12); top: -200px; right: -100px; }
  .orb-2 { width: 400px; height: 400px; background: rgba(45,212,191,0.06); bottom: 200px; left: -100px; }

  /* ─── NAVBAR ─── */
  nav {
    position: sticky; top: 0; z-index: 100;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 2.5rem;
    height: 64px;
    border-bottom: 1px solid var(--border);
    background: rgba(10,10,15,0.8);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
  }

  .nav-logo {
    font-family: var(--font-display);
    font-weight: 800;
    font-size: 20px;
    letter-spacing: -0.5px;
    color: var(--text);
    display: flex; align-items: center; gap: 8px;
    text-decoration: none;
  }

  .nav-logo-dot {
    width: 8px; height: 8px;
    background: var(--violet);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--violet);
    animation: pulse 2s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(0.85); }
  }

  .nav-links {
    display: flex; gap: 2rem; list-style: none;
  }

  .nav-links a {
    color: var(--text2);
    text-decoration: none;
    font-size: 14px;
    font-weight: 400;
    transition: color 0.2s;
  }
  .nav-links a:hover { color: var(--text); }

  .nav-actions { display: flex; align-items: center; gap: 10px; }

  .btn-ghost {
    background: transparent;
    border: 1px solid var(--border2);
    color: var(--text2);
    font-family: var(--font-body);
    font-size: 14px;
    padding: 8px 16px;
    border-radius: var(--r-sm);
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn-ghost:hover { color: var(--text); border-color: var(--border2); background: rgba(255,255,255,0.04); }

  .btn-primary {
    background: var(--violet);
    border: none;
    color: #fff;
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 500;
    padding: 9px 18px;
    border-radius: var(--r-sm);
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: 0 0 20px rgba(124,111,247,0.3);
  }
  .btn-primary:hover { background: var(--violet-light); transform: translateY(-1px); box-shadow: 0 4px 24px rgba(124,111,247,0.45); }

  .btn-primary-lg {
    background: var(--violet);
    border: none;
    color: #fff;
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 500;
    padding: 14px 28px;
    border-radius: var(--r-md);
    cursor: pointer;
    transition: all 0.25s;
    box-shadow: 0 0 30px rgba(124,111,247,0.35);
    display: inline-flex; align-items: center; gap: 8px;
  }
  .btn-primary-lg:hover { background: var(--violet-light); transform: translateY(-2px); box-shadow: 0 8px 32px rgba(124,111,247,0.5); }

  .btn-outline-lg {
    background: transparent;
    border: 1px solid var(--border2);
    color: var(--text2);
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    padding: 14px 28px;
    border-radius: var(--r-md);
    cursor: pointer;
    transition: all 0.2s;
    display: inline-flex; align-items: center; gap: 8px;
  }
  .btn-outline-lg:hover { color: var(--text); border-color: rgba(255,255,255,0.25); background: rgba(255,255,255,0.04); }

  /* ─── SECTIONS ─── */
  section { position: relative; z-index: 1; }

  .container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 2rem;
  }

  /* ─── HERO ─── */
  .hero {
    padding: 6rem 2rem 5rem;
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: var(--violet-bg);
    border: 1px solid rgba(124,111,247,0.3);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 12px;
    font-weight: 500;
    color: var(--violet-light);
    margin-bottom: 1.5rem;
    animation: fadeUp 0.6s ease both;
  }

  .hero-badge .dot {
    width: 6px; height: 6px;
    background: var(--green);
    border-radius: 50%;
    box-shadow: 0 0 6px var(--green);
    animation: pulse 2s ease-in-out infinite;
  }

  .hero h1 {
    font-family: var(--font-display);
    font-size: clamp(36px, 5vw, 58px);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -2px;
    margin-bottom: 1.25rem;
    animation: fadeUp 0.6s 0.1s ease both;
  }

  .hero h1 .accent {
    background: linear-gradient(135deg, var(--violet-light), var(--teal));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-sub {
    font-size: 17px;
    color: var(--text2);
    line-height: 1.7;
    margin-bottom: 2rem;
    max-width: 460px;
    animation: fadeUp 0.6s 0.2s ease both;
  }

  .hero-actions {
    display: flex; gap: 12px; flex-wrap: wrap;
    margin-bottom: 2.5rem;
    animation: fadeUp 0.6s 0.3s ease both;
  }

  .hero-social-proof {
    display: flex; align-items: center; gap: 12px;
    animation: fadeUp 0.6s 0.4s ease both;
  }

  .avatars {
    display: flex;
  }

  .avatar {
    width: 30px; height: 30px;
    border-radius: 50%;
    border: 2px solid var(--bg);
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; font-weight: 600;
    margin-left: -8px;
    flex-shrink: 0;
  }
  .avatar:first-child { margin-left: 0; }
  .av1 { background: linear-gradient(135deg, #7c6ff7, #5a52d5); color: #fff; }
  .av2 { background: linear-gradient(135deg, #2dd4bf, #0d9488); color: #fff; }
  .av3 { background: linear-gradient(135deg, #f59e0b, #d97706); color: #fff; }
  .av4 { background: linear-gradient(135deg, #ec4899, #be185d); color: #fff; }

  .social-text { font-size: 13px; color: var(--text2); }
  .social-text strong { color: var(--text); font-weight: 500; }

  /* ─── DASHBOARD MOCKUP ─── */
  .dashboard-mockup {
    background: var(--bg2);
    border: 1px solid var(--border2);
    border-radius: var(--r-xl);
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 12px;
    position: relative;
    animation: fadeUp 0.6s 0.2s ease both;
    box-shadow: 0 32px 64px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
  }

  .dashboard-mockup::before {
    content: '';
    position: absolute;
    top: -1px; left: 10%; right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,111,247,0.6), transparent);
  }

  .mock-topbar {
    display: flex; align-items: center; justify-content: space-between;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
  }

  .mock-dots { display: flex; gap: 6px; }
  .mock-dot { width: 10px; height: 10px; border-radius: 50%; }
  .md-r { background: #ff5f56; }
  .md-y { background: #febc2e; }
  .md-g { background: #27c840; }

  .mock-tabs { display: flex; gap: 4px; }
  .mock-tab {
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 6px;
    color: var(--text3);
    cursor: pointer;
  }
  .mock-tab.active { background: var(--violet-bg); color: var(--violet-light); }

  .mock-sprint-card {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: var(--r-md);
    padding: 14px;
  }

  .mock-sprint-header {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 10px;
  }

  .mock-sprint-title { font-size: 13px; font-weight: 500; }
  .mock-sprint-badge {
    font-size: 10px;
    background: var(--green-bg);
    color: var(--green);
    border: 1px solid rgba(74,222,128,0.2);
    padding: 2px 8px;
    border-radius: 12px;
  }

  .mock-progress-label {
    display: flex; justify-content: space-between;
    font-size: 11px; color: var(--text3);
    margin-bottom: 6px;
  }

  .mock-progress-bar {
    height: 6px;
    background: rgba(255,255,255,0.06);
    border-radius: 3px;
    overflow: hidden;
    margin-bottom: 12px;
  }

  .mock-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--violet), var(--violet-light));
    border-radius: 3px;
    width: 72%;
    position: relative;
  }

  .mock-progress-fill::after {
    content: '';
    position: absolute; right: 0; top: 50%;
    transform: translateY(-50%);
    width: 10px; height: 10px;
    background: var(--violet-light);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--violet);
  }

  .mock-members { display: flex; gap: 6px; align-items: center; }
  .mock-member-chip {
    display: flex; align-items: center; gap: 5px;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 3px 8px;
    font-size: 10px;
    color: var(--text2);
  }
  .mock-member-dot { width: 5px; height: 5px; border-radius: 50%; }

  .mock-stats-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 8px;
  }

  .mock-stat {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: var(--r-sm);
    padding: 10px 12px;
    text-align: center;
  }

  .mock-stat-num {
    font-family: var(--font-display);
    font-size: 20px;
    font-weight: 800;
    color: var(--violet-light);
    display: block;
  }

  .mock-stat-lbl {
    font-size: 10px;
    color: var(--text3);
    display: block;
    margin-top: 2px;
  }

  .mock-notif {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: var(--r-sm);
    padding: 10px 12px;
    display: flex; align-items: center; gap: 8px;
    font-size: 12px; color: var(--text2);
  }

  .mock-notif-icon {
    width: 22px; height: 22px;
    background: var(--green-bg);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px;
    color: var(--green);
    flex-shrink: 0;
  }

  /* ─── ANIMATIONS ─── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  /* ─── LOGOS STRIP ─── */
  .logos-strip {
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    padding: 1.5rem 0;
    overflow: hidden;
    position: relative; z-index: 1;
  }

  .logos-strip p {
    text-align: center;
    font-size: 12px;
    color: var(--text3);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 1.25rem;
  }

  .logos-track {
    display: flex; gap: 3rem; align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }

  .logo-item {
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 15px;
    color: var(--text3);
    letter-spacing: -0.5px;
    white-space: nowrap;
    transition: color 0.2s;
  }
  .logo-item:hover { color: var(--text2); }

  /* ─── FEATURES ─── */
  .features-section {
    padding: 5rem 0;
  }

  .section-label {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--violet-light);
    margin-bottom: 0.75rem;
  }

  .section-title {
    font-family: var(--font-display);
    font-size: clamp(26px, 4vw, 40px);
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.1;
    margin-bottom: 0.75rem;
  }

  .section-sub {
    font-size: 16px;
    color: var(--text2);
    max-width: 520px;
    line-height: 1.7;
    margin-bottom: 3rem;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }

  .feat-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: var(--r-lg);
    padding: 1.5rem;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
  }

  .feat-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(124,111,247,0.05), transparent);
    opacity: 0;
    transition: opacity 0.25s;
  }

  .feat-card:hover {
    border-color: rgba(124,111,247,0.3);
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.3);
  }

  .feat-card:hover::before { opacity: 1; }

  .feat-icon-wrap {
    width: 44px; height: 44px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    margin-bottom: 1rem;
  }

  .feat-card h3 {
    font-size: 15px;
    font-weight: 500;
    margin-bottom: 0.5rem;
  }

  .feat-card p {
    font-size: 13px;
    color: var(--text2);
    line-height: 1.65;
  }

  /* ─── PRICING ─── */
  .pricing-section {
    padding: 5rem 0;
    background: var(--bg2);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
  }

  .pricing-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    align-items: start;
  }

  .pricing-card {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: var(--r-xl);
    padding: 1.75rem;
    position: relative;
    transition: all 0.25s;
  }

  .pricing-card:hover { transform: translateY(-3px); box-shadow: 0 16px 48px rgba(0,0,0,0.35); }

  .pricing-card.featured {
    background: var(--bg2);
    border-color: var(--violet);
    box-shadow: 0 0 0 1px rgba(124,111,247,0.4), 0 20px 60px rgba(124,111,247,0.15);
  }

  .plan-badge {
    display: inline-block;
    font-size: 11px; font-weight: 500;
    background: var(--violet-bg2);
    color: var(--violet-light);
    border: 1px solid rgba(124,111,247,0.3);
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 1rem;
  }

  .plan-name {
    font-family: var(--font-display);
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 0.5rem;
  }

  .plan-price {
    font-family: var(--font-display);
    font-size: 40px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 4px;
    color: var(--text);
  }

  .featured .plan-price { color: var(--violet-light); }

  .plan-period { font-size: 13px; color: var(--text3); margin-bottom: 1rem; }

  .plan-desc { font-size: 13px; color: var(--text2); line-height: 1.6; margin-bottom: 1.25rem; }

  .plan-divider { height: 1px; background: var(--border); margin-bottom: 1.25rem; }

  .plan-features { list-style: none; display: flex; flex-direction: column; gap: 8px; margin-bottom: 1.5rem; }

  .plan-features li {
    display: flex; align-items: flex-start; gap: 8px;
    font-size: 13px; color: var(--text2);
  }

  .plan-features li .check {
    color: var(--green);
    font-size: 13px;
    margin-top: 1px;
    flex-shrink: 0;
  }

  .plan-cta {
    width: 100%;
    padding: 12px;
    border-radius: var(--r-sm);
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    border: 1px solid var(--border2);
    background: transparent;
    color: var(--text2);
  }
  .plan-cta:hover { color: var(--text); border-color: rgba(255,255,255,0.2); background: rgba(255,255,255,0.04); }

  .featured .plan-cta {
    background: var(--violet);
    border-color: transparent;
    color: #fff;
    box-shadow: 0 0 20px rgba(124,111,247,0.35);
  }
  .featured .plan-cta:hover { background: var(--violet-light); box-shadow: 0 4px 24px rgba(124,111,247,0.5); }

  /* ─── CTA SECTION ─── */
  .cta-section {
    padding: 6rem 2rem;
    text-align: center;
    position: relative; z-index: 1;
  }

  .cta-card {
    max-width: 680px;
    margin: 0 auto;
    background: var(--bg2);
    border: 1px solid var(--border2);
    border-radius: 28px;
    padding: 4rem 3rem;
    position: relative;
    overflow: hidden;
  }

  .cta-card::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 50% -20%, rgba(124,111,247,0.2) 0%, transparent 65%);
    pointer-events: none;
  }

  .cta-card::after {
    content: '';
    position: absolute;
    top: -1px; left: 15%; right: 15%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,111,247,0.8), transparent);
  }

  .cta-card h2 {
    font-family: var(--font-display);
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.1;
    margin-bottom: 1rem;
    position: relative; z-index: 1;
  }

  .cta-card p {
    font-size: 16px;
    color: var(--text2);
    margin-bottom: 2rem;
    position: relative; z-index: 1;
  }

  .cta-actions {
    display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;
    position: relative; z-index: 1;
  }

  /* ─── FOOTER ─── */
  footer {
    border-top: 1px solid var(--border);
    padding: 4rem 2rem 2rem;
    position: relative; z-index: 1;
  }

  .footer-grid {
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr 1fr;
    gap: 3rem;
    margin-bottom: 3rem;
  }

  .footer-brand p {
    font-size: 13px;
    color: var(--text2);
    line-height: 1.7;
    margin: 0.75rem 0 1.25rem;
    max-width: 220px;
  }

  .footer-social { display: flex; gap: 10px; }

  .footer-social a {
    width: 34px; height: 34px;
    border-radius: 8px;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--border);
    display: flex; align-items: center; justify-content: center;
    text-decoration: none;
    font-size: 14px;
    color: var(--text2);
    transition: all 0.2s;
  }
  .footer-social a:hover { background: var(--violet-bg); border-color: rgba(124,111,247,0.3); color: var(--violet-light); }

  .footer-col h4 {
    font-size: 13px;
    font-weight: 500;
    color: var(--text);
    margin-bottom: 1rem;
  }

  .footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 8px; }

  .footer-col ul a {
    font-size: 13px;
    color: var(--text2);
    text-decoration: none;
    transition: color 0.2s;
  }
  .footer-col ul a:hover { color: var(--text); }

  .footer-bottom {
    max-width: 1100px;
    margin: 0 auto;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    color: var(--text3);
    flex-wrap: wrap;
    gap: 1rem;
  }

  .footer-bottom-links { display: flex; gap: 1.5rem; }
  .footer-bottom-links a { color: var(--text3); text-decoration: none; transition: color 0.2s; }
  .footer-bottom-links a:hover { color: var(--text2); }

  /* ─── SCROLL REVEAL ─── */
  .reveal {
    opacity: 0;
    transform: translateY(28px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }
  .reveal.visible {
    opacity: 1;
    transform: translateY(0);
  }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 900px) {
    .hero { grid-template-columns: 1fr; gap: 3rem; padding: 4rem 1.5rem 3rem; }
    .features-grid { grid-template-columns: repeat(2, 1fr); }
    .pricing-grid { grid-template-columns: 1fr; }
    .footer-grid { grid-template-columns: 1fr 1fr; }
    .mock-stats-grid { grid-template-columns: repeat(2, 1fr); }
    nav { padding: 0 1.5rem; }
    .nav-links { display: none; }
  }

  @media (max-width: 600px) {
    .features-grid { grid-template-columns: 1fr; }
    .footer-grid { grid-template-columns: 1fr; }
    .cta-card { padding: 2.5rem 1.5rem; }
  }
</style>
</head>
<body>

<div class="orb orb-1"></div>
<div class="orb orb-2"></div>

<!-- ── NAVBAR ── -->
<nav>
  <a href="#" class="nav-logo">
    <div class="nav-logo-dot"></div>
    Flowly
  </a>
  <ul class="nav-links">
    <li><a href="#features">Producto</a></li>
    <li><a href="#pricing">Precios</a></li>
    <li><a href="#">Blog</a></li>
    <li><a href="#">Empresa</a></li>
  </ul>
  <div class="nav-actions">
    <button class="btn-ghost">Iniciar sesión</button>
    <button class="btn-primary">Comenzar gratis</button>
  </div>
</nav>

<!-- ── HERO ── -->
<section>
  <div class="hero">
    <!-- Texto -->
    <div>
      <div class="hero-badge">
        <span class="dot"></span>
        Nuevo — Automatización con IA
      </div>
      <h1>Gestiona tu equipo <span class="accent">sin fricciones</span></h1>
      <p class="hero-sub">Flowly centraliza tareas, métricas y comunicación en un solo lugar. Menos reuniones, más resultados reales.</p>
      <div class="hero-actions">
        <button class="btn-primary-lg">Empieza gratis →</button>
        <button class="btn-outline-lg">▶ Ver demo</button>
      </div>
      <div class="hero-social-proof">
        <div class="avatars">
          <div class="avatar av1">MR</div>
          <div class="avatar av2">AL</div>
          <div class="avatar av3">JK</div>
          <div class="avatar av4">CP</div>
        </div>
        <p class="social-text"><strong>+2,000 equipos</strong> ya usan Flowly</p>
      </div>
    </div>

    <!-- Dashboard mockup -->
    <div class="dashboard-mockup">
      <div class="mock-topbar">
        <div class="mock-dots">
          <div class="mock-dot md-r"></div>
          <div class="mock-dot md-y"></div>
          <div class="mock-dot md-g"></div>
        </div>
        <div class="mock-tabs">
          <div class="mock-tab active">Overview</div>
          <div class="mock-tab">Sprints</div>
          <div class="mock-tab">Team</div>
        </div>
        <div style="font-size:11px; color:var(--text3);">Q2 2026</div>
      </div>

      <div class="mock-sprint-card">
        <div class="mock-sprint-header">
          <span class="mock-sprint-title">Sprint #14 — Rediseño UI</span>
          <span class="mock-sprint-badge">En curso</span>
        </div>
        <div class="mock-progress-label">
          <span>Progreso</span>
          <span>72%</span>
        </div>
        <div class="mock-progress-bar">
          <div class="mock-progress-fill"></div>
        </div>
        <div class="mock-members">
          <div class="mock-member-chip"><div class="mock-member-dot" style="background:#7c6ff7"></div>Ana B.</div>
          <div class="mock-member-chip"><div class="mock-member-dot" style="background:#2dd4bf"></div>Luis R.</div>
          <div class="mock-member-chip"><div class="mock-member-dot" style="background:#f59e0b"></div>+4</div>
        </div>
      </div>

      <div class="mock-stats-grid">
        <div class="mock-stat">
          <span class="mock-stat-num">24</span>
          <span class="mock-stat-lbl">Tareas activas</span>
        </div>
        <div class="mock-stat">
          <span class="mock-stat-num" style="color:var(--green)">↑8%</span>
          <span class="mock-stat-lbl">Velocidad</span>
        </div>
        <div class="mock-stat">
          <span class="mock-stat-num">6</span>
          <span class="mock-stat-lbl">Miembros</span>
        </div>
        <div class="mock-stat">
          <span class="mock-stat-num" style="color:var(--amber)">3d</span>
          <span class="mock-stat-lbl">Al deadline</span>
        </div>
      </div>

      <div class="mock-notif">
        <div class="mock-notif-icon">✓</div>
        <span>Diseño UI aprobado por <strong style="color:var(--text)">Carlos R.</strong> hace 2 min</span>
      </div>
    </div>
  </div>
</section>

<!-- ── LOGOS ── -->
<section class="logos-strip">
  <p>Con la confianza de equipos en todo el mundo</p>
  <div class="logos-track">
    <span class="logo-item">Vercel</span>
    <span class="logo-item">Stripe</span>
    <span class="logo-item">Notion</span>
    <span class="logo-item">Linear</span>
    <span class="logo-item">Figma</span>
    <span class="logo-item">Loom</span>
    <span class="logo-item">Retool</span>
  </div>
</section>

<!-- ── FEATURES ── -->
<section class="features-section" id="features">
  <div class="container">
    <div class="reveal">
      <div class="section-label">Funcionalidades</div>
      <h2 class="section-title">Todo lo que tu equipo necesita</h2>
      <p class="section-sub">Sin integraciones complicadas. Sin configuraciones interminables. Todo incluido desde el día uno.</p>
    </div>

    <div class="features-grid">

      <div class="feat-card reveal" style="transition-delay:0.05s">
        <div class="feat-icon-wrap" style="background:rgba(124,111,247,0.12)">📋</div>
        <h3>Tableros Kanban</h3>
        <p>Visualiza el flujo de trabajo con drag-and-drop intuitivo y múltiples vistas personalizables por equipo y proyecto.</p>
      </div>

      <div class="feat-card reveal" style="transition-delay:0.1s">
        <div class="feat-icon-wrap" style="background:rgba(59,130,246,0.12)">📊</div>
        <h3>Analíticas en tiempo real</h3>
        <p>Métricas de productividad, velocidad de sprint y reportes automáticos que se actualizan con cada cambio.</p>
      </div>

      <div class="feat-card reveal" style="transition-delay:0.15s">
        <div class="feat-icon-wrap" style="background:rgba(124,111,247,0.12)">🤖</div>
        <h3>IA integrada</h3>
        <p>Sugerencias inteligentes, priorización automática y resúmenes diarios generados por IA directamente en tu flujo.</p>
      </div>

      <div class="feat-card reveal" style="transition-delay:0.2s">
        <div class="feat-icon-wrap" style="background:rgba(45,212,191,0.12)">💬</div>
        <h3>Chat contextual</h3>
        <p>Comunícate directamente dentro de cada tarea sin salir de la plataforma. Todo en contexto, nada se pierde.</p>
      </div>

      <div class="feat-card reveal" style="transition-delay:0.25s">
        <div class="feat-icon-wrap" style="background:rgba(251,191,36,0.12)">⏱</div>
        <h3>Time tracking</h3>
        <p>Registra tiempo por tarea automáticamente con un clic y genera reportes de horas listos para facturación.</p>
      </div>

      <div class="feat-card reveal" style="transition-delay:0.3s">
        <div class="feat-icon-wrap" style="background:rgba(74,222,128,0.12)">🔐</div>
        <h3>Permisos granulares</h3>
        <p>Control total de acceso por rol, proyecto o miembro. Cumplimiento SOC 2 Type II certificado.</p>
      </div>

    </div>
  </div>
</section>

<!-- ── PRICING ── -->
<section class="pricing-section" id="pricing">
  <div class="container">
    <div class="reveal" style="text-align:center">
      <div class="section-label" style="text-align:center">Planes</div>
      <h2 class="section-title" style="text-align:center">Elige tu plan</h2>
      <p class="section-sub" style="margin:0 auto 3rem; text-align:center">Sin tarjeta de crédito para empezar. Cancela cuando quieras. Sin letra pequeña.</p>
    </div>

    <div class="pricing-grid reveal">

      <!-- Starter -->
      <div class="pricing-card">
        <div class="plan-name">Starter</div>
        <div class="plan-price">$0</div>
        <div class="plan-period">gratis para siempre</div>
        <div class="plan-desc">Ideal para freelancers y equipos pequeños que están comenzando.</div>
        <div class="plan-divider"></div>
        <ul class="plan-features">
          <li><span class="check">✓</span> Hasta 3 proyectos activos</li>
          <li><span class="check">✓</span> 5 miembros por equipo</li>
          <li><span class="check">✓</span> 2 GB de almacenamiento</li>
          <li><span class="check">✓</span> Tableros Kanban básicos</li>
          <li><span class="check">✓</span> Soporte por email</li>
        </ul>
        <button class="plan-cta">Comenzar gratis</button>
      </div>

      <!-- Pro (destacado) -->
      <div class="pricing-card featured">
        <div class="plan-badge">⭐ Más popular</div>
        <div class="plan-name">Pro</div>
        <div class="plan-price">$19</div>
        <div class="plan-period">por usuario / mes, facturado anualmente</div>
        <div class="plan-desc">Para equipos en crecimiento que necesitan más potencia y automatización.</div>
        <div class="plan-divider"></div>
        <ul class="plan-features">
          <li><span class="check">✓</span> Proyectos ilimitados</li>
          <li><span class="check">✓</span> Hasta 20 miembros</li>
          <li><span class="check">✓</span> 50 GB de almacenamiento</li>
          <li><span class="check">✓</span> IA integrada y automatizaciones</li>
          <li><span class="check">✓</span> Analíticas avanzadas</li>
          <li><span class="check">✓</span> Time tracking automático</li>
          <li><span class="check">✓</span> Soporte prioritario</li>
        </ul>
        <button class="plan-cta">Empezar prueba gratuita</button>
      </div>

      <!-- Enterprise -->
      <div class="pricing-card">
        <div class="plan-name">Enterprise</div>
        <div class="plan-price" style="font-size:28px; padding-top:6px">Custom</div>
        <div class="plan-period">contacta a ventas</div>
        <div class="plan-desc">Para organizaciones con necesidades de seguridad y compliance avanzadas.</div>
        <div class="plan-divider"></div>
        <ul class="plan-features">
          <li><span class="check">✓</span> Todo lo de Pro incluido</li>
          <li><span class="check">✓</span> Miembros ilimitados</li>
          <li><span class="check">✓</span> Almacenamiento ilimitado</li>
          <li><span class="check">✓</span> SSO / SAML</li>
          <li><span class="check">✓</span> SLA garantizado 99.99%</li>
          <li><span class="check">✓</span> Onboarding dedicado</li>
          <li><span class="check">✓</span> Auditoría SOC 2 Type II</li>
        </ul>
        <button class="plan-cta">Contactar ventas</button>
      </div>

    </div>
  </div>
</section>

<!-- ── CTA FINAL ── -->
<section class="cta-section">
  <div class="cta-card reveal">
    <h2>¿Listo para trabajar mejor en equipo?</h2>
    <p>Únete a más de 2,000 equipos que ya eliminaron el caos de sus proyectos con Flowly.</p>
    <div class="cta-actions">
      <button class="btn-primary-lg">Empieza gratis hoy →</button>
      <button class="btn-outline-lg">Hablar con ventas</button>
    </div>
  </div>
</section>

<!-- ── FOOTER ── -->
<footer>
  <div class="footer-grid">
    <!-- Brand -->
    <div class="footer-brand">
      <div style="font-family:var(--font-display); font-weight:800; font-size:20px; letter-spacing:-0.5px">Flowly</div>
      <p>Gestión de equipos moderna, rápida y sin fricciones para equipos que quieren más resultados.</p>
      <div class="footer-social">
        <a href="#" title="Twitter">𝕏</a>
        <a href="#" title="GitHub">⌥</a>
        <a href="#" title="LinkedIn">in</a>
      </div>
    </div>

    <!-- Links -->
    <div class="footer-col">
      <h4>Producto</h4>
      <ul>
        <li><a href="#">Características</a></li>
        <li><a href="#">Precios</a></li>
        <li><a href="#">Roadmap</a></li>
        <li><a href="#">Changelog</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4>Empresa</h4>
      <ul>
        <li><a href="#">Sobre nosotros</a></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#">Carreras</a></li>
        <li><a href="#">Prensa</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4>Soporte</h4>
      <ul>
        <li><a href="#">Documentación</a></li>
        <li><a href="#">Centro de ayuda</a></li>
        <li><a href="#">Comunidad</a></li>
        <li><a href="#">Estado del sistema</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4>Legal</h4>
      <ul>
        <li><a href="#">Privacidad</a></li>
        <li><a href="#">Términos</a></li>
        <li><a href="#">Seguridad</a></li>
        <li><a href="#">Cookies</a></li>
      </ul>
    </div>
  </div>

  <div class="footer-bottom">
    <span>© 2026 Flowly Inc. Todos los derechos reservados.</span>
    <div class="footer-bottom-links">
      <a href="#">Privacidad</a>
      <a href="#">Términos</a>
      <a href="#">Cookies</a>
    </div>
  </div>
</footer>

<script>
  // Scroll reveal
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(el => observer.observe(el));

  // Navbar scroll effect
  const nav = document.querySelector('nav');
  window.addEventListener('scroll', () => {
    nav.style.borderBottomColor = window.scrollY > 20
      ? 'rgba(255,255,255,0.1)'
      : 'rgba(255,255,255,0.07)';
  });

  // Button hover ripple (subtle)
  document.querySelectorAll('button').forEach(btn => {
    btn.addEventListener('click', function(e) {
      this.style.transform = 'scale(0.97)';
      setTimeout(() => this.style.transform = '', 120);
    });
  });
</script>
</body>
</html>
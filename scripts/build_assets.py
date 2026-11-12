#!/usr/bin/env python3
"""Build the animated SVG assets used by the profile README.

Edit the data in this file (titles, impact tiles, project cards, terminal lines,
contact card), then run:

    python3 scripts/build_assets.py

Every asset is a self-contained dark card, so it reads the same in GitHub's light
and dark themes. Animations are CSS where possible and switch off for visitors
who set "reduce motion". Pass --static OUTDIR to write a motion-free copy for
previewing (thumbnails capture the first frame, which is mid-animation).
"""
import argparse
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "assets"

FONT = "'Segoe UI',-apple-system,'Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code','SF Mono',Menlo,Consolas,monospace"
STATIC = False


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def defs_common():
    return """
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#07021a"/><stop offset=".55" stop-color="#140640"/><stop offset="1" stop-color="#07021a"/>
  </linearGradient>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#6d28d9"/><stop offset=".5" stop-color="#c084fc"/><stop offset="1" stop-color="#6d28d9"/>
  </linearGradient>
  <linearGradient id="ic" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#7c3aed"/><stop offset="1" stop-color="#c026d3"/>
  </linearGradient>
  <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#ffffff" stop-opacity="0"/><stop offset=".5" stop-color="#ffffff" stop-opacity=".85"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#c4b5fd"/><stop offset=".45" stop-color="#c4b5fd"/><stop offset=".5" stop-color="#ffffff"/><stop offset=".55" stop-color="#c4b5fd"/><stop offset="1" stop-color="#c4b5fd"/>
    {sweep}
  </linearGradient>""".replace(
        "{sweep}",
        "" if STATIC else
        '<animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="4.5s" repeatCount="indefinite"/>',
    )


BASE_CSS = """
  .in   { animation: in .9s cubic-bezier(.16,1,.3,1) both; }
  .up   { animation: up .8s cubic-bezier(.16,1,.3,1) both; }
  .ring { transform-box: fill-box; transform-origin: center; animation: ring 2.6s ease-out infinite; }
  .pulse{ animation: pulse 2s ease-in-out infinite; }
  .comet{ stroke-dasharray: 90 910; animation: comet 7s linear infinite; }
  .blink{ animation: blink 1s step-end infinite; }
  .nudge{ animation: nudge 1.6s ease-in-out infinite; }
  @keyframes in    { from { opacity: 0; transform: translateX(-14px); } to { opacity: 1; transform: none; } }
  @keyframes up    { from { opacity: 0; transform: translateY(14px); }  to { opacity: 1; transform: none; } }
  @keyframes ring  { from { transform: scale(1); opacity: .7; } to { transform: scale(1.7); opacity: 0; } }
  @keyframes pulse { 0%,100% { opacity: .35; } 50% { opacity: 1; } }
  @keyframes comet { to { stroke-dashoffset: -1000; } }
  @keyframes blink { 50% { opacity: 0; } }
  @keyframes nudge { 0%,100% { transform: translateX(0); } 50% { transform: translateX(5px); } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
"""


def css(extra=""):
    off = "\n  * { animation: none !important; }" if STATIC else ""
    return f"<style>{BASE_CSS}{extra}{off}\n</style>"


def round_rect_path(x, y, w, h, r):
    return (f"M{x+r},{y} H{x+w-r} A{r},{r} 0 0 1 {x+w},{y+r} V{y+h-r} "
            f"A{r},{r} 0 0 1 {x+w-r},{y+h} H{x+r} A{r},{r} 0 0 1 {x},{y+h-r} "
            f"V{y+r} A{r},{r} 0 0 1 {x+r},{y} Z")


def frame(w, h, r=16, comet=True):
    """Dark panel with a faint border and a light that travels around it."""
    p = round_rect_path(1, 1, w - 2, h - 2, r)
    out = [f'<path d="{p}" fill="url(#bg)" stroke="#7c3aed" stroke-opacity=".35"/>']
    if comet:
        out.append(f'<path class="comet" d="{p}" pathLength="1000" fill="none" '
                   f'stroke="url(#edge)" stroke-width="2.2" stroke-linecap="round"/>')
    return "\n".join(out)


def svg(w, h, label, body, extra_css=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{attr(label)}">\n'
            f"<title>{esc(label)}</title>\n<defs>{defs_common()}\n</defs>\n"
            f"{css(extra_css)}\n{body}\n</svg>\n")


# ---------------------------------------------------------------- titles

TITLES = {
    "about":     ("👋", "About Me",           "who I am and what I build"),
    "impact":    ("📈", "Impact",             "results from production work"),
    "arsenal":   ("🛠️", "Technology Arsenal", "the tools I ship with"),
    "projects":  ("🌟", "Featured Projects",  "click a card to open the repo"),
    "expertise": ("🏆", "Expertise",          "where I go deep"),
    "stats":     ("📊", "GitHub Statistics",  "activity at a glance"),
    "principles": ("🧭", "How I Work",        "principles I don't compromise on"),
    "contact":   ("📫", "Get In Touch",       "open to senior backend & cloud roles"),
}


def build_title(icon, text, caption):
    w, h = 900, 72
    body = f"""{frame(w, h, 14)}
<circle class="ring" cx="40" cy="36" r="21" fill="none" stroke="#a78bfa" stroke-width="2"/>
<circle cx="40" cy="36" r="21" fill="url(#ic)"/>
<text x="40" y="43" font-family="{FONT}" font-size="19" text-anchor="middle">{icon}</text>
<text class="in" x="76" y="45" font-family="{FONT}" font-size="27" font-weight="700" fill="url(#tg)">{esc(text)}</text>
<text class="in" style="animation-delay:.25s" x="{w-26}" y="44" font-family="{FONT}" font-size="14" fill="#a19ccb" text-anchor="end">{esc(caption)}</text>"""
    return svg(w, h, text, body)


# ---------------------------------------------------------------- impact

IMPACT = [
    ("11",   "Spring Boot microservices", ["Independently deployable services", "powering a live FinTech platform"]),
    ("~30%", "Faster inter-service calls", ["Netflix Eureka + Spring Cloud Gateway", "replacing hardcoded service routing"]),
    ("50+",  "REST APIs designed",        ["Versioned, documented with OpenAPI,", "secured with JWT and role-based access"]),
    ("Zero", "Downtime deployments",      ["Rolling releases on AWS after", "re-architecting legacy modules —", "~30% less release effort"]),
    ("10+",  "CI/CD pipelines automated", ["Build, test, SonarQube quality gate,", "image push and deploy — no manual steps"]),
    ("TDD",  "JUnit 5 · Mockito · JaCoCo", ["Coverage gates enforced in CI,", "cutting regression risk across services"]),
]


def build_impact():
    w, h = 880, 410
    tw, th, gap, pad = 270, 178, 14, 20
    tiles = []
    for i, (num, label, subs) in enumerate(IMPACT):
        col, row = i % 3, i // 3
        x, y = pad + col * (tw + gap), pad + row * (th + gap)
        tp = round_rect_path(0, 0, tw, th, 10)
        lines = "\n".join(
            f'  <text x="{tw/2}" y="{118 + j*18}" class="sub">{esc(s)}</text>' for j, s in enumerate(subs))
        tiles.append(f"""<g transform="translate({x},{y})"><g class="up" style="animation-delay:{.12*i:.2f}s">
  <path d="{tp}" fill="#ffffff" fill-opacity=".035" stroke="#7c3aed" stroke-opacity=".38"/>
  <g clip-path="url(#tclip)"><rect class="tsweep" style="animation-delay:{.6*i:.1f}s" x="-120" y="0" width="120" height="2.5" fill="url(#shine)"/></g>
  <text x="{tw/2}" y="62" class="num" filter="url(#glow)">{esc(num)}</text>
  <text x="{tw/2}" y="92" class="lab">{esc(label)}</text>
{lines}
</g></g>""")
    extra = f"""
  .num {{ font: 700 40px {FONT}; fill: #c4b5fd; text-anchor: middle; }}
  .lab {{ font: 600 16px {FONT}; fill: #f5f3ff; text-anchor: middle; }}
  .sub {{ font: 400 13px {FONT}; fill: #b4b0d6; text-anchor: middle; }}
  .tsweep {{ animation: tsweep 4.2s linear infinite; }}
  @keyframes tsweep {{ from {{ transform: translateX(0); }} to {{ transform: translateX({tw+240}px); }} }}"""
    body = f"""<defs>
  <clipPath id="tclip"><rect x="0" y="0" width="{tw}" height="{th}" rx="10"/></clipPath>
  <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
{frame(w, h, 14)}
{chr(10).join(tiles)}"""
    alt = "; ".join(f"{n} {l}" for n, l, _ in IMPACT)
    return svg(w, h, "Impact: " + alt, body, extra)


# ---------------------------------------------------------------- project cards

PROJECTS = {
    "ecommerce": dict(
        icon="🛒", tag="FLAGSHIP", title="E-Commerce Microservices",
        repo="hayattarique/ecommerce-microservice",
        chips=["Java 21", "Spring Boot 4.1", "PostgreSQL", "LangChain4j"],
        desc=["Distributed e-commerce backend, built sprint by sprint:",
              "eight modules behind a gateway, a database per service."],
        bullets=["Reusable JWT security starter (auto-configuration)",
                 "Refresh-token rotation, revocation and RBAC",
                 "OpenTelemetry tracing exported to Jaeger",
                 "Per-service Jenkins pipelines gated on health",
                 "LLM assistant service built on LangChain4j"]),
    "spring-ai": dict(
        icon="🧠", tag="GENAI", title="Spring AI Lab",
        repo="hayattarique/spring-ai",
        chips=["Spring AI 2.0", "Qdrant", "Redis", "Ollama", "PostgreSQL"],
        desc=["Eight hands-on Spring AI projects, each building on",
              "the last, up to a production-shaped RAG pipeline."],
        bullets=["OpenAI, Ollama, Docker Model Runner, Bedrock",
                 "RAG with Qdrant and Tavily web search",
                 "Semantic cache in Redis",
                 "PII masking before anything reaches the model",
                 "Structured output and persistent chat memory"]),
    "saga": dict(
        icon="⚡", tag="EVENT-DRIVEN", title="Saga Choreography",
        repo="hayattarique/saga-choreography",
        chips=["Java", "Apache Kafka", "Spring Boot"],
        desc=["Distributed transactions with no central orchestrator:",
              "order and payment services talk only through Kafka."],
        bullets=["Choreographed saga over Kafka events",
                 "Compensating transactions when payment fails",
                 "Shared common-dtos event contract",
                 "Fault isolation between services"]),
    "gateway": dict(
        icon="🚪", tag="PLATFORM", title="Cloud Gateway",
        repo="hayattarique/cloud-gateway",
        chips=["Spring Cloud Gateway", "Eureka", "LoadBalancer"],
        desc=["The edge of a microservices estate: dynamic routing",
              "with service discovery and client-side balancing."],
        bullets=["Eureka discovery feeding gateway routes",
                 "Spring Cloud LoadBalancer across instances",
                 "Route configuration and filter chains",
                 "Production-shaped setup, not a one-file demo"]),
}


def build_card(p):
    w, h = 520, 440
    out = [frame(w, h, 18)]
    # header: icon tile + tag pill
    out.append(f'<rect x="28" y="28" width="50" height="50" rx="13" fill="url(#ic)"/>'
               f'<text x="53" y="62" font-family="{FONT}" font-size="25" text-anchor="middle">{p["icon"]}</text>')
    pw = len(p["tag"]) * 9.7 + 42
    out.append(f'<rect x="92" y="40" width="{pw:.0f}" height="26" rx="13" fill="#7c3aed" fill-opacity=".22" stroke="#a78bfa" stroke-opacity=".55"/>'
               f'<circle class="pulse" cx="107" cy="53" r="4" fill="#22c55e"/>'
               f'<text x="119" y="58" font-family="{FONT}" font-size="12" font-weight="700" letter-spacing="1.5" fill="#ddd6fe">{esc(p["tag"])}</text>')
    out.append(f'<text class="in" x="28" y="114" font-family="{FONT}" font-size="25" font-weight="700" fill="url(#tg)">{esc(p["title"])}</text>')
    # chips
    x = 28
    for i, c in enumerate(p["chips"]):
        cw = len(c) * 7.3 + 22
        assert x + cw <= w - 24, f"chips overflow in {p['title']}"
        out.append(f'<g class="up" style="animation-delay:{.25 + .08*i:.2f}s">'
                   f'<rect x="{x:.0f}" y="130" width="{cw:.0f}" height="26" rx="8" fill="#ffffff" fill-opacity=".06" stroke="#a78bfa" stroke-opacity=".35"/>'
                   f'<text x="{x + cw/2:.0f}" y="147.5" font-family="{FONT}" font-size="12.5" font-weight="600" fill="#e9d5ff" text-anchor="middle">{esc(c)}</text></g>')
        x += cw + 8
    # description
    for j, line in enumerate(p["desc"]):
        out.append(f'<text x="28" y="{190 + 22*j}" font-family="{FONT}" font-size="15" fill="#cfcbea">{esc(line)}</text>')
    # bullets
    for j, b in enumerate(p["bullets"]):
        y = 248 + 26 * j
        out.append(f'<g class="in" style="animation-delay:{.5 + .12*j:.2f}s">'
                   f'<text x="28" y="{y}" font-family="{FONT}" font-size="13" fill="#a78bfa">▸</text>'
                   f'<text x="46" y="{y}" font-family="{FONT}" font-size="14.5" fill="#ece9ff">{esc(b)}</text></g>')
    # footer: call to action + repo path
    out.append(f'<rect x="28" y="{h-60}" width="150" height="34" rx="17" fill="url(#ic)"/>'
               f'<text x="48" y="{h-38}" font-family="{FONT}" font-size="14" font-weight="700" fill="#ffffff">View project</text>'
               f'<text class="nudge" x="146" y="{h-38}" font-family="{FONT}" font-size="15" font-weight="700" fill="#ffffff">→</text>')
    out.append(f'<text x="{w-28}" y="{h-38}" font-family="{MONO}" font-size="12" fill="#8f89bd" text-anchor="end">{esc(p["repo"])}</text>')
    label = f'{p["title"]}: ' + " ".join(p["desc"]) + " " + "; ".join(p["bullets"]) + "."
    return svg(w, h, label, "\n".join(out))


# ---------------------------------------------------------------- terminal

# Each line is (kind, [(css class, text), ...]). Kind "cmd" lines are typed out.
P = "p"
TERMINAL = [
    ("cmd", [(P, "$ "), ("c", "whoami")]),
    ("out", [("o", "tarique-hayat · java backend & cloud engineer")]),
    ("cmd", [(P, "$ "), ("c", "jshell")]),
    ("cmd", [(P, "jshell> "), ("k", "var "), ("x", "me = "), ("k", "new "), ("t", "Engineer"), ("x", "(")]),
    ("out", [(P, "   ...> "), ("s", '  "Tarique Hayat"'), ("x", ",")]),
    ("out", [(P, "   ...> "), ("t", "  List"), ("x", "."), ("m", "of"), ("x", "("), ("s", '"Java 21"'), ("x", ", "), ("s", '"Spring Boot 4"'), ("x", ", "), ("s", '"Kafka"'), ("x", "),")]),
    ("out", [(P, "   ...> "), ("t", "  List"), ("x", "."), ("m", "of"), ("x", "("), ("s", '"Spring AI"'), ("x", ", "), ("s", '"LangChain4j"'), ("x", ", "), ("s", '"RAG"'), ("x", "),")]),
    ("out", [(P, "   ...> "), ("t", "  List"), ("x", "."), ("m", "of"), ("x", "("), ("s", '"AWS"'), ("x", ", "), ("s", '"Docker"'), ("x", ", "), ("s", '"Jenkins"'), ("x", "));")]),
    ("out", [("o", "me ==> Engineer[name=Tarique Hayat, ...]")]),
    ("cmd", [(P, "jshell> "), ("x", "me."), ("m", "openToWork"), ("x", "()")]),
    ("out", [("o", "$2 ==> "), ("n", "true")]),
]
TERM_COLORS = {"p": "#4ade80", "c": "#f5f3ff", "o": "#a19ccb", "k": "#c084fc", "t": "#67e8f9",
               "s": "#86efac", "m": "#fde68a", "x": "#e9e6ff", "n": "#fb923c"}


def build_terminal():
    w, lh, top, fs, cw = 580, 24, 70, 14.5, 8.75
    h = top + lh * (len(TERMINAL) + 1) + 6
    out = [frame(w, h, 14, comet=False)]
    out.append(f'<path d="M1,15 A14,14 0 0 1 15,1 H{w-15} A14,14 0 0 1 {w-1},15 V38 H1 Z" fill="#ffffff" fill-opacity=".05"/>'
               f'<line x1="1" y1="38" x2="{w-1}" y2="38" stroke="#7c3aed" stroke-opacity=".35"/>'
               '<circle cx="22" cy="20" r="6" fill="#ff5f57"/><circle cx="42" cy="20" r="6" fill="#febc2e"/><circle cx="62" cy="20" r="6" fill="#28c840"/>'
               f'<text x="{w/2}" y="24.5" font-family="{MONO}" font-size="12.5" fill="#a19ccb" text-anchor="middle">tarique@hayat: ~</text>')
    t = 0.3
    clips = []
    for i, (kind, toks) in enumerate(TERMINAL):
        y = top + lh * i
        spans = "".join(f'<tspan fill="{TERM_COLORS[c]}">{esc(s)}</tspan>' for c, s in toks)
        length = sum(len(s) for _, s in toks)
        if kind == "cmd":
            width = length * cw + 6
            dur = max(.35, length * .045)
            # one step per character; the last step opens wide so wider fallback fonts are never cut off
            steps = [str(int(k * cw)) for k in range(length)] + [f"{width + 40:.0f}"]
            anim = "" if STATIC else (f'<animate attributeName="width" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze" '
                                      f'calcMode="discrete" values="{";".join(steps)}" '
                                      f'keyTimes="{";".join(f"{k/length:.4f}" for k in range(length + 1))}"/>')
            start_w = f"{width + 40:.0f}" if STATIC else "0"
            clips.append(f'<clipPath id="l{i}"><rect x="20" y="{y-lh+6}" width="{start_w}" height="{lh}">{anim}</rect></clipPath>')
            out.append(f'<text clip-path="url(#l{i})" x="22" y="{y}" font-family="{MONO}" font-size="{fs}" xml:space="preserve">{spans}</text>')
            t += dur + .25
        else:
            out.append(f'<text class="up" style="animation-delay:{t:.2f}s;animation-duration:.35s" x="22" y="{y}" '
                       f'font-family="{MONO}" font-size="{fs}" xml:space="preserve">{spans}</text>')
            t += .18
    y = top + lh * len(TERMINAL)
    out.append(f'<g class="up" style="animation-delay:{t:.2f}s;animation-duration:.3s">'
               f'<text x="22" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{TERM_COLORS["p"]}">jshell&gt; </text>'
               f'<rect class="blink" x="{22 + 8*cw:.0f}" y="{y-13}" width="9" height="17" fill="#c4b5fd"/></g>')
    body = "<defs>" + "".join(clips) + "</defs>\n" + "\n".join(out)
    label = ("Terminal: whoami prints tarique-hayat, java backend and cloud engineer. In jshell, an Engineer "
             "record lists Java 21, Spring Boot 4 and Kafka; Spring AI, LangChain4j and RAG; AWS, Docker and "
             "Jenkins. me.openToWork() returns true.")
    return svg(w, h, label, body)


# ---------------------------------------------------------------- contact card

def build_cta():
    w, h = 900, 250
    chips = ["Full-time", "Remote", "Hyderabad · Kolkata · Delhi"]
    out = [frame(w, h, 18)]
    out.append(f'<text class="up" x="{w/2}" y="70" font-family="{FONT}" font-size="34" font-weight="800" fill="url(#tg)" text-anchor="middle">Let’s build something that stays up</text>')
    out.append(f'<text class="up" style="animation-delay:.15s" x="{w/2}" y="102" font-family="{FONT}" font-size="16" fill="#b4b0d6" text-anchor="middle">'
               'Open to Senior Java Backend &amp; Cloud Engineer roles · including GenAI on the JVM</text>')
    bw, bh, bx, by = 380, 54, (w - 380) / 2, 124
    out.append(f'<rect class="bring" x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="27" fill="none" stroke="#a78bfa" stroke-width="2"/>')
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="27" fill="url(#ic)"/>')
    out.append(f'<g clip-path="url(#btn)"><rect class="bsweep" x="{bx-140}" y="{by}" width="140" height="{bh}" fill="url(#shine)" opacity=".35"/></g>')
    out.append(f'<text x="{w/2}" y="{by+34}" font-family="{FONT}" font-size="18" font-weight="700" fill="#ffffff" text-anchor="middle">✉  hayattarique3@gmail.com</text>')
    # availability chips, centred as a row
    widths = [len(c) * 6.9 + 40 for c in chips]
    total = sum(widths) + 12 * (len(chips) - 1)
    x = (w - total) / 2
    for i, (c, cw) in enumerate(zip(chips, widths)):
        out.append(f'<g class="up" style="animation-delay:{.35 + .1*i:.2f}s">'
                   f'<rect x="{x:.0f}" y="198" width="{cw:.0f}" height="28" rx="14" fill="#22c55e" fill-opacity=".12" stroke="#22c55e" stroke-opacity=".5"/>'
                   f'<circle class="pulse" style="animation-delay:{.3*i:.1f}s" cx="{x+16:.0f}" cy="212" r="4" fill="#22c55e"/>'
                   f'<text x="{x+28:.0f}" y="216.5" font-family="{FONT}" font-size="13" font-weight="600" fill="#bbf7d0">{esc(c)}</text></g>')
        x += cw + 12
    extra = f"""
  .bring {{ transform-box: fill-box; transform-origin: center; animation: bring 2.8s ease-out infinite; }}
  @keyframes bring {{ from {{ transform: scale(1); opacity: .7; }} to {{ transform: scale(1.1, 1.5); opacity: 0; }} }}
  .bsweep {{ animation: bsweep 3.2s ease-in-out infinite; }}
  @keyframes bsweep {{ from {{ transform: translateX(0); }} to {{ transform: translateX({bw+280}px); }} }}"""
    body = f'<defs><clipPath id="btn"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="27"/></clipPath></defs>\n' + "\n".join(out)
    return svg(w, h, "Let's build something that stays up. Email hayattarique3@gmail.com. Open to full-time, remote, "
                     "and Hyderabad, Kolkata or Delhi roles.", body, extra)


# ---------------------------------------------------------------- main

def main():
    global STATIC
    ap = argparse.ArgumentParser()
    ap.add_argument("--static", metavar="OUTDIR", help="write motion-free previews to OUTDIR instead")
    args = ap.parse_args()
    root = ROOT
    if args.static:
        STATIC = True
        root = pathlib.Path(args.static)
    files = {f"titles/{k}.svg": build_title(*v) for k, v in TITLES.items()}
    files.update({f"projects/{k}.svg": build_card(v) for k, v in PROJECTS.items()})
    files["impact.svg"] = build_impact()
    files["terminal.svg"] = build_terminal()
    files["cta.svg"] = build_cta()
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path}")


if __name__ == "__main__":
    main()

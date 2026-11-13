#!/usr/bin/env python3
"""Build the SVG assets used by the profile README.

Every asset is written twice, as NAME-light.svg and NAME-dark.svg, using GitHub's own
colour tokens, so the README can serve the right one with <picture> and the graphics
sit natively on either theme. Edit the data below, then run:

    python3 scripts/build_assets.py

Only the hero has motion (request packets moving through a small service graph), and
it switches off for visitors who prefer reduced motion.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "assets"

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# GitHub Primer colour tokens
THEMES = {
    "light": dict(bg="#ffffff", surface="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#656d76",
                  subtle="#8c959f", accent="#8250df", link="#0969da", green="#1a7f37", java="#b07219",
                  grid="#d0d7de", glow=".06", btn="#8250df"),
    "dark":  dict(bg="#0d1117", surface="#161b22", border="#30363d", text="#e6edf3", muted="#8d96a0",
                  subtle="#6e7681", accent="#a371f7", link="#4493f8", green="#3fb950", java="#b07219",
                  grid="#30363d", glow=".12", btn="#8957e5"),
}


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def svg(w, h, label, body, css=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{attr(label)}">\n<title>{esc(label)}</title>\n'
            f'{"<style>" + css + "</style>" if css else ""}\n{body}\n</svg>\n')


# ------------------------------------------------------------------ hero

HERO = dict(
    eyebrow="JAVA BACKEND & CLOUD ENGINEER",
    name="Tarique Hayat",
    line="Resilient, observable Java services, and LLM features on the JVM.",
    status="Open to senior backend & cloud roles",
    location="Hyderabad · Kolkata · Delhi · Remote",
)

# Service graph drawn on the right of the hero: name -> (centre x, centre y, highlighted)
NODES = {
    "gateway":  (840, 170, False),
    "auth":     (985, 100, False),
    "user":     (985, 170, False),
    "ai · llm": (985, 240, True),
    "kafka":    (1120, 135, False),
    "postgres": (1120, 205, False),
}
EDGES = [("gateway", "auth"), ("gateway", "user"), ("gateway", "ai · llm"),
         ("auth", "postgres"), ("user", "kafka"), ("user", "postgres"), ("ai · llm", "kafka")]
NODE_W, NODE_H = 100, 32


def edge_path(a, b):
    (x1, y1, _), (x2, y2, _) = NODES[a], NODES[b]
    x1 += NODE_W / 2
    x2 -= NODE_W / 2
    return f"M{x1:.0f},{y1} C{x1+28:.0f},{y1} {x2-28:.0f},{y2} {x2:.0f},{y2}"


def build_hero(t):
    w, h = 1200, 320
    css = """
  .pkt { opacity: 0; }
  @supports (offset-path: path('M0,0 L1,1')) {
    .pkt { animation: travel 2.8s cubic-bezier(.45,0,.55,1) infinite both; }
  }
  @keyframes travel { 0% { offset-distance: 0%; opacity: 0; } 12% { opacity: 1; } 88% { opacity: 1; } 100% { offset-distance: 100%; opacity: 0; } }
  .live { animation: live 2.4s ease-in-out infinite; }
  @keyframes live { 0%,100% { opacity: .35; } 50% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) { .pkt { animation: none; opacity: 0; } .live { animation: none; } }"""
    out = [f"""<defs>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.2" fill="{t['grid']}"/></pattern>
  <radialGradient id="fade" cx="980" cy="170" r="330" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
  <mask id="m"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
  <radialGradient id="glow" cx="1000" cy="150" r="320" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{t['accent']}" stop-opacity="{t['glow']}"/><stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/>
  </radialGradient>
  <clipPath id="card"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12"/></clipPath>
</defs>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12" fill="{t['bg']}" stroke="{t['border']}"/>
<g clip-path="url(#card)">
  <rect width="{w}" height="{h}" fill="url(#dots)" mask="url(#m)"/>
  <rect width="{w}" height="{h}" fill="url(#glow)"/>
</g>"""]
    # text block
    out.append(f'<text x="64" y="104" font-family="{MONO}" font-size="13" letter-spacing="2.4" fill="{t["accent"]}">{esc(HERO["eyebrow"])}</text>')
    out.append(f'<text x="62" y="172" font-family="{SANS}" font-size="62" font-weight="600" letter-spacing="-1.2" fill="{t["text"]}">{esc(HERO["name"])}</text>')
    out.append(f'<text x="64" y="214" font-family="{SANS}" font-size="20" fill="{t["muted"]}">{esc(HERO["line"])}</text>')
    out.append(f'<circle class="live" cx="70" cy="257" r="4" fill="{t["green"]}"/>'
               f'<text x="84" y="262" font-family="{MONO}" font-size="13" fill="{t["text"]}">{esc(HERO["status"])}'
               f'<tspan fill="{t["subtle"]}">   /   </tspan><tspan fill="{t["muted"]}">{esc(HERO["location"])}</tspan></text>')
    # service graph
    for i, (a, b) in enumerate(EDGES):
        d = edge_path(a, b)
        out.append(f'<path d="{d}" fill="none" stroke="{t["border"]}" stroke-width="1.4"/>')
        out.append(f'<circle class="pkt" r="3" fill="{t["accent"]}" '
                   f'style="offset-path:path(\'{d}\');animation-delay:{(i * 0.45) % 2.8:.2f}s"/>')
    for name, (cx, cy, hl) in NODES.items():
        x, y = cx - NODE_W / 2, cy - NODE_H / 2
        stroke = t["accent"] if hl else t["border"]
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{NODE_W}" height="{NODE_H}" rx="6" fill="{t["surface"]}" stroke="{stroke}"/>'
                   f'<text x="{cx}" y="{cy+4.5}" font-family="{MONO}" font-size="12" text-anchor="middle" '
                   f'fill="{t["accent"] if hl else t["muted"]}">{esc(name)}</text>')
    label = f'{HERO["name"]}, Java backend and cloud engineer. {HERO["line"]} {HERO["status"]}: {HERO["location"]}.'
    return svg(w, h, label, "\n".join(out), css)


# ------------------------------------------------------------------ impact

IMPACT = [
    ("11",   "Spring Boot microservices",  ["Independently deployable services", "powering a live FinTech platform"]),
    ("~30%", "Faster inter-service calls", ["Eureka and Spring Cloud Gateway", "replacing hardcoded routing"]),
    ("50+",  "REST APIs designed",         ["Versioned, OpenAPI-documented,", "secured with JWT and RBAC"]),
    ("Zero", "Downtime deployments",       ["Rolling releases on AWS after", "re-architecting legacy modules;", "~30% less release effort"]),
    ("10+",  "CI/CD pipelines automated",  ["Build, test, SonarQube gate, image", "push and deploy, no manual steps"]),
    ("TDD",  "JUnit 5 · Mockito · JaCoCo", ["Coverage gates enforced in CI,", "cutting regression risk"]),
]


def build_impact(t):
    w, cols, ch = 880, 3, 164
    rows = (len(IMPACT) + cols - 1) // cols
    h = rows * ch
    cw = w / cols
    out = [f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>']
    for c in range(1, cols):
        out.append(f'<line x1="{c*cw:.1f}" y1="1" x2="{c*cw:.1f}" y2="{h-1}" stroke="{t["border"]}"/>')
    for r in range(1, rows):
        out.append(f'<line x1="1" y1="{r*ch}" x2="{w-1}" y2="{r*ch}" stroke="{t["border"]}"/>')
    for i, (num, label, subs) in enumerate(IMPACT):
        x, y = (i % cols) * cw + 28, (i // cols) * ch
        out.append(f'<text x="{x:.1f}" y="{y+54}" font-family="{SANS}" font-size="34" font-weight="600" letter-spacing="-.6" fill="{t["text"]}">{esc(num)}</text>')
        out.append(f'<text x="{x:.1f}" y="{y+82}" font-family="{SANS}" font-size="14" font-weight="600" fill="{t["accent"]}">{esc(label)}</text>')
        for j, s in enumerate(subs):
            out.append(f'<text x="{x:.1f}" y="{y+106+18*j}" font-family="{SANS}" font-size="12.5" fill="{t["muted"]}">{esc(s)}</text>')
    label = "Impact: " + "; ".join(f"{n} {l}" for n, l, _ in IMPACT)
    return svg(w, h, label, "\n".join(out))


# ------------------------------------------------------------------ project cards

PROJECTS = {
    "ecommerce": dict(
        tag="FLAGSHIP", title="E-Commerce Microservices",
        desc=["Distributed e-commerce backend on Java 21 and Spring",
              "Boot 4: eight modules, a database per service."],
        points=["Reusable JWT security starter (auto-configuration)",
                "Per-service Jenkins pipelines gated on health",
                "OpenTelemetry tracing and an LLM assistant service"],
        stack="Spring Boot 4.1 · Spring Cloud · PostgreSQL"),
    "spring-ai": dict(
        tag="GENERATIVE AI", title="Spring AI Lab",
        desc=["Eight Spring AI projects, each building on the last,",
              "up to a production-shaped RAG pipeline."],
        points=["RAG with Qdrant and Tavily web search",
                "Semantic cache in Redis, PII masking before the LLM",
                "OpenAI, Ollama, Docker Model Runner, Bedrock"],
        stack="Spring AI 2.0 · Spring Boot 4.1 · Qdrant · Redis"),
    "saga": dict(
        tag="EVENT-DRIVEN", title="Saga Choreography",
        desc=["Distributed transactions with no orchestrator: order",
              "and payment services coordinate over Kafka."],
        points=["Choreographed saga over Kafka domain events",
                "Compensating transactions when payment fails",
                "Shared event contract in a common-dtos module"],
        stack="Apache Kafka · Spring Boot"),
    "gateway": dict(
        tag="PLATFORM", title="Cloud Gateway",
        desc=["API gateway with service discovery and client-side",
              "load balancing across service instances."],
        points=["Eureka discovery feeding gateway routes",
                "Spring Cloud LoadBalancer across instances",
                "Route configuration and filter chains"],
        stack="Spring Cloud Gateway · Eureka"),
}


def build_card(p, t):
    w, h = 440, 250
    assert 80 + len(p["stack"]) * 7.0 <= w - 20, f'stack line too long: {p["title"]}'
    assert all(len(s) <= 56 for s in p["desc"] + p["points"]), f'line too long: {p["title"]}'
    out = [f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>']
    out.append(f'<text x="24" y="38" font-family="{MONO}" font-size="11" letter-spacing="1.6" fill="{t["accent"]}">{esc(p["tag"])}</text>')
    out.append(f'<text x="{w-24}" y="40" font-family="{SANS}" font-size="16" text-anchor="end" fill="{t["subtle"]}">↗</text>')
    out.append(f'<text x="24" y="70" font-family="{SANS}" font-size="20" font-weight="600" fill="{t["link"]}">{esc(p["title"])}</text>')
    for j, line in enumerate(p["desc"]):
        out.append(f'<text x="24" y="{98 + 20*j}" font-family="{SANS}" font-size="14" fill="{t["muted"]}">{esc(line)}</text>')
    for j, pt in enumerate(p["points"]):
        y = 152 + 21 * j
        out.append(f'<rect x="24" y="{y-5}" width="8" height="1.6" fill="{t["accent"]}"/>'
                   f'<text x="40" y="{y}" font-family="{SANS}" font-size="13" fill="{t["text"]}">{esc(pt)}</text>')
    out.append(f'<line x1="1" y1="{h-44}" x2="{w-1}" y2="{h-44}" stroke="{t["border"]}"/>')
    out.append(f'<circle cx="30" cy="{h-22}" r="5" fill="{t["java"]}"/>'
               f'<text x="42" y="{h-17.5}" font-family="{SANS}" font-size="12.5" fill="{t["muted"]}">Java</text>'
               f'<text x="80" y="{h-17.5}" font-family="{MONO}" font-size="11.5" fill="{t["subtle"]}">{esc(p["stack"])}</text>')
    label = f'{p["title"]} ({p["tag"].lower()}): ' + " ".join(p["desc"]) + " " + "; ".join(p["points"]) + f'. Stack: Java, {p["stack"]}.'
    return svg(w, h, label, "\n".join(out))


# ------------------------------------------------------------------ shared drawing helpers

# Rough glyph widths (px per character) used to assert that text fits its box.
W_SANS, W_SANS_B, W_MONO = 0.53, 0.58, 0.61

MOTION_CSS = """
  .pkt { opacity: 0; }
  @supports (offset-path: path('M0,0 L1,1')) {
    .pkt { animation: travel 2.6s cubic-bezier(.45,0,.55,1) infinite both; }
  }
  @keyframes travel { 0% { offset-distance: 0%; opacity: 0; } 15% { opacity: 1; } 85% { opacity: 1; } 100% { offset-distance: 100%; opacity: 0; } }
  @media (prefers-reduced-motion: reduce) { .pkt { animation: none !important; opacity: 0; } }"""


def fits(text, size, avail, kind=W_SANS, what=""):
    need = len(text) * size * kind
    assert need <= avail, f"text too wide ({need:.0f}>{avail:.0f}px): {what or text!r}"


def box(t, x, y, w, h, title, sub=None, accent=False, dashed=False, size=13):
    stroke = t["accent"] if accent else t["border"]
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    fits(title, size, w - 24, W_SANS_B, title)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{t["surface"]}" stroke="{stroke}"{dash}/>']
    ty = y + (h / 2 + 4.5 if not sub else h / 2 - 2)
    out.append(f'<text x="{x+12}" y="{ty:.1f}" font-family="{SANS}" font-size="{size}" font-weight="600" '
               f'fill="{t["accent"] if accent else t["text"]}">{esc(title)}</text>')
    if sub:
        fits(sub, 10.5, w - 24, W_MONO, sub)
        out.append(f'<text x="{x+12}" y="{ty+16:.1f}" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">{esc(sub)}</text>')
    return "\n".join(out)


def curve(x1, y1, x2, y2):
    dx = max(18, (x2 - x1) * .45)
    return f"M{x1:.0f},{y1:.0f} C{x1+dx:.0f},{y1:.0f} {x2-dx:.0f},{y2:.0f} {x2:.0f},{y2:.0f}"


def wire(t, d, dashed=False, packet=None):
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    out = [f'<path d="{d}" fill="none" stroke="{t["border"]}" stroke-width="1.4"{dash} marker-end="url(#arr)"/>']
    if packet is not None:
        out.append(f'<circle class="pkt" r="3" fill="{t["accent"]}" style="offset-path:path(\'{d}\');animation-delay:{packet:.2f}s"/>')
    return "\n".join(out)


def arrow_marker(t):
    return (f'<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,1 L9,5 L0,9 z" fill="{t["subtle"]}"/></marker>')


def frame_rect(t, w, h):
    return f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>'


def caption(t, x, y, text, anchor="start", color=None):
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="10.5" letter-spacing="1.4" text-anchor="{anchor}" '
            f'fill="{color or t["subtle"]}">{esc(text)}</text>')


# ------------------------------------------------------------------ flagship architecture

ARCH_SERVICES = [  # (name, detail, highlighted)
    ("auth-service", ":9091 · JWT issuance", False),
    ("user-service", ":9092 · RBAC", False),
    ("product-service", ":9093 · catalogue", False),
    ("ai-service", ":9094 · LangChain4j", True),
]
ARCH_PLATFORM = ["discovery-server · Eureka", "config-server", "OpenTelemetry → Jaeger", "Jenkins · health-gated"]


def build_architecture(t):
    w, h = 880, 440
    out = [f"<defs>{arrow_marker(t)}</defs>", frame_rect(t, w, h)]
    for x, label in [(28, "CLIENT"), (186, "EDGE"), (384, "SERVICES"), (624, "DATA & AI")]:
        out.append(caption(t, x, 32, label))
    # client and gateway
    out.append(box(t, 24, 166, 124, 48, "Client", "REST + JWT"))
    out.append(box(t, 182, 166, 156, 48, "gateway", ":9999 · JWT at edge"))
    # shared starter band above the services
    out.append(f'<rect x="380" y="46" width="176" height="26" rx="6" fill="none" stroke="{t["accent"]}" stroke-dasharray="4 3"/>'
               f'<text x="468" y="63" font-family="{MONO}" font-size="10.5" text-anchor="middle" fill="{t["accent"]}">utility · JWT starter</text>')
    ys = [84, 140, 196, 252]
    for i, ((name, sub, hl), y) in enumerate(zip(ARCH_SERVICES, ys)):
        out.append(box(t, 380, y, 176, 44, name, sub, accent=hl))
        out.append(wire(t, curve(338, 190, 378, y + 22), packet=.9 + .35 * i))
    out.append(wire(t, curve(148, 190, 180, 190), packet=0.2))
    # data and AI
    out.append(box(t, 620, 96, 236, 60, "PostgreSQL 16", "database per service · Flyway"))
    out.append(box(t, 620, 186, 236, 44, "Kafka + outbox", "planned", dashed=True))
    out.append(box(t, 620, 252, 236, 44, "OpenAI GPT", "chosen tool → service call", accent=True))
    for y in ys[:3]:
        out.append(wire(t, curve(556, y + 22, 618, 126)))
    out.append(wire(t, curve(556, 218, 618, 208), dashed=True))
    out.append(wire(t, curve(556, 274, 618, 274), packet=2.3))
    # platform band
    out.append(f'<line x1="24" y1="330" x2="{w-24}" y2="330" stroke="{t["border"]}"/>')
    out.append(caption(t, 28, 356, "PLATFORM"))
    x = 24
    for item in ARCH_PLATFORM:
        cw = len(item) * 12 * W_SANS + 40
        out.append(f'<rect x="{x:.0f}" y="368" width="{cw:.0f}" height="34" rx="17" fill="{t["surface"]}" stroke="{t["border"]}"/>'
                   f'<circle cx="{x+16:.0f}" cy="385" r="3.5" fill="{t["green"]}"/>'
                   f'<text x="{x+26:.0f}" y="389.5" font-family="{SANS}" font-size="12" fill="{t["text"]}">{esc(item)}</text>')
        x += cw + 12
    assert x <= w - 12, "platform chips overflow"
    out.append(f'<text x="{w-24}" y="424" font-family="{SANS}" font-size="11.5" text-anchor="end" fill="{t["subtle"]}">'
               'Dashed = planned. Every service owns its schema; no shared tables.</text>')
    label = ("Architecture of the e-commerce platform: a client calls the gateway, which validates the JWT and routes to "
             "auth-service, user-service, product-service and ai-service. Services share a JWT security starter, each owns "
             "its PostgreSQL schema, ai-service calls OpenAI through LangChain4j, and Kafka with an outbox is planned. "
             "Platform: Eureka discovery, config server, OpenTelemetry to Jaeger, Jenkins health-gated deploys.")
    return svg(w, h, label, "\n".join(out), MOTION_CSS)


# ------------------------------------------------------------------ GenAI request flow

GENAI_FLOW = [  # (title, line 1, line 2, highlighted)
    ("Question", "“laptops under", "₹50,000”", False),
    ("gateway", "validates the", "user's JWT", False),
    ("ai-service", "LangChain4j +", "system prompt", True),
    ("LLM", "picks a @Tool:", "findProducts()", True),
    ("product-service", "called with the", "caller's JWT", False),
    ("Answer", "grounded in", "live data", False),
]


def build_genai_flow(t):
    w, h = 880, 206
    n, bw, gap = len(GENAI_FLOW), 130, 10.4
    out = [f"<defs>{arrow_marker(t)}</defs>", frame_rect(t, w, h)]
    for i, (title, l1, l2, hl) in enumerate(GENAI_FLOW):
        x = 24 + i * (bw + gap)
        stroke = t["accent"] if hl else t["border"]
        out.append(f'<circle cx="{x+16}" cy="36" r="11" fill="{t["accent"] if hl else t["surface"]}" stroke="{stroke}"/>'
                   f'<text x="{x+16}" y="40" font-family="{MONO}" font-size="11" text-anchor="middle" '
                   f'fill="{t["bg"] if hl else t["muted"]}">{i+1}</text>')
        fits(title, 12.5, bw - 20, W_SANS_B, title)
        for line in (l1, l2):
            fits(line, 11, bw - 20, W_SANS, line)
        out.append(f'<rect x="{x:.1f}" y="58" width="{bw}" height="82" rx="6" fill="{t["surface"]}" stroke="{stroke}"/>'
                   f'<text x="{x+10:.1f}" y="84" font-family="{SANS}" font-size="12.5" font-weight="600" fill="{t["accent"] if hl else t["text"]}">{esc(title)}</text>'
                   f'<text x="{x+10:.1f}" y="106" font-family="{SANS}" font-size="11" fill="{t["muted"]}">{esc(l1)}</text>'
                   f'<text x="{x+10:.1f}" y="122" font-family="{SANS}" font-size="11" fill="{t["muted"]}">{esc(l2)}</text>')
        if i < n - 1:
            out.append(wire(t, f"M{x+bw+2:.1f},99 L{x+bw+gap-2:.1f},99", packet=.4 * i))
    out.append(f'<line x1="24" y1="160" x2="{w-24}" y2="160" stroke="{t["border"]}"/>')
    out.append(f'<text x="24" y="184" font-family="{SANS}" font-size="12.5" fill="{t["muted"]}">'
               'Tools call services, never databases: the LLM chooses, the service enforces the permission.</text>')
    out.append(caption(t, w - 24, 184, "WIRED · TOOLS IN PROGRESS", anchor="end", color=t["accent"]))
    label = ("GenAI request flow in ai-service: 1 a user asks for laptops under 50,000 rupees; 2 the gateway validates the "
             "user's JWT; 3 ai-service sends the question with a system prompt through LangChain4j; 4 the LLM picks a tool, "
             "findProducts; 5 product-service is called with the caller's JWT; 6 the answer is grounded in live data. "
             "Status: wiring done, tools in progress.")
    return svg(w, h, label, "\n".join(out), MOTION_CSS)


# ------------------------------------------------------------------ delivery pipeline

PIPELINE = [  # (stage, command)
    ("Parent POM", "mvn -N install"),
    ("Starter", "mvn install"),
    ("Test", "mvn test"),
    ("Package", "mvn package"),
    ("Stop old", "SIGTERM → 15s"),
    ("Deploy jar", "java -jar"),
    ("Health gate", "actuator → UP"),
]


def build_pipeline(t):
    w, h = 880, 164
    n, bw, gap = len(PIPELINE), 108, 12.67
    css = MOTION_CSS + """
  .run { transform-box: fill-box; transform-origin: left center; animation: run 6s cubic-bezier(.4,0,.2,1) infinite; }
  @keyframes run { 0% { transform: scaleX(0); opacity: 1; } 80% { transform: scaleX(1); opacity: 1; } 100% { transform: scaleX(1); opacity: 0; } }
  @media (prefers-reduced-motion: reduce) { .run { animation: none !important; } }"""
    out = [f"<defs>{arrow_marker(t)}</defs>", frame_rect(t, w, h)]
    out.append(caption(t, 24, 30, "JENKINS · ONE PIPELINE PER SERVICE"))
    out.append(f'<text x="{w-24}" y="30" font-family="{SANS}" font-size="12" text-anchor="end" fill="{t["muted"]}">'
               'fails the build unless the new instance reports UP</text>')
    for i, (stage, cmd) in enumerate(PIPELINE):
        x = 24 + i * (bw + gap)
        last = i == n - 1
        stroke = t["green"] if last else t["border"]
        fits(stage, 12.5, bw - 20, W_SANS_B, stage)
        fits(cmd, 10, bw - 20, W_MONO, cmd)
        out.append(f'<rect x="{x:.1f}" y="46" width="{bw}" height="74" rx="6" fill="{t["surface"]}" stroke="{stroke}"/>'
                   f'<circle cx="{x+17:.1f}" cy="64" r="7" fill="none" stroke="{t["green"]}" stroke-width="1.4"/>'
                   f'<path d="M{x+13.5:.1f},64 l2.5,2.5 l4.5,-5" fill="none" stroke="{t["green"]}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
                   f'<text x="{x+bw-10:.1f}" y="68" font-family="{MONO}" font-size="10" text-anchor="end" fill="{t["subtle"]}">{i+1:02d}</text>'
                   f'<text x="{x+10:.1f}" y="91" font-family="{SANS}" font-size="12.5" font-weight="600" fill="{t["text"]}">{esc(stage)}</text>'
                   f'<text x="{x+10:.1f}" y="108" font-family="{MONO}" font-size="10" fill="{t["muted"]}">{esc(cmd)}</text>')
        if not last:
            out.append(f'<path d="M{x+bw+1:.1f},83 L{x+bw+gap-1:.1f},83" stroke="{t["subtle"]}" stroke-width="1.4" marker-end="url(#arr)"/>')
    out.append(f'<rect x="24" y="136" width="{w-48}" height="4" rx="2" fill="{t["surface"]}" stroke="{t["border"]}" stroke-width=".6"/>'
               f'<rect class="run" x="24" y="136" width="{w-48}" height="4" rx="2" fill="{t["green"]}"/>')
    label = ("Delivery pipeline, one Jenkins pipeline per service: install parent POM, install the shared starter, test, package, "
             "stop the old instance with SIGTERM, deploy the jar, then a health gate on /actuator/health that fails the build "
             "unless the new instance reports UP.")
    return svg(w, h, label, "\n".join(out), css)


# ------------------------------------------------------------------ principles

ICONS = {
    "shield": 'M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6l7-3z M9 12l2 2 4-4',
    "eye": 'M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z M12 9a3 3 0 1 1 0 6a3 3 0 1 1 0-6z',
    "cycle": 'M20 11a8 8 0 0 0-14.9-3 M5 3v5h5 M4 13a8 8 0 0 0 14.9 3 M19 21v-5h-5',
}
PRINCIPLES = [
    ("shield", "Design for failure", ["Circuit breakers, bulkheads and", "timeouts go in on day one, not", "after the first incident."]),
    ("eye", "Observability is part of done", ["If you can't see inside a service,", "it isn't finished. Logs, traces and", "health ship with the feature."]),
    ("cycle", "Automate the second time", ["CI/CD, provisioning and coverage", "gates. Manual steps are technical", "debt in a process costume."]),
]


def build_principles(t):
    w, h, cols = 880, 184, 3
    cw = w / cols
    out = [frame_rect(t, w, h)]
    for c in range(1, cols):
        out.append(f'<line x1="{c*cw:.1f}" y1="1" x2="{c*cw:.1f}" y2="{h-1}" stroke="{t["border"]}"/>')
    for i, (icon, title, lines) in enumerate(PRINCIPLES):
        x = i * cw + 26
        out.append(f'<rect x="{x:.1f}" y="24" width="40" height="40" rx="8" fill="{t["surface"]}" stroke="{t["border"]}"/>'
                   f'<path transform="translate({x+8:.1f},32)" d="{ICONS[icon]}" fill="none" stroke="{t["accent"]}" '
                   'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
        fits(title, 14, cw - 52, W_SANS_B, title)
        out.append(f'<text x="{x:.1f}" y="96" font-family="{SANS}" font-size="14" font-weight="600" fill="{t["text"]}">{esc(title)}</text>')
        for j, line in enumerate(lines):
            fits(line, 12.5, cw - 52, W_SANS, line)
            out.append(f'<text x="{x:.1f}" y="{122 + 18*j}" font-family="{SANS}" font-size="12.5" fill="{t["muted"]}">{esc(line)}</text>')
    label = "How I work: " + " ".join(f"{title}: {' '.join(lines)}" for _, title, lines in PRINCIPLES)
    return svg(w, h, label, "\n".join(out))


# ------------------------------------------------------------------ contact card

CONTACT = dict(
    title="Let’s build something that stays up.",
    line="Open to senior Java backend & cloud roles, including GenAI on the JVM.",
    status="Available",
    location="Hyderabad · Kolkata · Delhi · Remote",
    email="hayattarique3@gmail.com",
)


def build_contact(t):
    w, h = 880, 164
    css = """
  .live { animation: live 2.4s ease-in-out infinite; }
  @keyframes live { 0%,100% { opacity: .35; } 50% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) { .live { animation: none; } }"""
    c = CONTACT
    bw = len(c["email"]) * 14 * W_SANS_B + 60
    bx = w - 28 - bw
    fits(c["title"], 24, bx - 56, W_SANS_B, "contact title")
    fits(c["line"], 14, bx - 56, W_SANS, "contact line")
    out = [frame_rect(t, w, h)]
    out.append(f'<text x="28" y="56" font-family="{SANS}" font-size="24" font-weight="600" letter-spacing="-.3" fill="{t["text"]}">{esc(c["title"])}</text>')
    out.append(f'<text x="28" y="86" font-family="{SANS}" font-size="14" fill="{t["muted"]}">{esc(c["line"])}</text>')
    out.append(f'<circle class="live" cx="33" cy="121" r="4" fill="{t["green"]}"/>'
               f'<text x="45" y="125.5" font-family="{MONO}" font-size="12" fill="{t["text"]}">{esc(c["status"])}'
               f'<tspan fill="{t["subtle"]}">   /   </tspan><tspan fill="{t["muted"]}">{esc(c["location"])}</tspan></text>')
    out.append(f'<rect x="{bx:.0f}" y="{h/2-22:.0f}" width="{bw:.0f}" height="44" rx="8" fill="{t["btn"]}"/>'
               f'<text x="{bx+22:.0f}" y="{h/2+5:.0f}" font-family="{SANS}" font-size="14" font-weight="600" fill="#ffffff">{esc(c["email"])}  →</text>')
    label = f'{c["title"]} {c["line"]} {c["status"]}: {c["location"]}. Email {c["email"]}.'
    return svg(w, h, label, "\n".join(out), css)


# ------------------------------------------------------------------ main

def main():
    files = {}
    for mode, t in THEMES.items():
        files[f"hero-{mode}.svg"] = build_hero(t)
        files[f"impact-{mode}.svg"] = build_impact(t)
        for key, p in PROJECTS.items():
            files[f"projects/{key}-{mode}.svg"] = build_card(p, t)
        files[f"architecture-{mode}.svg"] = build_architecture(t)
        files[f"genai-flow-{mode}.svg"] = build_genai_flow(t)
        files[f"pipeline-{mode}.svg"] = build_pipeline(t)
        files[f"principles-{mode}.svg"] = build_principles(t)
        files[f"contact-{mode}.svg"] = build_contact(t)
    for rel, text in files.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path}")


if __name__ == "__main__":
    main()

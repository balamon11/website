from http.server import HTTPServer, BaseHTTPRequestHandler 
content = ''' <html><head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>My PC Specifications</title>
<style>
  :root{
    --bg: #f4f6f8;
    --card: #ffffff;
    --accent: #2b6cb0;
    --muted: #6b7280;
    --dash: rgba(43,108,176,0.25);
    --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Segoe UI Mono", monospace;
  }

  /* page */
  html,body{
    height:100%;
    margin:0;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    background: linear-gradient(180deg, var(--bg), #fff);
    display:flex;
    align-items:center;
    justify-content:center;
    padding:32px;
    color:#111827;
  }

  /* card */
  .spec-card{
    width:min(760px, 96%);
    background:var(--card);
    border-radius:14px;
    padding:28px;
    box-shadow: 0 8px 30px rgba(16,24,40,0.08);
    border: 1px solid rgba(16,24,40,0.04);
    position:relative;
    overflow:hidden;
  }

  /* big title */ 
  .spec-title{
    margin:0 0 12px 0;
    font-size:1.6rem;
    letter-spacing: -0.02em;
    display:flex;
    align-items:center;
    gap:16px;
  }

  /* dashed rule element (visually matches your hyphen line) */
  .dash-rule{
    flex:1;
    height:1px;
    background:
      repeating-linear-gradient(
        to right,
        var(--dash) 0 6px,
        transparent 6px 12px
      );
    border-radius:2px;
    align-self:center;
  }

  /* specs box */
  .spec-body{
    margin-top:18px;
    background: linear-gradient(180deg, rgba(43,108,176,0.02), transparent 30%);
    padding:18px;
    border-radius:10px;
    border:1px solid rgba(43,108,176,0.05);
  }

  /* definition-list layout for key: value */
  dl{
    display:grid;
    grid-template-columns: 220px 1fr;
    gap:12px 20px;
    align-items:center;
    margin:0;
    font-size:1rem;
  }

  dt{
    color:var(--muted);
    font-weight:600;
    font-family: var(--mono);
    letter-spacing:0.02em;
  }

  dd{
    margin:0;
    font-weight:700;
    font-family: var(--mono);
    color:#0f172a;
  }

  /* lower dashed rule */
  .dash-rule-bottom{
    margin:18px -28px 0 -28px;
    height:1px;
    background:
      repeating-linear-gradient(
        to right,
        var(--dash) 0 6px,
        transparent 6px 12px
      );
  }

  /* mobile adjustments */
  @media (max-width:520px){
    dl{ grid-template-columns: 1fr; }
    dt{ font-size:0.92rem; }
    dd{ font-size:1rem; }
    .spec-title{ font-size:1.25rem; gap:10px; }
  }
</style>
</head>
<body>

  <article class="spec-card" aria-labelledby="pc-title">
    <header style="display:flex;align-items:center;gap:12px;">
      <h1 id="pc-title" class="spec-title">My Pc Specifications
        <span class="dash-rule" aria-hidden="true"></span>
      </h1>
    </header>

    <section class="spec-body" aria-label="PC specifications">
      <dl>
        <dt>Processor</dt><dd>Intel(R) Core(TM) Ultra 5 125H</dd>
        <dt>Number of Cores</dt><dd>18</dd>
        <dt>Speed</dt><dd>4.5 GHz</dd>
        <dt>RAM</dt><dd>16 GB</dd>
        <dt>Video Card</dt><dd>Intel(R) Graphics</dd>
      </dl>

      <div class="dash-rule-bottom" aria-hidden="true"></div>
    </section>
  </article>

</body>
</html> '''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...") 
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('', 8000)
httpd=HTTPServer (server_address, MyServer)
httpd.serve_forever()
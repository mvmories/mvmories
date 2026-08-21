import base64, pathlib
D = '/Users/miguel.vilhena/workspace/portfolio/frontend_react/dist/assets/'
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
jak = b64(D + 'plus-jakarta-sans-latin-wght-normal-eXO_dkmS.woff2')
dm  = b64(D + 'dm-sans-latin-wght-normal-Xz1IZZA0.woff2')

THEMES = {
 'light': dict(surface='#f9fafc', text='#10121c', muted='#6c6e77', brand='#4555c8',
               w1='rgba(97,118,222,0.18)', w2='rgba(55,170,227,0.14)',
               particles='particles-light.svg'),
 'dark':  dict(surface='#10121c', text='#f1f2f6', muted='#aeb1ba', brand='#8398ee',
               w1='rgba(69,85,200,0.30)', w2='rgba(0,139,204,0.20)',
               particles='particles-dark.svg'),
}

TPL = """<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:Jak;src:url(data:font/woff2;base64,{jak}) format('woff2');font-weight:200 800}}
@font-face{{font-family:DM;src:url(data:font/woff2;base64,{dm}) format('woff2');font-weight:100 1000}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1000px;height:300px;overflow:hidden}}
.b{{position:relative;width:1000px;height:300px;background-color:{surface};
  background-image:radial-gradient(ellipse 80% 60% at 15% 0%,{w1},transparent 60%),
                   radial-gradient(ellipse 70% 70% at 88% 25%,{w2},transparent 65%);
  display:flex;align-items:center;overflow:hidden}}
.t{{padding:0 56px;max-width:640px;position:relative;z-index:2}}
.eyebrow{{font-family:ui-monospace,'SF Mono',Menlo,monospace;font-size:11px;
  letter-spacing:.16em;text-transform:uppercase;color:{brand};font-weight:500;margin-bottom:14px}}
h1{{font-family:Jak;font-weight:700;font-size:54px;line-height:1.05;
  letter-spacing:-.03em;color:{text}}}
p{{font-family:DM;font-weight:400;font-size:19px;line-height:1.5;color:{muted};margin-top:12px}}
.p{{position:absolute;right:44px;bottom:0;height:300px;z-index:1}}
.p img{{height:340px;display:block;margin-bottom:-40px}}
</style>
<div class="b">
  <div class="t">
    <div class="eyebrow">Frontend engineer &middot; Amsterdam</div>
    <h1>Miguel Vilhena</h1>
    <p>I take products from a blank page to 30 countries.</p>
  </div>
  <div class="p"><img src="{particles}"></div>
</div>"""

for name, t in THEMES.items():
    pathlib.Path(f'banner-{name}.html').write_text(TPL.format(jak=jak, dm=dm, **t))
    print('wrote', name)

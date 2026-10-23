"""Original Geography teaching SVGs, not survey maps or observed climate records."""
import json
import re

def expression(svg):
    """Render displayed {expressions} through the engine, preserving SVG coordinates."""
    parts=re.split(r'(\{[^{}]+\})',svg)
    return ' + '.join('fmt('+p[1:-1]+')' if p.startswith('{') else json.dumps(p,ensure_ascii=False) for p in parts if p)

def frame(body,height,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 {height}" role="img" aria-label="{title}" font-family="sans-serif" fill="#183428"><rect width="320" height="{height}" fill="#fffdf5"/>{body}</svg>'

def soil_profile():
    rows=[('O','organic litter','#503f2c'),('A','mineral topsoil','#806448'),('B','altered subsoil','#b88251'),('C','parent material','#d6bf91'),('R','hard bedrock','#b5b4ad')]
    b='<text x="12" y="20" font-size="13">Illustrative profile, not to scale</text>'
    for i,(label,desc,color) in enumerate(rows):
        y=34+i*42
        ink='white' if i<2 else '#183428'
        b+=f'<rect x="18" y="{y}" width="100" height="42" fill="{color}" stroke="#fefaf0"/><text x="65" y="{y+27}" text-anchor="middle" font-size="20" fill="{ink}">{label}</text><text x="132" y="{y+26}" font-size="13">{desc}</text>'
    b+='<text x="12" y="269" font-size="11">E may occur; not all soils have every layer.</text>'
    return frame(b,284,'Illustrative soil profile: O, A, B, C, R from surface downward')

def erosion_map(slopes,covers):
    b='<text x="10" y="19" font-size="13">Classroom plots: equal soil and rain</text><path d="M300 44V27l-4 7m4-7 4 7" stroke="#183428" fill="none"/><text x="296" y="58" font-size="11">N</text>'
    for i,(s,c) in enumerate(zip(slopes,covers)):
        x=12+(i%2)*151; y=70+(i//2)*96
        color='#eed4ac' if c=='bare' else '#d6e9cf'
        b+=f'<rect x="{x}" y="{y}" width="143" height="88" rx="5" fill="{color}" stroke="#49674d"/><text x="{x+10}" y="{y+22}" font-size="16">Plot {chr(65+i)}</text><text x="{x+10}" y="{y+44}" font-size="13">Slope: {{{s}}}°</text><text x="{x+10}" y="{y+65}" font-size="13">Cover: {c}</text>'
    b+='<text x="12" y="277" font-size="11">Sketch only; not a real farm or field plan.</text>'
    return frame(b,292,'Classroom erosion priority map with slope and cover for plots A to D')

def rain_chart(values):
    assert len(values)==12 and max(values)<=400
    b='<text x="8" y="18" font-size="12">Invented monthly rainfall (mm)</text>'
    for v in [0,100,200,300,400]:
        y=224-v*0.44
        b+=f'<path d="M34 {y}H315" stroke="#d8ddda"/><text x="29" y="{y+4}" text-anchor="end" font-size="9">{{{v}}}</text>'
    for i,v in enumerate(values):
        x=38+i*23; h=v*0.44
        b+=f'<rect x="{x}" y="{224-h}" width="16" height="{h}" fill="#448d98"/><text x="{x+8}" y="{219-h}" text-anchor="middle" font-size="10">{{{v}}}</text><text x="{x+8}" y="241" text-anchor="middle" font-size="10">{list("JFMAMJJASOND")[i]}</text>'
    b+='<text x="8" y="263" font-size="10">Jan to Dec; model data, not a town record.</text>'
    return frame(b,278,'Invented monthly rainfall chart, January to December, millimetres')

def drainage():
    b='<text x="10" y="20" font-size="13">Cameroon drainage connections</text><text x="10" y="38" font-size="11">Schematic, not a river course map</text>'
    for i,(river,dest) in enumerate([('Sanaga / Nyong','Atlantic Ocean'),('Benue','Niger → Atlantic'),('Dja / Sangha','Congo → Atlantic'),('Logone / Chari','Lake Chad basin')]):
        y=67+i*49
        b+=f'<rect x="8" y="{y-17}" width="116" height="33" rx="4" fill="#e0e9d2"/><text x="66" y="{y+4}" font-size="12" text-anchor="middle">{river}</text><path d="M128 {y}h28l-6-4m6 4-6 4" stroke="#28758c" fill="none"/><text x="165" y="{y+4}" font-size="12">{dest}</text>'
    return frame(b,250,'Schematic Cameroon river systems and downstream destinations')

"""Original schematic learning maps. No survey, navigation or live route data."""
import json
import re

def expression(svg):
    parts=re.split(r'(\{[^{}]+\})',svg)
    return ' + '.join('fmt('+p[1:-1]+')' if p.startswith('{') else json.dumps(p,ensure_ascii=False) for p in parts if p)

def frame(body,height,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 {height}" role="img" aria-label="{label}"><rect width="320" height="{height}" fill="#f5f5eb"/><g font-family="sans-serif" fill="#193a2a">{body}</g></svg>'

def location_triangle(weighted=False):
    a='A input: {a} t' if weighted else 'Material A / Site A'
    b='B input: {b} t' if weighted else 'Material B / Site B'
    m='Output: {p} t / Site M' if weighted else 'Market / Site M'
    d='{d}' if weighted else '{20}'
    body='<text x="160" y="19" text-anchor="middle" font-size="14">Invented candidate triangle</text>'
    body+='<path d="M40 65H280L160 230Z" stroke="#48725a" stroke-width="2" fill="none"/>'
    for x,y,label in [(40,65,'A'),(280,65,'B'),(160,230,'M')]:
        body+=f'<circle cx="{x}" cy="{y}" r="12" fill="white" stroke="#356"/><text x="{x}" y="{y+5}" text-anchor="middle" font-size="15">{label}</text>'
    body+=f'<g font-size="13" text-anchor="middle"><text x="82" y="44">{a}</text><text x="238" y="44">{b}</text><text x="160" y="260">{m}</text><text x="160" y="127">Each link: {d} km</text><text x="160" y="153">Only A, B, M are candidates</text><text x="160" y="282">Schematic - not to scale</text></g>'
    return frame(body,295,'Invented Weber candidate location triangle, not a continuous optimum diagram')

def landuse_map(plots):
    body='<text x="160" y="20" text-anchor="middle" font-size="14">Invented land-use site map</text><path d="M8 170H312" stroke="#555" stroke-width="5"/><text x="160" y="160" text-anchor="middle" font-size="12">Main road</text>'
    for i,p in enumerate(plots):
        x=12+(i%2)*158;y=36+(i//2)*160
        color='#c5e1f2' if p['flood'] else '#f4deb0' if p['reserve'] else '#d9e8ce'
        flood='yes' if p['flood'] else 'no';road='yes' if p['road'] else 'no';land='school reserve' if p['reserve'] else 'available'
        body+=f'<rect x="{x}" y="{y}" width="145" height="116" fill="{color}" stroke="#547466"/><g font-size="13"><text x="{x+8}" y="{y+20}">Plot {p["name"]}</text><text x="{x+8}" y="{y+44}">Land: {land}</text><text x="{x+8}" y="{y+68}">Flood: {flood}</text><text x="{x+8}" y="{y+92}">Road: {road}</text></g>'
        if p['road']:
            end=y+116 if i<2 else y
            body+=f'<path d="M{x+72} {end}V170" stroke="#555" stroke-width="3"/>'
    body+='<g font-size="12"><text x="12" y="337">Blue: flood zone. Gold: school reserve.</text><text x="12" y="358">Classroom rules only - not a real permit.</text></g>'
    return frame(body,370,'Invented land-use decision map with plot status and road access')

def route_map(dynamic=True):
    ab='{ab}' if dynamic else '{10}';bd='{bd}' if dynamic else '{15}';ac='{ac}' if dynamic else '{20}';cd='{cd}' if dynamic else '{15}'
    blocked='{X.block}' if dynamic else 'none'
    body='<text x="160" y="20" text-anchor="middle" font-size="14">Invented communication network</text><path d="M35 70H280M35 70V220" stroke="#497257" stroke-width="3" fill="none"/><path d="M280 70V220M35 220H280" stroke="#497257" stroke-width="3" stroke-dasharray="8 5" fill="none"/>'
    for x,y,label in [(35,70,'A'),(280,70,'B'),(35,220,'C'),(280,220,'D')]:
        body+=f'<circle cx="{x}" cy="{y}" r="13" fill="white" stroke="#234"/><text x="{x}" y="{y+5}" text-anchor="middle" font-size="16">{label}</text>'
    body+=f'<g font-size="14" text-anchor="middle"><text x="160" y="57">AB: {ab} km</text><text x="160" y="248">CD: {cd} km</text><text x="17" y="145" transform="rotate(-90 17 145)">AC: {ac} km</text><text x="303" y="145" transform="rotate(90 303 145)">BD: {bd} km</text><text x="160" y="278">Solid: road. Dashed: rail.</text><text x="160" y="301">Closed link: {blocked}</text><text x="160" y="323">Transfers at nodes allowed. Not to scale.</text></g>'
    return frame(body,337,'Invented route network with link distances, modes and closure information')

def cameroon_links():
    body='<g font-size="13" text-anchor="middle"><text x="160" y="20">Selected Cameroon transport nodes</text><text x="160" y="39">Schematic - not a route guide</text></g><path d="M14 65V260" stroke="#85bccb" stroke-width="9"/><path d="M55 166L175 137L239 72" fill="none" stroke="#3b644d" stroke-width="3" stroke-dasharray="7 4"/><path d="M55 166L70 252" stroke="#777" stroke-width="3"/>'
    for x,y,label,tx,ty in [(239,72,'Ngaoundéré',235,58),(175,137,'Yaoundé',218,151),(55,166,'Douala',67,189),(70,252,'Kribi',108,261)]:
        body+=f'<circle cx="{x}" cy="{y}" r="6" fill="#315f42"/><text x="{tx}" y="{ty}" font-size="14" text-anchor="middle">{label}</text>'
    body+='<g font-size="12"><text x="130" y="212">Dashed: selected rail links</text><text x="130" y="236">Grey: selected road link</text><text x="20" y="291">Ports: Douala and Kribi; selected links only.</text></g>'
    return frame(body,308,'Selected Cameroon transport-node schematic distinguishing existing rail and road links')

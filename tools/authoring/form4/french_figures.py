"""Scènes scolaires originales en SVG, sans ressource extérieure."""
def scene(kind):
    start='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" role="img" aria-label="Scène scolaire inventée pour préparer une description orale" font-family="sans-serif" fill="#183428"><rect width="320" height="200" fill="#fffdf5"/><text x="12" y="22" font-size="13">Scène scolaire inventée</text>'
    if kind=='file':
        body='<rect x="245" y="50" width="55" height="120" fill="#dbc8a3" stroke="#183428"/><text x="250" y="42" font-size="12">Entrée</text>'
        for x in [50,115,180]: body+=f'<circle cx="{x}" cy="90" r="13" fill="#447d68"/><path d="M{x} 104v34m0-20-16 13m16-13 16 13m-16 7-12 28m12-28 12 28" fill="none" stroke="#183428" stroke-width="4"/>'
    elif kind=='silence':
        body='<text x="70" y="50" font-size="15">Bibliothèque</text><path d="M40 85q50-20 100 0v80q-50-20-100 0zm100 0q50-20 100 0v80q-50-20-100 0z" fill="#e0e9d2" stroke="#183428"/><path d="M210 65h76v45h-42l-15 12v-12h-19z" fill="white" stroke="#183428"/><path d="M220 78h55m-55 12h42" stroke="#183428"/><path d="M205 117l85-60" stroke="#a34732" stroke-width="7"/>'
    elif kind=='tri':
        body='<rect x="38" y="77" width="104" height="95" fill="#e0e9d2" stroke="#183428"/><rect x="178" y="77" width="104" height="95" fill="#e0e9d2" stroke="#183428"/><text x="62" y="108" font-size="14">Papier</text><text x="195" y="108" font-size="14">Autres</text><path d="M51 60h75v10H51zm140 0h75v10h-75z" fill="#447d68"/><path d="M90 35v16m-5-5 5 5 5-5" stroke="#183428" fill="none"/>'
    else:
        body='<text x="30" y="48" font-size="15">Après le lavage des mains</text><path d="M80 90h75v25h45v25h-65v-25H80z" fill="#b4c8cc" stroke="#183428"/><path d="M145 90V70m-20 0h40" stroke="#183428" stroke-width="5"/><path d="M188 148q-14 19 0 23q14-4 0-23z" fill="#4c8eac"/><path d="M225 72l-29-12 7 9-7 6z" fill="#a34732"/><text x="230" y="98" font-size="12">Fermer</text>'
    return start+body+'<text x="12" y="190" font-size="11">Modèle de classe, sans enregistrement sonore.</text></svg>'

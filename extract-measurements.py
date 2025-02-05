# menuTitle: extract parametric blends from Amstelvar1 extrema

import os, glob, json
from xTools4.modules.measurements import FontMeasurements, permille

subFamilyName    = ['Roman', 'Italic'][0]
baseFolder       = os.getcwd()
sourcesFolder    = os.path.join(baseFolder, subFamilyName)
# instancesFolder  = os.path.join(sourcesFolder, 'instances')
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')
blendsPath       = os.path.join(sourcesFolder, 'blends.json')

parametricAxesRoman  = 'XOUC XOLC XOFI YOUC YOLC YOFI XTUC XTLC XTFI YTUC YTLC YTAS YTDE YTFI XSHU YSHU XSVU YSVU XSHL YSHL XSVL YSVL XSHF YSHF XSVF YSVF XTTW YTTL YTOS XUCS WDSP XDOT'.split() # XVAU YHAU XVAL YHAL XVAF YHAF XTEQ YTEQ
parametricAxesItalic = 'XOUC XOLC XOFI YOUC YOLC YOFI XTUC XTLC XTFI YTUC YTLC YTAS YTDE YTFI XSHU YSHU XSVU YSVU XSHL YSHL XSVL YSVL XSHF YSHF XSVF YSVF XTTW YTTL YTOS XUCS WDSP XDOT'.split() # XVAU YHAU XVAL YHAL XVAF YHAF XTEQ YTEQ

parametricAxes = parametricAxesRoman if subFamilyName == 'Roman' else parametricAxesItalic

assert os.path.exists(sourcesFolder)
assert os.path.exists(measurementsPath)

# define blended axes

axes = {
    "opsz" : {
      "name"    : "Optical size",
      "default" : 14,
      "min"     : 8,
      "max"     : 144,
    },
    "wght" : {
      "name"    : "Weight",
      "default" : 400,
      "min"     : 100,
      "max"     : 1000,
    },
    "wdth": {
      "name"    : "Width",
      "default" : 100,
      "min"     : 50,
      "max"     : 125,
    }
}
# axes = _axes[subFamilyName]

# extract measurements from Amstelvar1 instances

ufos = [f for f in glob.glob(f'{sourcesFolder}/*.ufo') if 'GRAD' not in f]

sources = {}
for ufoPath in sorted(ufos):
    fontName = os.path.splitext(os.path.split(ufoPath)[-1])[0]
    styleName = '_'.join(fontName.split('_')[1:])
    f = OpenFont(ufoPath, showInterface=False)
    M = FontMeasurements()
    M.read(measurementsPath)
    M.measure(f)
    sources[styleName] = { k: permille(v, 2000) for k, v in M.values.items() if k in parametricAxes }

# save measurements to JSON blends file

blendsDict = {
    'axes'    : axes,
    'sources' : sources,
}

with open(blendsPath, 'w', encoding='utf-8') as f:
    json.dump(blendsDict, f, indent=2)

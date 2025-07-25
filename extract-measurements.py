# menuTitle: extract parametric blends from Amstelvar1 extrema

import os, glob, json
from xTools4.modules.measurements import FontMeasurements, permille

subFamilyName    = ['Roman', 'Italic'][0]
baseFolder       = os.getcwd()
sourcesFolder    = os.path.join(baseFolder, subFamilyName)
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')
blendsPath       = os.path.join(sourcesFolder, 'blends.json')

parametricAxesRoman  = 'XOUC XOLC XOFI YOUC YOLC YOFI XTUC XTUR XTUD XTUA XTLC XTLR XTLD XTLA XTFI YTUC YTLC YTAS YTDE YTFI XSHU YSHU XSVU YSVU XSHL YSHL XSVL YSVL XSHF YSHF XSVF YSVF XVAU YHAU XVAL YHAL XVAF YHAF XTTW YTTL YTOS XUCS XUCR XUCD XLCS XLCR XLCD XFIR WDSP XDOT XQUC XQLC XQFI YQUC YQLC YQFI'.split() # XTAB BARS 
parametricAxesItalic = parametricAxesRoman

parametricAxes = parametricAxesRoman if subFamilyName == 'Roman' else parametricAxesItalic

assert os.path.exists(sourcesFolder)
assert os.path.exists(measurementsPath)

# define blended axes

axes = {
    "opsz" : {
      "name"    : "Optical size",
      "default" : 14,
      "minimum" : 8,
      "maximum" : 144,
    },
    "wght" : {
      "name"    : "Weight",
      "default" : 400,
      "minimum" : 100,
      "maximum" : 1000,
    },
    "wdth": {
      "name"    : "Width",
      "default" : 100,
      "minimum" : 50,
      "maximum" : 125,
    }
}

# extract measurements from Amstelvar1 instances

ufos = [f for f in glob.glob(f'{sourcesFolder}/*.ufo') if 'GRAD' not in f]

print(f'extracting measurements from {subFamilyName} sources...')

sources = {}
for ufoPath in sorted(ufos):
    fontName = os.path.splitext(os.path.split(ufoPath)[-1])[0]
    styleName = '_'.join(fontName.split('_')[1:])
    f = OpenFont(ufoPath, showInterface=False)
    print(f'\t{fontName}')
    M = FontMeasurements()
    M.read(measurementsPath)
    M.measure(f)
    sources[styleName] = { k: permille(v, f.info.unitsPerEm) for k, v in M.values.items() if k in parametricAxes }

print()

# save measurements to JSON blends file

blendsDict = {
    'axes'    : axes,
    'sources' : sources,
}

print('saving measurements data to blends.json...\n')

with open(blendsPath, 'w', encoding='utf-8') as f:
    json.dump(blendsDict, f, indent=2)

print('...done!\n')

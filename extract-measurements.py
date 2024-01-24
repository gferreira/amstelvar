# menuTitle: extract parametric blends from Amstelvar1 extrema

import os, glob, json
from variableValues.measurements import FontMeasurements, permille

subfamilyName    = ['Roman', 'Italic'][0]
baseFolder       = os.getcwd()
sourcesFolder    = os.path.join(baseFolder, subfamilyName)
instancesFolder  = os.path.join(sourcesFolder, 'instances')
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')
blendsPath       = os.path.join(sourcesFolder, 'blends.json')
parametricAxes   = 'XOPQ XTRA YOPQ YTUC YTLC YTAS YTDE YTFI XSHU YSHU XSVU YSVU XSHL YSHL XSVL YSVL XSHF YSHF XSVF YSVF XTTW YTTL YTOS XUCS'.split()

assert os.path.exists(sourcesFolder)
assert os.path.exists(measurementsPath)

# define blended axes

axes = {
    "opsz": {
      "name"    : "Optical size",
      "default" : 14,
      "min"     : 8,
      "max"     : 144,
    },
    "wght": {
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

# extract measurements from Amstelvar1 instances

ufos = glob.glob(f'{instancesFolder}/*.ufo')

sources = {}
for ufoPath in sorted(ufos):
    fontName = os.path.splitext(os.path.split(ufoPath)[-1])[0]
    styleName = '_'.join(fontName.split('_')[1:])
    # # don't include the default
    # if styleName == 'wght400':
    #     continue
    # ignore GRAD sources
    # if 'GRAD' in styleName:
    #     continue
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

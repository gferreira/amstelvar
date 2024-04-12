Amstelvar
=========

fork of the original Amstelvar, with all unnecessary files removed and a few new ones added

this repository is used to produce the initial blend parameters for [AmstelvarA2](http://github.com/gferreira2/amstelvar-avar2)

Steps
-----

1. build a designspace with `opsz` `wght` `wdth` axes only

2. generate instances at AmstelvarA2 extrema locations (duovars, trivars, quadravars)
  - `opsz` 8-144
  - `wght` 200-800
  - `wdth` 85-125

3. measure the instances using the measurements defined in `measurements.json` and [VariableValues](http://github.com/gferreira/fb-variable-values)

4. save measurements into a `blends.json` file

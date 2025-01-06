Amstelvar
=========

A fork of the original Amstelvar used to produce the initial blend parameters for [AmstelvarA2], with all unnecessary files removed and a few new ones added.

[AmstelvarA2]: http://github.com/gferreira2/amstelvar-avar2

Steps
-----

1. Build a designspace with `opsz` `wght` `wdth` axes only.

2. Generate instances at AmstelvarA2 extrema (duovars, trivars, quadravars):
  - `opsz` 8-144
  - `wght` 200-800
  - `wdth` 85-125

3. Using the [Measurements tool], measure the instances using the measurements defined in the `measurements.json` file.

4. Save measurements into a `blends.json` file.

[Measurements tool]: http://gferreira.github.io/xTools4/reference/tools/variable/measurements/

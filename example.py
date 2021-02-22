#! /usr/bin/env python3

import os
from Spectra.Spectra_3 import Spectra

sp_file = os.path.join("Data", "Wire.spc")

sp = Spectra(sp_file)

sp.show_spectra()

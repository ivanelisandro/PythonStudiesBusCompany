spin = input()
charge = input()
particles_charges = {
    '-1/3': 'Strange Quark',
    '2/3': 'Charm Quark',
    '-1': 'Electron Lepton',
    '0': 'Neutrino Lepton',
}

if spin == "1/2":
    print(f"{particles_charges[charge]}")
elif spin == "1":
    print("Photon Boson")

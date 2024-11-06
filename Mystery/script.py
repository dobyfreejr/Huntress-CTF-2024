from enigma.machine import EnigmaMachine

# Set up the Enigma machine with provided settings
machine = EnigmaMachine.from_key_sheet(
    rotors='VI I III',
    reflector='B',
    ring_settings=[1, 1, 1],  # Ring settings are given as A, which translates to 1
    initial_positions='AQL',
    plugboard_settings='BQ CR DI EJ KW MT OS PX UZ GH'
)

# The given ciphertext
ciphertext = "rkenr wozec gtrfl obbur bfgma fkgyq ctkvq zeucz hlvwx yyzat zbvns kgyyd sthmi vsifc ovexl zzdqv slyir nwqoj igxuu kdqgr fdbbd njppc mujyy wwcoy"

# Remove spaces from the ciphertext for the Enigma input
ciphertext = ciphertext.replace(" ", "")

# Decrypt the message
plaintext = machine.process_text(ciphertext)
print("Decrypted Message:", plaintext)

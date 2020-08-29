# BSD-3 Clause:
# Copyright 2020 Erwin Kooi
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This program generates codebooks for the Enigma-E emulator in *M4* mode
# https://www.cryptomuseum.com/kits/enigma/

import calendar
import random

year = 2020

# Generate random reflector settings (Umkehrwalze)
# There are two reflectors, B and C
def fnReflectorSetting():
    returnstring = ""
    reflectorList = random.sample('BC', 1)
    returnstring += "{} ".format(reflectorList[0])
    return returnstring

# Generate random rotor settings (Walzenlage)
# There are four rotors, one a/b and three 1 - 8
def fnRotorSetting():
    returnstring = ""
    rotorList = random.sample(range(1,6), 3)
    for i in range (len(rotorList)):
        returnstring += "{} ".format(rotorList[i])
    return returnstring

# Generate random internal ring settings (Ringstellung)
# Each ring can be shifted internally by a - z amount.
def fnRingSetting():
    returnstring = ""
    ringList = random.sample(range(65, 91), 3)
    for i in range (len(ringList)):
        returnstring += "{} ".format(chr(ringList[i]))
    return returnstring

# Generate random plugboard settings (Steckerverbindungen)
# Each letter maps to another letter. Letters can occur only once.
def fnPlugboardSetting():
    success = 0
    while success == 0:
        plugboardListCharL = random.sample(range(65,91), 10)
        plugboardListCharR = random.sample(range(65,91), 10)
        success = 1
        for i in range (len(plugboardListCharL)):
            for j in range (len(plugboardListCharR)):
                if plugboardListCharL[i] == plugboardListCharR[j]:
                    success = 0
    returnstring = ""
    for i in range (len(plugboardListCharL)):
        returnstring += "{}{} ".format(chr(plugboardListCharL[i]), chr(plugboardListCharR[i]))
    return returnstring

# Generate random indicator groups (Kenngruppen)
# Four three-letter groups indicating the used key.
def fnIndicatorGroup():
    returnstring = ""
    indicatorGroup = ["","","",""]
    for i in range(0, 4):
        indicatorGroup = random.sample(range(65,91), 3)
        for j in range(0, 3):
            returnstring += "{}".format(chr(indicatorGroup[j]))
        returnstring += " "
    return returnstring

# Generate key sheet per monthrandom
for month in range(1, 13):
    print("+-----------------------------------------------------------------------------------------+")
    print("| Enigma-E Key sheet for *M3* emulation                                                   |")
    print("+----------+-------------+--------------+-------------------------------+-----------------+")
    print("| Date     | Wheel order | Ring setting | Plugboard setting             | Indicator group |")
    for day in range(1, (calendar.monthrange(year, month)[1] + 1)):
        print("+----------+-------------+--------------+-------------------------------+-----------------+")
        print("| %04d%02d%02d | %s    %s|        %s| %s| %s|" %(year, month, day, fnReflectorSetting(), fnRotorSetting(), fnRingSetting(), fnPlugboardSetting(), fnIndicatorGroup()))
    print("+----------+-------------+--------------+-------------------------------+-----------------+")
    print("")

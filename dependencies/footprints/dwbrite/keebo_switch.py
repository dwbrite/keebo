import os

baseName = "KeeboHR"

def MX_CENTER_THRUHOLE(padType="np_thru_hole"): return '  # MX/Alps center mounting hole\n  (pad "" '+padType+' circle (at 0 0) (size 4 4) (drill 4) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n'
def MX_SIDE_THRUHOLES(padType="np_thru_hole"): return '  # MX/Alps side mounting holes\n  (pad "" '+padType+' circle (at -5.08 0) (size 1.7 1.7) (drill 1.7) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n  (pad "" '+padType+' circle (at 5.08 0) (size 1.7 1.7) (drill 1.7) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n'

def LP_CENTER_THRUHOLE(padType="np_thru_hole"): return '  # LP center mounting hole\n  (pad "" '+padType+' circle (at 0 0) (size 3.4 3.4) (drill 3.4) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n'
def LP_SIDE_THRUHOLES(padType="np_thru_hole"): return '  # LP side mounting holes\n  (pad "" '+padType+' circle (at -5.5 0) (size 1.7 1.7) (drill 1.7) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n  (pad "" '+padType+' circle (at 5.5 0) (size 1.7 1.7) (drill 1.7) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n'

def MX_PINS(padType="thru_hole"): return '  # Cherry MX pin thru-holes\n  (pad 1 '+padType+' circle (at 3.81 2.54) (size 2.5 2.5) (drill 1.5) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n  (pad 2 '+padType+' circle (at -2.54 5.08) (size 2.5 2.5) (drill 1.5) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n'
def MX_SOLDERLESS(): return '    # Solderless mount\n    (pad 1 smd rect (at 5.334 2.54) (size 2 1) (drill 1.5) (layers B.Cu B.Mask))\n    (pad 2 smd rect (at -4.064 5.08) (size 2 1) (drill 1.5) (layers B.Cu B.Mask))\n'

def LP_PINS(padType="thru_hole"): return '  #Kailh LP pins\n  (pad 1 '+padType+' circle (at 0 5.9) (size 2 2) (drill 1.2) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n  (pad 2 '+padType+' circle (at -5 3.8) (size 2 2) (drill 1.2) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n'
def LP_SOLDERLESS(): return '    # Solderless mount\n    (pad 1 smd rect (at 1.25 5.9) (size 2 1) (drill 1.2) (layers B.Cu B.Mask))\n    (pad 2 smd rect (at -6.25 3.8) (size 2 1) (drill 1.2) (layers B.Cu B.Mask))\n'

def ALPS_PINS(padType="thru_hole"): return '  # Matias Alps pin thru-holes\n  (pad 1 '+padType+' circle (at 2.5 3.683) (size 2.5 2.5) (drill 1.5) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n  (pad 2 '+padType+' circle (at -2.5 4) (size 2.5 2.5) (drill 1.5) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n\n'

def LED(padType="smd"): return '  # LED\n  (pad 3 smd circle (at 1.27 -5.08) (size 1.7 1.7) (drill 1) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n  (pad 4 smd rect (at -1.27 -5.08) (size 1.7 1.524) (drill 1) (layers ' + ((("B.Cu") if padType=="smd" else "*.Cu") + ' ' + (("B.Mask") if padType=="smd" else "*.Mask")) + '))\n'

def MODEL(switch):
	if switch.mx:
		return '  # 3D model\n  (model /home/dwbrite/code/keebo/dependencies/packages3d/switch_mx.packages3d/cherry_mx_blue_plate.wrl\n    (at (xyz 0 0 -0.069))\n    (scale (xyz 1 1 1))\n    (rotate (xyz 0 180 0))\n  )\n'
	else: return '  # No 3D model available\n'

def unitsToMm( units ):
	# Shaves 5 mils off for clearance between keycaps
	return ((units*375)-5)*0.0254

def getName(switch):
	size = '{:<03}'.format(str(switch.keycap).replace(".", "")) if switch.keycap else ""
	return baseName + '_' + size + '_' + switch.getTypeAsStr()

def genLine(start, end, layer, width):
	line = "  (fp_line "
	line += "(start " + str(start[0]) + " " + str(start[1]) + ") "
	line += "(end " + str(end[0]) + " " + str(end[1]) + ") "
	line += "(layer " + layer + ") "
	line += "(width " + width + "))\n"
	return line

def genRect(x, y, comment, layer, width):
	outline = "  # " + comment + "\n"
	coords = [ (-x, -y), ( x, -y), ( x,  y), (-x,  y) ]
	for i in range(0, 4):
		n = (i+1)%4
		outline += genLine(coords[i], coords[n], layer, str(width))
	return outline

def genSwOutline():
	dist = 300*0.0254
	comment = "Switch outline"
	return genRect(dist, dist, comment, "Dwgs.User", 0.3) + "\n"

def genKeycapOutline(keycap):
	x = unitsToMm(keycap)
	y = unitsToMm(1)
	comment = "Keycap outline"
	return genRect(x, y, comment, "Dwgs.User", 0.1524) + "\n"

def genStart(switch, ref, val):	return '(module '+getName(switch)+' (layer B.Cu) (tedit 0)\n  (tags switch)\n  (fp_text reference "'+ref+'" (at 0 -8.382) (layer Dwgs.User)\n    (effects (font (size 1.016 1.27) (thickness 0.1778)))\n  )\n  (fp_text value '+val+' (at 0 8.636) (layer B.SilkS) hide\n    (effects (font (size 1.27 1.524) (thickness 0.2032)))\n  )\n\n'

def genBody(switch):
	body = ""

	body += genSwOutline()
	body += genKeycapOutline(switch.keycap) if switch.keycap else ""

	if switch.mx or switch.alps:
		if not switch.lp:
			body += MX_SIDE_THRUHOLES(switch.padType) if switch.padType else MX_SIDE_THRUHOLES()
			body += "\n"
		body += MX_CENTER_THRUHOLE(switch.padType) if switch.padType else MX_CENTER_THRUHOLE()
		body += "\n"
	if switch.lp:
		body += LP_SIDE_THRUHOLES(switch.padType) if switch.padType else LP_SIDE_THRUHOLES()
		body += "\n"
		if not (switch.mx or switch.alps):
			body += LP_CENTER_THRUHOLE(switch.padType) if switch.padType else LP_CENTER_THRUHOLE()
			body +="\n"

	if switch.mx:
		body += MX_PINS(switch.padType) if switch.padType else MX_PINS()
		if switch.solderless: body += MX_SOLDERLESS()
		body += "\n"
	if switch.lp:
		body += LP_PINS(switch.padType) if switch.padType else LP_PINS()
		if switch.solderless: body += LP_SOLDERLESS()
		body += "\n"
	if switch.alps:
		body += ALPS_PINS(switch.padType) if switch.padType else ALPS_PINS()

	if switch.useModel:
		body += MODEL(switch)
	return body

def genEnd(): return ')\n# Generated by Devin Brite (dwbrite)\n'

def genSwFootprint(switch):
	doc = genStart(switch, "Keebo Custom", "SW")
	doc += genBody(switch)
	doc += genEnd()
	return doc

class Keyswitch:
	def getStrTypes():
		return {
                        1: 'MX',
                        2: 'LP',
                        3: 'MX_LP',
                        4: 'ALPS',
                        5: 'MX_ALPS',
                        6: 'LP_ALPS',
                        7: 'MX_LP_ALPS'
                }

	def __init__(self, keycap = False, solderless = False, mx = True, lp=False, alps=False, padType=False, useModel=True):
		self.keycap = keycap
		self.solderless = solderless
		self.switchType = 0
		self.setType(mx, lp, alps)
		self.mx = mx
		self.lp = lp
		self.alps = alps
		self.padType = padType
		self.useModel = useModel

	def setType(self, mx, lp, alps):
		self.switchType = 0
		self.mx = mx
		self.lp = lp
		self.alps = alps
		if mx: self.switchType += 1
		if lp: self.switchType += 2
		if alps: self.switchType += 4

	def setTypeViaStr(self, strType):
		mx = False
		lp = False
		alps = False
		if 'MX' in strType: mx = True
		if 'LP' in strType: lp = True
		if 'ALPS' in strType: alps = True
		self.setType(mx, lp, alps)

	def getTypeAsStr(self):
		return Keyswitch.getStrTypes().get(self.switchType, None)


def writeFootprint(switch):
	directory = ((switch.padType + "/") if switch.padType else "") + switch.getTypeAsStr() + ".pretty/"
	if not os.path.exists(directory):
		os.makedirs(directory)

	filename = getName(switch) + ".kicad_mod"
	f = open(directory + filename, 'w')
	f.write(genSwFootprint(switch))
	print(directory + filename)

# May the Lord forgive me for the sins I have made, and may He strike down the serpent who brought life to this unholy beast.
for keySize in range(100, 750, 25):
	for switchType in range(1, 8):
		switch = Keyswitch(keySize/100, True)
		switch.setTypeViaStr(Keyswitch.getStrTypes()[switchType])
		writeFootprint(switch)
		switch.padType = "smd"
		writeFootprint(switch)

# find best dpi and sensitivity to convert csgo sensitivity to valorant
# the program will find closest match of dpi and ingame sensitity with constraint stated below

# constraint
# with logitech g304, dpi can be adjusted in increment of 50, from 0 to 12000
# but we will pick 1000 as dpi starting point, as mouse movement can be jerky below that point
# for valorant, in game sensitivy can be adjusted to 3 digits behind decimal place


# mouse constraint
DPI_STEP = 50
DPI_MIN = 1000
DPI_MAX = 12000

GAME_SENS_PRECISION = 3
TARGET_TO_SRC_SENS_RATIO = 1 / 3.3735

# effective DPI (eDPI) is game sensitivity * dpi
SRC_EDPI = 1000 # source game = csgo

# calculate valorant sensitivity
def sens(dpi):
	return SRC_EDPI * TARGET_TO_SRC_SENS_RATIO / dpi

"""Count the difference between actual sens and closest ingame adjustable sens at specific dpi"""
def diff_sens(dpi):
	return abs(sens(dpi) - round(sens(dpi), GAME_SENS_PRECISION))

"""Find dpi with minimum diff sens """
def find_best_dpi():
	best_dpi = min((dpi for dpi in range(DPI_MIN, DPI_MAX, DPI_STEP)), key=diff_sens)
	return best_dpi

def main():
	print("Best match")
	dpi = find_best_dpi()
	print("DPI: ", dpi)
	print("SENS: ", sens(dpi))

if __name__ == "__main__":
	main()

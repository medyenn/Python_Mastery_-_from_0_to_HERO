# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄.
# 		 ███████╗███╗   ██╗███╗   ██╗███████╗███████╗██╗    ██╗      .
# 		 ██╔════╝████╗  ██║████╗  ██║██╔════╝██╔════╝╚██╗  ██╔╝      .
# 		 █████╗  ██╔██╗ ██║██╔██╗ ██║█████╗  █████╗    ╚███╔╝        .
# 		 ██╔══╝  ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══╝   ██╔  ██╗       .
# 		 ███████╗██║ ╚████║██║ ╚████║███████╗███████╗██╔╝   ██╗      .
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄.
# ╔═════════════════════════════════════════════════════════════════╗.
# ║  ⚡ ENNEEX         ▸		AERO-DATA SYSTEMS ENGINEER		⚡     ║.
# ║  ⚡ Mohamed ENNIH  ▸			enneex0113@gmail.com		⚡     ║.
# ║  ⟡ File	 	: tuples.py		    								║.
# ║  ⟡ Created		: 2026-02-06	                                ║.
# ║  ⟡ Updated		: 2026-02-06	                                ║.
# ╚═════════════════════════════════════════════════════════════════╝.
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄.


# a tuple acts similarly to a list unless in a tuple we can not add, modify or\
# remove any element
# it's mostly used when we need a list with fixed values
# it's more efficient on scale of memory since we get only what we need for\
# the exact fixed values

def location():
    coordinates = (41.8838272094727, -87.6386642456055)
    # we can't do his : coordinates[0] = 2
    # Because tuples don't support assignments
    latitude, longitude = coordinates
    print(coordinates[0], "=", latitude)
    print(coordinates[1], "=", longitude)

/* ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ */
/*	 ███████╗███╗   ██╗███╗   ██╗███████╗███████╗██╗    ██╗            */
/*	 ██╔════╝████╗  ██║████╗  ██║██╔════╝██╔════╝╚██╗  ██╔╝            */
/*	 █████╗  ██╔██╗ ██║██╔██╗ ██║█████╗  █████╗    ╚███╔╝              */
/*	 ██╔══╝  ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══╝   ██╔  ██╗             */
/*	 ███████╗██║ ╚████║██║ ╚████║███████╗███████╗██╔╝   ██╗            */
/* ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ */
/* ╔═════════════════════════════════════════════════════════════════╗ */
/* ║  ⚡ ENNEEX         ▸		AERO-DATA SYSTEMS ENGINEER	⚡        ║ */
/* ║  ⚡ Mohamed ENNIH  ▸			enneex0113@gmail.com		⚡    ║ */
/* ║  ⟡ File		: revenues.py									 ║ */
/* ║  ⟡ Created	    : 2026-02-05	                                 ║ */
/* ║  ⟡ Updated	    : 2026-02-05	                                 ║ */
/* ╚═════════════════════════════════════════════════════════════════╝ */
/* ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ */



def revenues():
    job = input("What is your Job title: ").strip().title()
    match job:
        case "Data Analyst" | "IT Project Manager":
            print("Average Revenue : $100k per year")
        case "Data Engineer" | "DevOps Engineer" | "Software Developer":
            print("Average Revenue : $140k per year")
        case "Data Scientist" | "Ai Engineer" | "Enterprise Architect":
            print("Average Revenue : $220k per year")
        case _:
            print("I have no idea (>^o^<)")

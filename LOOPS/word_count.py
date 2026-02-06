/* ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ */
/*	 ███████╗███╗   ██╗███╗   ██╗███████╗███████╗██╗    ██╗            */
/*	 ██╔════╝████╗  ██║████╗  ██║██╔════╝██╔════╝╚██╗  ██╔╝            */
/*	 █████╗  ██╔██╗ ██║██╔██╗ ██║█████╗  █████╗    ╚███╔╝              */
/*	 ██╔══╝  ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══╝   ██╔  ██╗             */
/*	 ███████╗██║ ╚████║██║ ╚████║███████╗███████╗██╔╝   ██╗            */
/* ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ */
/* ╔═════════════════════════════════════════════════════════════════╗ */
/* ║  ⚡ ENNEEX         ▸		AERO-DATA SYSTEMS ENGINEER	    ⚡    ║ */
/* ║  ⚡ Mohamed ENNIH  ▸			enneex0113@gmail.com		⚡    ║ */
/* ║  ⟡ File		: word_count.py									 ║ */
/* ║  ⟡ Created	    : 2026-02-06	                                 ║ */
/* ║  ⟡ Updated	    : 2026-02-06	                                 ║ */
/* ╚═════════════════════════════════════════════════════════════════╝ */
/* ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ */



def main():
    word_count()


def word_count():
    text = "rain falls and rain nourishes the earth the earth grows as the \
        rain falls sunlight warms and sunlight guides the seeds the seeds \
        bloom where sunlight warms".split(" ")
    print(text)
    words = [word.lower() for word in text if len(word) > 3]
    counts = {word: words.count(word) for word in words}
    for item in counts:
        print(item, " : ", counts[item])


main()

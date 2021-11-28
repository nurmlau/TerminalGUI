import curses
from curses.textpad import Textbox, rectangle


def draw(scrn):



    scrn.clear()
    scrn.refresh()

    topic = "-"
    
    # Alustus ikkunan edelliselle koolle

    prevmaxy = scrn.getmaxyx()[0]
    prevmaxx = scrn.getmaxyx()[1]

    while True:
        

        scrn.refresh()


        
    # Kehyksen kulmat

        maxY = int(scrn.getmaxyx()[0] - 1)
        maxX = int(scrn.getmaxyx()[1] - 2)
        minY = int(scrn.getbegyx()[0]    )
        minX = int(scrn.getbegyx()[1] + 1)

    # Haetaan ikkunan keskipiste. Jos ei ole jaollinen kahdella, niin vähennetään 0.5

        topicCenter = maxX / 2

        if (maxX % 2) != 0:
            topicCenter -= 0.5

    # Piirretään kehys ja estetään mahdollinen virhe out of boundarystä
        try:
           rectangle(scrn, minY, minX, maxY, maxX)
           rectangle(scrn, minY + 2, minX + 1, maxY - 4, int(topicCenter))
           rectangle(scrn, minY + 2, int(topicCenter) + 1, maxY - 4, maxX - 1)
           rectangle(scrn, maxY - 4, minX + 1, maxY, maxX - 1)
    
    # Piiretään hienommat kulmat

           scrn.addstr(minY, minX, "+")
           scrn.addstr(minY, maxX, "+")
           scrn.addstr(maxY, minX, "+")
           scrn.addstr(maxY, maxX, "+")

        except Exception as e:
           pass

    # Otsikko

        
        curses.echo()
        scrn.addstr(maxY - 2, minX + 3, "# ")
        
        entry = scrn.getstr(maxY - 2, 6)

        if len(entry) > 0:
            topic = entry
            scrn.clear()
        

            
    # Haetaan Otsikon keskipiste offsettiä varten
        
        if ((len(topic) / 2) % 2) != 0:

            offset = len(topic) / 2 - 0.5
        
        else:

            offset = len(topic) / 2
        
        scrn.addstr(1, int(topicCenter - offset), topic)
        

        


        # Katsotaan onko ikkunan koko muuttunut. Jos koko muuttunut, niin clear ja refresh

        if prevmaxx != scrn.getmaxyx()[0] or prevmaxy != scrn.getmaxyx()[1]:
            curses.resizeterm(*scrn.getmaxyx())
            scrn.clear()
            scrn.refresh()
        
        # Ikkunan edellinen koko

        prevmaxx = scrn.getmaxyx()[0]
        prevmaxy = scrn.getmaxyx()[1]


def main():
    curses.wrapper(draw)

if __name__ == "__main__":
    main()
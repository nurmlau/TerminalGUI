import curses
from curses.textpad import Textbox, rectangle



def draw_menu(stdscr):

    stdscr.clear()
    stdscr.refresh()
    
    # Alustus ikkunan edelliselle koolle

    prevmaxy = stdscr.getmaxyx()[0]
    prevmaxx = stdscr.getmaxyx()[1]

    while True:

        stdscr.refresh()
        
    # Kehyksen kulmat

        maxY = int(stdscr.getmaxyx()[0] - 1)
        maxX = int(stdscr.getmaxyx()[1] - 2)
        minY = int(stdscr.getbegyx()[0])
        minX = int(stdscr.getbegyx()[1])

    # Piirretään kehys ja estetään mahdollinen virhe out of boundarystä
        try:
           rectangle(stdscr, minY, minX, maxY, maxX)

        except Exception as e:
            pass
    
    # Piiretään hienommat kulmat

        stdscr.addstr(minY, minX, "+")
        stdscr.addstr(minY, maxX, "+")
        stdscr.addstr(maxY, minY, "+")
        stdscr.addstr(maxY, maxX, "+")

    # Otsikko

        topic = "iiiiiiiiii"

    # Haetaan ikkunan keskipiste. Jos ei ole jaollinen kahdella, niin vähennetään 0.5

        topicCenter = maxX / 2

        if (topicCenter % 2) != 0:
            topicCenter -= 0.5

    # Haetaan Otsikon keskipiste offsettiä varten
        
        if ((len(topic) / 2) % 2) != 0:

            offset = len(topic) / 2 - 0.5
        
        else:

            offset = len(topic) / 2
        
        stdscr.addstr(1, int(topicCenter - offset), topic)


        # Katsotaan onko ikkunan koko muuttunut. Jos koko muuttunut, niin clear ja refresh

        if prevmaxx != stdscr.getmaxyx()[0] or prevmaxy != stdscr.getmaxyx()[1]:
            curses.resizeterm(*stdscr.getmaxyx())
            stdscr.clear()
            stdscr.refresh()
        
        # Ikkunan edellinen koko

        prevmaxx = stdscr.getmaxyx()[0]
        prevmaxy = stdscr.getmaxyx()[1]


def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
from peli.netti_peli import main as run
"""Kutsuu pelin netti version ratkojalle
"""


def main():
    """Kutsuu pelin
    """

    kerrat = int(input("Montako kertaa haluat ajaa ratkojan?\n"))
    for i in range(kerrat):
        run()

if __name__ == "__main__":
    main()

"""Kutsuu pelin ratkoja version komentorivillä
"""

from peli.peli import main_ratkoja as run


def main():
    """Kutsuu pelin
    """

    taulukko = run()

    for i in taulukko:
        print(i)


if __name__ == "__main__":
    main()

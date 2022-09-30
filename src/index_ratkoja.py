from peli.peli import main_ratkoja as run
"""Kutsuu pelin ratkoja version
"""


def main():
    """Kutsuu pelin
    """

    taulukko = run()

    for i in taulukko:
        print(i)


if __name__ == "__main__":
    main()

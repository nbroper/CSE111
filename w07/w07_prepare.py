def main():
    fabrics = []

    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")

    fabrics.insert(0, "chiffon")
    print(fabrics)

    if "gingham" in fabrics:
        print("gingham is in the list.")
    else:
        print("gingham is NOT in the list.")

    i = fabrics.index("velvet")

    fabrics[i] = "taffeta"

    fabrics.pop()
    fabrics.remove("denim")


    n = len(fabrics)
    print(f"The fabrics list contains {n} elements. ")
    print(fabrics)


if __name__ == "__main__":
    main()
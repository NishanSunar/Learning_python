with open("CHAPTER_9/practiceset/poem.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("Thw word twinkle is present in the poem")
    else:
        print("The word twinkle is not present in the poem")
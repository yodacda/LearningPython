inputStr = "()"
mapping_data = {
    "(":")",
    "[":"]",
    "{":"}"
}
for ch in inputStr:
    if mapping_data.get(ch, "not available"):
        print("Parentheses Matching")



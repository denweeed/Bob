def bob(question: str):
    """

    :param question:
    :return:
    """
    if question.lower() == "bob":
        return "okay be soo"
    elif question.endswith("?") and question.isupper():
        return "relax, I know what I'm doing"
    elif question.endswith("?"):
        return "Of course"
    elif question.isupper():
        return "wow relax"
    else:
        return "wothewer"


if __name__ == '__main__':
    print(bob("BOB?"))

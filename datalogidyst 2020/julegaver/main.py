Anna, Laura, Oscar = list(map(int, input().split()))

def main():
    answer = []

    if Laura > Anna and Oscar > Anna:
        answer.append("Anna")

    if Anna > Laura:
        answer.append("Laura")

    if Anna > Oscar or Laura > Oscar:
        answer.append("Oscar")

    if len(answer) == 0:
        answer.append("INGEN")

    for line in answer:
        print(line)

main()

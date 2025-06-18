from runner import run


def main():
    result = run()
    print(result)

    relative_base_path = "./results"
    result_filename = f"{result.id}.txt"
    path = f"{relative_base_path}/{result_filename}"

    with open(path, "w") as file:
        file.write(result.value)


if __name__ == "__main__":
    main()

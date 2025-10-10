# Week3- Activity 1: Work with .txt file
# Using the attached text file, open, read, and write the complete information for the demo.txt.
# Share the GitHub link here(with adding the screenshot of the result).


class FileReaderWriter:

    def file_reader(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
            file.close()
            print(f"contents of the file is {content} ")

    def write_into_file(self, additional_file_content, file_path):
        with open(file_path, "a") as file:
            file.write(additional_file_content)
            file.close()


if __name__ == "__main__":
    file_path = "Week-3-Assignment/demo.txt"
    file_read_writer = FileReaderWriter()
    file_read_writer.file_reader(file_path)
    file_read_writer.write_into_file("Hey, this is MSE Assignment week 3", file_path)
    file_read_writer.file_reader(file_path)

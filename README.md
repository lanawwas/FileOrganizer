# Organize Resources

This Python script automates the creation of a directory structure for resources and updates an index/catalog of the contents.

## Purpose

The purpose of this script is to provide a convenient way to organize and manage resources such as articles, books, reports, tutorials, presentations, research papers, guidelines, tools, templates, references, meeting notes, and miscellaneous files.

## Directory Structure

The script creates the following directory structure within the main directory (`Resources` by default):

Resources/

    |-- Articles/
    |   |-- DataScience/
    |   |-- Management/
    |   |-- Technology/
    |   |-- Marketing/
    |
    |-- Books/
    |   |-- DataScience/
    |   |-- Management/
    |   |-- Technology/
    |
    |-- Reports/
    |   |-- Annual/
    |   |-- Quarterly/
    |   |-- ProjectSpecific/
    |
    |-- Tutorials/
    |   |-- R/
    |   |-- Python/
    |   |-- SQL/
    |
    |-- Presentations/
    |-- ResearchPapers/
    |-- Guidelines/
    |-- Tools/
    |-- Templates/
    |-- References/
    |-- MeetingNotes/
    |-- Miscellaneous/

## Usage

1. **Initial Setup:**
   - Replace `C:\Users\YourUsername\Documents\OrgResources` with your desired path in the script (`organize_resources.py`).
   - Install Python if not already installed.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `organize_resources.py`.
   - Run the script using:
     ```
     python organize_resources.py --create --update
     ```
     or specify only `--create` or `--update` as needed.

3. **Optional Arguments:**
   - `--create`: Create the directory structure.
   - `--update`: Update the index/catalog.

4. **Additional Notes:**
   - The script does not require any external packages beyond the Python standard library.
   - You can add more subdirectories or customize the directory structure as needed by modifying the `subdirs` list in the script.

## License

This project is licensed under the [MIT License](LICENSE).


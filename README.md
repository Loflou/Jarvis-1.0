
# Jarvis 1.0

Welcome to the Jarvis 1.0 repository!

## Purpose
This repository is dedicated to scripts and tools designed to automate repetitive tasks and enhance productivity. It serves as a central hub for various automation projects aimed at streamlining workflows and saving time.

## Structure
- **Scripts**: Contains individual scripts for specific automation tasks.
- **Tools**: Includes comprehensive tools and applications built for automation.
- **Documentation**: Provides detailed tocumentation on how to use and contribute to the repository.
- **Examples**: Showcases examples of automation in action.

## Getting Started
To get started, clone the repository and explore the available scripts and tools. Contributions are welcome! Feel free to submit pull requests or report issues.

## Contributions
If you'd like to contribute to this repository, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Submit a pull request with a detailed description of your changes.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

Happy automating!

## rename_files.py Usage

### Purpose
This script renames all files in a specified directory by adding a prefix.

### Usage
1. **Run the Script**:
   ```bash
   python rename_files.py
   ```
2. **Follow the Prompts**:
   - Enter the directory path: `test_directory`
   - Enter the prefix to add: `test_`

### Example
#### Before Running the Script
```
test_directory/
  file1.txt
  file2.txt
  file3.txt
```

#### After Running the Script
```
test_directory/
  test_file1.txt
  test_file2.txt
  test_file3.txt
```

### Common Errors and Solutions
- **Error**: Directory not found.
  - **Solution**: Ensure the directory path is correct.
- **Error**: Permission denied.
  - **Solution**: Ensure you have the necessary permissions to rename files in the directory.

### Edge Cases
- Files that already start with the prefix will not be renamed again.
- Empty directories will not cause any issues.

# Learning Python
## Part 1
This part covers python basics, you should be familiar with variables, functions, modules & classes

Feel free to read on the subjects on the internet - **Don't look up algorithms**
1. **Factorial** - Write a recursive function to calculate a factorial of a number
2. **Anagram** - Write a function that checks if two strings are anagrams of each other
3. **Pancake Sort** - Write a function to sort an array of integers. Use the `pancake sort` algorithm 
4. **Remove Duplicates** - Write a function that removes duplicate characters from a string
5. **Permutation** - Write a recursive function that prints all the permutations of the set {1...n}
6. **Highest Occurred Character** - Write a function that returns the highest occurred character in a string
## Part 2
This part covers slightly more complex exercises. Feel free to use libraries. Use proper OOP

Here, you should be familiar with design principles, SOLID & design patterns

In addition, you need to be familiar with APIs, HTTP and REST.
### FTP Server
1. **Python Accessibility** - Write a simple FTP server, accessible via python code (no need for an HTTP API or a CLI). The server should allow getting the files on the server, getting a specific file, storing a new file
2. **REST API** - Expose the functionality through a REST API (use a library of your choice). Should expose a /files endpoint with support for POST, GET, DELETE, PUT
### Coronavirus Collisions
1. Write a RESTful API that allows:
- CRUD for people that tested positive for the virus (POST, GET, DELETE, PUT)
- Given a location and time, check if you should be in isolation
2. Allow live updates. Using a techonology of your choice, allow getting updates from the server about new infected location and times, so you can know ASAP if you should be isolated.
## Part 3
### ProLog
#### Description
Write a CLI tool, called ProLog&trade; for advanced log reading/filtering, with the following features (ordered by importance):

1. `prolog print from_file(file_path.log)` - print logs from a specific file path
2. `prolog print from_dir(dir_path)` - print logs from all files within a directory
3. `prolog write_to(result.prolog) <source/input>` - write logs from a source to a .prolog file
4. `prolog <target/output> <source/input> level(ERROR/INFO/WARN,FATAL,DEBUG)`
- Extract logs content filtered by `level`
- Allow specifying multiple `level`s
- Allow using multuple filters, e.g. `prolog print from_file(file.log) level(ERROR,FATAL) contains(DB disconnected)`
5. `prolog print watch_file(file_path.log)` - watch the file file_path.log, and print any new logs added to it

#### Usage Examples
- `prolog print file_file(amazing.log)` - prints all the logs within amazing.log
- `prolog print from_file(cool.log) level(ERROR)` - prints all ERROR level logs from cool.log
- `prolog write_to(bad.prolog) file_file(nice.log) level(ERROR,FATAL)` - create a file named bad.prolog that contains all FATAL & ERROR level logs from nice.log
- `prolog write_to(summary.prolog) from_dir(logs_dir)` - create a file named summary.prolog containing all the logs from logs_dir
- `prolog write_to(new_logs.prolog) watch_file(all_logs.log)` - write all new logs written to all_logs.log to a file named new_logs.prolog
#### Notes
- The command format is: `prolog <target_argument>(<target_params>) <source_argument>(<source_params>) [<filter_argument>(<filter_params>)...]`

- The log format is: `[LEVEL] message` - e.g. "[ERROR] Something bad happened"

- **the ProLog&trade; program can only read .log or .txt files, and only creates files of type .prolog**
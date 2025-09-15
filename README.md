# Text Processing Server

A client-server application that provides various text processing and utility services using TCP sockets in Python.

## Description

This system consists of a server that performs text processing operations and a client that sends text processing requests. The client sends the operation name, text data, and optional parameters to the server, which processes the request and returns the result.

## Features

The text processing server supports the following operations:
- **reverse**: Reverse the input text
- **upper**: Convert text to uppercase
- **lower**: Convert text to lowercase
- **count**: Count occurrences of a substring in the text
- **replace**: Replace all occurrences of one substring with another
- **hash**: Generate MD5 or SHA256 hash of the text
- **password**: Generate a random password of specified length
- **analyze**: Get text statistics (word count, character count, sentences

## How to Run

1. **Start the server**:
   ```bash
   python server.py
   ```
   The server will start listening on localhost:12345

2. **Run the client**:
   ```bash
   python client.py
   ```
   The client will connect and show available operations

3. **Using the client**:
   - Choose an operation from the menu
   - Provide the required text input and parameters
   - View the processed result
   - Type "help" to see operations again
   - Type "quit" to exit

## Example Usage

```
Operation: reverse
Enter text: Hello World
Result: dlroW olleH

Operation: count
Enter text: The quick brown fox jumps over the lazy dog
What to count: the
Result: 2

Operation: replace
Enter text: I like cats and cats like me
Replace what,with what: cats,dogs
Result: I like dogs and dogs like me

Operation: hash
Enter text to hash: secret123
Hash type (md5/sha256) [md5]: sha256
Result: 2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b

Operation: password
Password length [12]: 16
Result: K8mP@x9vL2nQ$wR3

Operation: analyze
Enter text: Hello world! This is a test. How are you?
Result: Words: 9, Characters: 39, Characters (no spaces): 31, Sentences: 3
```

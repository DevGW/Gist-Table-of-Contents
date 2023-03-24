# Gist Table of Contents

This is a Python script that generates a table of contents for a users Gists on GitHub. It creates links to each Gist and categorizes them, making it easier to navigate a users entire Gist collection.

## Installation

To use this script, you will need Python 3 installed on your machine. If you don't have it installed, you can download it from the official website: https://www.python.org/downloads/

Next, you'll need to clone this repository to your local machine. You can do this by running the following command in your terminal or command prompt:

```shell
git clone https://github.com/DevGW/Gist-Table-of-Contents.git
```


Once you have cloned the repository, navigate to the directory where the `gistToc.py` file is located.

## Requirements

This script requires the `requests` library to be installed. You can install it by running the following command:

```shell
pip install requests
```

## Usage

To use the script, follow these steps:

1. Navigate to the directory where the `gistToc.py` file is located.
2. Run the script with the following command:

```shell
python3 gistToc.py <github_username>
```


Replace `<github_username>` with the username you want to generate a table of contents for. You can find the username in the URL of the Gist.

For example, if the URL of your Gist is `https://gist.github.com/awesome_username/1234567890abcdef`, then the username is `awesome_username`.

5. The script will output a table of contents for the specified username.

## Example

Here's an example of what the generated TOC might look like: [table_of_contents.md](table_of_contents.md)

## Contributing

Contributions are welcome! If you find a bug or want to suggest a feature, please open an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

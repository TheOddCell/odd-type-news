# Odd Type News
a simple API for news, blogging, or posting your weird opinions online.

## How to use
### Servers
Before starting, choose a place to host it. For example: `news.example.com/examplenews/`.

#### Automatic Setup
(Only tested on Debain/Ubuntu)
1. Download [server.py](https://github.com/TheOddCell/odd-type-news/releases).
2. Move `server.py` to the directory (eg. `news.example.com/examplenews/server.py`)
3. Run `server.py` and follow the instructions. (this will also create a new post.)

4. For each new post, use the manual setup steps 6-8 or run server.py.
#### Manual Setup
1. Add the files `num.txt`, `disc.txt`, and `title.txt` to the root of this directory. (eg `news.example.com/examplenews/num.txt`)
2. Fill `num.txt` with -1 for now.
3. Put a discription (with backslashes as newlines) in `disc.txt`.
4. Choose a title, and put it in `title.txt`.
5. Create a folder called `news`.

Note: Starting from here is repeted for each post.

6. Put another folder named the number of posts you have before this one in `news` Start with 0.
7. Create two files inside this folder called `metadata.txt` and `content.txt`.
8. In `metadata.txt`, type in the title of your post followed by a backslash, and the date also followed by a backslash.
10. In `content.txt`, put whatever you want in your post with newlines as backslashes.
11. Add 1 to the number in `num.txt`.

You have succsessfully made a post! (for an example, go to [/example](https://github.com/TheOddCell/odd-type-news/tree/main/example) or connect to `https://otn.oddcell.ca/example/`.)
### Users
Download [client.py](https://github.com/TheOddCell/odd-type-news/releases), and type `switch` into the command line, then type in the url. (eg. `news.example.com/examplenews/`)

Done!

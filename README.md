# Odd Type News
a simple API for news, blogging, or posting your weird opinions online.

## How to use
### Servers
1. Choose a place to host it. For example: `news.example.com/examplenews/`
2. Add the files `num.txt`, `disc.txt`, and `title.txt` to the root of this directory. (eg news.example.com/examplenews/num.txt)
3. Fill `num.txt` with -1 for now.
4. Put a discription (with backslashes as newlines) in `disc.txt`.
5. Choose a title, and put it in `title.txt`.
6. Create a folder called `news`.

Note: Starting from here is repeted for each post.

7. Put another folder named the number of posts you have before this one in `news` Start with 0.
8. Create two files inside this folder called `metadata.txt` and `content.txt`.
9. In `metadata.txt`, type in the title of your post followed by a backslash, and the date also followed by a backslash.
10. In `content.txt`, put whatever you want in your post with newlines as backslashes.
11. Add 1 to the number in `num.txt`.

You have succsessfully made a post!
### Users
Download [client.py](https://otn.oddcell.ca/client.py), and type `switch` into the command line, then type in the url. (eg. `news.example.com/exammplenews/`)

Done!
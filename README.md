# Stratus

Free, unlimited cloud storage! Powered by familiar FTP-style command line 
controls.

## Dependencies

1. [pip][pip] and [node.js][npm] for installation
2. An instance of [MongoDB][mongo] running as a separate task

[pip]: https://pypi.python.org/pypi/pip
[npm]: http://nodejs.org/
[mongo]: http://www.mongodb.org/

## Installation

1. Create a "master" [Dropbox][Dropbox] account to run your application.
2. Visit the [developer site app console][developer] and create a Dropbox API 
app with files and datastores. The app data folder and name settings are 
up to you.
3. Execute the following:

 ```
git clone git@github.com:akalicki/stratus.git
cd stratus
npm install -g phantomjs
pip install -r requirements.txt
```

4. Replace the `app_key` and `app_secret` fields in the `config.py` file with 
the strings provided to your app in the Dropbox app console.

[Dropbox]: https://www.dropbox.com/
[developer]: https://www.dropbox.com/developers/apply?cont=/developers/apps

## Usage

The app runs almost identically to the FTP console interface once initialized. 
From the stratus folder, simply type `python stratus.py` to begin and `help` 
for the list of commands:

```
stratus - v0.1.0
---------------------
  help - list all commands
  quit - exit the program (aliases: exit, logout)

# Navigation:
  pwd          - get path of stratus directory
  lpwd         - get path of local directory
  ls           - list files in stratus directory
  lls          - list files in local directory
  cd    [path] - navigate to stratus directory at path
  lcd   [path] - navigate to local directory at path
  mkdir [path] - create stratus directory at given path
  rmdir [path] - remove stratus directory at given path

# File Operations:
  put  [lpath] [spath] - upload file from lpath to spath
  get  [spath] [lpath] - download file at spath to lpath
  mv   [path1] [path2] - move stratus file from path1 to path2
  link [path]          - get web links to stratus file at given path
  rm   [path]          - delete stratus file at given path
```

## Future Plans

1. Autocomplete to make navigating faster
2. Some kind of search?
3. Chunked upload and upload status indication

## Disclaimer

1. Each time stratus needs to generate a new Dropbox account, it takes a bit 
of time. Please be patient on the first upload and every time you use up 2GB.
2. Due to Dropbox developer limitations stratus can only create up to 100 
accounts (200GB of storage) at the present time. Looking for a way around this.
3. The current upload function only supports individual files of 150MB or 
smaller. This will be fixed in an upcoming patch when I switch upload 
protocols.

## Thanks

This project was heavily based on Raymond Jacobson 
([@raymondjacobson][rayaccount])'s ideas and account generation process 
demonstrated in his project [Monsoon][monsoon]. The apps differ a bit in 
functionality and usage, so go check his out!

[rayaccount]: https://github.com/raymondjacobson
[monsoon]: https://github.com/raymondjacobson/monsoon
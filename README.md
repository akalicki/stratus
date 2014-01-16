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
for a list of commands.

## Future Plans

1. Autocomplete to make navigating faster
2. Some kind of search?

## Thanks

This project was heavily based on Raymond Jacobson 
([@raymondjacobson][rayaccount])'s ideas and account generation process 
demonstrated in his project [Monsoon][monsoon]. The apps differ a bit in 
functionality and usage, so go check his out!

[rayaccount]: https://github.com/raymondjacobson
[monsoon]: https://github.com/raymondjacobson/monsoon
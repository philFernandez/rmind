
[![philFernandez](https://circleci.com/gh/philFernandez/rmind.svg?style=shield)](https://app.circleci.com/pipelines/github/philFernandez/rmind)

![Logo](./img/logo/logo.png)
---

### TOC

-   [About](#about)
-   [Usage](#usage)
    -   [Create](#create)
    -   [Read](#read)
    -   [Update](#update)
    -   [Delete](#delete)
- [Install Pre-release](#install-pre-release)
-   [Install Tab Completion](#install-tab-completion)
-   [Motivation](#motivation)
- [Standing on the Shoulder's of Giants](#standing-on-the-shoulders-of-giants)

---

![Tables](./img/screenshots/Tables.png)

![Tags](./img/screenshots/Tags.png)

## About
#### :ledger: A notebook CLI

`rmind` is loosely inspired by another CLI called
[taskwarrior](https://github.com/GothenburgBitFactory/taskwarrior). The goal
of `rmind` is to provide a more streamlined list oriented application, that
takes advantage of modern CLI libraries to pile on the command line eye candy
(tastefully of course :wink:). Taskwarrior is great, and I will continue to
use it for keeping track of structured tasks, but IMHO it isn't ideal for
keeping track of random ideas for future reference. Thats why I made `rmind`.
As a person who spends *allot* of time in a terminal, I wanted a place to
store my ideas quickly without having to take my hands off the keyboard, and
without needing to open another application, while also having something
that's powerful and nice to look at. `rmind` is my solution to that problem.

#### Features

- Organize notes with tags for easy categorization and batch retrieval
- Embedded inline markup, powered by [rich](https://github.com/willmcgugan/rich), for coloring, styling, and emoji-ing your notes
- Easily edit all aspects of any entry at any time

## Usage

-   #### Create
    -   `rmind add`
        -   invokes a prompt asking for your input.
    -   `rmind add -a 'My awesome note to remember'`
        -   bypasses the prompt and saves input given after `-a`.
    -   `rmind add -t some_tag -a 'Awesome note'`
        -   saves input and association with tag given after `-t`.
        -   `-t` option can be given multiple times for multiple tags.
        -   `-a` option can be omitted to invoke a prompt for your input here too.
-   #### Read
    -   `rmind`
        -   returns all currently saved notes in tabular form.
    -   `rmind -t some_tag`
        -   returns all currently saved notes that are tagged with `some_tag` in tabular form.
        -   `-t` option can be given multiple times.
    -   `rmind -v`
        -   returns all currently saved notes with additional information such as entry date and time in tabular form.
        -   This can also be used with the `-t` option.
    -   `rmind -vv`
        -   same as `-v` but shows additional "Tags" column in tabular output.
-   #### Update
    -   `rmind update [id] -u 'Updated awesome note to remember'`
        -   updates entry with id `[id]` if the id exists in the database.
        -   displays output letting user know if update succeeded.
        -   `-u` option can be omitted to invoke a prompt for your input.
-   #### Delete
    -   `rmind delete [id]`
        -   deletes entry with id `[id]` if the id exists in the database.
        -   displays output letting user know if update succeeded.

## Install Pre-Release
`pip install https://github.com/philFernandez/rmind/archive/refs/tags/v0.1a2.tar.gz`

**Or download the [release archive](https://github.com/philFernandez/rmind/releases/tag/v0.1a2)**


The pre-release is definitely usable. The --help messages aren't completely refined, and there
are still more features and polishing that will show up in the first major release. There will
also be install options for at least PyPi, and probably Homebrew, and possibly more.

## Install Tab Completion

Add one of the following to your shell's startup file.

<!-- eg. `~/.zlogin` or `~/.zshrc` for zsh, `~/.profile` or `~/.bashrc` for bash, and `~/.config/fish/completions/rmind.fish` for fish. -->

-   #### For ZSH - `~/.zshrc` or `~/.zlogin`
    -   #### `eval "$(_RMIND_COMPLETE=source_zsh rmind)"`
-   #### For BASH - `~/.bashrc` or `~/.profile`
    -   #### `eval "$(_RMIND_COMPLETE=source_bash rmind)"`
-   #### For FISH - `~/.config/fish/completions/rmind.fish`
    -   #### `eval "$(_RMIND_COMPLETE=source_fish rmind)"`

---

## Motivation

I'm making this CLI for myself so that I can have a simple place to _quickly_
jot down my ideas in a unified place such that I can revisit them later
without having to remember too much. I previously used note taking
applications, like [vimwiki](https://github.com/vimwiki/vimwiki), OneNote,
Google Keep, but these tend to quickly devolve into a mess of pages and
unorganized musings that asymptote towards worthlessness. I'm not saying
these applications are worthless, they just don't work for me with the goal
of saving and organizing my ideas. Another drawback for me is that some of
these tools are packed with features, which I end up fiddling with more than
I actually record my ideas.

I recently started using [task
warrior](https://github.com/GothenburgBitFactory/taskwarrior) and have found
it to be the best thing for me so far. Its great for keeping track of active
projects, and steps that need to be crossed off a list as completed, but I
still feel like I need something for just jotting down random ideas that pop
up, or random cool things that I discover and want to revisit. I can kind of
make [task warrior](https://github.com/GothenburgBitFactory/taskwarrior) work
for me in that way, but there are still allot of features in the way that I'd
rather be able to strip out. I just need to be able to capture my ideas in a
sentence or two and have the option to add tags. That way
I can come back later and query the saved data and filter by tag(s). That is
what this project aims to provide.


## Standing on the Shoulder's of Giants

Without the hard work and passion of those who contribute their time and talent to open source,
this project wouldn't have been possible for me. These projects in particular
play a huge role in making *this* project work.

| Project | How I used it |
|---------|---------------|
| [rich](https://github.com/willmcgugan/rich)    | Tables, colors, styling, emoji. CLI eye candy in general. |
| [click](https://github.com/pallets/click)    | CLI options and arguments parsing, help messages and tab completion. |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | Mapping application objects to sql data, and handling the persistence and lookup of said data. |
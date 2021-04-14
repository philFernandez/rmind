# `rmind`

    Currently in development phase.

### TOC

-   [About](#about)
-   [Usage](#usage)
    -   [Create](#create)
    -   [Read](#read)
    -   [Update](#update)
    -   [Delete](#delete)
-   [Install Tab Completion](#install-tab-completion)
-   [Motivation](#motivation)
- [Standing on the Shoulder's of Giants](#standing-on-the-shoulders-of-giants)

## About

-   #### :ledger: A notebook cli.
-   #### Loosely inspired by [`task` warrior](https://github.com/GothenburgBitFactory/taskwarrior).

-   #### The goal is to offer a less feature rich alternative.

-   #### Something for quickly jotting down and organizing concise ideas with user defined tags.

-   #### Ideas can later be recalled and filtered by tag(s) or as a complete list.

-   #### Using tags is optional. It can be used as an idea dump without categories.

-   #### The goal is to focus on getting your ideas recorded and categorized without focusing on the tool you're using to do it.

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

I'm making this cli for myself so that I can have a simple place to _quickly_
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
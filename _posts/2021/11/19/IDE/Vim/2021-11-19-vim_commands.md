---
layout: post
title: "[IDE] VIM Commands"
description: " "
date: 2021-11-19
tags: [IDE]
comments: true
share: true
---



## VIM Commands
> I'am currently using 
* VIM Editor for Python <small>(iTerm)</small>
* IdeaVim for Golang <small>(IntellJ)</small>
* VSCodeVim for JavaScript <small>(VS Code)</small>

![vimvim](https://user-images.githubusercontent.com/48475824/73815465-672bbc80-4829-11ea-8683-6e890c7d276d.png)

Vim has 3 modes.
1. **Insert Mode**  
  Write text
1. **Normal Mode (Visual Mode)**  
  Navigate and manipulate text
1. **Command Mode**  
  Can input a wide variety of commands.


## Change Modes
  * Normal Mode → Insert mode   
  <code>i</code> : insert   
  Enter insert mode
    * Insert at the beginning of the line  
    <code>I</code>
    * Insert end of the line  
    <code>A</code>
    * Insert at the nend of the word  
    <code>ea</code>

  * Insert mode → Normal Mode   
  <code>v</code> : Visual  
  Enter visual mode   
  <code>V</code>   
  Enter linewise visual mode

  * Command mode   
  <code>esc</code>  
  Enter Command mode


## Left, Down, Up, Right
  * Move Left  
  <code>h</code>

  * Move Down  
  <code>j</code>

  * Move Up  
  <code>k</code>

  * Move Right  
  <code>l</code>


## Undo, Redo
  * Undo  
  <code>u</code>
  * Redo  
  <code>ctr</code> + <code>r</code>


## Delete
  * Delete a character    
  <code>x</code> : Delete character after the cursor.   
  <code>X</code> : Delete character before the cursor.

  * Delete a word  
  <code>dw</code>

  * Delete the line   
  <code>d</code> + <code>d</code> : Delete current line.  

  * Delete to end of line.   
  <code>D</code>

  * Delete number of lines.  
  <code>\<#>d</code>  
  <code>d\<#>j</code> : delete # of lines down(j)
    * e.g.  
    <code>3d</code> : Delete 3 lines.
    <code>100d</code> : Delete 100 lines.


## Move cursor
  * Beginning of the file.  
  <code>gg</code>  
  <code>[[</code>
  Move to beginning of the file.

  * End of the file.  
  <code>G</code>  
  <code>]]</code>  
  Move to end of the file.

  * Move to the top of the screen.  
  <code>H</code> : High

  * Move to the middle of the screen.  
  <code>M</code> : Middle

  * Move to the bottom of the screen.  
  <code>L</code> : Low



## Jumping around
  * Jump to specific line.  
  <code>:\<line#></code>
    * e.g.  
    <code>:14</code> : Will Jump to line 14.  
    <code>:55</code> : Will Jump to line 55.

  * Jump to end of a word.  
  <code>e</code>

  * Jump to end of a word (before whitespace)  
  <code>E</code>

  * Jump to beginning of next word.  
  <code>w</code>

  * Jump to beginning of next word (before whitespace)  
  <code>W</code>

  * Jump to previous beginning of word.  
  <code>b</code>

  * Jump to previous beinning of word (before whitespace)  
  <code>B</code>

  * Jump to beginning of the line.  
  <code>0</code>

  * Jump to end of the line.  
  <code>$</code>
  
  * Jump to next paragraph  
  <code>}</code>
  
  * Jump to previous paragraph  
  <code>{</code>


## Scrolling screen
  * Move to current cursor position.  
  <code>z</code>
  
  * Move forward a full screen.  
  <code>ctr</code> + <code>f</code>  
  f : forward

  * Move backward a full screen.  
  <code>ctr</code> + <code>b</code>  
  b : backward

  * Move forward half a screen.  
  <code>ctr</code> + <code>d</code>  
  d : down

  * Move backward half a screen.  
  <code>ctr</code> + <code>u</code>  
  u : up


## Find, Search
  * Find a word under cursor.  
  <code>*</code>

  * Find a character after cursor in the line   
  <code>f</code>

  * Serach string.  
  <code>/\<string></code>
    * e.g  
    <code>/baby</code> : baby will be searched  
    <code>/tiger</code> : tiger will be searched


## Copy, Paste
  * Copy.  
  <code>y</code>  
  y : yank

  
  * Copy the line.  
  <code>yy</code>  

  * Copy the current word.  
  <code>yiw</code>
  
  * Copy to the end of the line.  
  <code>y$</code> : Copy from current cursor to the end of the line.

  * Paste copied.  
  <code>p</code> : Paste after the cursor.  
  <code>P</code> : Paste before the cursor.


## Add new lines.
  * Add new line before cursor.  
  <code>o</code>

  * Add new line after cursor.
  <code>O</code>


## Indentation
  * Auto indentatation.  
  <code>==</code>

  * Indent.  
  <code>></code>

  * Outdent.  
  <code><</code>


## Save, quite File
Save and quite in command mode.   
  * Save it  
  <code>:w</code> : write

  * Quit  
  <code>:q</code> : quite

  * Force Quit  
  <code>:q!</code>  
  Quit w/o saving changes.

  * Save and Quite  
  <code>:wq</code>  
  Save and quite file.  

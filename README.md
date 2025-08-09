# UltraCTF

A Python-based CLI tool that's used for CTFs, whether you're a beginner or an advanced CTFer, I do hope this tool is of good use to you :D

## Current Features
- Base Conversions
  - Binary -> Decimal/Hex/Octal
  - Decimal -> Binary/Hex/Octal/Unicode
  - Hex -> Binary/Decimal/Octal/Unicode
  - Octal -> Binary/Decimal/Hex
  - Unicode -> Decimal/Hex
  - Base32 Encoding/Decoding
  - Base58 Encoding/Decoding
  - Base64 Encoding/Decoding
- Cryptography (WIP)
  - Hash Generator [MD5, SHA1, SHA256, SHA512] (Completed)
  - ROT13 (Completed)
  - XOR [ASCII/Hex Inputs With Given Fixed Key] (Currently WIP)
  - Caeser Cipher Brute Force
  - Atbash Cipher
  - Single-Byte XOR Brute Force
  - Morse Code Encode/Decode
- More to come :D

## Why this exists
The second of many random posts that track my progress as a programmer. This time a more serious project with a proper idea and drive in mind.

The idea of this came from a CTF me and my mates went to in the past. My friend who didn't do any CTFs before struggled, so thinking back to back then I figured a tool that could help beginners carve a path for themselves, and him especially, would be quite useful.

So behold the second of many repos to come about my progress and improvement. If anyone who sees this has any tips, ideas or comments, just lemme know, all feedback is much appreciated.

## How to run
```bash
git clone https://github.com/kaizokuv/UltraCTF.git
cd UltraCTF
python3 main.py
```

## For those of you who are lazy and willing to tweak around with aliases
Here are some aliases you guys can use for your terminal shells (bash, fish, zsh) to simplify calling the tool. 

Mind you you will still need to clone the repo first, and this is assuming you cloned the repo into your desktop and not a file. 

The alias will cd in a subshell so that once you're done using the tool, you'll go back to your original directory.

### For bash/zsh shell
```bash
alias ultractf='(cd ~/UltraCTF && python main.py)'
```
Change '~/UltraCTF' to the desired file path if you want to set a custom file path

### For fish shell
```bash
function ultractf
  pushd ~/UltraCTF > /dev/null
  python main.py
  popd > /dev/null
end
```
Change '~/UltraCTF' to the desired file path if you want to set a custom file path


# Thank you for using my tools :D

# UltraCTF

A Python-based CLI tool that's used for CTFs and works offline, whether you're a beginner or an advanced CTFer, I do hope this tool is of good use to you :D

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
- Cryptography
  - Hash Generator [MD5, SHA1, SHA256, SHA512]
  - ROT13
  - XOR [ASCII/Hex inputs with use given keys]
    - Gives the user the option to use ACSII or hex strings inputs
    - Keys can be in the form of ASCII, hex or single-bytes (WIP: single-byte inputs)
  - Caeser Cipher Brute Force
    - Brute forces through all 26 possible shifts
  - Atbash Cipher 
  - Single-Byte XOR Brute Force
    - Brute force with all 256 single-byte keys
    - If you do have the key, you can input it
  - Morse Code
  - Normal Substitution (Only Letters)
    - Takes any printable ASCII characters but will only scramble the letters with given values
    - Any non-ASCII characters will flag an error
    - Uppercased letters will stay uppercased, same for lowercased letters
    - When reversing, if you have the pattern, it'll auto reverse the pattern for you
      - For example if you scrambled 'beans' with the pattern '+5, -4' and you want to reverse, you can put in the same pattern and the program will reverse it for you to '-5, +4'
    - If the pattern is shorter than the text, the pattern will repeat
      - For example the word 'beans' with the pattern '+5,-4' will give the output for 'b +5, e -4, a +5, n -4,s -5', which will be 'gafjx' 
    - For example 'flag{beans}' with the pattern '+1, -14, +7, -5, +12' will give you 'gXhb{cQhiE}'
  - Custom Substitution (Printable ASCII Range)
    - Takes any printable ASCII characters and scrambles them
    - Any non-ASCII characters will flag an error
    - Uppercased letters will stay uppercased, same for lowercased letters
    - When reversing, if you have the pattern, it'll auto reverse the pattern for you
      - For example if you scrambled 'b3ans' with the pattern '+5, -4' and you want to reverse, you can put in the same pattern and the program will reverse it for you to '-5, +4'
    - If the pattern is shorter than the text, the pattern will repeat
      - For example the word 'b3ans' with the pattern '+5,-4' will give the output for 'b +5, 3 -4, a +5, n -4,s -5', which will be 'g (enter) fjx' 
    - For example 'flag{beans}' with the pattern '+1, -14, +7, -5, +12' will give you 'g7hb5c0hiE~'
- More to come :D

## Why this exists
The second of many random posts that track my progress as a programmer. This time a more serious project with a proper idea and drive in mind.

The idea of this came from a CTF me and my mates went to in the past. My friend who didn't do any CTFs before struggled, so thinking back to back then I figured a tool that could help beginners carve a path for themselves, and him especially, would be quite useful.

This tool also came to idea with CyberChef by gchq on Github (go check it out, it's an amazing tool at https://github.com/gchq/CyberChef), I wanted to make my own offline version that could be run offline, since as far as I knew, CyberChef could not be run offline. It may not be as feature rich, but it does work and I'm working to add more tools.

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

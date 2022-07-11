# BookCypher

## Introduction

I wrote this book cypher encoder/decoder as a tool for the ongoing Tabletop Roleplaying games that I run for a group of my friends. 
I wrote this for the purpose of encoding a character's notes with the World of Darkness Book of Nod. This is an initial attempt to do so.
Likely, the actual implementation of the encoder that will be used for the game materials will be slightly more complicated than what is here.

## Usage

The Book class will take a text file where pages are separated with "---PAGE---" and the lines are dilineated with /n. 
It will generate a dictionary with the word and a list of Word class objects which store the word itself, and the page, line, and word numbers.

The encode function takes a plain text file name, and outputs the the encoded string.

The decode function takes an encoded text file and returns the decoded text as a string.

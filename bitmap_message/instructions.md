# Bitmap Message Instructions

This program uses a multiline string as a _bitmap_, a 2D image with only two possible colors for each pixel, to determine how it should display a message from the user. 

In this bitmap, space characters represent an empty space, and all other characters are replaced by characters in the user’s message. 

The provided bitmap resembles a world map, but you can change this to any image you’d like. 

<br>

## The Program in Action

When you run _bitmapmessage.py_, the output will look like this:

```
Bitmap Message, by Al Sweigart al@inventwithpython.com
Enter the message to display with the bitmap.
> Hello!

Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He
   lo!Hello!Hello   l  !He lo  e      llo!Hello!Hello!Hello!Hello!He
  llo!Hello!Hello!Hello He lo H  l !Hello!Hello!Hello!Hello!Hello H
 el      lo!Hello!Hello!He       lo!Hello!Hello!Hello!Hello!Hel
          o!Hello!Hello          lo  e lo!H ll !Hello!Hello!H l
           !Hello!He            llo!Hel   Hello!Hello!Hell ! e
            Hello!He           ello!Hello!Hello!Hello!Hell  H
   l        H llo! ell         ello!Hello!Hell !Hello  el o
               lo!H  l         ello!Hello!Hell   ell !He  o
                 !Hello         llo!Hello!Hel    el   He  o
                 !Hello!H        lo!Hello!Hell    l  !H llo
                   ello!Hel         Hello!He          H llo Hell
                   ello!Hell         ello!H  l        Hell !H l o!
                   ello!Hell         ello!H l o           o!H l   H
                     lo!Hel          ello! el             o!Hel   H
                     lo!He            llo! e            llo!Hell
                    llo!H             llo!              llo!Hello
                    llo!              ll                 lo!Hell   e
                    llo                                       l    e
                    ll     l                    H
Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He
```

## How It Works

The `bitmap.splitlines()` method call on line 43 returns a list of strings, each of which is a line in the multiline `bitmap` string. 
Using a multiline string makes the bitmap easier to edit into whatever pattern you like. 
The program fills in any non-space character in the pattern, which is why asterisks, periods, or any other character do the same thing.

The `message[i % len(message)]` code on line 51 causes the repetition of the text in `message`. 
As `i` increases from `0` to a number larger than `len(message)`, the expression `i % len(message)` evaluates to `0` again. 
This causes `message[i % len(message)]` to repeat the characters in `message` as `i` increases.
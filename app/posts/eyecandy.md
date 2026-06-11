---
title: "Crackmes.one: EyeCandyLOCKED"
slug: "crackmes-eyecandylocked"
date: 11/06/2026
excerpt: "Trying out some stuff from crackmes.one."
---

I've been trying to do some crackmes from [crackmes.one](https://crackmes.one), and thought it'd be an interesting exercise to write up my solutions. I've wanted to post some different things here for quite a while now anyway, I just haven't been able to think of anything until now. There may be more of these in the future, there may not be, who knows? Anyway, on to my solution to EyeCandyLOCKED.

This was a pretty simple one, but I did come across some interesting things while doing it that I wasn't expecting. It does have a difficulty rating of 1.0, so I suppose that tracks.

To start with, let's run the binary which results in the following:

![Running the binary](../static/img/posts/crackmes_eyecandy/running_binary.jpg)

So we need a password. Okay... Opening the file in Ghidra allows us to have a look at the `main` function, which shows an interesting `if` statement. It seems to lead to a branch that detects debuggers using `ptrace` (will amend details of how this works once I've done more reading). The decompiled code can be seen below:

![Debugger resistance](../static/img/posts/crackmes_eyecandy/resistance.jpg)

We can demonstrate this by trying to run the binary in `gdb`:

![Debugger Detected](../static/img/posts/crackmes_eyecandy/debug.jpg)

This could potentially be patched within gdb to bypass it, but if we keep looking through the main function in Ghidra, there's actually some more useful information. Below is the branch which seems to lead to the door being unlocked, and the variable that leads to this branch is `bVar1 = checkIt((string)local_58);`.

![checkIt](../static/img/posts/crackmes_eyecandy/checkit.jpg)

Double clicking `checkIt` brings us directly into the decompiled code for that function, which contains an interesting array. That probably contains the password, but it's encoded in a combination of hex and decimal.

![Encoded](../static/img/posts/crackmes_eyecandy/encoded.jpg)

However, in Ghidra we can right click on each value, and select Char, which converts it for us:

![Decoded](../static/img/posts/crackmes_eyecandy/decoded.jpg)

So the decoded password is `d00r1$m@licious`, which we can enter within the program:

![Unlocked](../static/img/posts/crackmes_eyecandy/unlocked.jpg)

Success! I hope this write up is at least interesting to someone, and if not, then it was interesting to me. There may be more of this in the future, I'm not sure when though. I will definitely be exploring more crackmes, but there may not be a post for every single one.

-- Lolei <3

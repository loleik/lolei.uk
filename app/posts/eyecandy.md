---
title: "Crackmes.one: EyeCandyLOCKED"
slug: "crackmes-eyecandylocked"
date: 11/06/2026
excerpt: "Trying out some stuff from crackmes.one."
---

I've been trying to do some crackmes from [crackmes.one](https://crackmes.one), and thought it'd be an interesting excercise to write up my solutions. I've wanted to post some different things here for quite a while now anyway, I just haven't been able to think of anything until now. There may be more of these in the future, there may not be, who knows? Anyway, on to my solution to EyeCandyLOCKED.

This was a pretty simple one, but I did come across some interesting things while doing it that I wasn't expecting. It does have a difficulty rating of 1.0, so I suppose that tracks.

To start with, let's ran the binary which results in the following:

![Running the binary](../static/img/posts/crackmes_eyecandy/running_binary.jpg)

So we need a password. Okay... Opening the file in Ghidra allows us to have a look at the `main` function, which showed the following interesting `if` statement:

![Debugger resistance](../static/img/posts/crackmes_eyecandy/resistance.jpg)

There's a condition that seems to detect debuggers. We can demonstrate this by trying to run the binary in `gdb`:

![Debugger Detected](../static/img/posts/crackmes_eyecandy/debug.jpg)

This could potentially be patched within gdb to bypass it, but before doing that, let's make sure there's nothing else useful in Ghidra...

![checkIt](../static/img/posts/crackmes_eyecandy/checkit.jpg)

The success branch is here, showing the door being unlocked. The password isn't directly visible here, but notice the variable that leads down to this branch is `bVar1 = checkIt((string)local_58);`. Double clicking `checkIt` brings us directly into the decompiled code for that function, which contains the following:

![Encoded](../static/img/posts/crackmes_eyecandy/encoded.jpg)

That array looks like it's probably the password, but each value is encoded in either hex or decimal. However, in Ghidra we can right click on each value, and select Char, which converts it for us:

![Decoded](../static/img/posts/crackmes_eyecandy/decoded.jpg)

So the decoded password is `d00r1$m@licious`, which we can enter within the program:

![Unlocked](../static/img/posts/crackmes_eyecandy/unlocked.jpg)

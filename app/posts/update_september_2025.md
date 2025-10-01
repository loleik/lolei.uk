---
title: "Updates - September 2025"
slug: "update_september_2025"
date: 11/09/2025
excerpt: "Site updates and general thoughs."
---

It has been a few months since I have written a post here, and a lot has changed/happened in that time. Firstly, I have some quick thoughts on OPAD which I’ll include here briefly:

+ I have stopped logging the settings I use, partly due to convenience and partly because it doesn't matter much. I'll include them if they're relevant.
+ I didn’t write a post for day 150, so I’ll do one for 182 instead, seeing as that’s the halfway mark.
+ I’m going back and forth on whether I’m enjoying it or if it even feels worthwhile anymore, but I won’t go into that here.

As I said, the halfway mark is coming up. I’ll write a post for that and go over my thoughts in more detail, as well as celebrate what I have done so far. On the point of writing posts, I haven’t written any recently as I said. I had planned to write some posts on the following:

+ More trichromes.
+ More film development.
+ Harman Phoenix II.
+ Kodak Aerocolour.
+ More DIY redscale film.

As you can see, I haven’t. The main reason is that I just don’t have enough to say about them. I like Phoenix II, I love Aerocolour, and redscale is fun, but I don’t have anything to say outside of that, so I don’t see much of a point. So I’ll hold onto those ideas and see if they can fit into a bigger idea later on, no point in forcing anything. 

Now, for the trichromes and development, neither of my last attempts at either went smoothly, so I don’t really want to write about them. The development ended up being a bit of a mess and I contaminated half of the chemicals, and the trichromes just weren’t interesting. For the trichromes in particular, I do have some changes to try that could potentially improve them, and I will try development again. If they go well then maybe I’ll post about them.

The final thing I’d like to talk about is the site as a whole. There’s a new section, some stuff has moved around, and the whole deployment process has improved significantly. The new section is [here](https://lolei.uk/rust-test), and is intended for WebAssembly experiments. I wanted to try messing with it, so I’ve decided to implement some of my Rust projects in it. Currently there’s just a demo of Conway’s Game of Life, but it should expand in the future.

The oldest part of the website, the list of film rolls, has moved. It’s now on its own archive page. This is just to get it out of the navbar as the code is just a liability as long as it’s in there.

The biggest change, and the one I’m most proud of, is the deployment side of things. This won’t be obvious from the client-side though. Over the last day or so, I containerized the website using docker, and set up a Github repository for it again. I had the code on a Github repository before, but it wasn’t maintained and wasn’t useful outside of just being a backup. Now, it serves as a CI/CD workflow that builds, tests, and deploys the Docker image, and makes it available for my server to pull. This is a big change for me, as until now I’ve just been uploading files manually and restarting the server, now that’s all automated, and it’s much more than I had ever expected to get done with this project when I started it years ago.

Anyway, that’s pretty much everything I have updates on. I’m proud of how this has all developed since I decided to revive it, and hopefully the development continues.

-- Lolei <3
---
layout: default
title: Home
permalink: index.html
---

<h1 style="margin-top:-1em">MIT 2.166 - Autonomous Driving - Spring 2016</h1>

Backstory: Duckietown is a pleasant little town in the sovereign state of Duckieland. 

You moved to Duckietown last summer, after graduating from MIT. You were following the love of your life. You were working remotely for your friend’s social networking startup. Life was good, for a while. But things didn’t quite work out the way they were supposed to---the start-up went south and so did your love life. As the winter begins, you are now single and jobless in Duckietown.

In a fortuitous late-night encounter at a Karaoke bar, you meet a funny old man and you become best friends over saké. You learn that he is a high-ranking official in the Duckie Party. 
A couple of weeks later, the Duckieland Ministry of Transportation gives you the task of designing a mobility-on-demand system based on autonomous cars for the entire country of Duckieland. You have to build this system from scratch. 


<h2>Learn more</h2>

This is an <strong>open-source class</strong>. All these links are Google Docs documents 
on which everybody can comment:

- [Syllabus][syllabus]


[syllabus]: https://docs.google.com/document/d/1xkYod3ZepC3oMLTH-YCdMXlJRDWUQ8w14ROIh0yDsOE/edit

<div class="home">

  <!-- <h1 class="page-heading">News</h1> -->

  <h2 style='margin-top: 5em'> News </h2>
  <ul class="post-list">
    {% for post in site.posts %}
      <li>
        <span class="my-post-date">{{ post.date | date: "%Y-%m-%d" }}</span>

        <span class="my-post-title">{{ post.title }}</span>

        <!-- <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a> -->
  
        {{ post.content }}
      </li>
    {% endfor %}
  </ul>
<!-- 
  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p> -->

</div>
 


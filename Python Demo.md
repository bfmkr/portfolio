---
layout: default
title: Python Demo
---

# Python Demo

&nbsp;

This demo uses Python to showcase some web scraping, data analysis, and data visualizations.

In the first part, I do some simple web scraping to investigate the impact of "**Editor's Suggestion**" -- a feature of the world's largest physics journal Physical Review B (PRB) whereby a handful of publications are highlighted out of the 90 or so published each week.
Many publishers have adopted such a *highlights* feature for papers which are deemed to be of higher quality than the average paper, or otherwise thought to be influential.
PRB's own discussion about the impact of highlighting can be read [here](https://journals.aps.org/prb/edannounce/PhysRevB.92.210001).
<!-- To get  idea about the topic and keep the discussion brief, I focus only on publications from 2019. -->

In the second part, I detail the construction of two figures I made for my first scientific paper which was featured in PRB's Editor's Suggestions in 2019.
The tools used included Python, Wolfram Mathematica, and Inkscape.


## Part 1: Investigating the impact of Editor's Suggestion in Physical Review B

## Part 2: Data visualizations from a paper highlighted in Editor's Suggestion

### Introduction

On the 26th of February 2019, my publication in Physical Review B was featured on the highlights page for the journal as it had been selected for **Editor's Suggestion**, *Fig. 1*.
Eighty one other papers were published in the same issue of the journal, out of which three others were similarly highlighted.

![2019-02-26_prb-highlights-page](/assets/images/2019-02-26_prb-highlights-page.png)
*Fig. 1 Highlights page of Physical Review B on Feb 26th 2019*

At the time of writing this, more than four years later, the paper we published has gained 32 citations.
This is a respectable number, but not particularly remarkable.
My suspicion at the time was that we were not featured due to the impact our research might have in the future (it addressed a niche problem which would primarily interest other theorists working in our specialized area), but rather because the paper stood out among other submissions due to the colorful figures inside.

Regardless of the reason, I had spent significant time and attention ensuring we used a consistent color scheme across all figures, such that the essence of the story we were telling was evident from glancing through the manuscript without needing to scan through the detailed walls of text.

In this part, I wish to write a few details about the construction of a few of those figures.


### A bit of physics

The problem we addressed in our manuscript involved describing an excitation of a [magnetic skyrmion](https://en.wikipedia.org/wiki/Magnetic_skyrmion) known as the "breathing mode". 
This is where the skyrmion -- a circular-like deformation in the magnetization field of a ferromagnet -- appears to be growing and shrinking while retaining its hallmark circular shape; and, at the same time, the spins comprising the skyrmion collectively precess around their equilibrium values.



### The figures

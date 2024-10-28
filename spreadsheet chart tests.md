---
    layout: default-wide
    title: Spreadsheet Demo
---

# Spreadsheet chart tests

&nbsp;

Interactive charts embedded on websites from Google Sheets which use more than 1 data series are not loading currently because something broke on the server side in the javascript. Below is a minimal working example to show the bug. The second chart should show both sin(x) and cos(x) on the same chart. The example spreadsheet can be seen [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vQzOEaCipHHtdjkzqHbAmBt5sgVEoC6rOU7dsecO3Khc6O3I1mgg50q8I3BQo22xJqz6RXjiujLXlAY/pubhtml).

## Chart with one set of x-y pairs (works)

<iframe width="653" height="404" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQzOEaCipHHtdjkzqHbAmBt5sgVEoC6rOU7dsecO3Khc6O3I1mgg50q8I3BQo22xJqz6RXjiujLXlAY/pubchart?oid=399434830&amp;format=interactive"></iframe>

## Chart with two sets of x-y pairs (doesn't work 28/10/2024)

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQzOEaCipHHtdjkzqHbAmBt5sgVEoC6rOU7dsecO3Khc6O3I1mgg50q8I3BQo22xJqz6RXjiujLXlAY/pubchart?oid=420846860&amp;format=interactive"></iframe>

When the Google Sheets team fixes this bug I will revert to the interactive charts used previously in the <a href="{{ "/Spreadsheet%20Demo.html" | prepend: site.baseurl }}">main demo</a>.
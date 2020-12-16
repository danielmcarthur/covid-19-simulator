# covid-19-simulator
The intention of this project was to simulate the ways in which social distancing restrictions can affect the spread of a simulated contagious virus. It uses a population of 200 persons, each with a described list of friends whom they visit. The Python functions read this list, define the names as 'Person' class objects, each with another list of 'Persons' in their friend list. Then these persons are given health attributes and are able to become infected with the virus if their health is depleted enough. Then, the simulation is run over a set number of days, with a patient zero of a defined starting health level. Further, each day every individual is able to visit their list of friends, by a set likelihood of meeting. E.g. if a likelihood of meeting is 0.5, then an individual has a 0.5 chance of visiting each person in their friends list. Over each day in the simulation, the amount of infectious persons is recorded. Finally the results are shown on a infectious persons over time graph using `matplotlib`. 

[![You can watch my video explanation here](https://i.vimeocdn.com/video/1016431723.webp?mw=1100&mh=591)](https://vimeo.com/491460076)

<p><a href="https://vimeo.com/491460076">Daniel McArthur | Python Project | COVID-19 Spread Simulator</a> from <a href="https://vimeo.com/user129314614">Daniel McArthur</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

All work shown in this video has been completed by myself, Daniel McArthur in Python using PyCharm CE environment.


<figure class="video_container">
  <iframe src="https://vimeo.com/491460076" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

<iframe src="https://player.vimeo.com/video/491460076" width="640" height="344" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
<p><a href="https://vimeo.com/491460076">Daniel McArthur | Python Project | COVID-19 Spread Simulator</a> from <a href="https://vimeo.com/user129314614">Daniel McArthur</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

<p align="center">
<img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/header_main_wide_edt.png" width="900px">
<p>
<ol><b>Mars</b> is the fourth planet from the Sun and the second-smallest planet in the Solar System. Mars has long been the subject of human interest. This planet has been explored remotely by spacecraft. In the late 20th century, Earth-based probes have made it possible to learn more about the Martian system, particularly its geology and potential for habitability.</ol>

<p align="center">
<img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/po_file_main_edt.png" width="900px">
<p>

<ol><b>Objective</b></ol>
<ol>
This project, consists of two technical products:</br>

 <img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/dot_main_edt.png" width="7px"> <b>First:</b> scrape titles and preview text from <a href="https://static.bc-edx.com/data/web/mars_news/index.html">Mars News Site</a>
.</br>
 <img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/dot_main_edt.png" width="7px"> <b>Second:</b> scrape and analyze Mars weather data, which exists in a <a href="https://static.bc-edx.com/data/web/mars_facts/temperature.html">Mars Temperature Data Site</a>, and answering the following question:</br>
 1. how many months are there on mars?
 2. mow many martian days' worth of data are there?
 3. What is the average low temperature by martian month?
 4. What is the average pressure by martian month?
 5. How many terrestrial (earth) days are there in a martian year?




 
<h4>Methods, Software and Attribution:</h4>
<img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/dot_main_edt.png" width="7px"> Following programming languages, software, and libraries were used in this project:</br>

 1. `python v.3.9.13`</br>
 2. `jupyter notebook v.6.4.12`  `Visual Studio v.1.73.1`  `PowerPoint v.16.0.14026.20298` </br> 
 3. `splinter v.0.19.0` `pandas v.1.4.4`  `Beautiful Soup v.4.11.0`  `Matplotlib v.3.6.0`  `DateTime v.5.0`  `NumPy v.1.23.4` `json v.0.9.6`</br></br>
       
<img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/dot_main_edt.png" width="7px"> The project header GIF has been designed by powerpoint and <a href="https://photopea.com">photopea.com</a> using assets from <a href="https://Freepik.com">Freepik.com</a>.

</ol>
<p align="center">
<img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/re_file_main_edt.png" width="900px">
<p>

<ol>
<p align="center"><ins><b>Scrape Titles and Preview Text from Mars News</b></ins></p>
The result looks as follows , and it is stored as <a href="https://github.com/theidari/marsjo/blob/main/output/News_Result_Data.json">.json</a> and <a href="https://github.com/theidari/marsjo/blob/main/output/News_Result_Data.csv">.csv</a> files.</br>

```python
{'title': "NASA's MAVEN Observes Martian Light Show Caused by Major Solar Storm",
  'preview': 'For the first time in its eight years orbiting Mars, NASA’s MAVEN mission witnessed two different types of ultraviolet aurorae simultaneously, the result of solar storms that began on Aug. 27.'}  
```

<p align="center"><ins><b>Scrape and Analyze Mars Weather Data</b></ins></p>

 1. how many months are there on mars? <b>12</b>
 2. mow many martian days' worth of data are there? <b>1867</b>
 3. What is the average low temperature by martian month? </br>
  result for average low temperature is stored in <a href="https://github.com/theidari/marsjo/blob/main/output/min_temp.csv">.csv</a> file and shows in figure [1].</br>
<h6 align="center">Fig[1]: average low temperature by martian month</h6>
<p align="center">
<img src="https://github.com/theidari/marsjo/blob/main/output/Average%20Min_temp_per_Month.png" width="900px">
<p>

 4. What is the average pressure by martian month?
 5. How many terrestrial (earth) days are there in a martian year?


</ol>
<p align="center">
<img src="https://raw.githubusercontent.com/theidari/marsjo/main/design/doref_file_main_edt.png" width="900px">
<p>
<ol><b>Documents</b></ol>

<ol><b>References</b></ol>
<ol>
<sup>[1]</sup> The <a href="https://static.bc-edx.com/data/web/mars_news/index.html">Mars News website</a> is operated by edX Boot Camps LLC for educational purposes only. The news article titles, summaries, dates, and images were scraped from <a href="https://mars.nasa.gov/">NASA's Mars News</a>website in November 2022. Images are used according to the <a href="https://www.jpl.nasa.gov/jpl-image-use-policy">JPL Image Use Policy</a>courtesy NASA/JPL-Caltech.</br>
<sup>[2]</sup> Trilogy Education Services, a <a href="https://2u.com/">2U, Inc.</a> brand.
</ol>


<p align="right">
<a href="https://github.com/theidari/pymaceuticals#overview-of-project-"><sup>TOP PAGE</sup></a>
</P>


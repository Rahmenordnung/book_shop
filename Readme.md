# Book_shop (Forth Milestone Project)
 
 #### <a name="Description"></a>Description :

This project is built for Code Institute as a part of Full Stack Software Development Diploma course. Project was build using semantic HTML5, CSS3, JavaScript along with Python framework Django 2.2. For it I have been using Visual Studio Code that as a Source Code Editor for the local development. Heroku as a web plataform for the website deployment.

A small resumee of the features would be:

* Sign up, Log-in as a user, View books, chapters, fragments, and essays from a specific book, Add a book to shopping cart, Adjust the quantity of items in shopping cart, delete the item from the shopping cart, Pay for the desired products in shopping cart checkout, as a registered user see in the profile site, what products have been already bought.
 

Reset password with a registered username
Search products (by 12 parts categories)
Pay for products in shopping cart checkout
Vote to like / dislike products
Contact us via contact page
View websits satistics charts

#### Sumary :


* [Description](#Description)
* [Name](#Name)
* [UX](#UX)
* [User Stories](#User_Stories)
   - [Wireframes](#Wireframes)
* [Features](#Features)
  * [Current Features](#Current_Features)
 
    --[Existing_functionality](#Existing_functionality)
    
    --[Coding languages](#Coding_languages)

    --[Libraries](#Libraries)
    
    --[Miscelaneous](#Miscelaneous)
    
    --[Google API](#Google_API)
    
* [Features left to implement](#Features_left_to_implement)    
* [Testing](#Testing)
  * [Responsiveness Testing](#Responsiveness_Testing)
  * [Code Testing](#Code_Testing)
  * [Ux Testing](#Ux_Testing)
* [Dataset](#Dataset)
* [Media](#Media)
* [Deployment](#Deployment)
  * [Local Deployment](#Local_Deployment)
* [The DOM](#The_DOM)
* [Challenges](#Challenges)
* [Bugs](#Bugs)
* [Acknowledgements](#Acknowledgements) 
 

#### <a name="Name"></a>Name :

The name is purely discribing what the user can expect from the site, a __Book shop__ , but in the same manner by being such a common name for a bussines, in some way makes the customer wonder if that is just what is going to happen in this __Book shop__, or there is something more. Well then, the only thing left is for him just to come and visit the site.

 
A link of the working project can be found [here](https://rahmenordnung.github.io/toy_storie_shop/)

---
## <a name="UX"></a>UX :

### <a name="User_Stories"></a>User Stories :

"Reading means dreaming by someone else's hand."  – Fernando Pessoa

But how many hands have been shovelling trough this dream, and what they dream about this time spend reading? This is the milestoneproyect theme. __A page where the the lector not only is able to read one book and dream alone but, also to be able to look at what other people, writers, and not only have thought about when reading the literary work that they have been treating with.__

"When you write, you show a world at your size" - Jesús Fernández Santos.

---
### <a name="Wireframes"></a>Wireframes :

You can find a pdf link for the wirefranes here: [Mockups](https://github.com/Rahmenordnung/toy_storie_shop/tree/master/assets/images/mockups)

---
##  <a name="Features"></a>Features

In the constuction of the project I have used the libraries donated by the Code institute, and other functional elements.


#### <a name="Current_Features"></a>Current Features ##


#### <a name="Existing_functionality"></a> Existing functionality ##

-- __Navbar__: Allows all users to easily navigate to the different sections of the website and interpretate the theme which relates them, regardless of which page they are currently on, simply by clicking the name of the area they wish to visit in the navbar. Also contain an logo that redirect to the home page (in this case, the same page).

-- __Shopping_list__: Display a list of the products that have been added to the shopping trolley, that will be in the future purchased.

-- __Product_cart__: Presents a miniature view of the literary work with ----image, title, price, among other attributes---

-- __Full screen background with button in hover effect__: The image contextualize the business in an the right sector. And the __hover efect__ brings the attention to the the __button__ that leads the user to the charts page.

--__Intro.js__ Thanks to javascript it makes a tour with messages and arrows and opacity. It highlights some key elements in the page that the User should pay attention to in order to understand correctly its purpose.

-- __Charts in bootrap cards in differnt sizes__: This charts represent the data in easy to understand manner and makes easy to find connections between different variables from the dataset. Each chart is contained in a bootstrap card that improves the visibility and ads some extra info. The site contains the following types of graphs: bar charts, row charts, pie charts, and scatter plots.

-- __Sections separators__ They are simple headers that group the charts below them to a comun theme.

-- __Useful information__: Allows the user to understand better the charts, and to discover them in a better way, with more detail and attention. this is contained in __bootrap cards__

-- __Toggle hide button__: Once one graph is fully viewed one can hide it or make it appear back so that it will visualize only the needed information.

-- __Search selectors__: There are three selectors that ease the customers display a lot. One can look after the __City__ where the products were delievered, the __Customer name__ and the __order date__ of the delievery. In that way the user can have differents perspectives in which the the data can be analized

-- __Google map__: Allwos the user to locate precisely all the custommers adresses listed in the database. On hover it appears the city name and by clicking the marker, the Customer firma name and the adress available in the records. (Uses Google Maps and Google Places). See js/maps.js. *Mistakes by the adress could appear due to the geographical localizators or incomplete data in the dataset

-- __Footer__: Informs the user that the site is hosted by Github Pages, and provides us a link to where they can view the source code on Github, and also a link to the dataset in a elegant dark green color.

#### <a name="Coding_languages"></a>Current Features ##

-- [HTML5](https://www.w3schools.com/html/html_intro.asp) --Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser.

-- [CSS3](http://www.css3.info/) is a style sheet language used for describing the presentation of a document written in a markup language like HTML.[

------------- [Javascript](https://www.javascript.com/) is a high-level, interpreted programming language that conforms to the ECMAScript specification.-----

-- [jquery.js](https://jquery.com/) is a library of Java scripts that simplifies lots of its functions, the main differance with javascriptis that it performs many common scripting functions in fewer lines of codes

-- [Python](https://www.python.org/)  Python is a general purpose programming language. Usefull for developing both desktop and web applications is designed with features to facilitate data analysis and visualization

-- [Django](https://www.djangoproject.com/) Django is an open source web framework written in Python that follows a model-view-presenter schema. 

-- [Bootstap](https://getbootstrap.com/) is a framework to help you design websites faster and easier.

-- [Stripe](https://dashboard.stripe.com/)Stripe is an online payment service, to enable secure payments using credit cards on the website. Stripe also uses a self-learning fraud prevention system.

-- [Font-awesome](https://fontawesome.com/) Font Awesome is a web font containing all the icons from the Twitter Bootstrap framework, and now many more.

-------Travis
Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub.
-------EmailJS
We use EmailJS to link up the modal contact form to an actual e-mail address---

----------------------------------------

#### <a name="Google_API"></a> Google API  ## 

--[Google APIs(Google maps)](https://developers.google.com/maps/documentation/) is a set of application programming interfaces developed by Google which allow communication with Google Services and their integration to other services

Finally I have used the Google Maps API and added to it the clients adresses so that the user can relate and see where each project has been delivered.

These is a representative map, but not a dynamic one connected to the crossfilter, because that is beyond the lessons provided in the course and my skills, yet

## <a name="Features left to implement"></a>Features_left_to_implement ##

* First of all I like a lot the graphical distributions in general. So one of the thing that I would like to do is to implement more types of Charts, but for that I have to learn more abot javascript.

* I would like also to connect maybe more datasets and work with them

* Also is my intention to maybe work with geographical data in which I am interested.

* Also it would be nice also to make maybe graphics more complicated with more variables connected.

---
## <a name="Dataset"></a>Dataset

The data set has been exported from Kaggle. A link of the exact dataset used can be found here .>>[Kaggle](https://www.kaggle.com/kyanyoga/sample-sales-data)

## <a name="Media"></a> Media  ##
All the images used in the project are taken from Google images page and there are free of copyright.

In this project I used just one image __[link](https://papers.co/ipad/mm13-old-car-street-vintage/)__  

## <a name="Testing"></a> Testing  ## 

#### <a name="Responsiveness_Testing"></a> Responsiveness Testing  ## 

The responsiveness of the website was tested on Chrome developer tool and also in the Mozzila developer tool.

At this stage, the positioning of the footer and background image  and charts cards was tested on the following devices:

Blackberry Playbook
Galaxy sIII, NOte II, 3
Laptop with HiDPI
Microsoft Lumia 550
Nexus 4,5,6,10, etc
Nokia Lumia, N9
iPhone 5/SE,6 7,8,X
iPad, /Pro/ Mini
etc

The full page is responsive in small, medium, and big devices. The charts are fully responsive thanks to the __.useViewBoxResizing(true)__ property added in all the charts. Also I create this responsivness with help of the bootrap cards and classes used in their grid system. The selector bar, navbar and footer I edited myself and created some media queries with css help as I learned in previous modules.

#### <a name="Code_Testing"></a> Code Testing  ####
The HTML was validated using the HTML Validator.

The CSS was validated using the CSS Validator. In total, 1 issues was found. This has to do with the parsing of a property. But as it doesn´t really affect the project I considerated to ignore it.

TheJavaScript files were tested using JSHint.com. Initially, 1 warnings were detected: Duplicate key 'mapTypeId'. But that is the normal type of expression for map.js. The rest is clean.

#### <a name="Ux_Testing"></a> Ux Testing ####

The normal functionality of the page has been tested through this tests:

__Full Background start image__: When hovered over it shows a dinamic effect contains a button.

__Go and play button__: When hovered changes color and adds margin around. When clicked hides the hole _start image_ and the _background page_ and displays the charts page that beginns with _intro.js tour_

__intro.js tour__ it will be displayed when firsly showing the charts page or each time we refresh it and it will guide the User, explain and show him the first steps that the User can do in order understand better the page and its purpose.

__Select bar__ When clicking have to display to indicated data from the dataset, and if clicked to filter throgh the selection and limit the other elements.

__Toggle button__ When clicked once it hides the respective card where the charts are contained, twice it shows it back again. This can be helpfull in order to ease the graphs display and their analysis.

__The charts__ are interactive and responsive and if clicked they will show the section clicked and if clicked back again that will go to the normal view again. And they will be responsive to mobile devices.

__Back to top button__ It will take the user when clicked to the top of the page. So that the user experience is improved in that one can move easily on top or down (with scrolling or navbarlinks) of the page.

__Reset button__ When clicked it resets the charts filtering selection.

__Footer__ It contains anchors, social media, dataset, main page that takes the User to the desired links.

## <a name="Deployment"></a> Deployment  #### 

This project is deployed on heroku: https://django-ecommerce-milestone.herokuapp.com/

#### <a name="Local_Deployment"></a>Local Deployment

In order to run this project __locally__ on your own system, you need following:

It's highly recommended to work in a virtual environment, but not absolutely required.

* Python 3.1.0 (the version that I used) to run the application
* PIP to install all requirements wit `pip install -r requirements.txt`
* GIT(hub) for cloning and version control and to download the repo in zip format

##### Next one should follow this steps in order to make this project work:
---

* Clone the repo with command git clone or donwloand the zip file
* Unpack the zip file and go to the file location and cd <path to folder>
* Create .env with the command in `python -m venv .env` in the terminal 
* Select the virtual environment in the interpreter
* Install all requirements with pip3 -r requirements.txt
* Launch the project python manage.py runserver
* The Django server has this url http://127.0.0.1:8000/
* Create .gitignore file where you will add all the files that you don´t want to be shared in github, such as Secret keys, virtual environments, or local databases, etc. In my case I created a env.py and that must be added in the SETTINGS from the main app (book_shop) and import env under import os 
* Make first steps saving(implementing) the data with: __python manage.py makemigrations__ and __python manage.py migrate__
* To use Django Admin Panel, you must generate a superuser:__python manage.py createsuperuser__



#### <a name="Developer_environment"></a> Developer environment  #### 

As for the external use of the program, the user should download first the Toys shop data base.csv file.
and upload then the above mentionated libraries, after that ,load the bootstap file and the dc.css as well as jquery so that the program should deploy as expected.                                                                                   

---                                                                                                                                      

## <a name="Challenges"></a> Challenges  ## 

For me was something really exciting to work with data and create amazing graphics. Hard to find a good dataset, to learn at the beggining was the crossfilter, the reduce function, even to adjust the graphs to the cards had some issues for me as I am still a rookie. But the most challenging, and that is why I add it to the project was the map.js, whict took me long time , and still not is not brought to a sublime status, though a functional one. Displaying data in the data-grid was also a hard task for me.

## <a name="Bugs"></a> Bugs  ## 
I had some problems with the graphs display and the bootrap classes. 
Second problem was the size of the background image and it was because of the use of useless classes.
## <a name="Acknowledgements"></a> Acknowledgements  ## 
Carina_lead had a video about her project and that helped me when I was stucked in my page. At that time I had only the graphics done, but not a good display. And her call/video helped me.

Many thanks also to the Tutors, my mentor Guido Cecilio Bernal, and to the Code Institute Slack channel was invaluable!


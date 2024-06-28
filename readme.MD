# Kong's Market

<div id="header" align="center">

  <img src="./purplegorilla/static/images/banner.jpg" width="800" height="600">

</div>

## :pencil: Descriptions:

This is a marketplace web app created using Django and BootStrap. Users can create, sell, and buy products. Buyers have the ability to view and cancel orders, while sellers can cancel orders or update order statuses. Both products and orders have full CRUD functionalities. PostgreSQL is used as the database to store all information. The project is fully deployed on Heroku.

## :computer: Getting Started:

You can access the app by clicking the link [here](https://kong-market-5f9a6bf5752f.herokuapp.com/).

## :bust_in_silhouette: Attributions:

For this project, I used the Fake Store API to create fake products. The api can be found using this [link](https://fakestoreapi.com/).

For the initial Postgres database seeding, I borrowed the code from this stackoverflow [post](https://stackoverflow.com/questions/51577441/how-to-seed-django-project-insert-a-bunch-of-data-into-the-project-for-initi). To initialize the database with fake products run in the project's root directory:
```
python3 manage.py seed --mode=refresh
```

## :blue_book: Wireframes and ERD:

These are some page blueprints used to guide the development process.

![wireframe](./purplegorilla/static/images/kong1.jpg)
![wireframe](./purplegorilla/static/images/kong2.jpg)
![wireframe](./purplegorilla/static/images/kong3.jpg)
![wireframe](./purplegorilla/static/images/kong4.jpg)
![wireframe](./purplegorilla/static/images/kong5.png)



## :camera_flash: Kong's Market Images:

![images](./purplegorilla/static/images/img0.png)
![images](./purplegorilla/static/images/img1.png)
![images](./purplegorilla/static/images/img3.5.png)
![images](./purplegorilla/static/images/img4.png)
![images](./purplegorilla/static/images/img2.png)
![images](./purplegorilla/static/images/img5.png)
![images](./purplegorilla/static/images/img6.5.png)
![images](./purplegorilla/static/images/img7.png)



## :computer: Technologies Used:

![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![POSTGRESQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![HEROKU](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Git](https://img.shields.io/badge/-Git-05122A?style=flat&logo=git)
![Github](https://img.shields.io/badge/-GitHub-05122A?style=flat&logo=github)
![JavaScript](https://img.shields.io/badge/-JavaScript-05122A?style=flat&logo=javascript)
![HTML5](https://img.shields.io/badge/-HTML5-05122A?style=flat&logo=html5)
![CSS3](https://img.shields.io/badge/-CSS-05122A?style=flat&logo=css3)


## :satellite: Next Steps:

Here are some potential improvements to the project:

- Functionality to export order history as a PDF
- Send order confirmation email
- Add Cart to store products
- Compatibility with mobile devices

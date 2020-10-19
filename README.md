<img src="https://img.shields.io/github/issues/sanyam1992000/boringlectures"> <img src="https://img.shields.io/github/forks/sanyam1992000/boringlectures"> <img src="https://img.shields.io/github/stars/sanyam1992000/boringlectures"> <img src="https://img.shields.io/github/contributors/sanyam1992000/boringlectures">

[![Visits Badge](https://badges.pufler.dev/visits/sanyam1992000/boringlectures)](https://badges.pufler.dev)

# Boring Lecture - Free Engineering Notes
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://forthebadge.com)


## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
* [Frontend](#frontend)
* [Backend](#backend)
* [Screenshots](#screenshots)
* [Authors](#authors)
* [Contributing](#contributing)
* [License](#license)

## About the Project
This was made for Fun Purpose and for College Notes too.

### Built With
*   Django
*   HTML CSS
*   Celery
*   Redis

## Getting Started
### Prerequisites

* Python
* Django
* Celery


### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.

* With Docker compose

    ```bash
    docker-compose build
    docker-compose up
    docker exec -it django bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

## Usage

* To Create Super User

    ``` bash
    docker exec -it django bash
    python3 manage.py createsuperuser
    ```

## Backend <a class="headerlink" href="#backend" title="Permanent link">#</a>

* #### Django 
    Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source.
    
    * ###### Why Django ?
        *  Ridiculously fast
        *  Reassuringly secure
        *  Exceedingly scalable
        *  Incredibly versatile
        *  Easy to Integrate with Python Libraries/Functions
        
    
* #### Celery - Redis
    “Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.”
    * ###### Why is this useful ?
        * Think of all the times you have had to run a certain task in the future. Perhaps you needed to access an API every hour. Or maybe you needed to send a batch of emails at the end of the day. Large or small, Celery makes scheduling such periodic tasks easy.
        
        * You never want end users to have to wait unnecessarily for pages to load or actions to complete. If a long process is part of your application’s workflow, you can use Celery to execute that process in the background, as resources become available, so that your application can continue to respond to client requests. This keeps the task out of the application’s context.


## Screenshots

## Authors
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/sanyam1992000/">
            <img src="https://avatars2.githubusercontent.com/u/44235818?s=460&u=ace44cdd2bd36f9d187041adfe6565049275d77d&v=4" width="100px;" alt="Sanyam Mittal Picture" style="border-radius:50%;" /><br />
            <sub><b>Sanyam Mittal</b></sub></a><br /><a href="https://github.com/sanyam1992000/boringlectures/commits?author=sanyam1992000" title="Code">💻
        </a>
    </td>    
    <td align="center">
        <a href="https://github.com/v03012000/">
            <img src="https://www.linkedin.com/in/v03012000/detail/photo/" width="100px;" alt="Vidushi Tickoo Picture" style="border-radius:50%;" /><br />
            <sub><b>Vidushi Tickoo</b></sub></a><br /><a href="https://github.com/sanyam1992000/boringlectures/commits?author=v03012000" title="Code">💻
        </a>
    </td>
  </tr>
</table>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
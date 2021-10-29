function switchTheme(){

    let btn = document.getElementById('theme-btn');
    let logo = document.getElementById('flask-logo');
    let body = document.body.style;
    let nav_links = document.getElementsByClassName('navbar-link');

    if (btn.classList.contains("btn-dark")){

        // dark mode properties

        btn.classList.remove('btn-dark');
        btn.classList.add('btn-light');

        body.backgroundColor = "black";
        body.color = 'white';

        for (var i = 0; i < nav_links.length; i++){
            nav_links[i].style.color = 'white';
        };

        logo.src = "/static/media/img/flask-logo-dark.png";

    }else{

        //light mode properties

        btn.classList.remove('btn-light');
        btn.classList.add('btn-dark');

        body.backgroundColor = "white";
        body.color = 'black';

        for (var i = 0; i < nav_links.length; i++){
            nav_links[i].style.color = 'black';
        };

        logo.src = "/static/media/img/flask-logo.png";

    }


}
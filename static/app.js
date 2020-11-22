const navslide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-link');
    const navlinks = document.querySelectorAll('.nav-link li');
    // toggle nav
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-act');

    // Animation links
    navlinks.forEach((link,index) => {
        if(link.style.animation){
            link.style.animation = '';
 
        }
        else{
         link.style.animation = `navLinkfade 0.5s ease forwards ${index / 7 + 0.3}s`;
        }
 
 
     });

    });
    
  }
  navslide();

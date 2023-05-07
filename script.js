// script.js

// Define variables for the nav menu and sections
const navMenu = document.querySelector('nav ul');
const sections = document.querySelectorAll('main section');

// Add event listeners to the nav menu links
navMenu.addEventListener('click', e => {
  e.preventDefault();
  const target = e.target;
  const id = target.getAttribute('href');
  const section = document.querySelector(id);
  section.scrollIntoView({behavior: "smooth", block: "start"});
});

// Add intersection observers to the sections
const observerOptions = {
  root: null,
  rootMargin: '0px',
  threshold: 0.5
};

const observerCallback = (entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('active');
    } else {
      entry.target.classList.remove('active');
    }
  });
};

const observer = new IntersectionObserver(observerCallback, observerOptions);

sections.forEach(section => {
  observer.observe(section);
});

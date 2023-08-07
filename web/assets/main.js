
    function activateNavigation() {
      const sections = document.querySelectorAll(".section");
      const navContainer = document.createElement("nav");
      const navItems = Array.from(sections).map((section) => {
        return `
                        <div class="nav-item" data-for-section="${section.id}">
                            <a href="#${section.id}" class="nav-link"></a>
                            <span class="nav-label">${section.dataset.label}</span>
                        </div>
                    `;
      });
    
      navContainer.classList.add("nav");
      navContainer.innerHTML = navItems.join("");
    
      const observer = new IntersectionObserver(
        (entries) => {
          document.querySelectorAll(".nav-link").forEach((navLink) => {
            navLink.classList.remove("nav-link-selected");
          });
    
          const visibleSection = entries.filter((entry) => entry.isIntersecting)[0];
    
          document
            .querySelector(
              `.nav-item[data-for-section="${visibleSection.target.id}"] .nav-link`
            )
            .classList.add("nav-link-selected");
        },
        { threshold: 0.5 }
      );
    
      sections.forEach((section) => observer.observe(section));
    
      document.body.appendChild(navContainer);
    }
    
    activateNavigation();

    /* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginRight = "250px";
}




/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginRight = "0";
}


/* I screwed the toggle script up badly
const button = document.getElementById("mySidenav"); 
const buttonPressed = (e) => {
  e.target.classList.toggle("sidenav");
  e.target.classList.toggle("shownav");
}
button.addEventListener("click", buttonPressed);
*/
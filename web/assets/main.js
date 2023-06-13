document.addEventListener("DOMContentLoaded", function() {
    var wrap = document.getElementById('wrap');
    var fps = new FullPageScroll(wrap);
    var indicator = document.createElement('div');
    indicator.id = 'indicator';
    var slideIndicators = [];
    fps.slides.forEach(function(slide, index){
      var slideIndicator = document.createElement('div');
      slideIndicator.onclick = function() {
        fps.goToSlide(index);
      }
      if (index === fps.currentSlide) {
        slideIndicator.className = "active";
      }
      indicator.appendChild(slideIndicator);
      slideIndicators.push(slideIndicator);
    });
    document.body.appendChild(indicator);
    fps.onslide = function() {
      slideIndicators.forEach(function(slideIndicator, index) {
        if (index === fps.currentSlide) {
          slideIndicator.className = "active";
        } else {
          slideIndicator.className = "";
        }
      });
    }
  });